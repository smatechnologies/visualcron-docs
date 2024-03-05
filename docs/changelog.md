---
sidebar_label: 'Change Log'
hide_title: 'true'
---

## Change Log
 
## 10.0.2 [2023-09-27]  

:::info Notes
- This version contains new license changes. Below is a list of changes. Please contact sales@visualcron.com for further questions
- The following features require an active maintenance: Reports, ROI, Server monitor, Server sync, Windows Failover Cluster, Job Report Task
- The following features require a license of Subscription type: MFT, SLA, Health, Robot Task
- The following features require a license of unlimited type (Site or greater): Remote Execute Task
:::

### Features

:eight_spoked_asterisk: **Client/Server:** New Report->Server: Overview (VCP-312)

:eight_spoked_asterisk: **Client/Server:** New Report->Server: SLA (VCP-242,VCP-402,VCP-403)

:eight_spoked_asterisk: **Client/Server:** New Report->Server: Computer (VCP-295)

:eight_spoked_asterisk: **Client/Server:** Added SLA-stats (uptime, latency and outages) (VCP-366,VCP-355,VCP-403)

:eight_spoked_asterisk: **Client/Server:** Logs->New Transfer log table (VCPCM-445)

:eight_spoked_asterisk: **Client/Server:** New Report->Logs: Transfer log (VCPCM-158, VCPCM-443)

:eight_spoked_asterisk: **Client:** Various UI updates (VCP-354,VCP-326,VCP-389)

:eight_spoked_asterisk: **WebClient:** Various UI updates (VCP-351,VCP-352)

:eight_spoked_asterisk: **Server:** Server events->Logging internal events in the EventLogs table (VCP-359)

:eight_spoked_asterisk: **Client/Server:** Robot Task->Added Load list activity (VCP-397)

:eight_spoked_asterisk: **Client/Server:** Robot Task->Added ability to save Excel file in CSV format (VCP-392)

:eight_spoked_asterisk: **Client/Server:** Web macro Task->Added ability to use local URLs (VCP-377)

:eight_spoked_asterisk: **Client/Server:** Reports->Job list CSV output, Jobs and Groups filters, Job and Task column selection (VCP-322,VCP-391,VCP-405)

:eight_spoked_asterisk: **Client/Server:** Cloud transfer Tasks->Proxy settings can be configured for Azure Block Blob connection type (VCP-135)

### Bug Fixes

:white_check_mark: **Client:** SFTP component initialization (VCPCM-449)

:white_check_mark: **Client:** Server: Export Settings error when lacking Permissions (VCPCM-352)

:white_check_mark: **Client:** Server: WebMacro->Not saving "Allow to ignore the element" (VCPCM-356)

:white_check_mark: **Client:** Server: WebMacro->Table Extraction Wizard fixes (VCPCM-444)

:white_check_mark: **Client:** Server: WebMacro->TakeScreenshot Page mode (VCPCM-442)

:white_check_mark: **Client:** Server: Robot Task->Mapping mode (VCPCM-92)

:white_check_mark: **Client:** Client: Scan documents(local) bugfixes (VCPCM-450,VCPCM-452)

:white_check_mark: **Client:** Server: Email move Task folder bug fixed (VCP-328)

:white_check_mark: **Client:** Server: Email Get messages Task->Removing sensitive information from MailClient event log messages (VCPCM-43)

:white_check_mark: **Client:** Server: Execute script->Problem using multiple arguments in combination with quotes (VCP-314)

:white_check_mark: **Client:** Server: Robot Task->Fixed related actions issue (VCP-220)

:white_check_mark: **Client:** Server: Robot Task->Save record issue (VCP-300)

:white_check_mark: **Client:** Server: SFTP CreateFolder command fix (VCP-133)

:white_check_mark: **Client:** Server: Enforce HTTPS for amazon SNS (VCP-292)

:white_check_mark: **Client:** WebClient: AD authentication fix (VCP-344)

:white_check_mark: **Client:** Client/Server: AD authentication-> LDAP over SSL (LDAPS) support added for ports 636, 3269 (VCPCM-451)

:white_check_mark: **Client:** Client/Server: GroupOverride not working in connections fix (VCP-387)

:white_check_mark: **Client:** Client/Server: Reports->Various UI feedback (VCP-351,VCP-353,VCP-409)

:white_check_mark: **Client:** Client/Server: Reports->Report run "forever" issue (VCP-327)

:white_check_mark: **Client:** Client/Server: Job->Result report date filter issue (VCP-231)

:white_check_mark: **Client:** Client: Email Move Task->Fixed issue with destination folder (VCP-398,VCP-328)

