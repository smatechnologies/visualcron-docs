---
sidebar_label: 'Event Trigger - Mail'
hide_title: 'true'
---

## Event Trigger - Mail

The Mail Trigger watches a mailbox folder and starts the Job once for each new email that meets its conditions. It can also delete, move, copy, mark, save or forward the emails that fire it. The mailbox is reached through an IMAP4, Exchange EWS, Exchange WebDAV or Microsoft Graph API Connection, defined in the [Connections](global-connections) window.

This Trigger fires once per email and can delete each email before the Job starts. See [Event Triggers](event-triggers#triggers-that-fire-once-per-item) for how to keep a skipped run from losing an email.

The general settings are on the ***Main settings*** tab.

![The Main settings tab of the Add/Edit event window for a Mail Trigger: Description, Active, Run delay, Polling interval set to 60 seconds, the Credentials list, Extended Trigger debug logging and Ignore Server Off (always run)](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Mail.png)

*Description*, *Active*, *Run delay* and *Ignore Server Off (always run)* work as for every Event Trigger: see [Event Triggers](event-triggers).

**Polling interval**

How often, in seconds, the mailbox is checked. The default is 60. The first check is made as soon as the Trigger starts, for example when you click *OK*. The box is unavailable while *Keep connection* is checked, so set it before you check *Keep connection*.

**Credential**

The [Credential](global-credentials) that the Trigger uses to write saved emails and attachments to disk (***Save mail*** sub tab). The connection to the mailbox uses the Connection's own settings. Select a Credential in the combo box, or click the icon next to it to open *Manage credentials*.

The mailbox settings are on the ***Email*** tab, ***Main settings*** sub tab.

![The Main settings sub tab of the Email tab: the Connection list, Mail folder with Use default folder and Use specified folder, Is public folder, Error handling with Connection timeout 180 and Number of retries 3, Reset checked emails when modified and Keep connection](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Mail%20Settings.png)

**Connection**

Select an existing IMAP4, Exchange EWS, Exchange WebDAV or Microsoft Graph API Connection. If none exists, click the icon next to the list to open the Connections window and add one; it can then be selected in the combo box.

**Mail folder**

By default (*Use default folder*), the Trigger checks the default folder of the mailbox. To check another folder, select *Use specified folder* and enter the full path of the folder as the server names it, for example `Inbox/Processed`, or click the folder icon to browse the folders on the server. The folder name accepts Variables. Check *Is public folder* when the folder is a public folder. Browsing for a folder sets *Is public folder* to match the folder you select. With an Exchange WebDAV Connection, public folders are not offered when you browse, and *Is public folder* currently has no effect: the Trigger looks for the folder, and for the folder of *Copy message to folder (not POP3)*, among the mailbox's own folders.

**Reset checked emails when modified**

VisualCron remembers each email that fired the Trigger and was not deleted, and does not fire for it again. The list is kept with the Job, so it survives a Server restart and saving the Job. Emails that did not fire the Trigger are not remembered: they are checked again at every poll.

Check this box and click *OK* to clear the list. At the next poll, every email in the folder that the Trigger reads is checked as new. The box is not saved checked: it clears the list once, when you save the Trigger.

**Error handling**

**Connection timeout**

How many seconds to wait for the mail server before an operation fails (up to 1000; default 180). It is also how long the Trigger waits after a failed check before it continues.

**Number of retries**

How many times the Trigger tries again after failed checks in a row (up to 9999; default 3). If the check after the last retry also fails, the Trigger is deactivated and the error is written to the log. A successful check resets the count.

Only errors while connecting, selecting the folder or closing the connection count as failed checks. An error while reading the list of emails, or one email, is only written to the log. An email that cannot be read ends that check; the emails after it are read at the next check.

If the folder in *Use specified folder* is not found, the Trigger stops checking at once, without retries. With *Keep connection* cleared, it can then still show as active: correct the folder name, then deactivate and activate the Trigger, or save the Job.

**Keep connection**

When checked, VisualCron keeps the connection to the mail server open and checks the folder every *Connection timeout* seconds, instead of connecting at every *Polling interval*; the *Polling interval* box is unavailable. When the Trigger starts, VisualCron tests whether the server supports this. If it does not, the Trigger connects at every *Polling interval* instead, using the value saved in that box. *Keep connection* is not supported for Microsoft Graph API Connections: leave it cleared for them.

:::warning

With *Keep connection*, the Job's time exceptions are checked only when the Trigger starts. If a time exception begins later, emails are still read and their actions still run, for example *Delete message on Server*, but the Job does not start for them. If the Trigger starts during a time exception, it stops checking the mailbox but still shows as active. If the Job uses time exceptions, clear *Keep connection*.

:::

The decryption settings are on the ***Email*** tab, ***S/MIME*** sub tab.

![The S/MIME sub tab of the Email tab: the Decryption list of certificates with Key, Bits and User columns](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Mail%20Key.png)

VisualCron is able to decrypt S/MIME emails and verify signatures.

**Decryption**

To read encrypted emails, check the certificate to decrypt them with in the *Decryption* list. Only one certificate can be checked. The list shows the certificates in [Manage Certificates](global-certificates) that can be used for encryption. If an encrypted email cannot be decrypted, for example because no certificate is checked, the error is written to the log and the email does not fire the Trigger; it is checked again at the next poll.

When an email is signed, VisualCron checks the signature. The result is in the result Variables `Mail.Result.Mail.IsSigned` and `Mail.Result.Mail.ValidSignature`.

**Manage Certificates**

Click *Manage Certificates* to open the *Manage certificates* window, where you create or import certificates. See [Manage Certificates](global-certificates).

The conditions are on the ***Email*** tab, ***Conditions*** sub tab.

![The Conditions sub tab of the Email tab: From address, Subject, Body and Received date, each set to Don't check; Subject and Body have Case sensitive checked; Received date shows {DATENOWADD(Minutes,10,T)}](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Mail%20Conditions.png)

Each condition compares one part of the email with the text you enter. The text accepts Variables. A condition set to *Don't check* is left out. The Trigger then counts the conditions that are checked and gives one result:

* *All match*: every checked condition matches. This is also the result when every condition is *Don't check*
* *Any match*: at least one checked condition matches, but not all
* *No match*: no checked condition matches

The result decides which actions run (***Actions*** sub tab). For *From address*, *Subject* and *Body* the checks are:

* *Equal (=)*: the value is exactly the text
* *Not equal (!=)*: the value is not exactly the text
* *Contains (=%)*: the text appears anywhere in the value, as one piece
* *Not contains (!=%)*: the text does not appear in the value
* *Don't check*: the condition is not used. This is the default for every condition

**From address**

Checks the sender's email address, not the display name. The comparison is never case-sensitive.

**Subject**

Checks the subject of the email. *Case sensitive* is checked by default; clear it to ignore case.

**Body**

Checks the body of the email. When the email has both a text body and an HTML body, they are checked together as one text, the text body first. *Case sensitive* is checked by default; clear it to ignore case.

**Received date**

Compares the date and time the email was received with a date. Enter a date Variable, or click the icon to insert one; the default is `{DATENOWADD(Minutes,10,T)}`. Seconds are compared; fractions of a second are ignored.

* *Equal (=)* / *Not equal (!=)*: the email was (or was not) received at that date and time
* *Larger than (>)* / *Larger than or equal (>=)*: the email was received after (or at) that date and time
* *Smaller than (<)* / *Smaller than or equal (<=)*: the email was received before (or at) that date and time
* *Don't check*: the condition is not used

:::warning

If the value cannot be read as a date, for example because a Variable is misspelled, the condition counts as a match for every email. Check the value with the *Variables* window before you activate the Trigger.

:::

The actions are on the ***Email*** tab, ***Actions*** sub tab.

![The Actions sub tab of the Email tab with the default settings: Trigger All match; Message on Server Always with Delete message on Server selected; Copy message to folder (not POP3) Never; Forward email cleared](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Mail%20Actions.png)

Actions run only for an email that fires the Trigger, and they run before the Job starts, even when *Run delay* holds the Job back. No action is applied to an email that does not fire the Trigger; it is checked again at the next poll. For each action, choose the condition result it runs for:

* *All match*
* *Any match*: also runs for an email whose result is *All match*
* *No match*
* *Always*: whatever the result
* *Never*: the action does not run. Not offered for *Trigger* and *Message on Server*

**Trigger**

Choose which condition result starts the Job. The default is *All match*. With the default conditions (all *Don't check*), every email fires the Trigger.

**Message on Server**

Controls what happens to the email on the mail server. Choose the condition result it applies to, then select:

* *Delete message on Server*: the email is deleted from the server
* *Leave message on Server*: the email stays on the server. Check *Mark as read (not POP3)* under *Message on Server* to mark it as read

:::warning

With the default settings, the first check, made as soon as you click *OK*, fires the Trigger for every unread email in the folder and deletes each one from the server (*Always* and *Delete message on Server*). Set the conditions and *Message on Server* first, or clear *Active* until the Trigger is ready.

:::

Which emails the Trigger reads depends on this setting. With *Delete message on Server*, or with *Leave message on Server* and its *Mark as read (not POP3)* checked, the Trigger reads only unread emails: an email that is already read never fires it. With *Leave message on Server* and its *Mark as read (not POP3)* cleared, the Trigger reads read and unread emails; an email that fired the Trigger once does not fire it again (see *Reset checked emails when modified*).

**Copy message to folder (not POP3)**

Copies the email to another folder on the mail server, for IMAP4, Exchange EWS, Exchange WebDAV and Microsoft Graph API Connections. Choose the condition result it applies to (default *Never*), then enter the full path of the folder, for example `Inbox/Processed`, or click the folder icon to browse. The folder name accepts Variables. Browsing for a folder also sets *Is public folder* on the ***Main settings*** sub tab to match the folder you select.

If *Message on Server* also applies to the email with *Delete message on Server*, the email is moved to the folder instead of copied.

:::warning

If the folder is not found, or the copy or move fails, the email is not copied, and with *Delete message on Server* it is still deleted. The log shows that the folder could not be found only with *Extended Trigger debug logging* checked. After each copy or move, the log currently also shows the error "Destination mail folder … not found.", even when the copy succeeded. Check the folder name with the folder icon before you activate the Trigger.

:::

*Mark as read (not POP3)* in this group, checked by default, marks the original email as read whenever this action runs, also when the folder is not found.

**Forward email**

Check *Forward email* to forward each email that fires the Trigger; then set it up on the ***Forward email*** sub tab. The forwarded email has the original body and attachments, and is sent from the first address in the original email's To field.

* *Connection*: the SMTP, Exchange EWS, Exchange WebDAV or Microsoft Graph API [Connection](global-connections) used to send it
* *Subject*: the subject of the forwarded email. An asterisk (`*`) inserts the original subject; the default is `FW: *`
* *Recipient separator*: the character between recipients in the *To..*, *Cc..* and *Bcc..* boxes or files: *Semicolon*, *Comma* or *Newline*
* *Send separate emails*: checked by default. Each recipient in *To..*, *Cc..* and *Bcc..* gets a separate email, with that recipient as the only To address
* *To..*, *Cc..*, *Bcc..*: for each, choose *Not used*, *Manual* (type the recipients) or *File* (a file that lists the recipients). For *File*, you can select a *Credential* to read the file. Values accept Variables

:::warning

Forwarding currently has these limits:

* The body of the forwarded email is passed through the Variable replacer, so Variables (text in braces) in an incoming email are replaced in the forwarded copy. Forward only emails from senders you trust, for example by setting a *From address* condition
* With *Send separate emails* cleared, the email is forwarded only when *To..* holds exactly one address. With more than one To address, nothing is sent and nothing is logged. To forward to several recipients, keep *Send separate emails* checked
* An email that has no To address is not forwarded; the error is written to the log
* After the first forward, the Trigger uses the forward *Connection* in place of the mailbox Connection until the Trigger restarts, for example when the Job is saved. Copying, moving and marking later emails as read can then fail, and an email set to be moved is deleted instead. With a Microsoft Graph API mailbox, the Trigger also stops renewing its sign-in, so later checks fail and the Trigger is deactivated after the retries. Use the mailbox Connection as the forward *Connection*, or do not use *Forward email*

:::

The save settings are on the ***Email*** tab, ***Save mail*** sub tab.

The email (as an `.eml` file) and its attachments can be saved to disk. Each email gets its own folder, named after the email's unique ID on the server. By default (*Save to default folder*) the email is saved in `data\triggers\mail\<ID>` in the VisualCron installation folder, and its attachments in `data\triggers\mail\<ID>\attachments`. The Trigger writes the files as the account the VisualCron service runs as, or as the *Credential* on the ***Main settings*** tab.

**Email**

Choose the condition result for which the email is saved (*Never*, the default, *Always*, *All match*, *Any match* or *No match*).

**Save location**

* *Save to default folder*: the default folders above
* *Save to folder:*: the folder you enter, or select with the folder icon. Accepts Variables

The email and its attachments use the same location.

**Create folder tree based on each email**

Applies to *Save to folder:*. When checked (the default), the email is saved in a subfolder named after its unique ID and the attachments in an `attachments` folder below it. When cleared, the email and its attachments are saved directly in the folder you entered. The default folders always use a folder per email.

**Save attachment(s)**

Choose the condition result for which attachments are saved, with the same options as *Email*. The default is *Never*; the ***Attachment filter*** sub tab is available only when this is not *Never*.

The attachment filter is on the ***Email*** tab, ***Attachment filter*** sub tab.

Use this tab to limit which attachments are saved when *Save attachment(s)* is set to save them.

**File mask**

Only attachments whose name matches the mask are saved. The default `*` saves all. Separate several masks with `;`, for example `*.pdf;*.xlsx`. Check *Is regex* to use a regular expression instead. The mask accepts Variables. Click the icon to pick a sample file and use its name.

:::note

The *Case sensitive* checkbox on this sub tab is currently not saved. The file mask is always matched without regard to case.

:::

**Size**

Check *Check if file is smaller than x size* or *Check if file is larger than x size* to save only attachments below or above a size. Each size has a value and a unit, from *byte(s)* to *terabyte(s)*; the default is *kilobyte(s)*. When both are checked, both must be true.

:::warning

The list that combines the two sizes offers *AND* and *OR*, but it currently always shows *AND* when you open the Trigger, so *OR* is lost unless you select it again each time you save the Trigger.

:::

**Overwrite existing file(s)**

Checked by default. When an attachment with the same name already exists in the folder, it is overwritten. When cleared, the existing file is kept and the attachment is not saved.

**Add number to existing file**

When checked, an attachment whose name already exists is saved with a number added to its name (for example `report1.pdf`), so no file is overwritten.

:::note

In the folder and file names, characters that are not allowed in Windows file names are replaced with `�` (U+FFFD). The full folder and file path are in the result Variables `Mail.Result.Mail.MailFolder` and `Mail.Result.Mail.MailPath`. To build the same name yourself from the email ID, use `{PATH(EncodeFileName|{TRIGGER(Active|LastTrigger|Mail.Result.Mail.MessageId)}|MASK)}`.

:::

### Result Variables

When the Trigger fires, it sets these result Variables for the email that fired it:

* `Mail.Result.Mail.MessageId`: the email's unique ID on the server
* `Mail.Result.Mail.Identifier`: a 32-character hexadecimal value calculated from the message ID
* `Mail.Result.Mail.FromAddress`: the sender's address
* `Mail.Result.Mail.ToAddresses` and `Mail.Result.Mail.CCAddresses`: the recipients, separated by `;`
* `Mail.Result.Mail.Subject`
* `Mail.Result.Mail.BodyText` and `Mail.Result.Mail.BodyHTML`: the text body and the HTML body
* `Mail.Result.Mail.Received`: the date received. For another format, use `Mail.Result.Mail.Received|<date format>`, for example `{TRIGGER(Active|LastTrigger|Mail.Result.Mail.Received|yyyy-MM-dd)}`
* `Mail.Result.Mail.IsEncrypted`, `Mail.Result.Mail.IsSigned`, `Mail.Result.Mail.ValidSignature`: `True` or `False`
* `Mail.Result.Mail.MailFolder`: the folder of the saved email; also set when only the attachments are saved. Empty when nothing is saved
* `Mail.Result.Mail.MailPath`: the file of the saved email; empty when the email is not saved
* `Mail.Result.Mail.AttachmentFolder`: the folder of the saved attachments
* `Mail.Result.Mail.NoAttachments`: the number of attachments
* `Mail.Result.Mail.AttachmentNames`: the names of all attachments, comma separated, including attachments that the ***Attachment filter*** leaves out. Set only when *Save attachment(s)* applies to the email; otherwise empty. Add an index for one name, for example `Mail.Result.Mail.AttachmentNames|0` for the first
* `Mail.Result.Mail.AttachmentPaths`: the paths of the saved attachments, comma separated; add an index for one path, for example `Mail.Result.Mail.AttachmentPaths|0`

For example, `{TRIGGER(Active|LastTrigger|Mail.Result.Mail.Subject)}` returns the subject of the email that fired the Trigger that started the run. *Last run*, `{TRIGGER(Active|LastTrigger|LastRun)}`, returns the time the Trigger fired. The *Variables* window also offers *Get local attachment name of a specific attachment*, which currently returns no value; use `Mail.Result.Mail.AttachmentNames|0` instead. See [Variables](global-variables) for how *Last trigger* and the other keys work.
