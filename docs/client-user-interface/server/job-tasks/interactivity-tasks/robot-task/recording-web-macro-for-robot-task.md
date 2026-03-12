---
sidebar_label: 'Recording Web Macro for Robot Task'
hide_title: 'true'
---

## Recording Web Macro for Robot Task

The Robot Task supports Web Macro actions natively, but building them action by action manually can be time consuming. A faster approach is to use the **Web Macro Recorder** to capture your browser interactions, then copy those recorded actions directly into your Robot Task sequence.

### Why Use This Approach

- The recorder captures all browser interactions automatically, including element paths, timing, and navigation steps
- Recorded actions can be reused and refined rather than built from scratch
- The resulting actions inside the Robot Task behave the same as manually configured Web Macro actions

### Step-by-Step: Record and Copy into Robot Task

**1. Create a Web Macro Task**

Add a new task to your job and select **Web Macro** as the task type. This is a temporary workspace for recording — it will not need to be scheduled or run on its own.

**2. Record Your Actions**

Inside the Web Macro Task, open the **Recorder** and walk through the browser interactions you want to automate. Record all steps from opening the browser through the final action.

Once finished, click **Stop**, then click **Yes** when prompted to save the recorded actions.

**3. Copy the Launch New Instance Action**

In the recorded action list, right-click the **Launch New Instance** action and select **Copy**.

> **Important:** Copy the *Launch New Instance* action — not the top-level *Sequence*. Copying the Sequence will not bring over the *Open Browser* action correctly.

**4. Paste into Your Robot Task**

Open your Robot Task and paste the copied action inside the existing **Sequence**. The *Open Browser* action will automatically appear as the parent, with *Launch New Instance* nested inside it as expected.

**5. Continue Building**

You can now continue adding additional Robot Task actions after the pasted Web Macro block — mouse actions, keyboard input, file operations, loops, or any other activity from the activity list.

### Structure Reference

When Web Macro actions are correctly placed in a Robot Task, the hierarchy should look like this:

```
Sequence
  └── Open Browser
        └── Launch New Instance
              ├── [recorded action 1]
              ├── [recorded action 2]
              └── ...
```

All Web Macro child actions must be inside the **Launch New Instance** action, which itself must be inside **Open Browser**.

### Tips

- After pasting, review each recorded action and rename it using the **Display Name** field so your sequence stays readable
- If the target website changes after recording (redesign, updated elements), re-record the Web Macro and replace the pasted block — the element paths captured during recording may no longer be valid
- You can record multiple Web Macro Tasks and copy blocks from each into a single Robot Task to combine workflows across different sites or applications
