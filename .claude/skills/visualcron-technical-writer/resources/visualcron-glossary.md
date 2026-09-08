# VisualCron Terminology Glossary

> **Source:** VisualCron Documentation (help.visualcron.com) | Last Updated: July 2026

---

## How to Use This Glossary

In the world of job scheduling and IT automation, the same concept can be described in many different ways. This glossary provides the preferred terminology used in VisualCron documentation. Use it as the definitive reference for all user-facing and internal communication.

This glossary is organized into two sections:

- **Preferred terms** (the main alphabetical glossary) — use these terms in all documentation, UI copy, and user communication
- **Confusable and legacy terms** (at the end) — terms that are ambiguous, come from other products, or appear in older content. The AI should recognize them in source material and map them to the correct VisualCron term.

### Notation Key

| Notation | Meaning |
|----------|---------|
| **Words users might use** | Alternative terms users may use in conversation |
| **Do not use** | Terms to avoid in documentation and user communication |
| **DRAFT** | Definition is still being revised or awaiting approval |
| **CONFUSABLE** | Term borrowed from another product or general usage that maps to a specific VisualCron term |
| **LEGACY** | Old term replaced by a current term; appears in older releases or historical content |

---

## A

### Active Job / Active Task

*noun*

The Job or Task currently being processed when a VisualCron variable is evaluated at run time. Active-object variables (for example, `{JOB(Active,Name)}` or `{TASK(Active,ExitCode)}`) resolve against whatever Job or Task is running, rather than a specific one identified by ID.

**See also:** Variable, Current Job/Task

---

### Audit Log

*noun*

A record in the VisualCron Client that tracks changes to objects such as Jobs, Tasks, Connections, and Variables. Each entry shows the event date, user, object type, event type, and a difference summary. The Audit Log supports viewing prior **Versions** of an object and reverting to a selected version.

**See also:** Version

---

### Automation Engineer

*noun*

A role that builds and maintains Jobs, Tasks, Triggers, Conditions, Connections, and Variables in VisualCron. See [visualcron-learner-roles.md](visualcron-learner-roles.md) for full audience guidance including knowledge domains, tone, assumed knowledge, and scope boundaries.

---

## C

### Client

See **VisualCron Client**.

> **Note:** In VisualCron, "Client" is a first-class product term (the desktop application). Do not avoid it. This differs from products where "client" is discouraged in favor of "customer."

---

### Condition

*noun*

A check that is evaluated before a Job or a Task runs. If the condition set does not match, the configured action determines what happens next — for example, **Continue**, **Next**, **Retry**, **Exit**, **Run Job**, or **Run Task**. Conditions can be attached at the Job level and at the Task level.

VisualCron supports several condition types: VisualCron, File, Folder, Process, Service, Variable, and .NET. A condition set is evaluated with a match outcome: **On Match All**, **On Match Any**, **On Match None**, or **On Match Error**.

**Words users might use:** check, rule, dependency

**Do not use:** dependency (as a synonym for Condition — a dependency in VisualCron is a Trigger-level relationship)

**See also:** Flow, Trigger, Dependency

---

### Connection

*noun*

A global, centrally stored definition of where and how VisualCron connects to an external system, such as an FTP/SFTP server, a database, or a cloud service. Because connections are global, changing one connection affects every Job or Task that references it. VisualCron supports many connection protocols (FTP, SFTP, SCP, SSH, SMTP, SQL, Amazon, Azure, SharePoint, and more).

**Words users might use:** profile, endpoint, connection string

**Do not use:** profile, endpoint (as synonyms for a VisualCron Connection)

**See also:** Credential, Task

---

### Credential

*noun*

A global, centrally stored account that VisualCron uses to run a Task or connect as a specific user. Because the VisualCron Server service runs as LOCALSYSTEM, credentials allow Tasks to run under a defined user context. VisualCron supports standard user accounts, (group) Managed Service Accounts ((g)MSA), local logon, and profile loading.

**Words users might use:** run-as account, service account, login

**Do not use:** batch user (a term from other schedulers)

**See also:** Connection, Execution context

---

### Current Job / Current Task

*noun*

The Job or Task marked with the green arrow indicator in the VisualCron Client — the object currently in focus or in progress. Variables can reference the current object, the previous Task (`{TASK(PrevTask,Name)}`), or a specific object by ID.

**See also:** Active Job/Task, Variable

---

## D

### Dependency

*noun*

