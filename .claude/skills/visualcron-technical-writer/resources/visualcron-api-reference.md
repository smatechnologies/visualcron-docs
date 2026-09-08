# API Reference Documentation

Output format and rules for documenting the VisualCron APIs. VisualCron exposes several programmatic interfaces, and each has its own documentation shape. Do not force a single REST-resource template across all of them — match the template to the interface.

## The VisualCron API Surface

| Interface | What it is | Primary audience |
|---|---|---|
| **.NET API** | The full object API (C# / VB.NET). The VisualCron Client uses it for every action. Shipped as self-contained DLLs (for example, `"VisualCron.dll"`, `"VisualCronAPI.dll"`) in `"C:\Program Files (x86)\VisualCron\lib"`. | Integration Developer |
| **PowerShell** | Scripted use of the same .NET API from PowerShell. | Integration Developer, System Administrator |
| **Web API (REST)** | HTTP interface returning Text, XML, or JSON. URL pattern: `/<format>/<object>/<method>?token=<token>`. Token or username/password auth. | Integration Developer |
| **Web API (SOAP)** | Web service with a WSDL and `BasicHttpBinding`. | Integration Developer |
| **VCCommand** | The `"VCCommand.exe"` command-line tool for scripted control of a local or remote Server. | System Administrator, Integration Developer |

> The definitive in-product reference is **Help > API** in the Client,
> which offers *Show documentation* (the API quick start) and
> *API reference* (the full member reference). Derive documentation from
> that reference and the live method list, never from guesswork.

## Source Material

Derive all documentation from authoritative sources — never guess signatures, parameter names, or return shapes.

- **.NET API:** the in-product *API reference* (Help > API), the API quick start, and the sample projects shipped in the API folder
- **Web API method list:** the live `/Docs` endpoint of a running Server, for example `http://localhost:8001/VisualCron/text/Docs`
- **Web API auth and ports:** the **Server -> Settings -> Web API** tab (encrypted and unencrypted ports, permissions)
- **SOAP:** the WSDL URL shown on the Web API tab, and the sample `TestClient` project
- **VCCommand:** the tool's own help output and the existing `vccommand.md` page
- **Permissions:** the Web API uses the same permission model as the Client (Manage user permissions), so document required permissions per method

## File Naming and Location

- Group API documentation under the existing "Interacting with VisualCron" area (`docs/using-visualcron/`)
- Use descriptive slugs: `visualcron-web-api.md`, `powershell.md`, `dot-net-csharp-vbnet.md`, `vccommand.md`
- For per-method Web API reference pages, name by object and method: `web-api-job-list.md`, `web-api-job-run.md`
- Register every new page in `sidebars.js` and `chm-config.json` (see the repo README)

---

## Template: Web API Method (REST)

Use this for each documented Web API method. The Web API is method-based (object + method), not resource/verb REST, so document it accordingly.

````markdown
---
sidebar_label: 'Web API: Job/List'
hide_title: 'true'
---

## Web API: Job/List

**Method:** `job/list`

**HTTP:** `GET /<format>/job/list`

**Description:** One sentence describing what this method returns or does.

## Formats

The Web API returns one of three output formats, selected in the URL path:

| Format | URL segment | Output |
|---|---|---|
| Text | `/text/` | Plain text, optionally with header row |
| XML | `/xml/` | XML |
| JSON | `/json/` | JSON |

## Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `token` | string | Yes* | Authentication token from the `logon` method. Required unless `username` and `password` are supplied. |
| `id` | integer | No | Return only the Job with this ID. |
| `columns` | string | No | Comma-separated list of properties to include, for example `id,name,tasks`. |
| `includeheaders` | boolean | No | For text output, whether to include the property-name header row. Default: `true`. |

> \* Provide either a `token` or a `username` + `password` pair.

## Sample Request

```
https://vcserver.contoso.com:8002/visualcron/json/job/list?token=<token>&columns=id,name,active
```

## Sample Response (JSON)

```json
[
  { "id": 12, "name": "Nightly Contoso ERP Export", "active": true },
  { "id": 13, "name": "Hourly Log Archive", "active": true }
]
```

## Permissions

State the Client permission required to call this method (for example, "View Jobs").

## Errors

Describe the failure responses, for example an invalid or expired token.
````

### Authentication note (include once, in the Web API overview)

```markdown
## Authentication

Obtain a token from the `logon` method:

`https://vcserver.contoso.com:8001/visualcron/text/logon?username=<user>&password=<password>`

The returned token is valid for 24 hours and is renewed on each call.
Pass it as `&token=<token>` on subsequent calls. Alternatively, pass
`username` and `password` on each call to skip token handling.
```

---

## Template: .NET API Member

Use this for classes, methods, and properties of the .NET API.

````markdown
---
sidebar_label: 'Client.Jobs.GetAll'
hide_title: 'true'
---

## Client.Jobs.GetAll

**Namespace / Class:** State the class that exposes the member.

**Description:** One sentence describing what the member does or returns.

## Signature

```csharp
List<VisualCron.JobClass> GetAll();
```

## Parameters

| Parameter | Type | Description |
|---|---|---|
| (none) | — | — |

## Returns

| Type | Description |
|---|---|
| `List<JobClass>` | All Jobs on the connected Server. |

## Example (C#)

```csharp
var client = new VisualCronAPI.Client();
client.Connect("vcserver.contoso.com", 16444, "svc-vc", "<password>");

foreach (var job in client.Jobs.GetAll())
{
    Console.WriteLine(job.Name);
}
```

## Example (PowerShell)

```powershell
[Reflection.Assembly]::LoadFile("C:\Program Files (x86)\VisualCron\lib\VisualCronAPI.dll")
$client = New-Object VisualCronAPI.Client
$client.Connect("vcserver.contoso.com", 16444, "svc-vc", "<password>")
$client.Jobs.GetAll() | ForEach-Object { $_.Name }
```

## Notes

Include version notes, threading notes, or the debugger-detection guidance
for v13 DLLs where relevant (use the DLLs in the `\lib` folder for
debugging).
````

---

## Template: VCCommand Command

Use this for each `VCCommand.exe` command.

````markdown
---
sidebar_label: 'VCCommand: Run Job'
hide_title: 'true'
---

## VCCommand: Run Job

**Description:** One sentence describing what the command does.

## Syntax

```
VCCommand.exe -server <server> -user <user> -password <password> -runjob -jobid <id>
```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `-server` | Yes | The VisualCron Server address. Use the local server if omitted. |
| `-jobid` | Yes | The ID of the Job to run. |

## Example

```
VCCommand.exe -server vcserver.contoso.com -user svc-vc -password <password> -runjob -jobid 12
```
````

---

## Format Rules

These apply to every API documentation file.

1. **Match the template to the interface.** Web API methods use the method template; .NET members use the member template; VCCommand uses the command template. Do not document the Web API as if it were resource/verb REST with request bodies.
2. **Front matter and headings.** Every page has `sidebar_label` and `hide_title: 'true'` and opens with a `## H2`. Section headings are `##`.
3. **Section order is fixed; presence is conditional.** Omit a section that does not apply, but keep the order shown in the template.
4. **Sample/parameter parity.** Every field in a sample response or request must appear in the corresponding table, and vice versa.
5. **Type vocabulary.** Use `string`, `integer`, `boolean`, `number`, `array`, `object`; for .NET, use the actual .NET type (`List<JobClass>`, `bool`, `int`).
6. **Realistic sample data.** Use plausible names for a general IT environment. Use **Contoso** as the sample organization and **contoso.com** as the sample domain. Sample Server host: `vcserver.contoso.com`. No "foo," "bar," or "test" placeholders.
7. **Redact secrets.** Never put a real password or token in a sample. Use `<password>` and `<token>` placeholders.
8. **Ports.** Use the documented defaults: Server communication `16444`; Web API on its configured unencrypted/encrypted ports (commonly `8001` unencrypted, `8002` encrypted). State that ports are configurable.
9. **Permissions.** Document the Client permission each Web API method or command requires, since the Web API uses the same permission model.
10. **No freeform prose in reference sections.** Keep tables and samples strict; put narrative in an overview page instead.

## Requirements

1. Read the in-product *API reference* (Help > API) and the live `/Docs` method list before documenting the Web API.
2. Use exact member names, parameter names, and return types from the API reference — do not paraphrase them.
3. Document authentication once in the overview and link to it from method pages.
4. Provide at least one working, copyable example per member or method, using Contoso sample data and secret placeholders.
5. Note version-specific behavior (for example, the v13 "Debugger Detected" behavior and the self-contained `\lib` DLLs) where it affects the reader.
