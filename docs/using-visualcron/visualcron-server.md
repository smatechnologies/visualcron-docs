---
sidebar_label: 'VisualCron Server'
hide_title: 'true'
---

## VisualCron Server

The VisualCron server runs as a Windows **service** in the background. The server service status is Started when the server computer is started.
 
The VisualCron **server** application status can be *On* or *Off*. If the server is On, it will be looking for Jobs to run. If Off, no Jobs will be run unless a user forces it manually in a client. The server application is running, even if no one is logged on to the computer where the server is running or if no client application is connected to the server.
 
In the VisualCron client, the currently selected server name is displayed in the main menu **Server `[<server name>]`** tab and in the Username/Server entry in the the Server/Groups/Jobs/Tasks grid and in status bar. Server connections are global, thus if you change a connection definition, this will affect all commands associated with this connection.
 
The default port number between the VisualCron Server and the Client is 16444. This means, that if you are connecting remotely from the outside you may have to open port 16444 in your firewall, software and/or hardware.