A relationship between Triggers that changes how they combine. By default, multiple Triggers on a Job are evaluated as an **OR** relationship — any one of them can start the Job. A dependency creates an **AND**-style relationship, so a Job starts only when the configured combination of Triggers has fired.

**Do not use:** dependency as a synonym for **Condition**. Conditions are evaluated before a Job or Task runs; dependencies define how Triggers combine to start a Job.

**See also:** Trigger, Condition

---

## E

### Event Trigger

*noun*

A Trigger that starts a Job in response to a system event rather than a time. Most event triggers are based on the Windows Management Instrumentation (WMI) interface. Event trigger types include File, Process, Service, Registry, Event Log, Mail, SQL, HTTP/REST, TCP, PowerShell, Performance Counter, and many others.

**See also:** Trigger, Time Trigger

---

### Execution context

*noun*

The Task setting that determines the user account and environment a Task runs under, including the credential used, whether to load the user profile, and processor affinity. The execution context is configured on the Task.

**See also:** Credential, Task

---

## F

### Flow

*noun*

The control layer, introduced in VisualCron 7.0.0, that merges on-error handling, condition handling, and notifications into a single model. Flow can be configured at both the Job level and the Task level. Flow responds to events — **On start**, **On error**, **On success**, **On complete**, and **On running longer than** — with actions such as **Stop Job**, **Wait and retry**, **Run Job**, **Run Notification**, and **Deactivate Job**.

**See also:** Condition, Notification

---

## G

### Grid

*noun*

The main visualization area of the VisualCron Client window, in which Servers, Jobs, and Tasks are displayed with basic data and their relationships. The Grid contains a Job track (Job List) and a Task track (Task List).

**Words users might use:** job list, main view

**See also:** Job List, Task List

---

### Global object

*noun*

An object that is stored centrally on the VisualCron Server and reused across Jobs and Tasks. Global objects include Connections, Credentials, Conditions, Notifications, Variables, Certificates, Network Drives, PGP Key Rings, SSH Keys, Time Exceptions, and the Task Repository.

---

## J

### Job

*noun*

The primary schedulable object in VisualCron. A Job is a container for one or more Tasks and is started by one or more Triggers. A Job can also include Conditions, Time exceptions, a Timeout, Flow, Notifications, and Job variables. The only mandatory Job setting is the **Name**. Job definitions are stored in `"jobs.xml"`.

**Do not use:** task, process (as synonyms for a VisualCron Job — a Job contains Tasks)

**See also:** Task, Trigger

---

### Job List

*noun*

The Job track of the Grid, listing the Jobs on the selected Server. Jobs can be organized with Groups and Job Folders.

**See also:** Grid, Task List, Job Folder

---

### Job Folder

*noun*

An organizational container used to group Jobs in the Job List for easier management. Job Folders organize the display and do not change how Jobs run.

---

## M

### MFT Server

*noun*

VisualCron's built-in Managed File Transfer server, which hosts SFTP/FTP endpoints inside VisualCron. File events on the MFT Server can start Jobs through the MFT Trigger.

---

## N

### Notification

*noun*

A way to deliver the result of a Job or Task. Since version 7.0.0, notifications are global, independent Tasks — any Task type can be used as a Notification. Notifications are invoked from Job Flow or Task Flow using the **Run Notification** action.

**Words users might use:** alert, message

**Do not use:** event (as a synonym for Notification — an event starts a Job through an Event Trigger)

**See also:** Flow, Task

---

## O

### Operations Staff

*noun*

A role that monitors running Jobs, responds to failures, and keeps automation running day to day. See [visualcron-learner-roles.md](visualcron-learner-roles.md) for full audience guidance.

---

## R

### Robot Task

*noun*

An interactivity Task type used for RPA-style automation of the Windows desktop (for example, mouse and keyboard actions). Related interactivity Tasks include Web Macro, Desktop Macro, Send Keys, and Popup.

---

### ROI (Return On Investment)

*noun*

A VisualCron feature that estimates how much time and money each Job execution saves, based on a configured hourly rate and currency. ROI helps communicate the business value of automation to managers and stakeholders.

---

## S

### Server

See **VisualCron Server**.

---

### Server status

*noun*

The **On** or **Off** state of the VisualCron Server. When the Server is Off, Jobs do not run even if the service is Started. Distinct from **Service status**.

**See also:** Service status

---

### Service status

*noun*

The **Started** or **Stopped** state of the VisualCron Server Windows service (`"VisualCronService.exe"`). Distinct from **Server status**.

**See also:** Server status

---