:white_check_mark: **Client:** Client/Server: Reports Task->Fixed Credential issue (VCP-357)

:white_check_mark: **Client:** WebClient: Fixed issue opening Server settings (VCP-368)

:white_check_mark: **Client:** Client/Server: Robot Task->Added missing file (fix for web macro) (VCP-408)

:white_check_mark: **Client:** Client/Server: Robot Task->Added missing icons (VCP-407)

:white_check_mark: **Client:** Client/Server: Robot Task->Fix for possible AccessViolationException (VCP-282)

:white_check_mark: **Client:** Client/Server: DB logging->Retry fixes (VCP-304)

:white_check_mark: **Client:** Client/Server: DB logging->Access of multiple VC Servers under different users to the same Oracle database (VCPCM-80)

:white_check_mark: **Client:** Client/Server: DB logging->Added re-impersonation attempt after first connection failure in DBLogger (VCPCM-360)

:white_check_mark: **Client:** Client/Server: SFTP SSH_MA_NONE may lead to NullReferenceException (VCP-411)

:white_check_mark: **Client:** Server: Web macro->Show steps issue (VCP-290)

:white_check_mark: **Client:** Client/Server: Web macro Task->Fixed video output issue (VCP-416)

:white_check_mark: **Client:** Client/Server: Web macro Task->Optimized playback performance 1000% (VCP-376)

:white_check_mark: **Client:** Client/Server: Web macro Task->Fixed destroyed webview issue (VCP-373)

:white_check_mark: **Client:** Client/Server: Flow chart->Various fixes (VCP-421, VCP-422, VCP-460, VCPCM-338)

:white_check_mark: **Client:** Client/Server: Reports->Better form initialization; optimized Server log report generator (VCP-409)

:white_check_mark: **Client:** Client: Main grid->Fixed an issue with Job folder rows filtering outside of GUI thread (VCPCM-354)

## 10.0.1 [2023-05-08]  

### Features

:eight_spoked_asterisk: **Client/Server:** New Report Task to automate any of the existing reports (VCP-142)
:eight_spoked_asterisk: **WebClient:** Added Web service Task to web client (VCP-39)

:eight_spoked_asterisk: **Client/Server:** Create/Set-cell Excel Task->Added new cell type Formula (VCP-179)

:eight_spoked_asterisk: **Client/Server:** AMQP Connection->Certificate authentication mode was added (VCP-149)

:eight_spoked_asterisk: **Client/Server:** Triggers->New PowerShell Trigger was added (VCP-53)

:eight_spoked_asterisk: **Client/Server:** Triggers->New .NET code execute Trigger was added (VCP-55)

:eight_spoked_asterisk: **Client/Server:** Triggers->New Variable Trigger was added (VCP-157)

:eight_spoked_asterisk: **Client/Server:** Health->Default Health conditions updated to include both VC and OS CPU (VCP-125)

:eight_spoked_asterisk: **Client/Server:** Robot Task->Added Outlook application awareness (VCP-116)

:eight_spoked_asterisk: **Client/Server:** Variables->Added folder path Variabels (VCP-259)

:eight_spoked_asterisk: **Client/Server:** SFTP->Implemented better auto detect of encryption algorithms (VCP-260,VCP-270)

### Bug Fixes

:white_check_mark: **WebClient:** Updated version of jQuery for security (VCP-61)

:white_check_mark: **WebClient:** Fixed issue with Popup Task (VCP-175)

:white_check_mark: **Server:** WebAPI->Fixed background checking for expired user tokens (VCP-184)

:white_check_mark: **Client:** Create/Set-cell Excel Task->Fixed renumbering of columns when items are deleted (VCP-177)

:white_check_mark: **Client:** NullReferenceException on Server Health window (VCP-229)

:white_check_mark: **Client/Server:** ExecuteScript task defaults to ScriptText (VCP-238)

:white_check_mark: **Client/Server:** Desktop Trigger->Fixed various issues (VCP-163)

:white_check_mark: **Client/Server:** Robot Task->Fixed various issues (VCP-43,VCP-112,VCP-150,VCP-151)

:white_check_mark: **Client/Server:** Robot Task->Added error handling (VCP-113)

:white_check_mark: **Client/Server:** Google Drive->Fixed upload issue (VCP-48)

:white_check_mark: **Client/Server:** Exchange EWS refresh Token for Email tasks (VCP-249)

:white_check_mark: **Server:** Cloud File Trigger error when updating statistics (VCP-222)

:white_check_mark: **Server:** Box file download issue (VCP-277)

:white_check_mark: **Server:** List folders Task->Fixed issue exception throwed using some wildcards (VCP-148)

