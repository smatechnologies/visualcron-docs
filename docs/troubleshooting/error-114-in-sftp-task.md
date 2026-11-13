---
sidebar_label: 'Error 114 in SFTP Task'
hide_title: 'true'
---

## Error 114 in SFTP Task

This page used to cover SFTP error 114, an authentication failure, which can have several causes depending on the authentication type. For each variant and its fix, see [Connection - SFTP: Troubleshooting](../client-user-interface/server/connection-sftp#troubleshooting). The SFTP server must also allow the authentication type that the Connection uses, for example `PasswordAuthentication yes` in the OpenSSH "sshd_config" file for password authentication.