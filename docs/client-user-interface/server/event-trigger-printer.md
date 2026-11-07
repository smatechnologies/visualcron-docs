---
sidebar_label: 'Event Trigger - Printer'
hide_title: 'true'
---

## Event Trigger - Printer

The Printer Trigger fires when a print job on a printer changes status in the Windows print spooler, for example when a document is spooled or printed. The Trigger reacts to spooler notifications as they happen; the *Polling interval* on the ***Main settings*** tab is not used.

:::note

The Trigger fires on every status change that matches, so one document can fire it several times, for example for *Spooling*, *Printing* and *Printed*. Check only the statuses you need.

:::

The *Computer name* in the *Remote event* group on the ***Main settings*** tab does not change which printers are listed or watched. When *Computer name* is neither "." nor exactly the name of the VisualCron Server computer (the comparison is case-sensitive), and a Credential is selected in the *Credentials* group on the ***Main settings*** tab, the Trigger runs as that Credential.

The settings are on the ***Printer*** tab.

![Printer tab of the Add/Edit event window with Printer name, Job name pattern, Checked job status, Job user pattern and Job machine pattern](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Printer.png)

**Printer**

**Printer name**

Select the printer to watch. The list shows the printers installed locally on the VisualCron Server computer; connections to shared printers on other computers are not listed. You can also type a printer name. You can use Variables. A printer name is required.

If no printer has the name you enter, the Trigger stays active but never fires, and nothing is written to the log.
 
**Job name pattern**

A pattern for the document name of the print job. Leave it empty to match every job.

The pattern is compared with the document name that Windows sends with the status change. Windows usually sends the document name only with some notifications, for example when the job is added, so later status changes such as *Printed* do not match a pattern like `*.pdf`. To fire on those statuses, leave *Job name pattern* empty and check the document name in the Job, for example with the `Printer.Result.Document` result Variable.

All patterns on this tab work the same way. They are not case-sensitive, and they use `*` for any characters, `?` for one character, `#` for one digit, and `[abc]` or `[a-z]` for one character from a list or range (`[!abc]` for one character not in it). A pattern without wildcards must match the whole value. You can use Variables; they are evaluated when the Trigger starts.
 
**Checked job status**

The print job statuses that fire the Trigger. Check one or more statuses in the list:

* *Blocked_DEVQ*
* *Complete*
* *Deleted*
* *Deleting*
* *Error*
* *Offline*
* *PaperOut*
* *Paused*
* *Printed*
* *Printing*
* *RenderingLocally*
* *Restart*
* *Retained*
* *Spooling*
* *UserIntervention*

By default, *Spooling*, *Printing*, *Printed*, *Deleting* and *Deleted* are checked. If you clear all statuses, every status change fires the Trigger.
 
**Job user pattern**

A pattern for the user who sent the document to the printer. Leave it empty to match every user.

**Job machine pattern**

A pattern for the name of the computer the document was sent from. Leave it empty to match every computer.

### Result Variables

In the *Variables* window, the result Variables are under the Job's Trigger, *Result*. In a run that this Trigger started, `{TRIGGER(Active|LastTrigger|Printer.Result.Document)}` returns the document name of the print job that started the run. See [Variables](global-variables).

When the Trigger fires, it sets these result Variables:

* `Printer.Result.Message`: fixed text that names the printer as entered in *Printer name*, `Printer '<printer name>' job state was changed`; Variables in *Printer name* are not replaced in this text
* `Printer.Result.Document`: the document name
* `Printer.Result.PrinterName`, `Printer.Result.MachineName`, `Printer.Result.UserName`, `Printer.Result.PortName`: the printer, the computer the document came from, the user, and the printer port
* `Printer.Result.Status`: the job status as Windows reports it, for example `JOB_STATUS_PRINTING`; several statuses are separated by commas
* `Printer.Result.TotalPages`, `Printer.Result.PagesPrinted`, `Printer.Result.TotalBytes`, `Printer.Result.BytesPrinted`: the size of the job and the progress
* `Printer.Result.Priority`, `Printer.Result.Position`, `Printer.Result.DataType`, `Printer.Result.PrintProcessor`, `Printer.Result.Parameters`, `Printer.Result.DriverName`: further job details from the spooler

The *Variables* window also offers `Printer.Result.NotifyName`, which always returns empty text.