## T

### Task

*noun*

A single unit of work within a Job. Each Task runs as a separate process and performs one activity defined by its **Task type**. A Job can contain one or more Tasks, and Tasks can run in order or in parallel. Each Task can have its own Conditions, Flow, Notifications, Timeout, and Output settings.

**Do not use:** job, step, action (as synonyms for a VisualCron Task)

**See also:** Job, Task type

---

### Task type

*noun*

The kind of activity a Task performs, selected in the **Add Job / Edit Job -> Tasks -> Add/Edit** dialog. VisualCron provides many Task types grouped into categories such as Process, Net, Messaging, Database, Encryption, File, Office, and Internal Tasks.

**Words users might use:** activity, command type, action

**Do not use:** activity, action (as synonyms for Task type)

---

### Task Repository

*noun*

A global store of reusable Tasks that can be referenced from multiple Jobs, so a common Task is defined once and maintained in one place.

---

### Time exception

*noun*

A rule that prevents a Job from running during specified periods (for example, holidays or maintenance windows). Time exceptions can be defined per Job or stored globally as Global Time Exceptions.

**Words users might use:** blackout, holiday calendar

---

### Time Trigger

*noun*

A Trigger that starts a Job based on time. VisualCron supports an **Interval time trigger** (run every N seconds/minutes/hours) and a **Custom time trigger** (specific dates, days, and times), with expiration handling.

**See also:** Trigger, Event Trigger

---

### Trigger

*noun*

The object that starts a Job. A Job can have one or more Triggers, and by default they combine as an OR relationship. A Trigger is either a **Time Trigger** (time-based) or an **Event Trigger** (system-event-based). Dependencies can be used to combine Triggers with AND logic.

**Words users might use:** schedule, frequency, job time

**Do not use:** frequency, schedule (as synonyms for a VisualCron Trigger)

**See also:** Time Trigger, Event Trigger, Dependency

---

## V

### Variable

*noun*

A VisualCron value token written in the form `{ROOT(args)}` — for example, `{DATE(Week)}`, `{JOB(id,Name)}`, `{TASK(TaskId,ExitCode)}`, or `{USERVAR(name)}`. Variables let Jobs and Tasks reference dynamic data such as dates, system values, Task output, and user-defined values. Root groups include Functions, Logic, Math, System variables, Server variables, Date variables, File variables, Folder variables, VisualCron variables, and User defined variables.

**Words users might use:** token, property, macro

**Do not use:** property, threshold (as synonyms for a VisualCron Variable)

**See also:** VisualCron variables

---

### Version

*noun*

A saved historical state of an object recorded in the Audit Log. Users can view versions of a Job or other object and revert to a selected version.

**See also:** Audit Log

---

### VisualCron

*proper noun*

An advanced Job/Task scheduler and automation tool for Windows, provided by NetCart AB, an SMA Technologies company. VisualCron runs commands, programs, and integrations at predefined times, intervals, or events.

---

### VisualCron Client

*noun*

The desktop application used to configure VisualCron and manage the Jobs and Tasks run by the Server. The Client itself uses the VisualCron API to perform all actions. Related interfaces include the **Tray Client**, the **Web Client**, and the **Mobile App**.

**Words users might use:** console, the app, the GUI

**Do not use:** console, portal (as the primary name for the Client)

**See also:** VisualCron Server, Web Client, Tray Client

---

### VisualCron Server

*noun*

The VisualCron engine that runs as a Windows service in the background and executes Jobs. The Server has an **On/Off** status (Server status) that is separate from the **Started/Stopped** status of its Windows service (Service status). The default communication port is 16444.

**Words users might use:** service, engine, agent

**Do not use:** agent (as a synonym for the VisualCron Server)

**See also:** Server status, Service status, VisualCron Client

---

### VisualCron variables

*noun*

The variable group (`{TASK(...)}`, `{JOB(...)}`, `{TRIGGER(...)}`, and related) that exposes VisualCron Job and Task data at run time. Described as the most powerful variables because they can access a large part of a Job's and Task's data.

**See also:** Variable

---

## W

### Web API

*noun*

An HTTP interface for interacting with VisualCron and extracting information. The Web API offers a REST style (with Text, XML, or JSON output and token or username/password authentication) and a SOAP web service. It is enabled under **Server -> Settings -> Web API**.

**See also:** API, VCCommand

---

### Web Client

*noun*

A browser-based interface for VisualCron, introduced in version 7.6.5, that provides access to Jobs and monitoring from a browser or phone.

