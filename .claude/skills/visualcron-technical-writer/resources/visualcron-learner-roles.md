# Learner Role Guidelines

Guidelines for understanding the audiences that use VisualCron. Use these guidelines to produce accurate, audience-appropriate documentation for each role. VisualCron is a general-purpose Windows automation and job-scheduling tool used across IT teams in many industries — these roles describe IT functions, not a specific vertical.

## Section Reference

Each role description includes the following sections:

| Section | Purpose |
|---------|---------|
| Who they are | Understand the audience and correctly describe the role in documentation |
| Why they matter | Frame content around value |
| Knowledge domains | Identify relevant topics — conceptual and durable, not tied to nav structure |
| Key terminology | Focus vocabulary when writing for this audience |
| This role does NOT | Prevent including out-of-scope content |
| Common overlap | Handle edge cases where roles share responsibilities |
| Tone adjustment | Calibrate writing style per audience |
| Assume they understand | Prevent over-explaining known concepts and under-explaining unfamiliar ones |

## Decision Framework

When writing documentation, identify the primary audience by role. Use that role's guidelines to determine appropriate terminology, scope, tone, and assumed knowledge. If a page serves multiple roles, use the least technical audience's tone while respecting the knowledge boundaries of all roles involved.

---

## 1. System Administrator

**Who they are:** Infrastructure staff responsible for installing, configuring, securing, and maintaining VisualCron — the Server service, the Client, licensing, user permissions, credentials, security settings, and (where used) failover clustering. In smaller teams, the System Administrator and Automation Engineer roles are often the same person.

**Why they matter:** They keep VisualCron running. Without correct installation, service configuration, credentials, and security, automation stops. They are the foundation everything else depends on.

**Knowledge domains:**
- Installing, upgrading, and uninstalling VisualCron (Client and Server)
- Software and hardware requirements (Windows, .NET Framework 4.8)
- Configuring the VisualCron Server service and the LOCALSYSTEM account context
- Managing Credentials, including (g)MSA accounts and execution context
- User permissions and permission groups (Administrators, Viewers, custom groups)
- Security settings, TLS between Client and Server, and AES-256 encryption of stored values
- Licensing, activation, maintenance, and moving licenses
- Server settings (email, proxy, folders, logging, Web API, Web Client)
- Clustered and failover-cluster deployments
- Backup and server health monitoring

**Key terminology:** VisualCron Server, VisualCron Client, service status, server status, Credential, execution context, user permissions, permission group, license, activation, Web API, Server settings, cluster, health

