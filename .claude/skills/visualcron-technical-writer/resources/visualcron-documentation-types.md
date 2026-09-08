# Documentation Types

Every documentation page falls into one of three types. Before writing or reviewing a page, identify its type and follow the corresponding structure. If a page combines types (for example, a conceptual overview followed by a procedure), use the structure for each section independently.

---

## How to Identify the Type

```
What is the reader trying to do?

  "I need to understand something."      → Conceptual
  "I need to do something."              → Procedural
  "I need to look something up."         → Reference
```

---

## 1. Conceptual Documentation

**Purpose:** Build understanding of broader ideas, principles, or how things connect. Helps readers understand what a feature is for, why it works a certain way, and when they would use it.

**When to use:** Overviews, introductions, feature explanations, "how it works" topics, and "why" explanations.

### Structure

| Section | Required | Description |
|---|---|---|
| Title (`## H2`) | Yes | Clear, descriptive title in sentence case. Answers "what is this about?" |
| Introduction | Yes | 1–3 sentences explaining what the topic covers and why it matters. State the value upfront. |
| Body | Yes | The explanation itself. Organize by subtopic, not chronologically. Use headings to break up distinct concepts. |
| Diagrams or examples | When helpful | Use diagrams, analogies, or real-world examples to make abstract concepts concrete. |
| How it connects | When applicable | Explain how this concept relates to other objects (Job, Task, Trigger, Condition, Flow). Link to related pages. |
| Related topics | When applicable | Links to related pages. |

### Guidelines

- Lead with **why it matters**, not just what it is
- Explain concepts in terms the target audience already understands (consult learner-roles)
- Use concrete, general IT examples (a nightly file transfer, a database export, a service restart)
- Do not include step-by-step instructions — link to the procedural page instead
- Keep paragraphs short (3–5 sentences)

### Example

```markdown
---
sidebar_label: 'How Triggers Work'
hide_title: 'true'
---

## How Triggers work

A Trigger is the object that starts a Job. Every Job needs at least one
Trigger. Triggers let VisualCron run a Job on a time schedule or in
response to a system event, so automation happens without anyone starting
it manually.

## Time versus event Triggers

A Time Trigger starts a Job based on the clock — on an interval or at
specific dates and times. An Event Trigger starts a Job when something
happens on the system, such as a file arriving in a folder or a service
stopping. Most event Triggers are based on Windows Management
Instrumentation (WMI).

## How multiple Triggers combine

A Job can have more than one Trigger. By default they combine as an OR
relationship, so any single Trigger can start the Job. To require a
combination of Triggers, use a dependency to create an AND relationship.

**Related topics:**

- [Add a Time Trigger to a Job](../server/time-triggers.md)
- [Add an Event Trigger to a Job](../server/event-triggers.md)
```

---

## 2. Procedural Documentation

**Purpose:** Explain how to do something in a sequential order using step-by-step instructions.

**When to use:** Any task the reader needs to complete — installing, configuring, creating a Job or Task, setting up a Connection, or any workflow with a defined sequence.

### Structure

| Section | Required | Description |
|---|---|---|
| Title (`## H2`) | Yes | Starts with a verb or describes the task clearly. Example: "Add a Task to a Job." |
| Introduction | Yes | 1–2 sentences stating what the procedure accomplishes and when to do it. |
| Prerequisites | When applicable | What must be true or completed before starting. Use an admonition. |
| Steps | Yes | Numbered, sequential, one action per step. Follows all rules in documentation-standards. |
| Result statement | Yes | Final step or sentence describing what changed. |
| Related topics | When applicable | Links to next steps or related procedures. |

### Guidelines

- Follow all procedural rules in documentation-standards (action verbs, one action per step, ~10 step limit)
- State the goal before the steps: "To [accomplish goal], complete the following steps:"
- Put prerequisites before the steps, not buried within them
- End with a result statement so the reader knows they succeeded
- Link to other procedures rather than duplicating steps

### Example

