const fs = require('fs');
const path = require('path');
const matter = require('gray-matter');
const { marked } = require('marked');

const SCRIPTS_DIR = __dirname;
const PROJECT_ROOT = path.resolve(SCRIPTS_DIR, '..');
const DOCS_DIR = path.join(PROJECT_ROOT, 'docs');
const STATIC_IMG_DIR = path.join(PROJECT_ROOT, 'static', 'img');
const OUTPUT_DIR = path.join(PROJECT_ROOT, 'chm-output');
const CSS_SOURCE = path.join(SCRIPTS_DIR, 'chm-template.css');
const CHM_CONFIG_PATH = path.join(PROJECT_ROOT, 'chm-config.json');
const SIDEBARS_PATH = path.join(PROJECT_ROOT, 'sidebars.js');

// ─── Load config ────────────────────────────────────────────────────────────

let chmConfig;
try {
  chmConfig = JSON.parse(fs.readFileSync(CHM_CONFIG_PATH, 'utf-8'));
} catch (err) {
  console.error(`Fatal: Cannot read chm-config.json at ${CHM_CONFIG_PATH}: ${err.message}`);
  process.exit(1);
}

let sidebar;
try {
  sidebar = require(SIDEBARS_PATH).mySidebar;
} catch (err) {
  console.error(`Fatal: Cannot load sidebars.js at ${SIDEBARS_PATH}: ${err.message}`);
  process.exit(1);
}

const mappings = chmConfig.mappings || {};
const defaultTopic = chmConfig.defaultTopic || 'index.htm';
const chmTitle = chmConfig.title || 'VisualCron Help';
const excludeSet = new Set(chmConfig.excludeFromChm || []);

// ─── Helpers ────────────────────────────────────────────────────────────────

function autoGenerateChmFilename(docId) {
  const lastSegment = docId.split('/').pop();
  return lastSegment.replace(/[\s-]+/g, '_') + '.htm';
}

function getChmFilename(docId) {
  const mapping = mappings[docId];
  if (mapping && mapping.chmFile) {
    return mapping.chmFile;
  }
  return autoGenerateChmFilename(docId);
}

function getMdFilePath(docId) {
  const mapping = mappings[docId];
  if (mapping && mapping.mdFile) {
    return path.join(PROJECT_ROOT, mapping.mdFile);
  }
  return path.join(DOCS_DIR, docId + '.md');
}

function getLabel(docId, frontmatterLabel) {
  const mapping = mappings[docId];
  if (mapping && mapping.label) {
    return mapping.label;
  }
  return frontmatterLabel || docId.split('/').pop().replace(/-/g, ' ');
}

// ─── Filter sidebar items by exclude set ─────────────────────────────────

function filterSidebarItems(items, exclude) {
  const result = [];
  for (const item of items) {
    if (typeof item === 'string') {
      if (!exclude.has(item)) {
        result.push(item);
      }
    } else if (item && typeof item === 'object' && item.type === 'category') {
      const filtered = filterSidebarItems(item.items || [], exclude);
      if (filtered.length > 0) {
        result.push({ ...item, items: filtered });
      }
    }
  }
  return result;
}

// ─── Collect all doc IDs from sidebar (preserving tree structure) ───────────

function collectDocIds(items) {
  const ids = [];
  for (const item of items) {
    if (typeof item === 'string') {
      ids.push(item);
    } else if (item && typeof item === 'object' && item.type === 'category') {
      const childIds = collectDocIds(item.items || []);
      ids.push(...childIds);
    }
  }
  return ids;
}

// ─── Image path handling ────────────────────────────────────────────────────

const imageFilenameMap = new Map(); // flattened name -> source absolute path
const imageCollisions = new Map(); // base filename -> count

function resolveImageSource(relImgPath, mdFileDir) {
  const decoded = decodeURIComponent(relImgPath.replace(/%20/g, ' '));
  const absPath = path.resolve(mdFileDir, decoded);
  if (fs.existsSync(absPath)) {
    return absPath;
  }
  return null;
}

function flattenImageName(absImgPath) {
  const relToStatic = path.relative(STATIC_IMG_DIR, absImgPath);
  const parts = relToStatic.split(path.sep);

  if (parts.length === 1) {
    return parts[0];
  }

  const flattened = parts.join('_');
  return flattened;
}

function registerImage(absImgPath) {
  const flatName = flattenImageName(absImgPath);

  if (imageFilenameMap.has(flatName)) {
    const existing = imageFilenameMap.get(flatName);
    if (existing === absImgPath) {
      return flatName;
    }
    // Collision with a different source file. Disambiguate.
    const count = (imageCollisions.get(flatName) || 1) + 1;
    imageCollisions.set(flatName, count);
    const ext = path.extname(flatName);
    const base = flatName.slice(0, -ext.length);
    const newName = `${base}_${count}${ext}`;
    imageFilenameMap.set(newName, absImgPath);
    return newName;
  }

  imageFilenameMap.set(flatName, absImgPath);
  return flatName;
}

