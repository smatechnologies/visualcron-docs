---
sidebar_label: 'Error 114 in SFTP Task'
hide_title: 'true'
---

## Error 114 in SFTP Task

If you get error 114 in the SFTP Task you have not enabled password authentication at your SFTP server. Edit the configuration file and set:
 
passwordauthentication no
 
to
 
passwordauthentication yes