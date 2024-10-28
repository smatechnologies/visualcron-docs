---
sidebar_label: 'Change Log'
hide_title: 'true'
---

## Change Log


 
11.2.3 [2024-09-23]

### Features

:eight_spoked_asterisk: Client/Server: Trial experience: Link to watch tutorial video redirect fix and update to content instructions (VCPCM-1609)

:eight_spoked_asterisk: Client/Server: Trial experience: Expiration path (VCPCM-1616)

:eight_spoked_asterisk: Client/Server: Trial experience: Path to purchase popups and trial expired window (VCPCM-950)

:eight_spoked_asterisk: Client/Server: Trial experience: Tutorial Window (VCPCM-945)

### Bug Fixes 

:white_check_mark: Client/Server: Reload button is not working for reloading the triggers during Task Creation for Inactivating/ Activating Triggers (VCPCM-1629)

:white_check_mark: Client/Server: Incorrect Triggers selected after clicking Reload button of the Inactivate Trigger Section (VCPCM-1628)

:white_check_mark: Client/Server: Robot Task: Interaction between the VisualCron client and third-party web browsers via web extensions (VCPCM-1608)

:white_check_mark: Client/Server: Activate/deactivate all triggers result not persisted (VCPCM-1562)

:white_check_mark: Client/Server: PGP Encryption reports error if file exists (VCPCM-1403)

