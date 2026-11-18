# Parameter and Field Descriptions

> For writing and formatting standards, see
> [visualcron-documentation-standards.md](visualcron-documentation-standards.md).

Guidelines for writing clear, consistent descriptions for VisualCron settings — Task-type parameters, Trigger and Condition fields, Connection settings, and the tooltips shown when a user hovers over a field, label, or list in the VisualCron Client.

> VisualCron's stated goal is to provide a tooltip for every field, label,
> and list in the Client. Hovering over a field is meant to give quick,
> reliable guidance on what to enter. These patterns keep that tooltip text
> consistent.

## Field Object Overview

Each configurable field in the Client generally has:

| Component | Purpose |
|-----------|---------|
| Name | The user-facing label shown in the UI |
| Description / tooltip | Explanatory text describing the field's effect |
| Type | The data type and input control (text, list, option, and so on) |
| Default | The value used when the field is left unset |

### Field Types

| Type | Use Case |
|------|----------|
| Option | A checkbox for a yes/no setting (most common) |
| Text | Single-line text input |
| Text area | Multi-line text input |
| Password | Masked input for a sensitive value |
| List | A selection from a fixed set of values |
| Variable-enabled field | A field that accepts VisualCron variables (`{...}`) |

## Quick Reference

| Field Type | Pattern | Example |
|----------------|---------|---------|
| Option (filter) | Results will include [items]. | Results will include Jobs that are currently inactive. |
| Option (toggle) | [Action/Feature] will be [enabled/applied]. | The Job will run only once and then be ignored. |
| Option (action) | Select this option to [action]. | Select this option to run the Tasks in order. |
| Credential / connection | Brief clarifying note. | The Credential used to run the Task. |
| Configuration | Defines/Specifies [what it sets]. | Specifies the interval between Trigger checks. |
| Variable-enabled | Note that the field accepts variables. | The target path. Supports VisualCron variables. |

## When to Include Descriptions

**Include descriptions when:**
- The field name alone is ambiguous
- Users need context about the effect
- There are important caveats or notes
- The field accepts VisualCron variables (say so)

**Omit descriptions when:**
- The field name is self-explanatory (for example, "Username," "Password")
- The purpose is obvious from context

## Description Patterns

### Option Fields (Filter)
Use when the option includes or excludes items in a result:

| Name | Description |
|------|-------------|
| Include inactive Jobs | Results will include Jobs that are currently inactive. |
| Include subfolders | Results will include files from subfolders. |

### Option Fields (Toggle)
Use when the option enables a behavior:

| Name | Description |
|------|-------------|
| Run once | The Job will run once and then be ignored on later checks. |
| Do not start if job is already running | A new run will be skipped while the Job is still running. |

### Option Fields (Action)
Use "Select this option to..." for clarity:

| Name | Description |
|------|-------------|
| Run Tasks in order | Select this option to run the Job's Tasks sequentially instead of in parallel. |
| Load profile | Select this option to load the Windows user profile for the Credential. |

### Credential and Connection Fields
Keep brief; clarify only when needed:

| Name | Description |
|------|-------------|
| Credential | The account used to run the Task. |
| Connection | The stored Connection used to reach the server. |

### Configuration Fields
Use "Defines" or "Specifies" for required settings:

| Name | Description |
|------|-------------|
| Polling interval | Specifies how often the Event Trigger checks for the event. |
| Timeout | Defines how long the Task may run before it is stopped. |

### Variable-Enabled Fields
State that the field accepts variables so users know they can insert dynamic values:

| Name | Description |
|------|-------------|
| Target path | The destination path for the file. Supports VisualCron variables. |
| Subject | The email subject line. Supports VisualCron variables. |

## Writing Guidelines

### Do
- Use present or future tense consistently
- Start filter descriptions with "Results will include..."
- Keep descriptions to one sentence when possible
- Be specific about what gets included, excluded, or changed
- Note when a field accepts VisualCron variables
- Use consistent terminology across similar fields (consult the glossary)

### Don't
- Use ambiguous terms like "may" or "might" — be definitive
- Add implementation details unless relevant to users
- Use bullet points or special formatting inside a tooltip
- Repeat information already conveyed by the field name
- Call a Task a "Job" or a Job a "Task"

### Common Mistakes

❌ "This might include inactive Jobs." (don't use "might" — be definitive)
❌ "Run once: Select this to run once." (redundant — don't repeat the field name)
❌ "Runs the job." (which object? Be precise: Job or Task)

## Caveats and Notes

For important context, append to the description:

```
Include subfolders
Results will include files from subfolders. Note: Including subfolders
can significantly increase the number of files processed.
```

## Checklist

- [ ] Description explains the field's effect
- [ ] Uses consistent tense (present or future)
- [ ] One sentence when possible
- [ ] Specific about what changes when the field is set
- [ ] Notes variable support where the field accepts `{...}`
- [ ] No redundant information from the field name
- [ ] Uses correct VisualCron terminology (Job vs Task, Trigger, Condition)
- [ ] Important caveats included when relevant
