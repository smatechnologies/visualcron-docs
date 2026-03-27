/** @type {import('@docusaurus/types').Config} */
module.exports = {
  title: 'VisualCron Documentation',
  tagline: 'VisualCron Documentation',
  url: 'https://help.visualcron.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  markdown: {
    format: 'md',
  },
  favicon: 'img/favicon.ico',
  organizationName: 'smatechnologies',
  projectName: 'visualcron-docs',
  themeConfig: {
    navbar: {
      title: 'Help',
      logo: {
        alt: 'SMA Technologies Help Logo',
        src: 'img/VisualCronBlue.png',
        href: 'https://www.visualcron.com',
      },
    },
    prism: {
      additionalLanguages: ['powershell', 'csharp'],
    },
    footer: {
      style: 'dark',
      copyright: `Copyright © ${new Date().getFullYear()} Continuous.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          breadcrumbs: false,
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/smatechnologies/visualcron-docs/blob/main',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
  plugins: [
    [
      '@docusaurus/plugin-google-gtag',
      {
        id: 'gtag-1',
        trackingID: 'G-7XYMFXX81Y',
      },
    ],
    [
      '@docusaurus/plugin-google-gtag',
      {
        id: 'gtag-2',
        trackingID: 'G-0VVXGG8JGT',
      },
    ],
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      {
        // Hashed index for better caching performance
        hashed: true,

        // English only
        language: ['en'],

        // Highlight search terms on destination page
        highlightSearchTermsOnTargetPage: true,

        // Show full breadcrumb path in results
        explicitSearchResultPath: true,

        // Show Cmd/Ctrl+K keyboard shortcut hint
        searchBarShortcutHint: true,
        searchBarPosition: 'right',

        // Limit to 5 results; show up to 200 chars of context
        searchResultLimits: 5,
        searchResultContextMaxLength: 200,

        // Index docs and pages, not blog
        indexDocs: true,
        indexBlog: false,
        indexPages: true,
      },
    ],
  ],
};