```markdown
---
sidebar_label: 'Add a Task to a Job'
hide_title: 'true'
---

## Add a Task to a Job

Add a Task to define a unit of work that runs when the Job runs. A Job
needs at least one Task.

:::note
The Job must exist before you can add a Task. See
[Add a Job](../server/jobs-jobs.md).
:::

To add a Task, complete the following steps:

1. In the Grid, right-click the Job and select _Edit_. The _Edit Job_ dialog is displayed.
2. Select the **_Tasks_** tab.
3. Select the _Add_ button. The _Add Task_ dialog is displayed.
4. Select the _Task type_ field and pick a Task type from the list.
5. In the _Name_ field, enter a name for the Task.
6. Configure the Task-type settings.
7. Select the _Save_ button. The Task is added to the Job.

**Related topics:**

- [How Tasks work](how-does-visualcron-work.md)
- [Add a Trigger to a Job](../server/job-triggers.md)
```

---

## 3. Reference Documentation

> For Task-type and parameter descriptions specifically, consult
> [visualcron-parameter-descriptions.md](visualcron-parameter-descriptions.md).
> For API documentation, do NOT use the reference template below — follow
> [visualcron-api-reference.md](visualcron-api-reference.md).

**Purpose:** Provide factual information that readers look up quickly. Organized for scanning, not reading start to finish.

**When to use:** UI field and setting definitions, Task-type lists, Trigger-type lists, Connection-protocol lists, variable references, requirements, and any factual lookup content.

### Structure

| Section | Required | Description |
|---|---|---|
| Title (`## H2`) | Yes | Names the reference subject clearly. |
| Introduction | Yes | 1–2 sentences explaining what information is provided and how it is organized. |
| Reference content | Yes | Tables, definition lists, or organized sections, sorted logically. |
| Notes or caveats | When applicable | Important context about limitations, special cases, or version differences. |

### Guidelines

- Optimize for **scanning**, not reading
- Use tables as the primary format
- Sort content in the order that makes sense for lookup (alphabetical, by category, or by UI order)
- Keep descriptions factual and concise — one to two sentences per item
- Include all items completely — reference docs must not have gaps

### Example

```markdown
---
sidebar_label: 'Trigger Types'
hide_title: 'true'
---

## Trigger types

VisualCron Triggers start a Job either on a time schedule or in response
to a system event. This page lists the Trigger types by category.

## Time Triggers

| Type | Description |
|---|---|
| Interval time trigger | Runs the Job every N seconds, minutes, or hours. |
| Custom time trigger | Runs the Job on specific dates, days, and times. |

## Event Triggers

| Type | Description |
|---|---|
| File | Runs the Job when a file is created, changed, or deleted. |
| Process | Runs the Job when a process starts or stops. |
| Service | Runs the Job when a Windows service changes state. |
| Event Log | Runs the Job when a matching entry is written to the Windows Event Log. |
```

---

## Combining Types on a Single Page

Some pages naturally combine types. When this happens:

1. **Identify the primary type** — this determines the page's overall structure and title
2. **Use clear section breaks** between types — a heading should signal the shift
3. **Keep each section's rules independent** — conceptual sections follow conceptual guidelines, procedural sections follow procedural guidelines

### Common Combinations

| Primary Type | Secondary Type | Example |
|---|---|---|
| Conceptual | Procedural | Feature overview followed by "Getting started" steps |
| Procedural | Reference | Setup procedure followed by a settings/options table |
| Conceptual | Reference | Explanation of a concept followed by a terminology or comparison table |

### What NOT to Do

- Do not embed a full procedure inside a conceptual explanation — link to it instead
- Do not scatter reference tables throughout a procedure — put them after the steps
- Do not write a reference page in paragraph form — use tables and lists

---

## Common Mistakes

### Conceptual page that should be procedural
❌ "The Job build process begins when you select the Add button and then choose the Task type..." (narrative description of steps)
✅ Link to the procedural page instead

### Procedural page with buried prerequisites
❌ Step 7: "Note: The Server must be On to run the Job."
✅ State prerequisites before the steps begin

### Reference page written as prose
❌ "The File Trigger runs the Job when a file is created, and it also supports change and delete events..."
✅ Use a table with columns for Type and Description

---

## Connecting Types to Audience

When writing a page, combine the documentation type (from this file) with the audience role (from visualcron-learner-roles.md):

| Step | Question | Source |
|---|---|---|
| 1 | Who is reading this? | visualcron-learner-roles.md |
| 2 | What are they trying to do? | This file (visualcron-documentation-types.md) |
| 3 | How should I write it? | visualcron-documentation-standards.md |

The **audience** determines tone, terminology depth, and assumed knowledge. The **type** determines structure and organization. The **standards** determine formatting and style. All three work together.