:white_check_mark: Client/Server: DEV: Introducing new client settings to remember where user left off (which videos they`ve had the chance to watch) (VCPCM-1344)

:white_check_mark: Client/Server: Deleting a server throws error (VCPCM-1163)

:white_check_mark: Client/Server: (g)MSA account behavior fixed for Execute and Execute Powershell tasks (VCPCM-1162)

:white_check_mark: Client/Server: Sharepoint server-side explorer (VCPCM-509)


## 11.2.2 [2024-07-29]

[NOTE] Client/Server: Load Balancing is available in preview mode for subscription-based Pro licenses (VCPCM-1417)

### Bug Fixes

:white_check_mark: Client/Server: WebMacro improved when doing Test Runs (VCPCM-1392)

:white_check_mark: Client/Server: WebMacro Click to overwriting previous populate step in Test Run (VCPCM-1391)

:white_check_mark: Client/Server: Credentials in the Output tab for Web Macro is not saved (VCPCM-1245)

:white_check_mark: Client/Server: "Email - Send task" logging improved (VCPCM-1120)

:white_check_mark: Client/Server: The Output section of a SQL task would include headers, regardless of if any records were pulled (VCPCM-1057)

:white_check_mark: Client/Server: Trial Experience Current registration window improved (VCPCM-944)

## 11.2.1 [2024-06-24]

### Features

:eight_spoked_asterisk: **Client/Server:** Load Balancer for VisualCron is available for Preview

:eight_spoked_asterisk: **Client/Server:** Fully Server-side Sql Server Explorer (VCPCM-569)

### Bug Fixes

:white_check_mark: **Client/Server:** Web Macro Task Test Run behavior improved (VCPCM-1219,VCPCM-1215)

:white_check_mark: **Client/Server:** Robot Task Excel RowCount action behavior switched over to UsedRange functinonality (VCPCM-1124)

:white_check_mark: **Client/Server:** SMTP Outlook connectivity fixed handling org policies(VCPCM-596)

## 11.1.4 [2024-05-02]

### Features 

:eight_spoked_asterisk: **Client:** Server SLA and Server Health moved to Subscription tier (VCPCM-850)

### Bug Fixes

:white_check_mark: **Client:** Main screen Grid filter improved (VCPCM-1055)

:white_check_mark: **Client/Server:** Excel Convert Task adjusted on processing date(time) values (VCPCM-1054)

:white_check_mark: **Client/Server:** File Sync Task Extend Debug logging added (VCPCM-1053)

:white_check_mark: **Client:** Job and Task Log screens UX improved (VCPCM-1031)

:white_check_mark: **Client/Server:** Object Replaces for User Variables processing has been improved (VCPCM-713)

:white_check_mark: **Client/Server:** Detailed error messages fully under control of extended debugging flag (VCPCM-1055)

## 11.1.1 [2024-03-12]  

### Features

:eight_spoked_asterisk: **Client/Server:** Connections management is now available in WebClient (VCPCM-471)

:eight_spoked_asterisk: **Client/Server:** Add the capability to save the email body to an RPA variable within the Outlook "Get Message" activity (VCPCM-833)

:eight_spoked_asterisk: **Client/Server:** Add the ability to handle errors in Web Macro activities using the TryCatch activity (VCPCM-763)

### Bug Fixes

:white_check_mark: **Client/Server:** Running job in asyncronous mode behavior improved (VCPCM-858)

:white_check_mark: **Client/Server:** HTTP triggers now present full certificate chain for HTTPS connections (VCPCM-812)

:white_check_mark: **Client/Server:** NRE fixed when flows are being processed (VCPCM-731)

:white_check_mark: **Client/Server:** "JSON Encode" Task was failing generating a valid array out of the text file (VCPCM-715)

:white_check_mark: **Client/Server:** Blank file with just the header line results an empty SQL query (VCPCM-689)

:white_check_mark: **Client/Server:** Archive task instances are now isolated by using different temporary folders (VCPCM-679)

:white_check_mark: **Client/Server:** WebClient refreshes whenever a Job gets updated on server (VCPCM-637)

:white_check_mark: **Client/Server:** Slack event trigger fixed when listening to a channel (VCPCM-589)

:white_check_mark: **Client/Server:** Fixed automatic addition of a user certificate with a private key to the Trusted Root Certificates store (VCPCM-837)


## 11.0.0 [2024-01-29]  

### Features 

:eight_spoked_asterisk: **Client/Server:** Cookies data stored in Robot Task (VCPCM-660)

:eight_spoked_asterisk: **Client/Server:** Key press events added for web activities (VCPCM-655)

:eight_spoked_asterisk: **Client/Server:** OCR Improvements and fixes regarding text recognition area, UI element behavior, noise processing and OCR activity designer (VCPCM-680)

### Bug Fixes

:white_check_mark: **Client/Server:** PGKKeyrings operations improved when manipulating private keys (VCPCM-712)

:white_check_mark: **Client:** "Loop Variables" menu improved when working with the Loop activity designer (VCPCM-698)

:white_check_mark: **Client/Server:** Iteraction between ContinueLoop and Loop activities improved (VCPCM-691)

:white_check_mark: **Client/Server:** WebAPI now disregards certificates without private key (VCPCM-686)

:white_check_mark: **Client/Server:** "Job - List" Report does not check Theme when outputting to CSV format (VCPCM-656)

:white_check_mark: **Client/Server:** "Continue with next Task" is added back into flow (VCPCM-650)

:white_check_mark: **Client/Server:** Job variable evaluation fixed in Robot Task (VCPCM-648)

:white_check_mark: **Client/Server:** NullReferenceException fixed in SharePoint Download task (VCPCM-642)

:white_check_mark: **Client/Server:** WebMacro Task behavior fix, ensuring stable performance during the concurrent execution of multiple instances (VCPCM-641)

:white_check_mark: **Server:** WebAPI UTF8 support fixed for JSON endpoints (VCPCM-636)

:white_check_mark: **Client/Server:** Web Macro designer fixed when a task is disabled (VCPCM-618)

:white_check_mark: **Client/Server:** WebAPI Authentication improved on token management (VCPCM-588)

:white_check_mark: **Client/Server:** SyncFiles Task fixed when operating between two remote file shares (VCPCM-565)

:white_check_mark: **Client/Server:** Azure Connection empty file upload fixed behavior (VCPCM-402)

:white_check_mark: **Client/Server:** WebMacro Show Debugger crash fixed (VCPCM-335)

:white_check_mark: **Client/Server:** Transport security protocols updated for Azure Cloud connections (VCPCM-334)


## 10.0.3 [2023-12-14]  

### Features

:::info Notes

**Client/Server:** Eliminated licensing restrictions for the MFT feature (VCPCM-599)

**Client/Server:** Eliminated licensing restrictions for the RemoteExecute Task (VCPCM-583)

:::

:eight_spoked_asterisk: **Client/Server:** Added a new category "User input" for Robot Task (VCPCM-83)

:eight_spoked_asterisk: **Client/Server:** Introduced new features for the "PDF - add header/footer" task, including angle of rotation (in degrees) and opacity settings, along with updated documentation (VCPCM-544)

:eight_spoked_asterisk: **WebClient:** Implemented the Tools->Gantt chart feature (VCPCM-194)

### Bug Fixes

:white_check_mark: **Client/Server:** Removed Debugger detection when using VisualCron .NET API in custom .NET projects (VCPCM-619)

:white_check_mark: **Client/Server:** Resolved the issue causing service crashes in certain cases when completing the last Task (VCPCM-95)

:white_check_mark: **Client/Server:** Implemented permission checks for Read and Add (or Edit for ServerSettings) permissions in the Export and Import forms. If certain settings are not available for export or import, a warning message is displayed to the user (VCPCM-79)

:white_check_mark: **Client/Server:** Updated the vulnerable "Apache log4net" file (log4net.dll) version 1.2.10.0 to address "CVE-2018-1285" security vulnerability, ensuring enhanced security on Windows Server 2019 (VCPCM-77)

:white_check_mark: **Client/Server:** Implemented error handling for the "No file(s) found" scenario in the following tasks: Cloud List items, WebDAV List items, and Sharepoint List files (VCPCM-71)

:white_check_mark: **Client/Server:** Resolved the issue of system crashes occurring when attempting to stop a job in the middle of executing a stored procedure in SQL Task (VCPCM-61)

:white_check_mark: **Client/Server:** Refined limitations for RobotTask operations during Trial period (VCPCM-586)

[BUGFIX] **Client/Server:** Enhanced ParseVariable() error reporting. Fixed FTP/SFTP/SCP reconnection process. Fixed event skipping in the File Trigger when the "Consolidate changes" timeout is specified (VCPCM-585)

:white_check_mark: **Client/Server:** Excessive locks removed when processing Task Started/Completed events (VCPCM-584)

:white_check_mark: **Client/Server:** Corrected handling of "List Variable" activities to ensure proper function when encountering empty items (VCPCM-576)

:white_check_mark: **Client/Server:** Updated job termination logic to ensure the status is set to "Failure" when a job is forcibly stopped, correcting the previous behavior where it could erroneously report "Success" (VCPCM-573)

:white_check_mark: **Client/Server:** Introduced functionality to regenerate a list variable in the "List Variable Load" activity (VCPCM-570)

:white_check_mark: **Client/Server:** Refined impersonation handling and enhanced logging details for Sync/Copy file(s) Tasks (VCPCM-565)

:white_check_mark: **Client/Server:** Updated SCP transfer tasks with an enhanced component for more reliable SCP connections (VCPCM-561)

:white_check_mark: **Client/Server:** End-User License Agreement (EULA) revised (VCPCM-560)

:white_check_mark: **Client/Server:** Resolved issue with auto-generation of default Task Flows in Import/Export function (VCPCM-559)

:white_check_mark: **Client/Server:** Added a column selection feature to the "Historic - transfers" tab in the Log section (VCPCM-558)

:white_check_mark: **Client/Server:** Implemented logging for user impersonation errors prior to task execution (VCPCM-553)

:white_check_mark: **Client/Server:** Corrected the output formatting in the function for retrieving values from a "List variable" result (VCPCM-548)

:white_check_mark: **Client/Server:** Resolved the issue where executing Robot Tasks outside of test mode used insufficient "VisualCron system group" permissions, hindering the creation of new variables (VCPCM-546)

:white_check_mark: **Client/Server:** Enhanced the deactivation process for Triggers with expiration settings to function correctly (VCPCM-545)

:white_check_mark: **Client/Server:** Resolved the issue where the VisualCron server was unable to apply a self-signed certificate for securing a WebAPI endpoint (VCPCM-542)

:white_check_mark: **Client/Server:** Enhanced server log precision, secured XML file saving with locks, and improved thread-safe authorization for Box Connections (VCPCM-541)

:white_check_mark: **Client/Server:** Corrected the functionality for accurately reporting the amount of available RAM in Server Monitor (VCPCM-524)

:white_check_mark: **Client/Server:** Introduced features for customizing text recognition area and added notifications with guidance on selecting an OCR area (VCPCM-520)

:white_check_mark: **Client/Server:** Resolved an issue where headless browser became unresponsive after completing a sequence of activities, by replacing asynchronous calls with synchronous ones based on investigation findings (VCPCM-517)

:white_check_mark: **WebClient:** Corrected the functionality of the `Install` and `Enable` buttons for IIS and IIS Express in the Server Settings form (VCPCM-504)

:white_check_mark: **Client/Server:** Improved documentation for RobotTask (VCPCM-501)

:white_check_mark: **Client/Server:** Robot Task: Implemented error handling settings, including the addition of a form and a dialog box for configuring these activity parameters (VCPCM-5)

:white_check_mark: **Client/Server:** Resolved an error encountered when interacting with a screenshot that was previously utilized by the Scan Document (local) task (VCPCM-498)

:white_check_mark: **Client/Server:** Addressed and eliminated memory leaks in WebMacro Tasks during extensive usage scenarios (VCPCM-487)

:white_check_mark: **Client/Server:** Enhanced SFTP client configuration by implementing automatic selection of all supported KEX, PK, EA, MAC algorithms instead of just the one last reported by server (VCPCM-477)

:white_check_mark: **Client/Server:** Restored synchronization block for SAP to manage connection opening and job creation more effectively, along with other miscellaneous fixes (VCPCM-476)

:white_check_mark: **Client/Server:** Corrected log messages related to the user login process for clarity and accuracy (VCPCM-469)

:white_check_mark: **Client/Server:** Added support for LDAP over SSL (LDAPS) in AD authentication, accommodating ports 636 and 3269 (VCPCM-451)

:white_check_mark: **Client/Server:** Implemented functionality in the login form to reset an invalid Active Directory (AD) token if required, ensuring proper authentication (VCPCM-41)

:white_check_mark: **Client/Server:** Enhanced locking mechanisms and exception handling for Job processes to prevent instances of hanging at 99% completion (VCPCM-385)

:white_check_mark: **Client:** Introduced the ability to reveal job folders not only via the settings form but also through manual adjustment of the splitter (VCPCM-378)

:white_check_mark: **Client/Server:** Reduced the occurrence of application crashes attributed to resource errors when operating through Citrix (VCPCM-372)

:white_check_mark: **Client/Server:** Resolved the issue of reading empty stored procedure results in the SQL Task (VCPCM-371)

:white_check_mark: **Client/Server:** Enhanced the SQL Task by adding additional debug logging when retrieving a list of stored procedures for improved debugging and error tracking (VCPCM-37)

:white_check_mark: **Client/Server:** Implemented processor affinity in the task to optimize the configuration of thread count for the 7-zip compressor, ensuring more accurate performance (VCPCM-368)

:white_check_mark: **Client/Server:** Enhanced the EventLog Trigger to make three attempts to initiate the watcher and generate a Client event in the event of a failure (VCPCM-350)

:white_check_mark: **Client/Server:** In the Sharepoint Upload file(s) Task, when uploading files with recursive subfolders, the corresponding subfolders are now automatically generated on the site (VCPCM-347)

:white_check_mark: **Client/Server:** Enhanced the XML validation process by improving the method for obtaining the targetNamespace from XSD files (VCPCM-341)

:white_check_mark: **Client/Server:** Fixed the calculation of the relative destination path in Cloud Upload files when the Source folder in the File filter ends with a path separator, ensuring proper functionality (VCPCM-34)

:white_check_mark: **Client/Server:** Resolved the Task form crash issue that occurred when selecting the Cloud Copy/move Task type on the Main settings tab (VCPCM-333)

:white_check_mark: **Client/Server:** Implemented auto-replacement of incorrect characters in the message ID when generating the save path in the Email function (VCPCM-284)

:white_check_mark: **Client/Server:** Corrected the behavior where "User name not found" was being written to the internal cache when a user was not found (VCPCM-182)

:white_check_mark: **Client/Server:** Implemented changes that involve checking the IsMSA flag when connecting to the remote ManagementScope and logging unhandled exceptions in Task`s Debugging mode for improved debugging and error handling (VCPCM-162)

:white_check_mark: **Client/Server:** Enhanced the configuration of Popups by adding the capability to save previous input data to the cache (VCPCM-155)

:white_check_mark: **Client/Server:** Removed duplicate and outdated topics from the CHM help documentation (VCPCM-145)

:white_check_mark: **Client/Server:** Implemented automatic decoding of TNEF (winmail.dat) attachments in the Email functions (VCPCM-123)

:white_check_mark: **Client/Server:** Added missing locks when accessing the collection of Jobs (VCPCM-602)

:white_check_mark: **Client/Server:** Correct DbConnection disposal after testing connection settings or retrieving SP list and params (VCPCM-526)

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