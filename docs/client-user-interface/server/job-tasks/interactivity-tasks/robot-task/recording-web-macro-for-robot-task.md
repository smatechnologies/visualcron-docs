---
sidebar_label: 'Recording Web Macro for Robot Task'
hide_title: 'true'
---

## Recording Web Macro for Robot Task

This page shows how to record browser actions with the [Web Macro Task](../../net-tasks/web-macro) recorder and copy them into a Robot Task sequence, which is faster than building [Web Macro activities](activities/web-macro) one by one.

### Why use this approach

- The recorder captures the browser interactions for you, including element paths and navigation steps
- Recorded actions can be reused and refined rather than built from scratch
- The pasted actions in the Robot Task work the same as Web Macro activities you configure yourself

### Record and copy into a Robot Task

1. Add a Web Macro Task to a Job. It is only a workspace for recording.

   :::warning

   A Web Macro Task in an active Job runs whenever the Job runs. Record in a Job that is not active, or delete the Web Macro Task when you have copied the actions.

   :::

2. In the Web Macro Task, click _Record_ and go through the browser interactions you want to automate, from opening the browser to the last action.
3. Stop the recording.
4. When you are asked whether to save the recorded actions, click _Yes_.
5. In the recorded action list, right-click the _Launch New Instance_ action and select _Copy_.

   Copy the _Launch New Instance_ action, not the top-level _Sequence_. Copying the _Sequence_ does not bring over the _Open Browser_ action correctly.

6. Open the Robot Task and paste the action inside its existing _Sequence_. The _Open Browser_ action appears as the parent, with _Launch New Instance_ inside it.
7. Add any further Robot Task activities after the pasted Web Macro block: mouse actions, keyboard input, file operations, loops or any other activity from the activity list.

### Structure reference

When Web Macro actions are placed correctly in a Robot Task, the hierarchy looks like this:

```text
Sequence
  └── Open Browser
        └── Launch New Instance
              ├── [recorded action 1]
              ├── [recorded action 2]
              └── ...
```

All Web Macro child actions must be inside the _Launch New Instance_ action, which itself must be inside _Open Browser_.

### Tips

- After pasting, review each recorded action and rename it with its _Display name_ property, so that the sequence stays readable
- If the target website changes after recording (a redesign, or updated elements), record again and replace the pasted block, because the element paths captured during recording may no longer be valid; see [Element Path](activities/element-path)
- You can record several Web Macro Tasks and copy blocks from each into one Robot Task, to combine workflows across different sites
