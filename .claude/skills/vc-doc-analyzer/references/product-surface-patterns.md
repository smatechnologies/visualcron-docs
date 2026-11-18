# Product Surface Patterns

How to extract the user-facing VisualCron surface, organized by the evidence
tier available. Work top-down: use the highest tier you have, and fall back
only as needed. Record the tier used on every finding.

VisualCron is closed-source commercial software. Unlike an open-source
product, **you will often not have Tier A**, and the extraction technique
changes completely per tier. Do not apply Tier A patterns to a Tier D source
and report the results with Tier A confidence.

---

## Tier A — Source code (C# / .NET)

Only available if the user has actual VisualCron source, normally the local, private
export at `VC_CODE_EXPORT`. Run from the source root (`cd "$VC_CODE_EXPORT"`). The
patterns below are written for C#; adapt them to the language each project uses.

```bash
# Task type definitions — adjust base type/interface to the real one
grep -rn "class .*Task\b" --include="*.cs" . | grep -v "//\|Test\|Spec"

# Trigger type definitions
grep -rn "class .*Trigger\b" --include="*.cs" . | grep -v "//\|Test"

# Condition, Connection, Notification types
grep -rn "class .*\(Condition\|Connection\|Notification\)\b" --include="*.cs" . | grep -v "//\|Test"

# Enums — these become dropdown values in the Client UI and documented value lists
grep -rn "^[[:space:]]*public enum " --include="*.cs" . | grep -v "Test\|Internal"

# Serialized property names — authoritative for exported XML and API field names
grep -rn "\[XmlElement(\|\[XmlAttribute(\|\[JsonProperty(\|\[JsonPropertyName(" --include="*.cs" .

# Defaults — property initializers and constructor assignments
grep -rn "public .* { get; set; } = " --include="*.cs" .

# Error strings and exception types (Common Issues candidates)
grep -rn "class .*Exception\b\|throw new " --include="*.cs" . | grep -v "//\|Test"

# Version gating in code
grep -rn "Obsolete\|Deprecated\|MinimumVersion\|IntroducedIn" --include="*.cs" .
```

Exclude test and internal projects early:

```bash
grep -rn "<pattern>" --include="*.cs" . --exclude-dir="*.Tests" --exclude-dir="test" -l
```

---

## Tier B — Compiled assemblies (reflection)

`VisualCron.dll` and `VisualCronAPI.dll` from the installation directory. Note
that recent versions ship isolated API assemblies in a `lib` subdirectory
specifically for third-party integration; prefer those if present.

**Caution:** v13 assemblies include debugger-detection behavior that can
terminate a debugging session with a "Debugger Detected" exception. Reflection
over metadata is generally fine; avoid attaching a debugger.

PowerShell, load-for-reflection only (does not execute the assembly):

```powershell
$path = "C:\Program Files (x86)\VisualCron\VisualCronAPI.dll"
$asm  = [System.Reflection.Assembly]::ReflectionOnlyLoadFrom($path)

# Public types — the documentable API surface
$asm.GetExportedTypes() |
  Select-Object FullName, IsEnum, IsClass |
  Sort-Object FullName

# Public properties per type — candidate documented fields
$asm.GetExportedTypes() | ForEach-Object {
  $t = $_
  $t.GetProperties('Public,Instance') | ForEach-Object {
    [PSCustomObject]@{ Type = $t.FullName; Member = $_.Name; PropType = $_.PropertyType.Name }
  }
}

# Enum members — documented valid-value lists
$asm.GetExportedTypes() | Where-Object { $_.IsEnum } | ForEach-Object {
  [PSCustomObject]@{ Enum = $_.FullName; Values = ($_::GetNames($_) -join ', ') }
}

# Public events raised on object change
$asm.GetExportedTypes() | ForEach-Object { $_.GetEvents('Public,Instance') } |
  Select-Object DeclaringType, Name
```

On Linux or without PowerShell, use `monodis --output=- assembly.dll`,
`ikdasm`, or a decompiler CLI to dump public metadata.

