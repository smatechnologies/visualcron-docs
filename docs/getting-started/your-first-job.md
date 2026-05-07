---
sidebar_label: 'Your First Job'
sidebar_position: 4
description: Create and run your first automated PowerShell job in VisualCron using the inline script editor.
---

# Your First Job

In this guide you will create a job that runs a PowerShell script on a schedule. The script is written directly inside VisualCron — no external files needed. By the end you will have a working scheduled job and understand the core **Trigger → Task → Notification** pattern.

---

## The Execution Model

Before you start, the key concept to understand is:

```
Trigger → Task → Notification
```

| Part | What it does |
|---|---|
| **Job** | The container — holds everything below |
| **Trigger** | What fires the job (a schedule, a file event, etc.) |
| **Task** | The actual work (run a script, send an email, copy a file, etc.) |
| **Notification** | Optional alert on success or failure |

---

## Step 1 — Create a new Job

Click **Add Job** in the toolbar at the top of the main window.

<figure>

![VisualCron toolbar showing the Add Job button highlighted with a red box, alongside Edit Job, Clone Job, Delete Job, Run Job, and Grid filter buttons](/img/getting-started/your-first-job/add-job-toolbar.png)

<figcaption><em>Fig. 1 — The main toolbar. Add Job opens the job dialog. You can also right-click anywhere in the Jobs grid and select Add Job.</em></figcaption>
</figure>

The job dialog opens on the **Main settings** tab. Fill in:
- **Name** → `My First Scheduled Script`
- **Description** → `Writes a timestamped entry to a log file on the Desktop`

Leave all other options at their defaults for now.

<figure>

![Add Job dialog showing the Main settings tab with Name set to "My First Scheduled Script" and Description filled in, alongside the Triggers, Time exceptions, Conditions, Tasks, TimeOut, Flow, and Agentdistribution tabs](/img/getting-started/your-first-job/main-settings-tab.png)

<figcaption><em>Fig. 2 — The Main settings tab. The tabs along the top — Triggers, Conditions, Tasks, Flow — are where the job's logic lives.</em></figcaption>
</figure>

---

## Step 2 — Add a Time Trigger

Click the **Triggers** tab, then click **Add**.

A list of trigger types appears. Select **Time trigger**.

The time trigger dialog opens. It has four top-level tabs: **Settings**, **Interval**, **Custom**, and **Expire**. Click **Custom**.

Within the Custom tab there are six sub-tabs: **Year**, **Month**, **Day**, **Hour**, **Minute**, and **Second**. Work through these three:

**Day sub-tab**

1. Select **Choose weekday(s)**
2. In the *Choose weekday(s)* panel on the right, click **Deselect all**
3. Check **Monday**, **Tuesday**, **Wednesday**, **Thursday**, **Friday**

<figure>

![Time trigger Custom tab, Day sub-tab, with Choose weekday(s) selected and Monday through Friday checked in the right-hand panel](/img/getting-started/your-first-job/time-trigger-day.png)

<figcaption><em>Fig. 3 — The Day sub-tab with Choose weekday(s) selected. Use the Deselect all button on the right panel, then check only Mon–Fri. The Next run time at the bottom updates live as you make changes.</em></figcaption>
</figure>

**Hour sub-tab**

1. Select **Choose hour(s)**
2. Click **Deselect all**
3. Check **7**

**Minute sub-tab**

1. Select **Choose minute(s)**
2. Click **Deselect all**
3. Check **0**

The **Second** sub-tab defaults to `0` — leave it as-is.

Click **Ok**. The bottom of the dialog shows the calculated **Next run** time before you confirm.

---

## Step 3 — Add a PowerShell Task

Click the **Tasks** tab, then click **Add Task**.

In the task picker, navigate to **Process → PowerShell** and select it.

<figure>

![Task type picker dialog showing task categories listed on the left with task types in the centre panel, PowerShell highlighted under the Process group](/img/getting-started/your-first-job/powershell-picker.png)

