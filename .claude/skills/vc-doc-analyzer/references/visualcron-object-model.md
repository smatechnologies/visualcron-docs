# VisualCron Object Model — Coverage Checklist

This is the audit checklist. Documentation coverage in VisualCron is measured
against the **object model**, not against a set of API controllers. Every
object type below is user-facing and therefore in scope for documentation.

Execution flow, which the docs themselves describe:

```
Trigger  →  Condition  →  Task  →  Notification
```

A **Job** is the container. Per the product docs, a Job is composed of six
element types: Triggers, Tasks, Notifications, Time exceptions, Conditions,
and Timeouts. **Connections** and **Credentials** are reusable global objects
attached to Jobs and Tasks. **Variables** carry runtime data between them.

Verify the specifics below against a Tier A–D source before logging findings.
Treat this file as a map of *what to check*, not as a spec of *what is true*.

---

## 1. Jobs

Audit for coverage of:

- Job settings (name, description, enabled/disabled, Job folders, Job groups)
- Job Variables and how they are set, overwritten, and made constant
- Time exceptions
- Job-level Conditions
- Timeout behavior and what happens on timeout
- Flow control between Tasks (on success / on error / on any)
- Concurrency: whether a Job can run multiple instances, and queueing behavior
- "Run missed" / catch-up behavior after server downtime
- Cloning behavior and the Variable-rewrite caveat it carries

---

## 2. Tasks

The largest documentation surface. Tasks are grouped into **categories**, each
with its own folder in the doc tree. Known categories include:

| Category | Examples |
|---|---|
| Process | Execute, Kill process |
| File | Copy, Move, Rename, Delete, Read, Write |
| Net | HTTP, FTP/SFTP/FTPS, SSH, download/upload |
| Messaging | Email send/receive, message queues |
| Database | Execute SQL, export/import |
| XML | Read node, create node, transform |
| Encryption | PGP, encrypt/decrypt |
| Service | Start, stop, query Windows services |
| System | Registry, restart, power, monitor control |
| Office | Excel/Word macro and document operations |
| Interactivity | Desktop macro, send keys |
| Internal | Job/Task control, Set Variable, flow helpers |
| Active Directory | Create/modify AD objects |
| Robot / RPA | Recorder-based desktop and web automation |

**Confirm the live category list and the Task types within each against the
product before auditing.** Categories are added and reorganized across
versions; do not assume this list is current.

For **each Task type**, check the doc page covers:

- [ ] What the Task does and when to use it
- [ ] Every configurable field, with type and default
- [ ] Which fields are required vs. optional
- [ ] Which fields accept Variables
- [ ] Connection or Credential requirements
- [ ] Output: what it writes to StdOut / StdErr / result Variables
- [ ] Exit codes and error behavior
- [ ] Version gate, if the Task or a field was introduced in a specific release

A Task page that lists fields but omits defaults, or omits which fields accept
Variables, is an **Unclear** finding (Section 2), not a pass.

---

## 3. Triggers

Two families: **time** Triggers (custom schedule, interval schedule) and
**event** Triggers (file, folder, process, service, email, database, event
log, HTTP, performance counter, WMI, and others).

Per Trigger type, check the doc covers:

- [ ] What fires it, and what does *not* fire it
- [ ] All configuration fields and defaults
- [ ] **The Variables the Trigger emits at runtime** — this is the most
      commonly under-documented aspect. Event Triggers supply realtime data
      (for example, a File Trigger supplies file name and path) that downstream
      Tasks consume. An undocumented Trigger Variable is a High-impact gap.
- [ ] Behavior when the Trigger fires while the Job is already running
- [ ] Behavior on server restart or reconnect failure
- [ ] Time zone and DST handling for time Triggers

---

## 4. Conditions

- [ ] Every Condition type and its operators
- [ ] Whether it applies at Job level, Task level, or both
- [ ] What happens when the Condition evaluates false (skip, fail, halt)
- [ ] How Conditions compose (AND/OR grouping)

---

## 5. Connections and Credentials

Security-relevant. Both are reusable and shared across Jobs and Tasks.

- [ ] Every Connection type and its required fields
- [ ] Authentication methods supported per type
- [ ] Where credentials are stored and how they are protected
- [ ] Certificate, key, and trust configuration
- [ ] Connection reuse, pooling, and timeout semantics
- [ ] Failure and reconnect behavior

Missing or wrong documentation here is **High impact by default** — see the
impact rubric.

---

## 6. Notifications

- [ ] Notification types available
- [ ] The trigger points (on error, on completion, on Job vs. Task)
- [ ] Which Variables are available in notification templates
- [ ] Where the server-level email/notification settings live

---

## 7. Variables

The runtime data layer. Check the Variables reference covers:

- [ ] Syntax and delimiters
- [ ] Scope prefixes and object accessors — Task output, Job values, Server
      values, Trigger output
- [ ] System Variables
- [ ] Built-in functions (string, date, math, file)
- [ ] User-defined Variables and constants
- [ ] Precedence and overwrite rules when keys collide
- [ ] Escaping, nesting, and resolution order
- [ ] What happens when a Variable fails to resolve

**A wrong Variable name or syntax in the docs fails silently at runtime** —
the Job runs, but with an empty or literal value. Always High impact.

---

## 8. Server, Client, and administration

- [ ] Installation, including silent/MSI install
- [ ] Server settings — every tab and field (log settings, email settings,
      folders, client connections)
- [ ] Folder locations and what each stores
- [ ] Users, Groups, and the permission model
- [ ] Audit log and log retention
- [ ] Backup and restore of settings
- [ ] Client/Server connection, ports, and encryption
- [ ] Multi-server management and remote server operations
- [ ] Licensing

---

## 9. Programmatic interfaces

Three distinct surfaces — each needs its own coverage check.

**.NET API** — `VisualCron.dll` and `VisualCronAPI.dll`
- [ ] Connection/authentication flow (Client → Server object model)
- [ ] Public classes and properties for Jobs, Tasks, Triggers, Connections
- [ ] Public events raised on object change
- [ ] Assembly location, supported .NET version, dependency requirements
- [ ] Known constraints (for example, debugger-detection behavior in v13 and
      the isolated library directory that avoids it)

**Web API** — REST and SOAP over HTTP/HTTPS
- [ ] Every object/action route pair
- [ ] Output format selection (text, XML, JSON)
- [ ] Authentication and token handling
- [ ] Query parameters (column selection, header inclusion, filtering)
- [ ] Default port and how to change it
- [ ] Error responses

**Command-line utility**
- [ ] Every switch and argument
- [ ] Exit codes
- [ ] Authentication

---

## 10. Cross-product integration

VisualCron is part of the Continuous (SMA Technologies) portfolio and is used
as the RPA agent for OpCon. If the doc scope includes integration content,
check for:

- [ ] Orchestration of VisualCron Jobs from OpCon
- [ ] Which side owns scheduling in an integrated deployment
- [ ] Variable and status passing across the boundary
- [ ] Whether integration docs live in the VisualCron repo, the OpCon repo, or
      both — and whether the two copies agree

Contradictions between the VisualCron docs and the OpCon docs on the same
integration are a **High impact** finding. Report them in Section 3 and name
both file paths.
