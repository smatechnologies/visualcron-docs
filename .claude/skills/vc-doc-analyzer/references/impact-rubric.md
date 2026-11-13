# Impact Rubric

Use this rubric to assign **High**, **Medium**, or **Low** impact to each
finding in the analysis report. Impact reflects the potential harm to a reader
who relies on the documentation.

VisualCron is a Windows automation and scheduling platform that runs
unattended, with broad privileges, against file systems, databases, mail
servers, remote hosts, and Active Directory. It is deployed in production at
organizations including financial institutions, and serves as the RPA agent
for OpCon. Three properties of the product raise severity above what a
comparable web application would warrant:

- **Unattended execution.** Nobody is watching when the doc's advice plays out.
- **Silent Variable resolution.** An unresolvable Variable does not stop a Job;
  it resolves to empty or literal text and the Job proceeds with wrong input.
- **Destructive Task types.** File delete/move/overwrite, service control,
  registry writes, AD modification, and SQL execution are first-class Tasks.

Apply this context when assessing severity.

---

## High Impact

Assign **High** when the finding could cause any of the following if a reader
acts on (or fails to act on) the documentation as written:

- **Data loss or destructive action** — a wrong field name, wrong default, or
  missing warning on a File, Database, Service, Registry, or Active Directory
  Task that could delete, overwrite, or corrupt
- **Silent wrong-value execution** — incorrect Variable syntax, a renamed
  Variable key, or wrong scope prefix. The Job succeeds and produces wrong
  output; this is worse than a failure and always High
- **Credential or Connection security exposure** — missing or incorrect
  documentation of authentication, credential storage, certificate/trust
  configuration, token handling, or Web API access control
- **Missed or duplicated runs** — wrong Trigger behavior, schedule, time
  zone/DST, concurrency, or "run missed" semantics documented incorrectly
- **Permission and separation-of-duties errors** — undocumented or wrong
  User/Group permission requirements, or audit-log behavior that affects
  regulatory workflows
- **Undocumented breaking change** — a Task field, API member, or behavior
  changed incompatibly with no documentation update
- **Zero coverage for a live, user-facing surface** — a Task type, Trigger,
  Connection type, Variable, or API route that exists in the product with no
  documentation at all
- **Contradiction between VisualCron and OpCon docs** on the same integration
  behavior — readers cannot tell which side is authoritative

---

## Medium Impact

Assign **Medium** when the finding would cause confusion, rework, or support
escalation, but is unlikely to cause data loss, security exposure, or a wrong
successful run:

- **Missing optional field** — a Task field is undocumented but its absence
  does not break the default workflow
- **Vague or incomplete procedural steps** — steps that leave a reader
  uncertain but not unable to finish
- **Stale menu path or UI label** — the doc names a path or label that has
  changed, but the underlying capability works the same way
- **Missing version gate** — a version-gated capability documented without its
  introducing release; readers on older builds waste time
- **Missing error or exit-code coverage** — a known failure mode is
  undocumented; readers hit it without guidance
- **Missing cross-reference** — a procedural page does not link to the
  Connection, Credential, or Variable setup it depends on
- **Incomplete Trigger output documentation** — the Trigger is documented but
  its emitted Variables are only partially listed
  *(escalate to High if the emitted Variables are omitted entirely — downstream
  Tasks will silently receive nothing)*

---

## Low Impact

Assign **Low** when the finding is a quality or completeness issue that does
not affect a reader's ability to use the capability correctly:

- **Minor wording ambiguity** — imprecise but not misleading
- **Object-noun casing drift** — "job" or "task" lowercase where the docs
  conventionally capitalize Job, Task, Trigger, Condition, Connection
- **Structural gap** — a page missing an Examples or Related Topics section
  but otherwise complete and correct
- **Stale version note** — a note referencing a release older than the oldest
  supported version
- **Redundant content** — accurate information repeated across pages
- **Orphaned but correct page** — reachable by URL, absent from the sidebar

---

## Escalation Rules

**When unsure between two levels, assign the higher level.** VisualCron runs
unattended with broad privileges; the cost of a misconfiguration a reader
cannot see is high.

Two automatic escalations:

1. **Anything touching Credentials, Connections, permissions, or the Web API
   token is High by default.** Demote only with an explicit reason recorded in
   the finding.
2. **Anything that could cause a Job to succeed with wrong data is High**,
   even if the individual field seems trivial. Silent wrongness outranks loud
   failure.

---

## Confidence is separate from impact

Do not lower an impact rating because your evidence is weak. Rate impact on
the harm if the finding is real; record confidence separately via the Evidence
Tier field.

A High-impact finding backed only by Tier E belongs in the report as **High
impact, Tier E, needs confirmation** — not as Medium. Downgrading severity to
express uncertainty hides risk from the reader.

If you cannot establish that the finding is real at all, it does not get an
impact rating — it goes to Section 6 (Unverifiable).

---

## Not a Finding

Do not log these:

- Internal implementation details not intended for user-facing documentation
- Test code, internal tooling, or developer-only members not exposed to customers
- Differences explained by a version mismatch between docs and product that you
  have already flagged in the report header
- A capability absent from a Tier D export but never claimed to be removed —
  absence from one server's configuration is not absence from the product
- Marketing copy on visualcron.com that differs from the docs — the docs are
  authoritative for behavior, not the website
- Stylistic preferences not covered by the VisualCron documentation standards
- Content that is accurate even if phrased differently than you would prefer
