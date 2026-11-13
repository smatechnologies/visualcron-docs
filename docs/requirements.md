---
sidebar_label: 'Requirements'
hide_title: 'true'
---

## Requirements

This page lists what a computer needs to run the VisualCron Server, the VisualCron Client, or both. VisualCron runs on Windows only.

### Software requirements

| Component | Requirement |
|---|---|
| Operating system | Microsoft-supported (Mainstream and Extended) Windows Server and Desktop versions |
| Processor architecture | 32-bit (x86) and 64-bit (x64) |
| .NET Framework | .NET Framework 4.8. The installation stops if it is not installed. The setup program offers to open the Microsoft download page |
| Database | None needed. SQL Server Compact 4.0 is included with VisualCron |
| Installation rights | A local administrator account |

The default installation folder is "C:\Program Files (x86)\VisualCron" on 64-bit Windows and "C:\Program Files\VisualCron" on 32-bit Windows.

### Network ports

| Port | Protocol | Used for |
|---|---|---|
| 16444 | TCP | Client and API connections to the VisualCron Server. The port can be changed in the *Server port* setting |
| 8001 | TCP | Web API over HTTP, only when *Allow Web API* is selected |
| 8002 | TCP | Web API over HTTPS, only when *Allow Web API* is selected |
| 9000 | TCP | Web Client, in IIS or IIS Express, only when the Web Client is installed |

The installer does not create a firewall rule. VisualCron also connects out to "www.visualcron.com" on TCP 443, for example for license activation. For the ports to open, from where, and the outbound connections, see [Firewall and network](get-visualcron/antivirus-exclusions#firewall-and-network).

### Hardware requirements

#### Server

| Component | Requirement |
|---|---|
| Operating system | Microsoft-supported (Mainstream and Extended) Windows Server and Desktop versions |
| Disk space | 1 GB to 4 GB (depending on logging volume) |
| CPU | 2 GHz or more, quad core or better |
| Memory | 6 GB or more |

#### Client

| Component | Requirement |
|---|---|
| Operating system | Microsoft-supported (Mainstream and Extended) Windows Server and Desktop versions |
| Disk space | 1 GB |
| CPU | 2 GHz or more, quad core or better |
| Memory | 6 GB or more |
| Screen resolution | Minimum 1920×1080 |

#### Client and Server on one computer

| Component | Requirement |
|---|---|
| Operating system | Microsoft-supported (Mainstream and Extended) Windows Server and Desktop versions |
| Disk space | 1 GB to 4 GB (depending on logging volume) |
| CPU | 2 GHz or more, quad core or better |
| Memory | 12 GB or more |
| Screen resolution | Minimum 1920×1080 |

:::note

By default, VisualCron stores its internal log database under "C:\ProgramData\VisualCron\output", on the system drive, whichever installation folder you choose. Plan the logging disk space on that drive.

:::

:::note

VisualCron supports third-party integrations but can only assist with versions that are actively maintained by their vendors. Requests involving end-of-life tools may be closed without resolution.

:::