// ─── Fix image paths in HTML ────────────────────────────────────────────────

function fixImagePaths(html, mdFileDir) {
  // Match <img> tags with src attribute
  return html.replace(/<img\s+([^>]*?)src="([^"]*)"([^>]*?)>/gi, (match, pre, src, post) => {
    const absImgPath = resolveImageSource(src, mdFileDir);
    if (!absImgPath) {
      console.warn(`  Warning: Image not found: ${src}`);
      return match;
    }
    const flatName = registerImage(absImgPath);
    return `<img ${pre}src="${flatName}"${post}>`;
  });
}

// ─── Emoji shortcode replacement ─────────────────────────────────────────────

const EMOJI_MAP = {
  'star': '\u2B50',
  'white_check_mark': '\u2705',
  'warning': '\u26A0\uFE0F',
  'x': '\u274C',
  'heavy_check_mark': '\u2714\uFE0F',
  'exclamation': '\u2757',
  'question': '\u2753',
  'info': '\u2139\uFE0F',
  'bulb': '\u1F4A1',
  'memo': '\uD83D\uDCDD',
  'rocket': '\uD83D\uDE80',
  'bug': '\uD83D\uDC1B',
  'fire': '\uD83D\uDD25',
  'link': '\uD83D\uDD17',
};

function replaceEmojiShortcodes(html) {
  return html.replace(/:([a-z_]+):/g, (match, name) => {
    return EMOJI_MAP[name] || match;
  });
}

// ─── HTML template ──────────────────────────────────────────────────────────

function wrapInTemplate(title, content) {
  return `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>${escapeHtml(title)}</title>
  <link rel="stylesheet" href="default.css">
</head>
<body>
  <h1>${escapeHtml(title)}</h1>
  ${content}
</body>
</html>`;
}

function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// ─── Process a single doc ───────────────────────────────────────────────────

function processDoc(docId) {
  const mdPath = getMdFilePath(docId);

  if (!fs.existsSync(mdPath)) {
    console.warn(`Warning: .md file not found for doc "${docId}": ${mdPath} - skipping`);
    return null;
  }

  const raw = fs.readFileSync(mdPath, 'utf-8');
  const { data: frontmatter, content: mdContent } = matter(raw);

  const sidebarLabel = frontmatter.sidebar_label || '';
  const title = getLabel(docId, sidebarLabel);
  const chmFile = getChmFilename(docId);

  let html = marked(mdContent);
  html = replaceEmojiShortcodes(html);
  const mdFileDir = path.dirname(mdPath);
  html = fixImagePaths(html, mdFileDir);

  const fullHtml = wrapInTemplate(title, html);
  const outPath = path.join(OUTPUT_DIR, chmFile);
  fs.writeFileSync(outPath, fullHtml, 'utf-8');

  return { docId, chmFile, title, sidebarLabel };
}

// ─── Generate HHP (project file) ───────────────────────────────────────────

function generateHHP(htmFiles) {
  const filesList = htmFiles.map(f => f).join('\n');
  return `[OPTIONS]
Compatibility=1.1
Compiled file=VisualCron.chm
Contents file=VisualCron.hhc
Default topic=${defaultTopic}
Display compile progress=No
Full-text search=Yes
Index file=VisualCron.hhk
Language=0x409 English (United States)
Title=${chmTitle}

[FILES]
${filesList}

[INFOTYPES]
`;
}

// ─── Generate HHC (table of contents) ──────────────────────────────────────

function generateHHCItems(items, processedDocs, indent) {
  let out = '';
  const pad = '  '.repeat(indent);

  for (const item of items) {
    if (typeof item === 'string') {
      const info = processedDocs.get(item);
      if (!info) continue;
      out += `${pad}<LI><OBJECT type="text/sitemap">\n`;
      out += `${pad}  <param name="Name" value="${escapeHtml(info.title)}">\n`;
      out += `${pad}  <param name="Local" value="${info.chmFile}">\n`;
      out += `${pad}</OBJECT>\n`;
    } else if (item && typeof item === 'object' && item.type === 'category') {
      const categoryLabel = item.label || 'Unknown';
      const children = item.items || [];

      // Check if the first child is a doc that serves as the category page
      let localFile = null;
      if (children.length > 0 && typeof children[0] === 'string') {
        const firstDoc = processedDocs.get(children[0]);
        if (firstDoc) {
          localFile = firstDoc.chmFile;
        }
      }

      out += `${pad}<LI><OBJECT type="text/sitemap">\n`;
      out += `${pad}  <param name="Name" value="${escapeHtml(categoryLabel)}">\n`;
      if (localFile) {
        out += `${pad}  <param name="Local" value="${localFile}">\n`;
      }
      out += `${pad}  <param name="ImageNumber" value="2">\n`;
      out += `${pad}</OBJECT>\n`;
      out += `${pad}<UL>\n`;
      out += generateHHCItems(children, processedDocs, indent + 1);
      out += `${pad}</UL>\n`;
    }
  }

  return out;
}

