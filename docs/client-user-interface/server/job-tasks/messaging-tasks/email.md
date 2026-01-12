---
sidebar_label: 'Task Messaging - Email'
hide_title: 'true'
---

## Task Messaging - Email - Send

The Messaging Email Task lets you send text and/or HTML emails that can be encrypted/signed through SMIME or PGP to one or more recipients. You may add attachments to the email. You can set priority and get notifications if file has been read or received.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send.png)

**Connection**

You have to select a SMTP Connection. All connections are "global" and you can add new connections by clicking on Manage connection.
 
**Subject**

Subject of your message.
 
**From name**

The name that will appear as "from" in the email.
 
**From email**

The email address that will appear as "from" in the email.
 
**Reply to email** 

If you want another reply address than the From email you enter it here. Leave blank if you don't want to use it.
 
**Priority**

The priority of the email. Will be marked differently depending on what type of client the recipient has.
 
**Security**

You can choose to Sign and/or Encrypt the message in S/MIME or PGP/MIME format. Select appropriate method. When selected new tabs Sign/Encrypt will be enabled which needs further settings to complete the Task.
 
**Message type**

The message can be sent in text and/or html format. Check the boxes here and tabs will be enabled for editing.
 
**Email -> Recipients** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20Recipients.png)

**Recipients separator**

If you specify multiple addresses manually or in a file, VisualCron needs to know how you separated these. Select the appropriate separator here.
 
**Specify manually**

Here you can manually enter email addresses separated by the appropriate separator.
 
**Load from file**

Specify a path to a file that contains a separated list of emails.
 
**Send separate emails**

By default, for privacy, VisualCron sends one email per recipient and does not show other recipients in the To-field. If you want to change this behavior you can uncheck this box.
 
**Email -> Text** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20Text.png)

Enter the text message here. Will only be enabled if you have selected Text as message type.
 
**Email -> HTML** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20HTML.png)

Enter the HTML message here. Will only be enabled if you have selected HTML as message type.
 
**Email -> Chrome Preview** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20Chrome.png)

In the Chrome Preview tab you can see how your HTML text would look in the Internet Explorer web browser.
 
**Email -> Attachments** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20Attachments.png)

You can send any kind of attachment with the Email Messaging Task. If the attachments are located on a restricted area/network drive you must use a Credential to access it. You select the Credential when editing the attachment. The attachment tab shows a list. Click on Add, Edit or Delete to alter which attachments to use.
 
If Add is selected, the standard [file filter](../../../server/job-tasks-file-filter) definitions are opened.
 
**Email > Sign (PGP/MIME)** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20Sign.png)

In order to be able to activate the Sign settings, the *Use PGP/MIME security features* must be selected in the Email > Main settings window.
 
**Sign message**

Click on Sign message to activate signing
 
**Use new features**

Use this property for compatibility with old versions of PGP-compatible software. If this property is set to True, then newer and stronger algorithms will be used. If the property is set to False, then the result will be compatible with PGP 2.6.x, while the keys are compatible (i.e. don't use features not supported by PGP 2.6.x).
 
**Choose key ring**

Select one of existing key rings to match for senders email. When selecting a key ring all existing keys will be listed in the grid.
 
**Manage key rings**

Click on this button to create/import new key rings.
 
**Password**

If your key requires a password you should enter it here.
 
**Email > Sign (S/MIME)** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20Sign.png)

In order to be able to activate the Sign settings, the *Use S/MIME security features* must be selected in the Email > Main settings window.
 
**Sign message**

Click on Sign message to activate signing
 
**Sign clear format**

There are two possible types of message signing. If the first type is used any user will be able to read the message. If program that can't process signatures is used there is no way to check signature but it is still possible to read the message. When this type is used content-type of the message is 'multipart/signed'.
When second type is used, such program will be only able to show attachment with no meaning. But the second type is more protected against damages during passing the mail servers. When this type is used, content-type of the message is 'application/pksc7-mime; smime-type=signed-data'.     Default value is True which corresponds to the first type.
 
**Sign root header**

Use this property to specify whether to sign root header of the message.
 
**Manage certificates**

Click on this button to create/import new certificates.
 
**Choose certificate grid**

You must select one certificate that matches your from address in order to be able to sign.
 
**Email > Encrypt (PGP/MIME)** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20Encrypt.png)

In order to be able to activate the Encrypt settings, the *Use PGP/MIME security features* must be selected in the Email > Main settings window.
 
**Encrypt message**

Click on Encrypt message to activate encryption
 
**Choose key ring**

Select one of existing key rings to match recipients email. When selecting a key ring all existing keys will be listed in the grid.
 
**Manage key rings**

Click on this button to create/import new key rings
 
**Email > Encrypt (S/MIME)** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20Encrypt%20with%20Key.png)

In order to be able to activate the Encrypt settings, the *Use S/MIME security features* must be selected in the Email > Main settings window.
 
**Encrypt message**

Click on Encrypt message to activate encryption
 
**Manage certificates**

Click on this button to create/import new certificates.
 
**Choose certificate grid**

You must select a certificate that matches each recipient in order to encrypt.