:white_check_mark: **Server:** Jobs->Fixed issue with file getting larged because of statistics stored (VCP-83)

:white_check_mark: **Client:** Scan document Task->Fixed admin permission requirements issue (VCP-275)

:white_check_mark: **Client:** Web macro Task->Fixed admin permission requirements issue (VCP-283)

:white_check_mark: **Client:** Main grid->Fixed progress update issue (VCP-285)

:white_check_mark: **Server:** HTTP Rest Trigger status code evaluation (VCP-289)

:white_check_mark: **Server:** Database copy->SqlCeCommand timeout error (VCP-287)

## 10.0.0 [2023-02-20]  

### Features

:eight_spoked_asterisk: **Client/Server:** Reports->Introducing Reports - advanced inside reports (VC-2910)

:eight_spoked_asterisk: **Client:** Flow chart->Added new flow chart (VC-2645)

:eight_spoked_asterisk: **Client/Server:** Tasks->New TCP Task was added (VCP-44)

:eight_spoked_asterisk: **Client/Server:** Triggers->New TCP Trigger was added (VCP-44)

:eight_spoked_asterisk: Server: Directory created variable for MFT (VCP-82)

:eight_spoked_asterisk: **Client/Server:** Execute Task->Added process queue functionality (VCP-159)

:eight_spoked_asterisk: **Client/Server:** File Trigger->Added consolidate changes option (VCP-162)

:eight_spoked_asterisk: **Client/Server:** Variables->Added number format Variables (VCP-170)

:eight_spoked_asterisk: **Client/Server:** RefreshToken stored encrypted (VCP-22)

### Bug Fixes

:white_check_mark: **Server:** Triggers->Fixed possible thread issue causing crash at high loads (VCP-73)
:white_check_mark: **Server:** Web client not updating/saving credentials (VCP-58)

:white_check_mark: **Server:** WebDAV download files task w/Variable in Path (VCP-27)

:white_check_mark: **Server:** HTTP Delete Method Issue (VCP-19)

:white_check_mark: **Server:** SqlConnection using service account works in SQL Trigger (VCP-23)

:white_check_mark: **Server:** Web client fix for crash when creating a job (VCP-72)

:white_check_mark: **Server:** Exchange EWS Certificate issue (VCP-52)

:white_check_mark: **Server:** Mail trigger for EWS: improved token expiry handlers (VCP-120,VCP-76)

:white_check_mark: **Server:** Mail trigger for EWS: custom folder setup minor bugfix (VCP-77)

:white_check_mark: **Server:** Mail trigger for EWS: minor bugfix when forwarding enabled (VCP-77)

:white_check_mark: **Server:** Mail trigger for EWS: AD users and groups permission check minor improvement (VCP-99)

:white_check_mark: **Server:** SSRS issue with Excel formatting (VCP-98)

:white_check_mark: **Client:** AddCredentials NRE fix (VCP-126)

:white_check_mark: **Server:** AD group integration/cache issue (VCP-99)

:white_check_mark: **Server:** Scan Document Task->Fixed potential crash (VCP-26)

:white_check_mark: **Server:** Bug with HTTPs webapi port (VCP-96)

:white_check_mark: **Server:** Slack Trigger bugfix (VCP-47)

:white_check_mark: **Server:** Server events->Fixed potential memory leak (VCP-155)

:white_check_mark: **Client:** SFTP connection editor for PublicKey authentication fix (VCP-161)

:white_check_mark: **Server:** JSON Decode Task empty value fix (VCP-49)

:white_check_mark: **Server:** WebAPI parameters fix (VCP-66)

:white_check_mark: **Server:** Web macro / Robot Edit Task exception fix (VCP-94)

:white_check_mark: **Server:** VCCommand missing file fix (VCP-136)

:white_check_mark: **Server:** SFTP list folders fix (VCP-32)

:white_check_mark: **Server:** List folder Task->Fixed wild card issue (VCP-148)

:white_check_mark: **Server:** Jobs definitions file grow issue (VCP-83)

:white_check_mark: **Client:** Main grid->Fixed filter re-sort issue after reconnecting (VCP-164)

:white_check_mark: **Client:** Execute/Kill Task (and more)->Fixed process selection issue (VCP-169)

:white_check_mark: **Server:** File Trigger->Fixed potential impersonation context leak to Job from Trigger (VCP-173)

:white_check_mark: **Server:** Triggers->Fixed potential Trigger result loss during execution (VCP-174)

:white_check_mark: **Client:** Script Execute Task->Fixed validation error that prevent save of option "Script text" (VCP-178)

:white_check_mark: **Client:** Local documentation updated (VCP-36,VCP-42)