**This role does NOT:**
- Build or maintain Jobs and Tasks (that is the Automation Engineer's responsibility)
- Monitor running Jobs in real time (that is the Operations Staff's responsibility)
- Automate VisualCron through the API (that is the Integration Developer's responsibility)

**Common overlap:** In smaller teams, System Administrators and Automation Engineers are often the same person. Documentation for System Administrators should focus on infrastructure, the service, security, and configuration — not on Job design or daily monitoring.

**Tone adjustment:** Highly technical audience. Comfortable with Windows Server, services, accounts, certificates, group policy, and networking. Prioritize precision, exact steps, and technical accuracy. They appreciate concise instructions without lengthy conceptual explanation.

**Assume they understand:** Windows Server administration, Windows services, user accounts and (g)MSA, Local Security Policy, TLS/certificates, DNS, SMTP, UNC paths, and general networking.

---

## 2. Automation Engineer

**Who they are:** The people who build and maintain automation in VisualCron — Jobs, Tasks, Triggers, Conditions, Connections, Credentials, Variables, and Flow. They translate requirements into working, reliable automation.

**Why they matter:** They are the builders. The quality of their Jobs and Tasks determines whether automation is reliable, maintainable, and correct.

**Knowledge domains:**
- Creating and configuring Jobs (Groups, run options, queueing, Job variables)
- Adding and configuring Tasks and choosing the right Task type
- Setting up Time Triggers and Event Triggers, and combining them with dependencies
- Configuring Conditions at the Job and Task level
- Building Flow for on-error handling, retries, and notifications
- Creating and reusing global Connections, Credentials, and Notifications
- Using VisualCron variables to pass dynamic values between Triggers, Tasks, and outputs
- Testing Jobs, reading Task output, and debugging failures
- Organizing Jobs with Job Folders and the Task Repository

**Key terminology:** Job, Task, Task type, Trigger, Time Trigger, Event Trigger, Condition, Flow, Connection, Credential, Variable, Notification, dependency, execution context, output, exit code

**This role does NOT:**
- Install or maintain the VisualCron Server or its service (System Administrator)
- Monitor running Jobs during operations (Operations Staff)
- Write external code against the VisualCron API (Integration Developer)

**Common overlap:** Automation Engineers frequently also perform Operations duties. Documentation for this role should focus on designing and configuring automation, not on infrastructure or real-time monitoring.

**Tone adjustment:** Technical audience comfortable with scripting, command lines, and system concepts. They want precise instructions with clear explanations of how configuration choices affect behavior. They value the reasoning behind design decisions, not just the steps.

**Assume they understand:** Basic scripting and command-line concepts, how job scheduling works generally, and intermediate Windows administration. Do not assume they administer the VisualCron Server service or write API integrations.

---

## 3. Operations Staff

**Who they are:** The people who monitor running Jobs, watch for failures, and keep the day's automation completing successfully. They work in the Grid, the Tray Client, the Web Client, or the Mobile App, and they read logs and respond to problems.

**Why they matter:** When something goes wrong, they respond. Without attentive operations coverage, failed Jobs go undetected and downstream processes are affected.

**Knowledge domains:**
- Monitoring Jobs and Tasks in the Grid and through the Web/Tray/Mobile clients
- Understanding Job and Task states and what each requires in response
- Running, stopping, activating, and deactivating Jobs manually
- Reading Job logs, Task logs, and Task output to diagnose failures
- Managing and responding to Notifications
- Using the Server monitor, Task Manager view, and health/SLA views
- Escalating unresolved issues to Automation Engineers or Administrators

**Key terminology:** Grid, Job List, Task List, run, stop, activate, deactivate, Job log, Task log, output, Notification, Server monitor, health, SLA

**This role does NOT:**
- Build or modify Job and Task definitions (Automation Engineer)
- Configure the Server, credentials, or permissions (System Administrator)
- Write API integrations (Integration Developer)

**Common overlap:** In smaller teams, Operations Staff also build automation. Documentation for this role should focus on real-time monitoring and response, not on how Jobs are designed or how the Server is maintained.

**Tone adjustment:** Task-oriented, time-pressured audience, often responding to an active problem. Instructions must be fast to scan and clearly stated, focused on the specific action required. Avoid lengthy explanation — they need to know what to do now.

**Assume they understand:** What automation is and why it matters, basic VisualCron Client navigation, how to read a Job/Task status, and who to escalate to. Do not assume they understand Job configuration or Server administration.

---

## 4. Integration Developer

**Who they are:** Developers who automate and extend VisualCron programmatically — through the .NET API (C#/VB.NET), PowerShell, the Web API (REST/SOAP), and the VCCommand command-line tool. They connect VisualCron to other systems and automate the management of VisualCron itself.

**Why they matter:** They enable VisualCron to fit into larger toolchains — provisioning Jobs from code, extracting status for dashboards, and triggering automation from external systems.

**Knowledge domains:**
- Using the .NET API (the same API the Client uses) to manage Servers, Jobs, Tasks, Connections, and Variables
- Referencing the VisualCron API DLLs and handling API versioning
- Automating VisualCron with PowerShell
- Calling the Web API over REST (Text/XML/JSON) with token or credential authentication
- Using the SOAP web service where required
- Running the VCCommand tool for scripted control of a local or remote Server
- Reading the in-app API reference (Help > API)

**Key terminology:** .NET API, VisualCronAPI.dll, PowerShell, Web API, REST, SOAP, token, method, VCCommand, Client object, Server object

**This role does NOT:**
- Install or maintain the Server infrastructure (System Administrator)
- Design production Job logic as a primary duty (Automation Engineer), though they often generate Jobs programmatically
- Monitor daily operations (Operations Staff)

**Common overlap:** Integration Developers work closely with Automation Engineers when generating or modifying Jobs from code, and with Administrators on authentication and permissions for the Web API.

**Tone adjustment:** Developer audience. They want accurate method signatures, parameter details, authentication specifics, and working code samples. Be precise about types, endpoints, and return values. Do not over-explain general programming concepts.

**Assume they understand:** .NET or PowerShell fundamentals, HTTP and REST, authentication tokens, and how to reference libraries. Do not assume they know VisualCron's internal object model without a clear conceptual map.

---

## 5. Manager / Stakeholder

**Who they are:** Team leads, IT managers, and business stakeholders who care about the outcomes of automation — what it saves, whether it is meeting service levels, and whether it is reliable. They typically do not configure VisualCron directly.

**Why they matter:** They justify and prioritize automation work. Their view of value, cost, and reliability drives investment and adoption.

**Knowledge domains:**
- Understanding what VisualCron automates and the value it delivers
- Reading ROI (Return On Investment) figures for automated Jobs
- Understanding SLA reporting (uptime, outages, latency)
- Reviewing high-level Job status and reports
- Understanding the impact when automation fails

**Key terminology:** ROI, SLA, uptime, Job, report, value

**This role does NOT:**
- Configure Jobs, Tasks, or the Server
- Monitor the Grid in real time
- Resolve technical failures
- Write integrations

**Common overlap:** Managers may also be Administrators in very small teams. Documentation for this role should connect features to outcomes and value, not to configuration mechanics.

**Tone adjustment:** Business-focused, less technical audience. Avoid deep VisualCron jargon. Focus on outcomes, value, and reliability. Use plain language and concrete examples.

**Assume they understand:** Their own operational goals and what "success" looks like. Do not assume they understand VisualCron configuration, Task types, or the API.

---

## Universal (All Roles)

This is not a separate role — readers don't self-identify as "Universal." It is an **audience designation** the writer chooses when no single role applies.

**When to use:**
- Content is conceptual, introductory, or an overview — the reader's specific role doesn't change what they need to know
- Source material is a product overview, feature introduction, or foundational explainer for any VisualCron user
- The team has combined roles and the reader's specific role is unknown (one person installs, builds, and monitors)
- The page is first-contact or getting-started content

**When NOT to use:**
- Any procedural content where steps, UI access, or available actions depend on the reader's role or permissions
- Content that requires domain knowledge specific to a single role (how to build a Job, how to configure the Server service, how to call the API)
- Any content where operational stakes differ by role — use the role with the highest stakes instead

**Assumed knowledge:** General Windows IT literacy. No VisualCron terminology, no scheduling concepts, and no prior product exposure assumed. If a reader has never opened the VisualCron Client, they should be able to follow Universal content without stopping to ask what a word means.

**Tone:** Patient, foundational, welcoming. Lead with a need the reader already recognizes — a routine task that needs to run reliably and unattended. Follow with how VisualCron addresses it. Define every VisualCron term the first time it appears. No jargon without explanation.

**Pitch level:** Use Manager / Stakeholder as the floor for tone, but include the concrete detail a general IT reader needs. If a non-specialist IT reader would follow it without confusion, all roles will.

**Note on combined roles:** In smaller teams, one person often installs VisualCron, builds Jobs, and monitors them. Universal content serves this reader without requiring them to identify which hat they are wearing at any given moment.
