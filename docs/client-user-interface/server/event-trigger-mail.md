---
sidebar_label: 'Event Trigger - Mail'
hide_title: 'true'
---

## Event Trigger - Mail

The Email event trigger is able to monitor a mailbox through the POP3 or the IMAP4 protocol. The actual connection properties are defined in the [Connections](../server/global-connections) window. Based on subject, sender and content different actions can be performed with the email.
 
**Triggers > Add > Event Trigger > Email > Main settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Mail.png)

**Description**

Description or name of your Trigger.
 
**Active**

If the Trigger is active (watching) or not.
 
**Polling interval**

How often the mailbox is to be checked.
 
**Credential**

To control a remote computer you may need to use a [Credential](../server/global-credentials). The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the Settings icon to open Manage credentials in order to add or edit Credentials.
 
**Ignore Server Off (always run)**

The Trigger will run even though Server is set to off.
 
**Triggers > Add > Event Trigger > Email > Email > Main settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Mail%20Settings.png)

**Connection**

Select an existing [POP3](../server/connection-pop3)/[IMAP4](../server/connection-imap4) connection, if not existing you need to create one first. Click the Settings icon to open the Manage Connections dialog. Once a connection is added you can select it in the combo box.
 
**Mail folder**

When VisualCron connects it uses the default folder retrieved from the mail server. If you want to change the folder you monitor you select **Use specified folder** and write the folder name in the text box. Click the **Select folder** button to browse for a folder on the mail server. Check **Is public** when the folder is a shared/public mailbox folder.
 
**Reset checked emails when modified**

VisualCron keeps tracks on which emails that have been checked or not. When an email has been checked it is added to an internal list. In the next polling interval VisualCron will check if that email has been parsed or not. To keep this list and efficiency to a minimum it is recommended that you either delete or move the email once the email has been parsed. This is controlled in the Actions tab. If you, for some reason, wants VisualCron to reset that list you check this box and VisualCron will consider all emails found in the mail folder as new.

**Error handling**

**Timeout**

The number of seconds to wait for a response from the mail server before considering the operation as failed.

**Number of retries**

The number of times VisualCron will retry the mail operation when the server does not respond before giving up.

**Keep connection**

When checked, VisualCron keeps the connection to the mail server open between polling intervals (IMAP IDLE), rather than reconnecting every time. This reduces overhead and allows the trigger to react more quickly to new messages on servers that support it.
 
**Triggers > Add > Event Trigger > Email > Email > S/MIME** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Mail%20Key.png)

VisualCron is able to decrypt S/MIME emails and verify signatures.
 
**Decryption**

If the email is encrypted you need a Certificate to decrypt it. A certificate is often retrieved from the sender of the Certificate and is in the X509 certificate standard. Once you have created or imported a certificate you need to check it in the list. If an email is encrypted VisualCron will try to use that certificate for decryption.
 
**Manage Certificates**

You can create/import your certificates defined in the [Manage Certificates](../server/global-certificates) window.
 
**Triggers > Add > Event Trigger > Email > Email > Conditions** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Mail%20Conditions.png)

The Email Trigger has some Conditions. The Conditions are there to evaluate certain values from the parsed email. Each evaluation returns a result. The following results exist: All match, Any match and No match. If all match the evaluation then it will return All match. If at least one is matching it will return Any match. If none are matching it will return No match. The actual evaluation of the Condition is different depending on what part of the email is evaluated. For example, when evaluating a subject you can choose among the following checks:
 
* "**Equal**" - the subject must match the string in the text box exactly
* "**Not equal**" - the subject must not match the string in the text box
* "**Contains**" - if any of the letters in the text box matches the subject it is returning a match
* "**Don't contain**" - if not any of the letters in the text box matches the subject it is returning a match
* "**Don't check**" - this Condition is not checked at all which is returning a match
 
**From address**

This Condition checks the actual address part of the message (not name of sender).
 
**Subject**

This Condition checks the subject of the email. Check **Case sensitive** to make the comparison case‑sensitive.
 
**Body**

his Condition checks the body of the email. Check **Case sensitive** to make the comparison case‑sensitive.
 
**Received date**

This Condition compares the date and time the message was received against a Variable. Please note that you can only use date Variables and that it does not matter what kind of formatting of the Variable you use. Click the variables button to insert a date variable.

The following comparison operators are available for _Received date_:

* **Equal** / **Not equal** — the received date must (or must not) match the supplied date exactly
* **Larger** / **Larger or equal** — the received date must be later than (or equal to) the supplied date
* **Smaller** / **Smaller or equal** — the received date must be earlier than (or equal to) the supplied date
* **Don't check** — this Condition is not checked

