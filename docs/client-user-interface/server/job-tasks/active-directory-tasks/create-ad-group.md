---
sidebar_label: 'Task Active Directory - Create AD Group'
hide_title: 'true'
---

## Task Active Directory - Create AD Group

Creates a new Active Directory Group in the specified parent container. Groups are Active Directory (or local computer) objects that can contain users, contacts, computers and other groups that can be managed as a single unit.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Active%20Directory%20Tasks/Create%20AD%20Group.png)

**Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the *Settings* icon to open *Manage credentials* in order to add or edit Credentials.
 
**Parent path**

The Lightweight Directory Access Protocol (LDAP) path of the parent Active Directory container. This is usually the top most container or the root of the directory data tree on a directory server. Click the *Select container* button to select an existing Active Directory container.
 
**Name**

The name of the Active Directory group to be created.
 
**Display name**

The display name of the Active Directory group to be created.
 
**Description**

The description of the Active Directory group to be created.
 
**Group type**

An e-mail sent to a Security or Distribution group type sends the message to all members of the group.

A Security group manages user and computer access to shared resources and group policy settings. This allows setting permissions once on multiple computers in order to be able to easily change the group membership. The groups can also be used as e-mail distribution lists.

A Distribution group is used only for e-mail distribution lists in e-mail applications such as Microsoft Exchange or Outlook.
 
**Group scope**

Usually describe which type of users that a group consists of.

The Domain Local Group grant permissions to domain resources that are located in the same domain in which you created the domain local group. Membership of this group makes it possible to add members as user accounts, universal and global groups from any domain.

The Global Group contains users with similar function and can be given permission to access e.g. a printer or shared folder available in a local or another domain in same forest.

The Universal Group are used for e-mail distribution and can be granted access to resources in all trusted domains as a security principal in a Windows 2000 native or Windows server 2003 domain.