<figcaption><em>Fig. 4 — The Add Task picker. Browse by category on the left or use the search bar at the bottom to find PowerShell under the Process group.</em></figcaption>
</figure>

In the PowerShell task editor:

1. Click the **Script** tab
2. Select **PowerShell script text** (the lower radio button)
3. Paste the following script into the code editor:

```powershell
$logDir  = "C:\VC-Logs"
$logFile = "$logDir\hello-world.txt"

if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir | Out-Null
}

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Add-Content -Path $logFile -Value "Job ran at: $timestamp"
Write-Output "Success — logged to $logFile"
```

When it runs it:
- Creates `C:\VC-Logs\` if it does not already exist
- Appends a timestamped line to `hello-world.txt`
- Outputs a `Success` message that VisualCron captures and displays

:::warning Common pitfall: user-profile paths
VisualCron runs as a **Windows Service**, so environment variables like `$env:USERPROFILE` and `$env:APPDATA` resolve to the **service account's profile** — not your own. Paths like `Desktop\`, `Documents\`, and `AppData\` will either not exist or won't be writable, and the job will silently fail or error. Always use absolute paths (e.g. `C:\VC-Logs\`) in VisualCron tasks, or configure the task to run under a specific user credential via the **Credentials** setting on the task.
:::

4. Leave all other settings at their defaults

<figure>

![PowerShell task editor showing the Script tab with the hello-world script pasted into the inline code editor, with the PowerShell script text radio button selected](/img/getting-started/your-first-job/powershell-task-editor.png)

<figcaption><em>Fig. 5 — The PowerShell task editor. Paste your script directly into the inline editor — no external file needed. Syntax highlighting is applied automatically.</em></figcaption>
</figure>

Click **OK** to save the task.

---

## Step 4 — Save the Job

Click **Ok** on the job dialog. Your new job appears in the Jobs grid with a **Result** of *Not run yet* and a **Status** of *Waiting*.

---

## Step 5 — Run it Now

Don't wait for 7am — right-click the job in the grid and select **Run Job → Without Conditions → From first Task**.

<figure>

![Right-click context menu on "My First Scheduled Script" with the Run Job submenu expanded, showing Without Conditions and From first Task options](/img/getting-started/your-first-job/right-click-run-job.png)

<figcaption><em>Fig. 6 — Right-click the job and select Run Job → Without Conditions → From first Task to run it immediately. The Next run column confirms the trigger is set for 3/26/2026 at 7:00 AM.</em></figcaption>
</figure>

---

## Step 6 — Check the Output

After the job runs, expand it in the grid by clicking the arrow on the left. You will see your PowerShell task listed underneath.

<figure>

![Jobs grid showing "My First Scheduled Script" expanded with a PowerShell task row beneath it, displaying Status, Output, Output (error), Exit code, Result, Last run, and Execution time columns](/img/getting-started/your-first-job/output-check.png)

<figcaption><em>Fig. 7 — The expanded job row shows each task alongside its last run status, exit code, output, and execution time. Click the value in the Output column to open the full output viewer.</em></figcaption>
</figure>

A **green** status icon means success; **red** means a failure occurred. Click the value in the **Output** column to open the output viewer. You should see:

```
Success — logged to C:\VC-Logs\hello-world.txt
```

Then open `C:\VC-Logs\hello-world.txt` to confirm the log entry was written.

---

## What Just Happened

You built a complete automated job:

1. VisualCron's scheduler fires the trigger every weekday at 7:00am
2. The PowerShell task runs your inline script
3. The script writes to a log file and returns a success message
4. VisualCron captures the output and records the result

---

## Next Steps

- **Add a failure notification** — go back into the job, open the **Flow** tab, and add an email alert so you know if the script ever fails → [Notifications](../core-concepts/notifications)
- **Pass data between tasks** — use [Variables](../core-concepts/variables) to share values across tasks in the same job
- **Add conditions** — run tasks only when certain criteria are met → [Conditions](../core-concepts/conditions)
- **Explore all task types** — there are 416+ task types available → [Tasks](../tasks/process/execute)