**What Tier B proves:** names, types, enum values, signatures.
**What Tier B does NOT prove:** default values assigned at runtime, validation
rules, or UI labels. A property named `Timeout` tells you nothing about its
default. Route defaults to Section 6 unless a Tier A, C, or D source confirms
them.

---

## Tier C — Live server surfaces

### Web API (REST)

Routes follow the shape `/{format}/{object}/{action}`, with format one of
`text`, `xml`, or `json`, plus a `token` query parameter:

```
https://<host>:<port>/visualcron/json/job/list?token=<token>
https://<host>:<port>/visualcron/text/job/list?token=<token>&includeheaders=false
https://<host>:<port>/visualcron/text/job/list?id=1&token=<token>&columns=id,name,runmissed,tasks
```

Method:

1. Enumerate the object/action pairs the docs claim exist.
2. Call each against a **non-production** server and record which respond.
3. Use `text` output **with** headers on to get authoritative property names,
   then diff those names against the doc's field tables. This is the cheapest
   reliable field-name check available at Tier C.
4. Probe for object/action pairs the docs *don't* list, using the object names
   from the object model checklist.

Do not run write actions. Restrict to `list`, `get`, and read-only actions.
Never place a token in anything you save into a report.

### Command-line utility

```
VCCommand.exe /?     # prints the switch list; confirm the help switch on the installed build
```

Diff the switch list against the command-line documentation page.

### Client UI labels

Where a doc cites a menu path (`Manage > Manage server settings > Log settings`)
or a field label, the Client UI is the authority. If you cannot see the UI,
this is a Section 6 item — say that a screenshot or a walkthrough would settle
it. Do not assume a menu path is stale just because it is old.

---

## Tier D — Exported configuration XML

Export Jobs and settings from a real server. This is often the **most
practical** high-value source: it reveals persisted field names and structure
without needing source or a live API.

```bash
# Element names in exported job XML — the persisted object vocabulary
grep -ohE "<[A-Za-z][A-Za-z0-9_]*" export.xml | sort -u

# Task type identifiers as persisted
grep -oE 'TaskType="[^"]+"|<TaskType>[^<]+' export.xml | sort -u

# Trigger and Condition type identifiers
grep -oE '(Trigger|Condition)Type="[^"]+"' export.xml | sort -u

# Variable references actually in use, to validate documented syntax
grep -ohE "\{[A-Za-z]+\([^)]*\)[^}]*\}" export.xml | sort -u
```

Then, for each identifier found, search the docs:

```bash
grep -rn "<IdentifierFromXml>" --include="*.md" docs/
```

No hit → candidate **Missing**. Hit with a different name → candidate
**Renamed / Outdated**.

**Caveat:** exported XML shows only what that server's configuration
*exercises*. A Task type nobody has configured will not appear. Absence from
an export is **not** evidence of absence from the product — never log a
"removed capability" finding from Tier D alone.

---

## Tier E — Changelog only

See [doc-repo-map.md](doc-repo-map.md), "Reading the changelog as an input
signal," for the full method. Summary: extract user-visible entries newer than
the last doc update, grep the doc tree for each, and mark every resulting
finding Tier E pending confirmation.

---

## Doc-side counter-search

For every product-side finding, search the docs *before* logging a gap:

```bash
# Exact term
grep -rni "TermFromProduct" --include="*.md" docs/

# Loosen for casing and spacing drift before concluding "missing"
grep -rniE "term[ _-]?from[ _-]?product" --include="*.md" docs/
```

Run the loose search too. VisualCron docs are inconsistent about hyphenation
and spacing in Task names, so a strict-match miss is frequently a false
positive for "missing."

---

## Efficiency tips

1. **Start with `-l`** to get a file list, then prioritize before reading.
2. **Batch by Task category.** Process one `*-tasks/` folder at a time: count
   pages, list the product's Task types for that category, diff, then move on.
   Findings stay organized and the user can interrupt cleanly.
3. **Count before you read.** Folder page counts vs. product type counts gives
   you the coverage headline in one command.
4. **Never mix tiers silently.** If you confirmed a Task exists at Tier D but
   its default at Tier B, the finding cites both and inherits the weaker
   confidence.