**See also:** VisualCron Client, Mobile App

---

---

## Confusable and Legacy Terms

> **Do not use these terms in VisualCron documentation.** They are included
> so the AI can recognize them in source material, other-product content,
> and older releases — and map them to the correct VisualCron term.

### Agent

*noun* — CONFUSABLE

A term from other schedulers for the software installed on a machine that runs work. In VisualCron, the equivalent is the **VisualCron Server**. Remote execution is handled through **Connections** and **Credentials**, not a separate "agent."

**In documentation:** Use **VisualCron Server** for the local engine; use **Connection**/**Credential** for remote execution.

---

### Batch user

*noun* — CONFUSABLE

A term from other schedulers for the account a job runs under. In VisualCron, use **Credential** and **Execution context**.

---

### Frequency

*noun* — CONFUSABLE

A term from other schedulers for when a job runs. In VisualCron, use **Trigger** (specifically a **Time Trigger**).

---

### Schedule (as a noun for a job group)

*noun* — CONFUSABLE

In some schedulers, a "schedule" is a named collection of jobs. VisualCron has no such object — Jobs are the top-level schedulable objects, organized with **Groups** and **Job Folders**, and started by **Triggers**. Avoid using "schedule" as a noun for a container of Jobs.

> The word "schedule" is acceptable in general phrasing (for example, "schedule a Job to run nightly") and in feature names such as the **Schedule Calendar**.

---

### Threshold

*noun* — CONFUSABLE

A term from other schedulers for a numeric flow-control value. In VisualCron, use a **Variable** (for example, a User variable) with **Conditions** and **Flow**.

---

### Plugin

*noun* — CONFUSABLE

In some products, an add-on connector is called a "plugin." In VisualCron, the equivalent capabilities are delivered as **Task types** and **Connection** protocols.

---

---

## Quick Reference: Object Model

| Object | Role in the flow | Contains / references |
|--------|------------------|-----------------------|
| **Trigger** | Starts a Job (time or event) | — |
| **Condition** | Checks evaluated before a Job or Task runs | — |
| **Job** | The schedulable container | Triggers, Conditions, Tasks, Flow, Notifications, Job variables |
| **Task** | A single unit of work; runs as its own process | Task type, Conditions, Flow, Notifications, Timeout |
| **Notification** | Delivers a result for a Job or Task | Any Task type |
| **Flow** | Control layer for on-error, conditions, notifications | Events and actions |
| **Connection** | Global endpoint definition | Referenced by Tasks |
| **Credential** | Global run-as account | Referenced by Tasks and Triggers |
| **Variable** | Dynamic value token `{...}` | System, Date, Job, Task, User data |

The canonical flow is: **Trigger > Condition > Task > Notification**.

---

## Quick Reference: Trigger Types

| Type | When to Use | Examples |
|------|-------------|----------|
| **Time Trigger** | Run on a time schedule | Interval (every N minutes), Custom (specific days/times) |
| **Event Trigger** | Run in response to a system event | File change, Process, Service, Event Log, Mail, SQL, HTTP/REST |

---

## Quick Reference: VisualCron Roles

| Role | Primary Responsibility |
|------|----------------------|
| **System Administrator** | Install, configure, secure, and maintain the VisualCron Server and Client |
| **Automation Engineer** | Build and maintain Jobs, Tasks, Triggers, Conditions, Connections, and Variables |
| **Operations Staff** | Monitor running Jobs and respond to failures |
| **Integration Developer** | Automate VisualCron through the .NET API, PowerShell, Web API, and VCCommand |
| **Manager / Stakeholder** | Understand outcomes, ROI, and SLA reporting |

---

## Quick Reference: Key Terminology Rules

| Correct Term | Do Not Use |
|---|---|
| **Job** | "Task," "process" (for the container) |
| **Task** | "Job," "step," "action" (for the unit of work) |
| **Task type** | "Activity," "action" |
| **Trigger** | "Frequency," "schedule" (as an object) |
| **Condition** | "Dependency" (for a pre-run check) |
| **Dependency** | "Condition" (for a Trigger AND relationship) |
| **Notification** | "Event," "alert" |
| **Connection** | "Profile," "endpoint" |
| **Credential** | "Batch user," "service account" |
| **Variable** | "Property," "threshold" |
| **VisualCron Server** | "Agent," "engine" (as the primary name) |
| **VisualCron Client** | "Console," "portal" |
| **Server status** vs **Service status** | Using them interchangeably |