**Triggers > Add > Event Trigger > Email > Email > Actions** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Mail%20Actions.png)

Actions are controlling what happens when the Conditions has been evaluated - depending on collective result. Most actions can be set to run for one of the following condition results:

* **All match** — every Condition matched
* **Any match** — at least one Condition matched
* **No match** — none of the Conditions matched
* **Always** — run regardless of Condition result
* **Never** — do not run the action
 
**Trigger**

This action controls if the Job should be triggered or not depending on result. Use the _Trigger when result is_ dropdown to choose which Condition result causes the Job to fire.
 
**Message on Server**

This controls what happens with the message on the mail server. It is recommended that you delete or move the mail or VisualCron will check that email again in the next polling interval.

Use the Condition‑result dropdown to choose when the action applies, then select one of the following radio options:

* **Delete from server** — remove the message from the mail server
* **Leave message on server** — keep the message on the server

When _Leave message on server_ is selected, the **Mark as read** checkbox becomes available. Checking it marks the message as read on the server (IMAP4 only; the POP3 protocol does not support this). Note that VisualCron does not care if it is read or not — VisualCron has its internal list to check if an email has been processed.
 
**Copy message to folder (_not POP3_)**

This option copies a mail to another folder. It does not delete it unless you set Delete message on Server in previous setting. This option is only available when using IMAP4 as protocol mode.

Choose when the copy is performed using the Condition‑result dropdown, then enter the target folder or click the Select folder button to browse. Check **Mark as read** to also mark the copied message as read.

**Forward email**

Open the **Forward Email** sub‑tab and check **Forward email** to enable forwarding of the matched email through an SMTP connection.

* **Connection** — the SMTP [Connection](../server/global-connections) used to send the forwarded email
* **Subject prefix** — text prepended to the original subject when forwarding
* **Recipient separator** — the character used to separate multiple recipients in the To/Cc/Bcc fields
* **Send separate emails** — when checked, a separate email is sent to each recipient instead of one email with multiple recipients
* **To / Cc / Bcc** — for each recipient group, choose the **Source** (_Not used_, _Manual_, or _File_), then either type recipients in the textbox or pick a file containing recipients. When _File_ is selected, a [Credential](../server/global-credentials) can be supplied for accessing the file

**Triggers > Add > Event Trigger > Email > Email > Save mail** tab

Both the actual mail and/or attachment can be saved to a file. By default the content is saved in ```"C:\Program Files\VisualCron\data\triggers\mail"```. Attachments of an email are by default stored in the attachments folder; ```"C:\Program Files\VisualCron\data\triggers\mail"```.

**Email save action**

Choose when the email itself should be saved to disk based on the Condition result (_Never_, _Always_, _All match_, _Any match_, _No match_).

**Save location**

Choose between:

* **Save to default folder** — store the email in the default VisualCron mail data folder
* **Save to custom folder** — pick a destination folder. Use the browse button to select a folder on disk

**Create folder tree for each email**

When checked, VisualCron creates a separate folder tree for each saved email so that the email and its attachments are grouped together.

**Attachment save action**

Choose when attachments should be saved to disk, using the same Condition‑result options as _Email save action_.

**Triggers > Add > Event Trigger > Email > Email > Attachment filter** tab

Use this tab to limit which attachments are saved when _Attachment save action_ is enabled.

**File mask**

A file mask used to match attachment names (for example `*.pdf`). Use the browse button to select a sample file, check **Is regex** to treat the mask as a regular expression, and check **Case sensitive** to make matching case‑sensitive.

**File size**

Optionally filter attachments by size:

* **Smaller than** — only save attachments smaller than the given size
* **Larger than** — only save attachments larger than the given size

Each size has its own numeric value and a unit dropdown (B, kB, mB, gB, tB). When both checks are enabled, use the operator dropdown to combine them with **AND** or **OR**.

**Overwrite existing files**

When checked, an attachment with the same file name as an existing file is overwritten.

**Add number to existing file**

When checked, a numeric suffix is added to the file name to avoid overwriting an existing file.
 
:::tip Note 

when forming the folder name and file name, all incorrect characters in _MailId_ are replaced with the � symbol.
The final folder and file path are stored in the trigger execution result variables: ```Mail.Result.Mail.MailFolder``` and ```Mail.Result.Mail.MailPath```, respectively.
Moreover, this folder and/or file name can also be calculated by applying the built-in variable function "_File variables / Encode FileName_" to _MailID_ as follows: ```{PATH(EncodeFileName|{TRIGGER(Active|LastTrigger|Mail.Result.Mail.MessageId)}|MASK)}```.

:::
