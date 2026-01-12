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

When VisualCron connects it uses the default folder retrieved from the mail server. If you want to change the folder you monitor you select "Use specified folder" and write the folder name in the text box.
 
**Reset checked emails when modified**

VisualCron keeps tracks on which emails that have been checked or not. When an email has been checked it is added to an internal list. In the next polling interval VisualCron will check if that email has been parsed or not. To keep this list and efficiency to a minimum it is recommended that you either delete or move the email once the email has been parsed. This is controlled in the Actions tab. If you, for some reason, wants VisualCron to reset that list you check this box and VisualCron will consider all emails found in the mail folder as new.
 
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

This Condition checks the subject of the email
 
**Body**

This Condition checks the body of the email
 
**Received date**

This Condition compares the date and time the message was received against a Variable. Please not that you can only use date Variables and that it does not matter what kind of formatting of the Variable you use.

**Triggers > Add > Event Trigger > Email > Email > Actions** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Mail%20Actions.png)

Actions are controlling what happens when the Conditions has been evaluated - depending on collective result.
 
**Trigger**

This action controls if the Job should be triggered or not depending on result.
 
**Message on Server**

This controls what happens with the message on the mail server. It is recommended that you delete or move the mail or VisualCron will check that email again in the next polling interval. If you leave the message on the server you can choose to mark it as read (this option is only available in IMAP4 because it does not exist in POP3 protocol). Note that VisualCron does not care if it is read or not - VisualCron has it's internal list to check if email has been checked or not.
 
**Copy message to folder (_not POP3_)**

This option copies a mail to another folder. It does not delete it unless you set Delete message on Server in previous setting. This option is only available when using IMAP4 as protocol mode.
 
**Save email**

Both the actual mail and/or attachment can be saved to a file. You can choose to save the email at a custom location or at the default location. By default the content is saved in ```"C:\Program Files\VisualCron\data\triggers\mail\{MailId}\{MailId}.eml"```. Attachments of an email are by default stored in the attachments folder; ```"C:\Program Files\VisualCron\data\triggers\mail\{MailId}\attachments"```.
 
:::tip Note 

when forming the folder name and file name, all incorrect characters in _MailId_ are replaced with the � symbol.
The final folder and file path are stored in the trigger execution result variables: ```Mail.Result.Mail.MailFolder``` and ```Mail.Result.Mail.MailPath```, respectively.
Moreover, this folder and/or file name can also be calculated by applying the built-in variable function "_File variables / Encode FileName_" to _MailID_ as follows: ```{PATH(EncodeFileName|{TRIGGER(Active|LastTrigger|Mail.Result.Mail.MessageId)}|MASK)}```.

:::