function generateHHC(sidebarItems, processedDocs) {
  let body = generateHHCItems(sidebarItems, processedDocs, 1);
  return `<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
<HTML>
<HEAD>
<meta name="GENERATOR" content="VisualCron CHM Builder">
</HEAD>
<BODY>
<UL>
${body}</UL>
</BODY>
</HTML>`;
}

// ─── Generate HHK (index) ──────────────────────────────────────────────────

function generateHHK(processedDocs) {
  let entries = '';
  const seen = new Set();

  for (const [, info] of processedDocs) {
    // Add both title and sidebar_label as keywords if they differ
    const keywords = new Set();
    if (info.title) keywords.add(info.title);
    if (info.sidebarLabel && info.sidebarLabel !== info.title) {
      keywords.add(info.sidebarLabel);
    }

    for (const kw of keywords) {
      const key = `${kw}::${info.chmFile}`;
      if (seen.has(key)) continue;
      seen.add(key);

      entries += `  <LI><OBJECT type="text/sitemap">\n`;
      entries += `    <param name="Name" value="${escapeHtml(kw)}">\n`;
      entries += `    <param name="Local" value="${info.chmFile}">\n`;
      entries += `  </OBJECT>\n`;
    }
  }

  return `<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
<HTML>
<HEAD>
<meta name="GENERATOR" content="VisualCron CHM Builder">
</HEAD>
<BODY>
<UL>
${entries}</UL>
</BODY>
</HTML>`;
}

// ─── Main ───────────────────────────────────────────────────────────────────

function main() {
  console.log('VisualCron CHM Builder');
  console.log('=====================');

  // Collect all unique doc IDs from sidebar, excluding filtered IDs
  const allDocIds = collectDocIds(sidebar);
  const uniqueDocIds = [...new Set(allDocIds)].filter(id => !excludeSet.has(id));
  if (excludeSet.size > 0) {
    console.log(`Excluding ${excludeSet.size} doc(s) from CHM: ${[...excludeSet].join(', ')}`);
  }
  console.log(`Found ${allDocIds.length} doc references in sidebar (${uniqueDocIds.length} unique after exclusions)`);

  // Create output directory
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  // Process each unique doc
  const processedDocs = new Map(); // docId -> { docId, chmFile, title, sidebarLabel }
  let processedCount = 0;
  let skippedCount = 0;

  for (const docId of uniqueDocIds) {
    const result = processDoc(docId);
    if (result) {
      processedDocs.set(docId, result);
      processedCount++;
    } else {
      skippedCount++;
    }
  }

  console.log(`Processed ${processedCount} docs, skipped ${skippedCount}`);

  // Copy images
  let imagesCopied = 0;
  for (const [flatName, absPath] of imageFilenameMap) {
    try {
      fs.copyFileSync(absPath, path.join(OUTPUT_DIR, flatName));
      imagesCopied++;
    } catch (err) {
      console.warn(`Warning: Failed to copy image "${flatName}": ${err.message}`);
    }
  }
  console.log(`Copied ${imagesCopied} images`);

  // Copy CSS
  if (fs.existsSync(CSS_SOURCE)) {
    fs.copyFileSync(CSS_SOURCE, path.join(OUTPUT_DIR, 'default.css'));
    console.log('Copied chm-template.css as default.css');
  } else {
    console.warn('Warning: chm-template.css not found at ' + CSS_SOURCE);
  }

  // Collect unique .htm filenames (multiple doc IDs can map to same file)
  const htmFileSet = new Set();
  for (const [, info] of processedDocs) {
    htmFileSet.add(info.chmFile);
  }
  const htmFiles = [...htmFileSet].sort();

  // Generate HHP
  const hhpContent = generateHHP(htmFiles);
  fs.writeFileSync(path.join(OUTPUT_DIR, 'VisualCron.hhp'), hhpContent, 'utf-8');
  console.log('Generated VisualCron.hhp');

  // Generate HHC (use filtered sidebar so excluded pages don't appear in TOC)
  const filteredSidebar = filterSidebarItems(sidebar, excludeSet);
  const hhcContent = generateHHC(filteredSidebar, processedDocs);
  fs.writeFileSync(path.join(OUTPUT_DIR, 'VisualCron.hhc'), hhcContent, 'utf-8');
  console.log('Generated VisualCron.hhc');

  // Generate HHK
  const hhkContent = generateHHK(processedDocs);
  fs.writeFileSync(path.join(OUTPUT_DIR, 'VisualCron.hhk'), hhkContent, 'utf-8');
  console.log('Generated VisualCron.hhk');

  console.log('');
  console.log(`Build complete. Output: ${OUTPUT_DIR}`);
  console.log(`  HTM files: ${htmFiles.length}`);
  console.log(`  Images:    ${imagesCopied}`);
}

main();
