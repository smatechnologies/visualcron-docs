---
sidebar_label: 'Change Log'
hide_title: 'true'
---

## Change Log

### 12.2.1 [2025-07-30]

#### Features

:star: Client/Server: Isolated and protected API library for custom Powershell or .NET integrations. .NET 4.8 assemblies to be found in lib directory in installation folder.


#### Bug Fixes


:white_check_mark: Client/Server: Oracle database driver support: dotConnect for Oracle by DevArt (VCPCM-2207)

:white_check_mark: Client/Server: Debugger detection still enabled for VisualCronAPI Libraries (VCPCM-2139)

:white_check_mark: Client/Server: WebMacro: Memory allocation improved (VCPCM-2111)

:white_check_mark: Client: Scrollbar missing from Job Grid (VCPCM-2102)

:white_check_mark: Client/Server: AD-group configuration credentials fix (VCPCM-2100)

:white_check_mark: Client/Server: RobotTask: Memory allocation improved (VCPCM-2098)

:white_check_mark: Client/Server: Timeout improved  when searching for objects (VCPCM-2082)

:white_check_mark: Client/Server: PGP - Encrypt not pulling up keys under "Signers" (VCPCM-2076)

:white_check_mark: Client/Server: License invalid due to problems with dotConnect Universal installation. (VCPCM-2065)

:white_check_mark: Client/Server: Unable to remove the default bucket name from an Amazon Connection (VCPCM-2001)

:white_check_mark: Client/Server: JSON task not working with Job variables (VCPCM-1990)

:white_check_mark: Client/Server: MSMQ Task: unable to set Label (VCPCM-1985)

:white_check_mark: Client/Server: Azure Files connectivity with storage-level SAS fixed (VCPCM-1978)

:white_check_mark: Client/Server: Installation package and MSI silent installation migrated (VCPCM-1963)

:white_check_mark: Client/Server: Automatically closing SFTP session when executing Sync Files task (VCPCM-1959)

:white_check_mark: Client/Server: CVE-2023-52168 with 7Zip out of compliance (VCPCM-1953)

:white_check_mark: Client: Customizable focused task menu/list for improved navigation (VCPCM-1870)

:white_check_mark: Client/Server: Installation of 12.0.2 was missing tasks folder and the exe for webmacro (VCPCM-1774)

:white_check_mark: Client/Server: Trying to delete credential just created fails (VCPCM-1772)

:white_check_mark: Client/Server: File Triggers retry logic improved (VCPCM-1737)

:white_check_mark: Client: Flow Chart Crashes (VCPCM-1718)

:white_check_mark: Client/Server: Scan task: Language option fixed (VCPCM-1713)

:white_check_mark: Client/Server: WebAPI: AD-authentication support (VCPCM-666)


### 12.1.4 [2025-04-14]

#### Bug Fixes


:white_check_mark: Client/Server: ROI feature availability fixed (VCPCM-1958)

:white_check_mark: Client/Server: Discrepancy between Connection Explorer and MFT server times adjusted (VCPCM-1951)

:white_check_mark: Client/Server: AWS S3 bucket upload failing error fixed (VCPCM-1950)

:white_check_mark: Client/Server: NRE when Accessing WebClient (VCPCM-1934)

:white_check_mark: Client/Server: NRE when doing Scan server(s) (VCPCM-1920)

:white_check_mark: Client/Server: Permission exceptions on startup (VCPCM-1918)

:white_check_mark: Client/Server: Add License expiration badge for connected server (VCPCM-1906)

:white_check_mark: Client/Server: Robot Task reduced perceived recording lag (VCPCM-1867)

:white_check_mark: Client/Server: AWS S3 not respecting default bucket configuration (VCPCM-1764)

:white_check_mark: Client/Server: Sharepoint Online Connection Explorer improved doing ASC based authentication (VCPCM-1741)

:white_check_mark: Client/Server: FTP(S) - Unable to view folders within remote folder browser (VCPCM-1723)

:white_check_mark: Client/Server: Trial Registratiuon routine improved (VCPCM-1706)


### 12.1.3 [2025-02-18]

#### Bug Fixes


:white_check_mark: Client/Server: Encryption init failure fix for new installations. (VCPCM-1892)


### 12.1.2 [2025-02-13]

#### Features

:star: Client/Server: CommandTimeout option for External Database logging implemented. (VCPCM-1869)

:star: Client/Server: Binary protection failure resolved. (VCPCM-1878)


#### Bug Fixes


:white_check_mark: Client/Server: Error in external SQL logging. (VCPCM-1876)

:white_check_mark: Client/Server: Job Variables evaluation fixed. (VCPCM-1866)


### 12.1.1 [2025-01-30]

#### Notes

:memo: Client/Server: Before upgrading to this version, please ensure you back up your data. Built-in users may experience compatibility issues due to the VCPCM-677 improvement.


#### Bug Fixes


:white_check_mark: Client/Server: Configuration files clean-up (VCPCM-1766)

:white_check_mark: Client/Server: Communication between Server and Tray Client fixed for sensitive data. (VCPCM-1756)

:white_check_mark: Client/Server: Hashing algorithm improved when securely storing built-in users passwords. (VCPCM-677)

:white_check_mark: Client/Server: Permissions discrepancies fixed (VCPCM-1739)


### 12.0.2 [2024-12-02]

#### Bug Fixes


:white_check_mark: Client/Server: Log Database cleanup improved (VCPCM-1563)

:white_check_mark: Client/Server: List permission has been discontinued. Please use Read permission to access object lists or individual objects. (VCPCM-1738)

:white_check_mark: Client/Server: Group Permission editing fixed for admin users. (VCPCM-1755)


### 12.0.1 [2024-10-31]

#### Bug Fixes


:white_check_mark: Client: User synchronization with the server was blocked due to permissions validation. (VCPCM-1714)


### 12.0.0 [2024-10-28]

#### Features

:star: Client/Server: Security Enhancement: Sensitive data is now obfuscated during transmission from server to client to prevent unauthorized access to server, user, or database credentials stored on the server. Note: This server version is not compatible with previous client versions. (VCPCM-672)

:star: Client/Server: Security Enhancement: Permissions are now evaluated server-side to prevent unauthorized access to sensitive functionality and data. Note: VisualCron clients from previous versions are not compatible with the current server version. (VCPCM-675)

:star: Client/Server: Connection Explorer now operates exclusively server-side. (VCPCM-468)


#### Bug Fixes


:white_check_mark: Client: SecurityException fix when starting the VisualCron Client (VCPCM-1673)

:white_check_mark: Client/Server: VisualCron Client is now responsive when Connection is being tested in Connection Editor (VCPCM-1669)

:white_check_mark: Client/Server: PGP Encryption reports process error if target file exists (VCPCM-1403)

:white_check_mark: Client/Server: Azure Datalake Gen 2 functionality fixed (VCPCM-668)

:white_check_mark: Client/Server: PGP Encryption reports error if file exists (VCPCM-1403)

:white_check_mark: Client/Server: NRE fix when there is version mismatch between the Client and the Server (VCPCM-1672)


### 11.2.3 [2024-09-23]

#### Features

:star: Client/Server: Trial experience: Link to watch tutorial video redirect fix and update to content instructions (VCPCM-1609)

:star: Client/Server: Trial experience: Expiration path (VCPCM-1616)

:star: Client/Server: Trial experience: Path to purchase popups and trial expired window (VCPCM-950)

:star: Client/Server: Trial experience: Tutorial Window (VCPCM-945)


#### Bug Fixes


:white_check_mark: Client/Server: Reload button is not working for reloading the triggers during Task Creation for Inactivating/ Activating Triggers (VCPCM-1629)

:white_check_mark: Client/Server: Incorrect Triggers selected after clicking Reload button of the Inactivate Trigger Section (VCPCM-1628)

:white_check_mark: Client/Server: Robot Task: Interaction between the VisualCron client and third-party web browsers via web extensions (VCPCM-1608)

:white_check_mark: Client/Server: Activate/deactivate all triggers result not persisted (VCPCM-1562)

:white_check_mark: Client/Server: PGP Encryption reports error if file exists (VCPCM-1403)

:white_check_mark: Client/Server: DEV: Introducing new client settings to remember where user left off (which videos they`ve had the chance to watch) (VCPCM-1344)

:white_check_mark: Client/Server: Deleting a server throws error (VCPCM-1163)

:white_check_mark: Client/Server: (g)MSA account behavior fixed for Execute and Execute Powershell tasks (VCPCM-1162)

:white_check_mark: Client/Server: Sharepoint server-side explorer (VCPCM-509)


### 11.2.2 [2024-07-29]

#### Notes

:memo: Client/Server: Load Balancing is available in preview mode for subscription-based Pro licenses (VCPCM-1417)


#### Bug Fixes


:white_check_mark: Client/Server: WebMacro improved when doing Test Runs (VCPCM-1392)

:white_check_mark: Client/Server: WebMacro Click to overwriting previous populate step in Test Run (VCPCM-1391)

:white_check_mark: Client/Server: Credentials in the Output tab for Web Macro is not saved (VCPCM-1245)

:white_check_mark: Client/Server: "Email - Send task" logging improved (VCPCM-1120)

:white_check_mark: Client/Server:  The Output section of a SQL task would include headers, regardless of if any records were pulled (VCPCM-1057)

:white_check_mark: Client/Server: Trial Experience  Current registration window improved (VCPCM-944)


### 11.2.1 [2024-06-24]

#### Features

:star: Client/Server: Load Balancer for VisualCron is available for Preview

:star: Client/Server: Fully Server-side Sql Server Explorer (VCPCM-569)


#### Bug Fixes


:white_check_mark: Client/Server: Web Macro Task Test Run behavior improved (VCPCM-1219,VCPCM-1215)

:white_check_mark: Client/Server: Robot Task Excel RowCount action behavior switched over to UsedRange functinonality (VCPCM-1124)

:white_check_mark: Client/Server:  SMTP Outlook connectivity fixed handling org policies(VCPCM-596)


### 11.1.4 [2024-05-02]

#### Features

:star: Client: Server SLA and Server Health moved to Subscription tier (VCPCM-850)


#### Bug Fixes


:white_check_mark: Client: Main screen Grid filter improved  (VCPCM-1055)

:white_check_mark: Client/Server: Excel Convert Task adjusted on processing date(time) values (VCPCM-1054)

:white_check_mark: Client/Server: File Sync Task Extend Debug logging added  (VCPCM-1053)

:white_check_mark: Client: Job and Task Log screens UX improved (VCPCM-1031)

:white_check_mark: Client/Server: Object Replaces for User Variables processing has been improved (VCPCM-713)

:white_check_mark: Client/Server: Detailed error messages fully under control of extended debugging flag (VCPCM-1055)


### 11.1.3 [2024-04-11]

#### Bug Fixes


:white_check_mark: Client: VisualCron Client WebView screens fine-tune regarding background process configuration (VCPCM-1030)

:white_check_mark: Client: Populate Field activity revised for WebMacro Task (VCPCM-981)


### 11.1.2 [2024-04-05]

#### Bug Fixes


:white_check_mark: Client/Server: RPA recorder improved while capturing steps (VCPCM-993)

:white_check_mark: Client/Server: Reports Task NRE fixed (VCPCM-992)

:white_check_mark: Client/Server: "Ignore server Off (always run)" now is respected if service is restarted (VCPCM-979)

:white_check_mark: Client/Server: Memory consumption fine-tuned for Robot Task (VCPCM-972)

:white_check_mark: Client/Server: Remote PowerShell Jobs behavior was improved (VCPCM-971)

:white_check_mark: Client/Server: Local OCR Task Task editor is fixed  (VCPCM-967)

:white_check_mark: Client/Server: Get Single Email Message task now has folder set up drop down  (VCPCM-966)

:white_check_mark: Client/Server: Optimization report base line was fixed (VCPCM-964)

:white_check_mark: Client/Server: Scan Document improvement. Generic Error GDI+ fix (VCPCM-925)

:white_check_mark: Client/Server: Report Task now supports Variables for Date Range (VCPCM-653)

:white_check_mark: Client/Server: File triggers now attempt to reconnect properly without disabling a trigger (VCPCM-639)


### 11.1.1 [2024-03-12]

#### Features

:star: Client/Server: Connections management is now available in WebClient (VCPCM-471)

:star: Client/Server: Add the capability to save the email body to an RPA variable within the Outlook "Get Message" activity (VCPCM-833)

:star: Client/Server: Add the ability to handle errors in Web Macro activities using the TryCatch activity (VCPCM-763)


#### Bug Fixes


:white_check_mark: Client/Server: Running job in asyncronous mode behavior improved (VCPCM-858)

:white_check_mark: Client/Server: HTTP triggers now present full certificate chain for HTTPS connections (VCPCM-812)

:white_check_mark: Client/Server: NRE fixed when flows are being processed (VCPCM-731)

:white_check_mark: Client/Server: "JSON Encode" Task was failing generating a valid array out of the text file (VCPCM-715)

:white_check_mark: Client/Server: Blank file with just the header line results an empty SQL query (VCPCM-689)

:white_check_mark: Client/Server: Archive task instances are now isolated by using different temporary folders (VCPCM-679)

:white_check_mark: Client/Server: WebClient refreshes whenever a Job gets updated on server (VCPCM-637)

:white_check_mark: Client/Server: Slack event trigger fixed when listening to a channel (VCPCM-589)

:white_check_mark: Client/Server: Fixed automatic addition of a user certificate with a private key to the Trusted Root Certificates store (VCPCM-837)


### 11.0.0 [2024-01-29]

#### Features

:star: Client/Server: Cookies data stored in Robot Task (VCPCM-660)

:star: Client/Server: Key press events added for web activities (VCPCM-655)

:star: Client/Server: OCR Improvements and fixes regarding text recognition area, UI element behavior, noise processing and OCR activity designer (VCPCM-680)


#### Bug Fixes


:white_check_mark: Client/Server: PGKKeyrings operations improved when manipulating private keys (VCPCM-712)

:white_check_mark: Client: "Loop Variables" menu improved when working with the Loop activity designer (VCPCM-698)

:white_check_mark: Client/Server: Iteraction between ContinueLoop and Loop activities improved (VCPCM-691)

:white_check_mark: Client/Server: WebAPI now disregards certificates without private key (VCPCM-686)

:white_check_mark: Client/Server: "Job - List" Report does not check Theme when outputting to CSV format (VCPCM-656)

:white_check_mark: Client/Server: "Continue with next Task" is added back into flow (VCPCM-650)

:white_check_mark: Client/Server: Job variable evaluation fixed in Robot Task (VCPCM-648)

:white_check_mark: Client/Server: NullReferenceException fixed in SharePoint Download task (VCPCM-642)

:white_check_mark: Client/Server: WebMacro Task behavior fix, ensuring stable performance during the concurrent execution of multiple instances (VCPCM-641)

:white_check_mark: Server: WebAPI UTF8 support fixed for JSON endpoints (VCPCM-636)

:white_check_mark: Client/Server: Web Macro designer fixed when a task is disabled (VCPCM-618)

:white_check_mark: Client/Server: WebAPI Authentication improved on token management (VCPCM-588)

:white_check_mark: Client/Server: SyncFiles Task fixed when operating between two remote file shares (VCPCM-565)

:white_check_mark: Client/Server: Azure Connection empty file upload fixed behavior (VCPCM-402)

:white_check_mark: Client/Server: WebMacro Show Debugger crash fixed (VCPCM-335)

:white_check_mark: Client/Server: Transport security protocols updated for Azure Cloud connections (VCPCM-334)


### 10.0.3 [2023-12-14]

#### Notes

:memo: Client/Server: Eliminated licensing restrictions for the MFT feature (VCPCM-599)

:memo: Client/Server: Eliminated licensing restrictions for the RemoteExecute Task (VCPCM-583)


#### Features

:star: Client/Server: Added a new category "User input" for Robot Task (VCPCM-83)

:star: Client/Server: Introduced new features for the "PDF - add header/footer" task, including angle of rotation (in degrees) and opacity settings, along with updated documentation (VCPCM-544)

:star: WebClient: Implemented the Tools->Gantt chart feature (VCPCM-194)


#### Bug Fixes


:white_check_mark: Client/Server: Removed Debugger detection when using VisualCron .NET API in custom .NET projects (VCPCM-619)

:white_check_mark: Client/Server: Resolved the issue causing service crashes in certain cases when completing the last Task (VCPCM-95)

:white_check_mark: Client/Server: Implemented permission checks for Read and Add (or Edit for ServerSettings) permissions in the Export and Import forms. If certain settings are not available for export or import, a warning message is displayed to the user (VCPCM-79)

:white_check_mark: Client/Server: Updated the vulnerable "Apache log4net" file (log4net.dll) version 1.2.10.0 to address "CVE-2018-1285" security vulnerability, ensuring enhanced security on Windows Server 2019 (VCPCM-77)

:white_check_mark: Client/Server: Implemented error handling for the "No file(s) found" scenario in the following tasks: Cloud List items, WebDAV List items, and Sharepoint List files (VCPCM-71)

:white_check_mark: Client/Server: Resolved the issue of system crashes occurring when attempting to stop a job in the middle of executing a stored procedure in SQL Task (VCPCM-61)

:white_check_mark: Client/Server: Refined limitations for RobotTask operations during Trial period (VCPCM-586)

:white_check_mark: Client/Server: Enhanced ParseVariable() error reporting. Fixed FTP/SFTP/SCP reconnection process. Fixed event skipping in the File Trigger when the "Consolidate changes" timeout is specified (VCPCM-585)

:white_check_mark: Client/Server: Excessive locks removed when processing Task Started/Completed events (VCPCM-584)

:white_check_mark: Client/Server: Corrected handling of "List Variable" activities to ensure proper function when encountering empty items (VCPCM-576)

:white_check_mark: Client/Server: Updated job termination logic to ensure the status is set to "Failure" when a job is forcibly stopped, correcting the previous behavior where it could erroneously report "Success" (VCPCM-573)

:white_check_mark: Client/Server: Introduced functionality to regenerate a list variable in the "List Variable Load" activity (VCPCM-570)

:white_check_mark: Client/Server: Refined impersonation handling and enhanced logging details for Sync/Copy file(s) Tasks (VCPCM-565)

:white_check_mark: Client/Server: Updated SCP transfer tasks with an enhanced component for more reliable SCP connections (VCPCM-561)

:white_check_mark: Client/Server: End-User License Agreement (EULA) revised (VCPCM-560)

:white_check_mark: Client/Server: Resolved issue with auto-generation of default Task Flows in Import/Export function (VCPCM-559)

:white_check_mark: Client/Server: Added a column selection feature to the "Historic - transfers" tab in the Log section (VCPCM-558)

:white_check_mark: Client/Server: Implemented logging for user impersonation errors prior to task execution (VCPCM-553)

:white_check_mark: Client/Server: Corrected the output formatting in the function for retrieving values from a "List variable" result (VCPCM-548)

:white_check_mark: Client/Server: Resolved the issue where executing Robot Tasks outside of test mode used insufficient "VisualCron system group" permissions, hindering the creation of new variables (VCPCM-546)

:white_check_mark: Client/Server: Enhanced the deactivation process for Triggers with expiration settings to function correctly (VCPCM-545)

:white_check_mark: Client/Server: Resolved the issue where the VisualCron server was unable to apply a self-signed certificate for securing a WebAPI endpoint (VCPCM-542)

:white_check_mark: Client/Server: Enhanced server log precision, secured XML file saving with locks, and improved thread-safe authorization for Box Connections (VCPCM-541)

:white_check_mark: Client/Server: Corrected the functionality for accurately reporting the amount of available RAM in Server Monitor (VCPCM-524)

:white_check_mark: Client/Server: Introduced features for customizing text recognition area and added notifications with guidance on selecting an OCR area (VCPCM-520)

:white_check_mark: Client/Server: Resolved an issue where headless browser became unresponsive after completing a sequence of activities, by replacing asynchronous calls with synchronous ones based on investigation findings (VCPCM-517)

:white_check_mark: WebClient: Corrected the functionality of the `Install` and `Enable` buttons for IIS and IIS Express in the Server Settings form (VCPCM-504)

:white_check_mark: Client/Server: Improved documentation for RobotTask (VCPCM-501)

:white_check_mark: Client/Server: Robot Task: Implemented error handling settings, including the addition of a form and a dialog box for configuring these activity parameters (VCPCM-5)

:white_check_mark: Client/Server: Resolved an error encountered when interacting with a screenshot that was previously utilized by the Scan Document (local) task (VCPCM-498)

:white_check_mark: Client/Server: Addressed and eliminated memory leaks in WebMacro Tasks during extensive usage scenarios (VCPCM-487)

:white_check_mark: Client/Server: Enhanced SFTP client configuration by implementing automatic selection of all supported KEX, PK, EA, MAC algorithms instead of just the one last reported by server (VCPCM-477)

:white_check_mark: Client/Server: Restored synchronization block for SAP to manage connection opening and job creation more effectively, along with other miscellaneous fixes (VCPCM-476)

:white_check_mark: Client/Server: Corrected log messages related to the user login process for clarity and accuracy (VCPCM-469)

:white_check_mark: Client/Server: Added support for LDAP over SSL (LDAPS) in AD authentication, accommodating ports 636 and 3269 (VCPCM-451)

:white_check_mark: Client/Server: Implemented functionality in the login form to reset an invalid Active Directory (AD) token if required, ensuring proper authentication (VCPCM-41)

:white_check_mark: Client/Server: Enhanced locking mechanisms and exception handling for Job processes to prevent instances of hanging at 99% completion (VCPCM-385)

:white_check_mark: Client: Introduced the ability to reveal job folders not only via the settings form but also through manual adjustment of the splitter (VCPCM-378)

:white_check_mark: Client/Server: Reduced the occurrence of application crashes attributed to resource errors when operating through Citrix (VCPCM-372)

:white_check_mark: Client/Server: Resolved the issue of reading empty stored procedure results in the SQL Task (VCPCM-371)

:white_check_mark: Client/Server: Enhanced the SQL Task by adding additional debug logging when retrieving a list of stored procedures for improved debugging and error tracking (VCPCM-37)

:white_check_mark: Client/Server: Implemented processor affinity in the task to optimize the configuration of thread count for the 7-zip compressor, ensuring more accurate performance (VCPCM-368)

:white_check_mark: Client/Server: Enhanced the EventLog Trigger to make three attempts to initiate the watcher and generate a Client event in the event of a failure (VCPCM-350)

:white_check_mark: Client/Server: In the Sharepoint Upload file(s) Task, when uploading files with recursive subfolders, the corresponding subfolders are now automatically generated on the site (VCPCM-347)

:white_check_mark: Client/Server: Enhanced the XML validation process by improving the method for obtaining the targetNamespace from XSD files (VCPCM-341)

:white_check_mark: Client/Server: Fixed the calculation of the relative destination path in Cloud Upload files when the Source folder in the File filter ends with a path separator, ensuring proper functionality (VCPCM-34)

:white_check_mark: Client/Server: Resolved the Task form crash issue that occurred when selecting the Cloud Copy/move Task type on the Main settings tab (VCPCM-333)

:white_check_mark: Client/Server: Implemented auto-replacement of incorrect characters in the message ID when generating the save path in the Email function (VCPCM-284)

:white_check_mark: Client/Server: Corrected the behavior where "User name not found" was being written to the internal cache when a user was not found (VCPCM-182)

:white_check_mark: Client/Server: Implemented changes that involve checking the IsMSA flag when connecting to the remote ManagementScope and logging unhandled exceptions in Task`s Debugging mode for improved debugging and error handling (VCPCM-162)

:white_check_mark: Client/Server: Enhanced the configuration of Popups by adding the capability to save previous input data to the cache (VCPCM-155)

:white_check_mark: Client/Server: Removed duplicate and outdated topics from the CHM help documentation (VCPCM-145)

:white_check_mark: Client/Server: Implemented automatic decoding of TNEF (winmail.dat) attachments in the Email functions (VCPCM-123)

:white_check_mark: Client/Server: Added missing locks when accessing the collection of Jobs (VCPCM-602)

:white_check_mark: Client/Server: Correct DbConnection disposal after testing connection settings or retrieving SP list and params (VCPCM-526)


### 10.0.2 [2023-09-27]

#### Notes

:memo: This version contains new license changes. Below is a list of changes. Please contact sales@visualcron.com for further questions

:memo: The following features require an active maintenance: Reports, ROI, Server monitor, Server sync, Windows Failover Cluster, Job Report Task

:memo: The following features require a license of Subscription type: MFT, SLA, Health, Robot Task

:memo: The following features require a license of unlimited type (Site or greater): Remote Execute Task


#### Features

:star: Client/Server: New Report->Server: Overview (VCP-312)

:star: Client/Server: New Report->Server: SLA (VCP-242,VCP-402,VCP-403)

:star: Client/Server: New Report->Server: Computer (VCP-295)

:star: Client/Server: Added SLA-stats (uptime, latency and outages) (VCP-366,VCP-355,VCP-403)

:star: Client/Server: Logs->New Transfer log table (VCPCM-445)

:star: Client/Server: New Report->Logs: Transfer log (VCPCM-158, VCPCM-443)

:star: Client: Various UI updates (VCP-354,VCP-326,VCP-389)

:star: WebClient: Various UI updates (VCP-351,VCP-352)

:star: Server: Server events->Logging internal events in the EventLogs table (VCP-359)

:star: Client/Server: Robot Task->Added Load list activity (VCP-397)

:star: Client/Server: Robot Task->Added ability to save Excel file in CSV format (VCP-392)

:star: Client/Server: Web macro Task->Added ability to use local URLs (VCP-377)

:star: Client/Server: Reports->Job list CSV output, Jobs and Groups filters, Job and Task column selection (VCP-322,VCP-391,VCP-405)

:star: Client/Server: Cloud transfer Tasks->Proxy settings can be configured for Azure Block Blob connection type (VCP-135)


#### Bug Fixes


:white_check_mark: Client: SFTP component initialization (VCPCM-449)

:white_check_mark: Server: Export Settings error when lacking Permissions (VCPCM-352)

:white_check_mark: Server: WebMacro->Not saving "Allow to ignore the element" (VCPCM-356)

:white_check_mark: Server: WebMacro->Table Extraction Wizard fixes (VCPCM-444)

:white_check_mark: Server: WebMacro->TakeScreenshot Page mode (VCPCM-442)

:white_check_mark: Server: Robot Task->Mapping mode (VCPCM-92)

:white_check_mark: Client: Scan documents(local) bugfixes (VCPCM-450,VCPCM-452)

:white_check_mark: Server: Email move Task folder bug fixed (VCP-328)

:white_check_mark: Server: Email Get messages Task->Removing sensitive information from MailClient event log messages (VCPCM-43)

:white_check_mark: Server: Execute script->Problem using multiple arguments in combination with quotes (VCP-314)

:white_check_mark: Server: Robot Task->Fixed related actions issue (VCP-220)

:white_check_mark: Server: Robot Task->Save record issue (VCP-300)

:white_check_mark: Server: SFTP CreateFolder command fix (VCP-133)

:white_check_mark: Server: Enforce HTTPS for amazon SNS (VCP-292)

:white_check_mark: WebClient: AD authentication fix (VCP-344)

:white_check_mark: Client/Server: AD authentication-> LDAP over SSL (LDAPS) support added for ports 636, 3269 (VCPCM-451)

:white_check_mark: Client/Server: GroupOverride not working in connections fix (VCP-387)

:white_check_mark: Client/Server: Reports->Various UI feedback (VCP-351,VCP-353,VCP-409)

:white_check_mark: Client/Server: Reports->Report run "forever" issue (VCP-327)

:white_check_mark: Client/Server: Job->Result report date filter issue (VCP-231)

:white_check_mark: Client: Email Move Task->Fixed issue with destination folder (VCP-398,VCP-328)

:white_check_mark: Client/Server: Reports Task->Fixed Credential issue (VCP-357)

:white_check_mark: WebClient: Fixed issue opening Server settings (VCP-368)

:white_check_mark: Client/Server: Robot Task->Added missing file (fix for web macro) (VCP-408)

:white_check_mark: Client/Server: Robot Task->Added missing icons (VCP-407)

:white_check_mark: Client/Server: Robot Task->Fix for possible AccessViolationException (VCP-282)

:white_check_mark: Client/Server: DB logging->Retry fixes (VCP-304)

:white_check_mark: Client/Server: DB logging->Access of multiple VC Servers under different users to the same Oracle database (VCPCM-80)

:white_check_mark: Client/Server: DB logging->Added re-impersonation attempt after first connection failure in DBLogger (VCPCM-360)

:white_check_mark: Client/Server: SFTP SSH_MA_NONE may lead to NullReferenceException (VCP-411)

:white_check_mark: Server: Web macro->Show steps issue (VCP-290)

:white_check_mark: Client/Server: Web macro Task->Fixed video output issue (VCP-416)

:white_check_mark: Client/Server: Web macro Task->Optimized playback performance 1000% (VCP-376)

:white_check_mark: Client/Server: Web macro Task->Fixed destroyed webview issue (VCP-373)

:white_check_mark: Client/Server: Flow chart->Various fixes (VCP-421, VCP-422, VCP-460, VCPCM-338)

:white_check_mark: Client/Server: Reports->Better form initialization; optimized Server log report generator (VCP-409)

:white_check_mark: Client: Main grid->Fixed an issue with Job folder rows filtering outside of GUI thread (VCPCM-354)


### 10.0.1 [2023-05-08]

#### Features

:star: Client/Server: New Report Task to automate any of the existing reports (VCP-142)

:star: WebClient: Added Web service Task to web client (VCP-39)

:star: Client/Server: Create/Set-cell Excel Task->Added new cell type Formula (VCP-179)

:star: Client/Server: AMQP Connection->Certificate authentication mode was added (VCP-149)

:star: Client/Server: Triggers->New PowerShell Trigger was added (VCP-53)

:star: Client/Server: Triggers->New .NET code execute Trigger was added (VCP-55)

:star: Client/Server: Triggers->New Variable Trigger was added (VCP-157)

:star: Client/Server: Health->Default Health conditions updated to include both VC and OS CPU (VCP-125)

:star: Client/Server: Robot Task->Added Outlook application awareness (VCP-116)

:star: Client/Server: Variables->Added folder path Variabels (VCP-259)

:star: Client/Server: SFTP->Implemented better auto detect of encryption algorithms (VCP-260,VCP-270)


#### Bug Fixes


:white_check_mark: WebClient: Updated version of jQuery for security (VCP-61)

:white_check_mark: WebClient: Fixed issue with Popup Task (VCP-175)

:white_check_mark: Server: WebAPI->Fixed background checking for expired user tokens (VCP-184)

:white_check_mark: Client: Create/Set-cell Excel Task->Fixed renumbering of columns when items are deleted (VCP-177)

:white_check_mark: Client: NullReferenceException on Server Health window (VCP-229)

:white_check_mark: Client/Server: ExecuteScript task defaults to ScriptText (VCP-238)

:white_check_mark: Client/Server: Desktop Trigger->Fixed various issues (VCP-163)

:white_check_mark: Client/Server: Robot Task->Fixed various issues (VCP-43,VCP-112,VCP-150,VCP-151)

:white_check_mark: Client/Server: Robot Task->Added error handling (VCP-113)

:white_check_mark: Client/Server: Google Drive->Fixed upload issue (VCP-48)

:white_check_mark: Client/Server: Exchange EWS refresh Token for Email tasks (VCP-249)

:white_check_mark: Server: Cloud File Trigger error when updating statistics (VCP-222)

:white_check_mark: Server: Box file download issue (VCP-277)

:white_check_mark: Server: List folders Task->Fixed issue exception throwed using some wildcards (VCP-148)

:white_check_mark: Server: Jobs->Fixed issue with file getting larged because of statistics stored (VCP-83)

:white_check_mark: Client: Scan document Task->Fixed admin permission requirements issue (VCP-275)

:white_check_mark: Client: Web macro Task->Fixed admin permission requirements issue (VCP-283)

:white_check_mark: Client: Main grid->Fixed progress update issue (VCP-285)

:white_check_mark: Server: HTTP Rest Trigger status code evaluation (VCP-289)

:white_check_mark: Server: Database copy->SqlCeCommand timeout error (VCP-287)


### 10.0.0 [2023-02-20]

#### Features

:star: Client/Server: Reports->Introducing Reports - advanced inside reports (VC-2910)

:star: Client: Flow chart->Added new flow chart (VC-2645)

:star: Client/Server: Tasks->New TCP Task was added (VCP-44)

:star: Client/Server: Triggers->New TCP Trigger was added (VCP-44)

:star: Server: Directory created variable for MFT (VCP-82)

:star: Client/Server: Execute Task->Added process queue functionality (VCP-159)

:star: Client/Server: File Trigger->Added consolidate changes option (VCP-162)

:star: Client/Server: Variables->Added number format Variables (VCP-170)

:star: Client/Server: RefreshToken stored encrypted (VCP-22)


#### Bug Fixes


:white_check_mark: Server: Triggers->Fixed possible thread issue causing crash at high loads (VCP-73)

:white_check_mark: Server: Web client not updating/saving credentials (VCP-58)

:white_check_mark: Server: WebDAV download files task w/Variable in Path (VCP-27)

:white_check_mark: Server: HTTP Delete Method Issue (VCP-19)

:white_check_mark: Server: SqlConnection using service account works in SQL Trigger (VCP-23)

:white_check_mark: Server: Web client fix for crash when creating a job (VCP-72)

:white_check_mark: Server: Exchange EWS Certificate issue (VCP-52)

:white_check_mark: Server: Mail trigger for EWS: improved token expiry handlers (VCP-120,VCP-76)

:white_check_mark: Server: Mail trigger for EWS: custom folder setup minor bugfix (VCP-77)

:white_check_mark: Server: Mail trigger for EWS: minor bugfix when forwarding enabled (VCP-77)

:white_check_mark: Server: Mail trigger for EWS: AD users and groups permission check minor improvement (VCP-99)

:white_check_mark: Server: SSRS issue with Excel formatting (VCP-98)

:white_check_mark: Client: AddCredentials NRE fix (VCP-126)

:white_check_mark: Server: AD group integration/cache issue (VCP-99)

:white_check_mark: Server: Scan Document Task->Fixed potential crash (VCP-26)

:white_check_mark: Server: Bug with HTTPs webapi port (VCP-96)

:white_check_mark: Server: Slack Trigger bugfix (VCP-47)

:white_check_mark: Server: Server events->Fixed potential memory leak (VCP-155)

:white_check_mark: Client: SFTP connection editor for PublicKey authentication fix (VCP-161)

:white_check_mark: Server: JSON Decode Task empty value fix (VCP-49)

:white_check_mark: Server: WebAPI parameters fix (VCP-66)

:white_check_mark: Server: Web macro / Robot Edit Task exception fix (VCP-94)

:white_check_mark: Server: VCCommand missing file fix (VCP-136)

:white_check_mark: Server: SFTP list folders fix (VCP-32)

:white_check_mark: Server: List folder Task->Fixed wild card issue (VCP-148)

:white_check_mark: Server: Jobs definitions file grow issue (VCP-83)

:white_check_mark: Client: Main grid->Fixed filter re-sort issue after reconnecting (VCP-164)

:white_check_mark: Client: Execute/Kill Task (and more)->Fixed process selection issue (VCP-169)

:white_check_mark: Server: File Trigger->Fixed potential impersonation context leak to Job from Trigger (VCP-173)

:white_check_mark: Server: Triggers->Fixed potential Trigger result loss during execution (VCP-174)

:white_check_mark: Client: Script Execute Task->Fixed validation error that prevent save of option "Script text" (VCP-178)

:white_check_mark: Client: Local documentation updated (VCP-36,VCP-42)


### 9.9.12 [2022-11-07]

#### Bug Fixes


:white_check_mark: Server: Email Trigger->Removed password from extended logging (VC-3096)

:white_check_mark: Server: Audit log->Removed some unnecessary diff objects (VC-2968)

:white_check_mark: Server: Database->Fixed audit log stats query (VC-3133)

:white_check_mark: Client/Server: Web macro->Fixed problem using Variables in main url (VC-3135)

:white_check_mark: Server: User Variables->API fix (VC-3137)

:white_check_mark: Client/Server: Sync files->Azure DataLake Gen2 SyncFiles fix (VCP-25)

:white_check_mark: Server: Notifications->Update Task Stats fix for Notification Tasks (VCP-29)

:white_check_mark: Server: Email Trigger->EWS Exchange oAuth trigger deactivating after first successful trigger (VC-3142)

:white_check_mark: Server: Email Trigger->Issue with path creation when saving Email in Email trigger (VCP-31)

:white_check_mark: Server: WebDAV Tasks->Move WebDAV storage calls from tasks to WebDAV API (VCP-28)

:white_check_mark: Server: Trial->Fixed offline trial registration issue (VCP-60)


### 9.9.10 [2022-09-21]

#### Features

:star: Client/Server: User Variables->Added object relation search (VC-3061)

:star: Client: Object search->Improved search speed for Credentials, Connections etc in Tasks/Triggers (VC-3080)


#### Bug Fixes


:white_check_mark: Server: Email Trigger->Component License issue (VC-3093)

:white_check_mark: Server: SSIS 2017->dll binding error (VC-3086)

:white_check_mark: Server: Slack->HTTPS fix for Slack redirect URI (VC-2904)

:white_check_mark: Server: Database->Optimized clear table methods (VC-3102)

:white_check_mark: Client/Server: OneDrive->TLS fix for OneDrive connection authentication (VC-3101)

:white_check_mark: Server: Database->MySQL .NET adapter update (VC-3104)

:white_check_mark: Server: Email Task->Exchange EWS connection sending mail fix (VC-3108)

:white_check_mark: Server: Database->Fixed issue with logging aborted when using Internal database (VC-3112)

:white_check_mark: Client/Server: Web macr->Fixed issue saving PDF with images and styles (VC-3110)

:white_check_mark: Server: Email Trigger->Fixed issue with saving attachments with long names (VC-3111)

:white_check_mark: Server: Execute script Task->Fixed script delete issue (VC-3113)

:white_check_mark: Server: Remote file Trigger->SessionId and Trigger object not set correctly (VC-3115)


### 9.9.9 [2022-09-05]

#### Features

:star: Client/Server: Health->Added new Server Health control (VC-2871)

:star: Client/Server: Object relations->Added SSH keys (VC-2887)

:star: Client/Server: Robot Task->Integrated web macro into Robot Task (VC-2683)

:star: Client/Server: Robot Task->Added stand-alone web browser (VC-2887)

:star: Client/Server: Robot Task->Add Workbook->Run macro actions (VC-2772)

:star: Client/Server: Robot Task->Added Workbook->Get info action (VC-2773)

:star: Client/Server: Robot Task->Added action Take screenshot (VC-2679)

:star: Client/Server: Robot Task->Added List Variables actions (VC-2718)

:star: Client/Server: Robot Task->Added File/Folders actions (VC-2682)

:star: Client/Server: Robot Task->Added playback speed control (VC-2717)

:star: Client/Server: Web macro Task->Added loop functionality (VC-2837)

:star: Client/Server: Web macro Task->Added maximize on record/test settings (VC-2963)

:star: Client/Server: Logs->New Health table (VC-2844)

:star: Client/Server: Logs->New Event log table (VC-2843)

:star: Client/Server: SSRS->Added connection variables support (VC-2895)

:star: Client/Server: Execute Task->Added Batch option (VC-2862)

:star: Client/Server: New Task: Excel - Delete cell(s) (VC-2921)

:star: Client/Server: New Task: Excel - Delete row(s) (VC-2921)

:star: Client: Main window->Added Job Id filter (VC-2799)

:star: Client/Server: Image convert Task->Added more image conversion options (VC-2946)

:star: Client/Server: Variables: Added variable type List for User Variables (VC-3057)

:star: Client/Server: Object search: Added support for case insensitive search (VC-2965)


#### Bug Fixes


:white_check_mark: Server: Assembly Execute Task->Fix x86 issue (VSPS-422)

:white_check_mark: Server: Archive - Extract->Fixed release of the file at the end of processing (VC-2851)

:white_check_mark: Client/Server: Popup Task->Fixed layout issue (VC-2882)

:white_check_mark: Server: HTTP Trigger->Not showing output Variables issue (VC-2761)

:white_check_mark: Client: SFTP\SSH Connection->Encryption encryption algorithms display names for connection properties (VC-2902)

:white_check_mark: Client: Web macro->Fixed new tab + enter url issue (VC-2840)

:white_check_mark: Client: Connection Explorer->Proxy setter fix (VC-2905)

:white_check_mark: Client: Themes->More theme fixes (VC-2660)

:white_check_mark: Client: Run/Pause Job->Fixed button update issue and stop problem (VC-2783)

:white_check_mark: Client/Server: Job result->Fixed chart and loading (VC-2781)

:white_check_mark: Server: Web API->Fixed null ref issue (VC-2897)

:white_check_mark: Client: Flow chart->Fixed crash (VC-2890)

:white_check_mark: Client: SQL Task->Sql Parameter editor fix (VC-2911)

:white_check_mark: Client/Server: SSRS Task->Fix for maximum rows issue in Excel (VC-2856)

:white_check_mark: Server: SharePoint Connection with Certificate not valid in task but works in Connection Explorer (VSPS-417)

:white_check_mark: Server: Webdav issue - outputs double URL (VC-2935)

:white_check_mark: Client/Server: Use Dropbox RefreshToken instead of short-term AccessToken (VC-2925)

:white_check_mark: Client: Robot Task->Fixed error message when adding new action (VC-2953)

:white_check_mark: Client/Server: Desktop macro->Issue with Stop/Save button at recording (VC-2932)

:white_check_mark: Client/Server: Web macro->Problems recording step on specific website (VC-2934)

:white_check_mark: Client/Server: Web macro->Fixed issue "Destroy must be called.." (VC-2934)

:white_check_mark: Client/Server: Web macro->Problem with downloading specific file (VC-2949)

:white_check_mark: Client/Server: Web macro->Fixed Gif recording stops to early (VC-2966)

:white_check_mark: Client/Server: Web macro->Fixed internal loop issue (VC-3062)

:white_check_mark: Client/Server: Main window->Various Run Job feedback (VC-2783)

:white_check_mark: Server: Archive - Compress->Not able to append to empty zip file fix (VC-2926)

:white_check_mark: Server: Archive - Extract->Problems with deleting archive (VC-2832)

:white_check_mark: Client/Server: SSRS->Parameter set issue (VC-2748)

:white_check_mark: Client/Server: Scan document (local)->Issue capturing scan Variables (VC-2966)

:white_check_mark: Client/Server: Web service Task->Fixed issue when selected Credential was used even though "None" was used in security settings (VC-2812)

:white_check_mark: Client/Server: Web service Task->Fixed issue stopping Task (VC-2813)

:white_check_mark: Client: Manage Servers->Fixed potential null reference error (VC-2962)

:white_check_mark: WebClient: Popup Task->Fixed radio button selection (VC-2991)

:white_check_mark: Server: Email Task->Handled time zone issue on message date (VC-3006)

:white_check_mark: Client/Server: BOX SSL/TLS issue (VC-3047)

:white_check_mark: Client/Server: Scan document->Issue seeing scanned values in output fixed (VC-2964)


### 9.9.8 [2022-05-18]

#### Features

:star: Client/Server: Authentication->Increased security for AD auth (VC-2587,VC-2539)

:star: Client/Server: Robot Task (RPA)->Fixed various issues (VC-2770)

:star: WebClient: Various web client feedback (VC-2763)

:star: Client/Server: Robot Task (RPA)->Futher Excel extensions (VC-2698)


#### Bug Fixes


:white_check_mark: Client: Themes->Fixed various theme issues (VC-2660)

:white_check_mark: Client: Popup Task->Fixed radio button presentation (VC-1312)

:white_check_mark: Client/Server: Excel->Get row count->Added Excel password property (VC-2808)

:white_check_mark: Client: Email Trigger->Added available Connection types for forwarding (SMTP) (VSPS-421)

:white_check_mark: Server: Loops->Fixed null reference issue with Next action in Conditions when used in loop (VC-2825)

:white_check_mark: Server: SNS Trigger->Updated connection settings (VC-2828)

:white_check_mark: Server: Image Tasks->Fixed issue with missing files (VC-2830)

:white_check_mark: Server: File Trigger->Fixed issue with activating polling (VC-2833)

:white_check_mark: Server: Impersonation using MSA account improved (VC-2692)

:white_check_mark: Server: HTTP request SSL\TLS channel failure (VC-2842)

:white_check_mark: WebClient: AD->Fixed username not populating (VC-2819)

:white_check_mark: Client/Server: Scan document(local)->Fixed license issue preventing scanning (VC-2806)

:white_check_mark: Server: VCTray->Fixed Windows auth issue (VC-2850)

:white_check_mark: Server: Credentials->Fixed impersonation issue with MSA (VC-2845)

:white_check_mark: Server: PowerShell/SSIS->Fixed issue running in x86 mode (VC-2866)

:white_check_mark: Server: Extract zip with password file handle remains open (VC-2869)

:white_check_mark: Client/Server: Popup Task->Fixed result conversion issues (VC-2820)

:white_check_mark: Client/Server: SSH Keys->Rolled back component for SSH key connection issue (VC-2886)

:white_check_mark: Client: Conditions->NullReferenceException when trying to add condition (VC-2889)

:white_check_mark: Server: Amazon S3->Added delete source option on download (VC-2891)


### 9.9.7 [2022-04-12]

#### Notes

:memo: All: New protocol version (9.9.7) for communication. Requires Server and Client version to be the same (VC-2725)


#### Features

:star: Client/Server: Translation->Added translation to many languages (VC-2050)

:star: Client/Server: Amazon AWS Create and Delete AMIs (VC-887)

:star: Client/Server: Performance->Faster connection for large Jobs (VC-2494)

:star: Client/Server: Web macro Task->Better dynamic download by search (VC-1578,VC-2606)

:star: Client/Server: Email Trigger->Better logging (VC-728)

:star: Client/Server: HTTP Task->Added Set-Cookie feature (VC-2551)

:star: Server: Web API->Added "processes" API support (VC-2593)

:star: Client/Server: Robot Task (RPA)->Added "Run from" functionality (VC-2728)

:star: Client/Server: Robot Task (RPA)->Added disable/enable step (VC-2706)

:star: Client/Server: Robot Task (RPA)->Added pause functionality when Task is running (VC-2685)

:star: Client/Server: Robot Task (RPA)->Added Wait action (VC-2678)

:star: Client/Server: Robot Task (RPA)->Added End loop action (VC-2677)

:star: Client/Server: Robot Task (RPA)->Added Create and Go to label action (VC-2676)

:star: Client/Server: Robot Task (RPA)->Added While and Do while conditions (VC-2664)

:star: Client/Server: Robot Task (RPA)->Added For and For each loop (VC-2663)

:star: Client/Server: Robot Task (RPA)->Added Clipboard actions (VC-2649)

:star: Client/Server: Robot Task (RPA)->Added Set text actions + keyboard (VC-2652)

:star: Client/Server: Robot Task (RPA)->Added element select context aware actions (VC-2690)

:star: Client/Server: Robot Task (RPA)->Added better Variable support (VC-2673)

:star: Client/Server: Robot Task (RPA)->Added notes to each action (VC-2650)

:star: Client/Server: Sharepoint Create Folder task, List Files and Delete Files support folders (VSPS-202)

:star: Client/Server: Web macro Task (RPA)->Improved table extraction (VC-2759)

:star: Client: Messageboxes->Add custom messagebox for faster UI (VC-2737)


#### Bug Fixes


:white_check_mark: Client: FTP Connection SSL\TLS checkboxes save their state when saving connection (VSPS-411)

:white_check_mark: Client: SSH Public\Private Key import routine fixed for remote servers (VSPS-412)

:white_check_mark: Server: Logging to MS SQL Server (native) database with trusted connection error fixed (VC-2459)

:white_check_mark: Client/Server: Execute task might hang in deadlock when both outputs are being collected (VC-2542)

:white_check_mark: Server: CPU utilization increases even when task is stopped (VC-2507)

:white_check_mark: Client/Server: Major updates of most client libraries and dependencies (VC-2568)

:white_check_mark: Server: SQL Task->Fix for error null ref error (VC-2492)

:white_check_mark: Client/Server: Web macro Task->Fixed Certificate auth issue (VC-1395)

:white_check_mark: Client: Conditions->Fixed crash in VisualCron Condition when Task not set (VC-2586)

:white_check_mark: Client/Server: Jobs->Fixed a cloning issue (VSPS-372)

:white_check_mark: Client/Server: Date filter->Fixed support for specific format (VSPS-352)

:white_check_mark: Client/Server: Powershell->Fixed issue not returning error (VSPS-336)

:white_check_mark: Client/Server: Connection Explorer->Fixed issue where Task worked but not Connection Explorer (VSPS-283)

:white_check_mark: Client/Server: Sharepoint Tasks->Added Variable support in List items Task (VSPS-277)

:white_check_mark: Client/Server: OneDrive->Fixed crashes when selecting folder/file (VSPS-299)

:white_check_mark: Client/Server: Archive - extract->Fixed filter when using 7z (VC-2545)

:white_check_mark: Client: SQL Task->Added warning for Oracle when missing SID and service name (VC-1266)

:white_check_mark: Server: Azure Storage Fileshares upload files in batches to avoid OutOfMemory exception (VSPS-414)

:white_check_mark: Server: Internal database->Handled errors when logging better (VC-2693)

:white_check_mark: Client/Server: Main grid->Fixed execution time issue when using Job Variables (VC-2709)

:white_check_mark: Server: Excel Convert Task->Not converting the last row issue (VC-2716)

:white_check_mark: Client: Further UI theme fixes (VC-2660)

:white_check_mark: Client/Server: Web macro->Fixed hanging processes and cleanup of cookies (VC-2671)

:white_check_mark: Client/Server: Excel - Create->Fixed missing dll "Microsoft.IO.RecyclableMemoryStream" issue (VC-2734)

:white_check_mark: Client: UseProxyForDataChannel not visible when editing proxy settings (VSPS-415)

:white_check_mark: Server: NullReferenceException in VisualCronAPI.Credentials for AD logon (VSPS-419)

:white_check_mark: Server: Robot Trigger->Fixed triggering issue (VC-2735)

:white_check_mark: Client/Server: Popup Task->Fixed various UI issues (VC-1312)

:white_check_mark: Client/Server: Popup Task->Fixed issues sending to tray/specific recipient (VC-1628,VC-1924)

:white_check_mark: Client: Audit log->Fixed issue with reversed result for activate/deactivate Trigger (VC-1863)

:white_check_mark: Web Client: Menus->Fixed a UI themes issue (VC-2749)

:white_check_mark: Web Client: Error handling->Added unhandled errors to messagebox (VC-2747)

:white_check_mark: Web Client: Execution progress->Fixed UI issues (VC-2714)

:white_check_mark: Web Client: Jobs table->Fixed column resizing issues (VC-2670)

:white_check_mark: Web Client: Logon->Fixed logon UI issues (VC-2668)

:white_check_mark: Web Client: Triggers->Added auto description settings and various UI issues in Trigger (VC-2644)

:white_check_mark: Web Client: Tasks->Fixed issues saving Tasks (VC-2643)

:white_check_mark: Web Client: General->Fixed various UI issues (VC-2672)

:white_check_mark: Server: PDF Split -> check destination directory exists (VSPS-420)

:white_check_mark: Server: Log->Fixed various error handling issues with db logging (VC-2792)


### 9.9.6 [2022-01-17]

#### Features

:star: Client/Server: Web API->Added support for all Job Variable methods (VC-2430)

:star: Client: Main grid->Added CTRL+A functionality (VC-1917)

:star: Client/Server: Translation->Added translation to many languages (VC-2050)


#### Bug Fixes


:white_check_mark: Client/Server: SharePointPnP.IdentityModel.Extensions missing (VSPS-391)

:white_check_mark: Client/Server: FTP connection threads count don't update when editing (VSPS-394)

:white_check_mark: Client/Server: Azure Management Connections using Azure AD application (VSPS-365)

:white_check_mark: Client/Server: Web macro->Fixed issue when stuck on entry url (VC-2464)

:white_check_mark: Client: Job reports Task->Fixed all columns included issue (VC-2474)

:white_check_mark: Client/Server: User Variables->Fixed problem using User Variables in Credentials (VC-2367)

:white_check_mark: Client: Translation->Fixed InvalidCastException when language of Windows is not English (VC-2475)

:white_check_mark: Server: Jobs->Improvements to load/saving to prevent issues (VC-2489)

:white_check_mark: Client/Server: AWS S3 Certificate authentication support for Tasks \ Connection Explorer (VSPS-402)

:white_check_mark: Client/Server: Output->Fixed output issue (null reference) (VC-2484)

:white_check_mark: Client/Server: Robot Task->Fixed issue showing Package manager (null reference) (VC-2501)

:white_check_mark: Client: Cloud List folder(s) Task: error editing task (VSPS-405)

:white_check_mark: Client: FTP client connection routine fix (VSPS-406)

:white_check_mark: Server: Output->Fixed ArgumentOutOfRange and OutOfMemory errors (VC-2505)

:white_check_mark: Client/Server: Web macro->Fixed certificate issue (VC-2434)

:white_check_mark: Client: Login->Fixed remember password issue (VC-2295)

:white_check_mark: Client/Server: PDF header/footer Task->Color fix (VC-2259)

:white_check_mark: Client: Obsolete connection protocol types might cause Connection Explorer to fail (VSPS-408)

:white_check_mark: Client: Fixed bug when displaying\updating Symmetric Encryption Task (VSPS-407)

:white_check_mark: Client/Server: Tasks->On error->Added missing "No files exception" in Tasks (VC-2135)

:white_check_mark: Client/Server: Telegram->Fixed invalid token error (VC-2526)

:white_check_mark: Client/Server: Powershell->Fixed hang issue (VC-2528)

:white_check_mark: Client/Server: Web AOPI->Fixed refresh of Client Job Variables after update (VC-2430)


### 9.9.5 [2021-12-02]

#### Features

:star: Client/Server: HTTP REST Trigger->Added JSON support (VC-2360)

:star: Client/Server: Sharepoint->Added more auth options (VSPS-320)

:star: Client/Server: Object search/Replace->Added option to search and replace specific value (VC-2139)

:star: Client/Server: SimpleDB->Added Tasks for SimpleDB (VC-635)

:star: Client/Server: PDF header footer->Added PAGE and NUMPAGE support (VC-938)

:star: Client/Server: .NET Code Task->Moved "Refresh" methods to Server (VC-2346)

:star: Client/Server: New Tasks->JSON Encode and Decode (VC-1594)


#### Bug Fixes


:white_check_mark: Client/Server: Web macro->Fixed cert loading issue (VC-2435,VS-1395)

:white_check_mark: Client/Server: Box->Fixed Box Connection/auth crash issue(VSPS-375)

:white_check_mark: Client/Server: Cloning->Fixed Clone Job/Task issue (VSPS-381)

:white_check_mark: Client/Server: Pause/Resume->Fixed event log issue (VC-2437)

:white_check_mark: Client/Server: Fixed Setup app / Create app link for ExchangeEWS, Google Drive, OneDrive (VSPS-383)

:white_check_mark: Client/Server: Fixed JobFlow UI radio buttons (VSPS-367)

:white_check_mark: Client/Server: Fixed Connections with VisualCron Protocol Type: username might be empty (VSPS-385)

:white_check_mark: Client/Server: Fixed Connections with Office365 Protocol Type: added missing Application info (VSPS-386)

:white_check_mark: Client/Server: Set folder permissions->Various fixes (VC-1732)

:white_check_mark: Client/Server: Object search->Fixed XML error in searching (VC-2440)

:white_check_mark: Client/Server: PDF Search Task->Fixed issue not saving settings (VC-2345)

:white_check_mark: Client/Server: Certificates->Fixes import issue "invalid certificate data" (VC-2443)

:white_check_mark: Client/Server: Audit log->Fixed searh default "from date" (VC-2439)

:white_check_mark: Client/Server: Connection Editor->Empty username allowed for PublicKey authentication (SFTP/SCP/SSH) (VSPS-389)

:white_check_mark: Client/Server: Web macro and more->Various minor UI fixes (VC-2454)

:white_check_mark: Client/Server: SFTP/SSH Connection->Fixed 0 timeout to be Max wait (VSPS-369)

:white_check_mark: WebClient: Connection->Fixed issue requiring administration permissions (VC-2435)


### 9.9.0 [2021-10-22]

#### Features

:star: Client/Server: Web macro Trigger->New Trigger->Web macro (VC-2281)

:star: Client: Connections->Added Connection filters in Object relations/finder and audit log (VC-2352)

:star: Client/Server: Sharepoint Tasks->Added support for date Variables (VSPS-338)

:star: Client/Server: HTTP Rest Trigger->Added support for application/x-www-form-urlencoded requests (VC-2331)

:star: Server: Variables->Added support for settings Variables through Web API (VC-1489)

:star: Client/Server: Web service Trigger->New Trigger added (VC-2376)

:star: Client/Server: Jobs/Tasks->Added pause/resume (VC-1726)

:star: Client/Server: JSON filter Task-> Added PreFormatting option for JSON Filter (VC-2371)

:star: Client/Server: Web API->Added AD support for authentication (VC-2373)

:star: Server: Job/Task history->Added export button (VC-2393)

:star: Client/Server: Added OAuth auth to the HTTP task (VC-1909)

:star: Client: Connections->Connections configuration windows split up for speed (VSPS-315)

:star: Client/Server: Audit log->Added export options (VC-2405)

:star: Client/Server: PGP->Added Import/Create right click alternatives (VC-2045)


#### Bug Fixes


:white_check_mark: Server: Crystal reports->Fixed issue with refreshing data (VSPS-334)

:white_check_mark: Client/Server: SSIS Task->Fixed 2019 dll version mismatch (VSPS-335)

:white_check_mark: Server: Connections->Fixed Oracle connection string to solve error "ProviderMustBeSpecifiedException" (VSPS-337)

:white_check_mark: Server: Cloud Tasks->Fixed issues with converting datetime from UTC (VSPS-339)

:white_check_mark: Client/Server: Web macro->Fixed issue setting delay (VC-2361)

:white_check_mark: Server: Email Trigger->Removed SMTP Connection support, addded IMAP4 Connection support (VSPS-342)

:white_check_mark: Server: Sync->Fixed possible dead lock at startup (VC-2369)

:white_check_mark: Client/Server: Slack->Fixed issue not being able to see private channels (VC-2366)

:white_check_mark: Server: Job Report Task->Fixed exception "KeyNotFoundException" (VSPS-343)

:white_check_mark: Client: Print document->Fixed crash when printing document (VC-2386)

:white_check_mark: Server: SAP->Fixed exception on invalid Connection (VSPS-350)

:white_check_mark: Server: Send Email Task->Replaced password in debug with asterix (VC-2390)

:white_check_mark: Client/Server: Job reports->Fixed output issues (VC-2389)

:white_check_mark: Server: SQL Task->Fixed empty row issue (VC-1986)

:white_check_mark: Client: Main form->Fixed set columns issue (VC-2364)

:white_check_mark: Server: Web macro->Fixed table extraction issues (VC-2394)

:white_check_mark: Client/Server: File Trigger->Fixed issue with file Trigger and semicolon separated file names (VC-2108)

:white_check_mark: Client: Connections->Fixed issue saving publishsettings path setting (VSPS-353)

:white_check_mark: Client: SQL Task->Fixed parameter type display for Oracle stored procedures (VSPS-354)

:white_check_mark: Server: Crystal reports->Mask password in log issue (VSPS-355)

:white_check_mark: Server: SSRS->Fixed timeout handling in web service call (VSPS-357)

:white_check_mark: Client/Server: Job reports->Output issues (VC-2389)

:white_check_mark: Client/Server: Excel Tasks->Various column issues (VC-2400)

:white_check_mark: Client/Server: Web macro Task->Fixed multiple Variable issue (VC-2403)

:white_check_mark: Client/Server: Foreground Tasks->Fixed problem stopping and tracking - no PID (VSPS-361)

:white_check_mark: Client/Server: Connections->Fixed "Use VisualCron app" default value issue (VSPS-362)

:white_check_mark: Client/Server: Azure VM Tasks->Fixed UI crash (VSPS-363)

:white_check_mark: Client/Server: Web service Task->Fixed issue not being to able to set SecurityMode to Transport (VSPS-364)

:white_check_mark: Web client: Popup Task->Fixed issue (VC-2392)


### 9.8.5 [2021-08-05]

#### Features

:star: Client/Server: Azure Block blobs->Added support for deleting folders/all files (VSPS-307)

:star: Client/Server: MSMQ->Added serialization options (VSPS-310)

:star: Client/Server: Email - Send->Added Credentials for mail recipient tab (VC-1479)

:star: Client: Connections/Credentials->Added filters where not used (VC-2268)

:star: Client/Server: Twitter Task->Updated to latest twitter dlls (VC-1399)

:star: Client/Server: Print Task->Added tray support (VC-1371)

:star: Client: Improved multi Connection/Credentials selection (VC-2279)

:star: Client/VCTray: Robot Task->Added CTRL+ALT+S sequence alternative for stopping (VC-2326)

:star: Client/Server: Email Task/Trigger->Added certificate support for Exchange (VSPS-304)

:star: Client/Server: New Trigger->Desktop Trigger (VC-1234)

:star: Client/Server: SQL Task/Trigger: Added native PostgreSQL Connection alternative (VC-2327)

:star: Client/Server: MFT->Added more native logging (VSPS-293)

:star: Client/Server: XML output->Fixed indent support (VC-2308)

:star: Client/Server: SQL Task->Added native PostgreSQL support (VC-2327)

:star: Client/Server: Excel->Added more Excel Tasks (VC-1593)

:star: Server: Copy files Task->Can now, optionally, create empty sub folders (VC-1731)

:star: Client/Server: Web macro Task->Improved the column extractor (VC-2235)

:star: Client/Server: DTS Task->Added password field support for file package (VSPS-324)


#### Bug Fixes


:white_check_mark: Server: Sync files Task->Fixed sync issue of modified file (VC-2254)

:white_check_mark: Client/Server: SQL Trigger->Added result parameters (VC-2296)

:white_check_mark: Client/Server: Web macro Task->Fixed issue reading specific sub menu/frame (VC-2299)

:white_check_mark: Client/Server: HTTP REST Trigger->Fixed POST key/values in Result (VC-2300)

:white_check_mark: Server: Server Sync->Fixed issue syncing new Notifications (VC-2307)

:white_check_mark: Client/Server: XML Tasks->Fixed issue with crash when using specific value (VSPS-306)

:white_check_mark: Client/Server: Web macro->Fixed issue with using Job Variables (VC-2313)

:white_check_mark: Client: SQL Trigger->Fixed issue saving retry option (VC-1946)

:white_check_mark: Client/Server: Fixed issue problem storing schema with stored procedures (VC-2315)

:white_check_mark: Client/Server: Azure file shares->Listing optimizations (VSPS-311)

:white_check_mark: Client: Time Trigger->FIxed display issue on workdays (VC-2328)

:white_check_mark: Client: SSH keys->Fixed client crash issue (VC-2321)

:white_check_mark: Server: Azure file shares->Listing optimizations (VSPS-313)

:white_check_mark: Server: Event log Task->Fixed issue writing to remote event log (VC-2293)

:white_check_mark: Client: VMWare->Added warning when saving with non-existent method in vSphere (VC-1813)

:white_check_mark: Client/Server: SQL Task->Added support for reserverd word (VSPS-314)

:white_check_mark: Server: Installation->Added fix for 'untrusted path' issue (VC-2311)

:white_check_mark: Server: Dynamics CRM->Fixed issue using Variables in parameters (VC-2290)

:white_check_mark: Server: Crystal reports->Fixed issue with executing parameters when using ODBC connection string (VSPS-323)

:white_check_mark: Client/Server: OneDrive->Handled error "Invalid server response" (VSPS-325)

:white_check_mark: Client/Server: OneDrive/GoogleDrive/Box->Handled 1 hour timeout issue (VSPS-321,VSPS-175)

:white_check_mark: Client/Server: Server settings->Fixed support for using Variables in Server settings (VSPS-331)

:white_check_mark: Server: Email Trigger->Fixed issue with subjet not being preserved when using forwarding (VSPS-329)

:white_check_mark: Server: Log->Now hidding external DB password at startup (was logged when using Extended debugging) (VSPS-328)

:white_check_mark: Server: SQL Task->Fixed issue with conversion of input parameters when using Oracle and stored procedures/packages (VSPS-322)

:white_check_mark: Client: UI->Fixed issue with Consolas font (VC-2320)

:white_check_mark: Client: Job reports Task->Fixed issue with up/down button not saving (VC-2332)

:white_check_mark: Client/Server: Web macro->Fixed issue with column extractor (VC-2325)	

:white_check_mark: Client: SSH Task->Fixed UI issue (VC-2353)

:white_check_mark: Client/Server: Web macro->Fixed potential download crash issue (VC-2354)

:white_check_mark: Client/Server: SQL Trigger->Fixed null reference issue when Result is not set (in Variables window) (VC-2359)

:white_check_mark: Server: Excel - Copy worksheet->Fixed problem creating new worksheet (VC-2355)

:white_check_mark: Server: Excel (general)->Added Variable support (VC-2355)

:white_check_mark: Server: Excel - Search/List worksheets->Fixed issue saving Task values (VC-2359)


### 9.8.0 [2021-05-21]

#### Features

:star: Client/Server: Azure->Added SAS token support (VSPS-282)

:star: Client/Server: Excel Convert->Added Start/End row support (VC-1528)

:star: Client/Server: Excel Convert->Added Password support (VC-1575)

:star: Client/Server: Triggers->Added new "Folder Trigger" (VC-655)

:star: Server: Error handling->Now logging if communication port is being used (VC-2197)

:star: Server: HTTP REST Trigger->Added support for waiting with response for Job/Task to fininish first (VC-2255)

:star: Client: Font->Now users can select Font to use in Client->File->Client settings (VC-2125)

:star: Client/Server: Variables->Added various new Math Variables (VC-1869)

:star: Client/Server: Powershell->Added stack trace on error to output (VC-2271)

:star: Client: Log->Added Execution time column on Task row (VC-2277)


#### Bug Fixes


:white_check_mark: Server: SQL Task->Fixed better validation of input/output direction values (VC-2234)

:white_check_mark: Server: Cloud Sync->Fixed cast error from TElGoogleDocument to TElGoogleDriveFolder error (VSPS-290)

:white_check_mark: Client: SQL Trigger->Fixed duplicate stored procedure error (VC-2237)

:white_check_mark: Client/Server: Memory leak->Fixed memory leak on failing Client connections (VC-2215)

:white_check_mark: Client: Output window->Fixed InvalidOperationException (VC-2233)

:white_check_mark: Client: Output window->Fixed some positioning of text (VC-2225)

:white_check_mark: Client: Job report->Fixed issues with checkboxes in settings (VC-2227)

:white_check_mark: Server: Azure Gen 2->Added different listing routine for blobs (VSPS-292)

:white_check_mark: Client: SQL Trigger->Optimized loading of stored procedures (VC-2241)

:white_check_mark: Client: Azure->Adding missing dll to installing (Microsoft.Bcl.AsyncInterfaces.dll) (VC-2250)

:white_check_mark: Client: Performance->Various performance optimization work in Client (VC-2221)

:white_check_mark: Client/Server: Google Drive->Fixed auth issues (VSPS-294)

:white_check_mark: Client/Server: Web macro Task->Fixed issue with lingering sub process (VC-2257)

:white_check_mark: Client: HTML output->Fixed adding html tags if missing (VC-2127)

:white_check_mark: Client: Google auth->Fixed browser issue (VC-2244)

:white_check_mark: Client/Server: Exchange EWS->Fixed auth issue (VSPS-297,VC-1206)

:white_check_mark: Client: Web macro/browser->Fixed problem opening/hanging under limited user account (VC-2209,VC-2207)

:white_check_mark: Client/Server: .NET code Task->Fixed issue with temp file error while opening Task (VC-2260)

:white_check_mark: Client/Server: Amazon S3->Region changes and exception logging added (VSPS-279)

:white_check_mark: Client/Server: HTTP REST Trigger->Added regex alternative for url (VC-2255)

:white_check_mark: Client/Server: SQL Task/Trigger->Fixed bit data type validation issue for stored procedures (VSPS-302)

:white_check_mark: Client/Server: SQL Task->Fixed issue calling stored procedures in Oracle->ODBC (VC-2238)

:white_check_mark: Client: Fonts->Fixed issue with missing Roboto font and possibility to select own font (VC-2125)

:white_check_mark: WebClient: Next run->Fixed time zone issue (VC-2283)

:white_check_mark: Server: Crystal reports->Fixed ODBC crash when many Tasks ran at the same time (VC-2282)

:white_check_mark: Client: SQL Task->Handled possible duplicate stored procedure names (VC-2237)

:white_check_mark: Client/Server: SQL Task/Trigger->Auto update of "DBA Privilege=SYSDBA" parameter to "Connect Mode=SYSDBA" (VC-2202)

:white_check_mark: Client/Server: Web macro Task->Fixed a Variables issue in Download action (VC-2289)

:white_check_mark: Server: Excel Convert->Fixed incorrect settings change on upgrade (VC-2291)


### 9.7.5 [2021-04-15]

#### Features

:star: Client/Server: Added multi domain/forest support for logon (VC-575)

:star: Client/Server: New Trigger->Added HTTP Trigger (VC-975)

:star: Client: Google Big Query->Fixed UI issues (VSPS-241)

:star: Client: Result->Created a better GIF player (VC-1954)

:star: Client/Server: Variables->Added Task.Description (VC-2140)

:star: Server: Output->Added realtime output support for more Task types (VC-1652)

:star: Client/Server: Dynamics CRM->Added support for Variables in Dynamics CRM Tasks (VC-2128)

:star: Client: Dark theme UI fixes (VC-2115)

:star: VCCommand: Implemented "port" argument (VC-2142)

:star: Client/Server: New Task->Scan document (cloud) (VC-2122)

:star: Client/Server: Object relations->Added replace from "No x" to something and the other way round (VC-1982)

:star: Server: Output->Added more result for various Tasks (VC-1997)

:star: Client/Server: PGP Keys->Added import/create features (VC-2049)

:star: Client/Server: .NET code Task->Now always compiling on Server side (VC-1958)


#### Bug Fixes


:white_check_mark: Client/Server: SQL Task->Fixed date validation and conversion in stored procedures (VC-2123)

:white_check_mark: Server: Log/Result->Fixed issue serializing DBNull value (VC-2137)

:white_check_mark: Server: Web macro->Fixed wait element before download (VC-2109)

:white_check_mark: Client/Server: SQL Task->Fixed output System.XML.XMLNode[] issue (VC-2121)

:white_check_mark: Client/Server: Variables->Workday output format fix (VC-2144)

:white_check_mark: Server: MSMQ Trigger->Fixed issue with path (VC-2149)

:white_check_mark: Client/Server: Amazon S3->Added further support and changes to Amazon S3 compatible servers (VSPS-278)

:white_check_mark: Server: AMQP->Handled memory/thread leak (VC-2126)

:white_check_mark: Client: Audit log - versions->Changed default query (VC-2002)

:white_check_mark: Client: Email Task->Switched to EO browser instead of IE (VC-1980)

:white_check_mark: Client: Connections->Fixed an issue switching protocol type (VSPS-280)

:white_check_mark: Client/Server: Robot Task->Fixed incorrect menu item issue (VC-2158)

:white_check_mark: Client/Server: Robot Task->Fixed issue finding element after reboot (VC-2158)

:white_check_mark: Server: Settings->Fixed issue recovered broken settings at startup (VC-2171)

:white_check_mark: Server: HTTP/REST Trigger->Fixed issue with result values (VC-2167)

:white_check_mark: Server: HTTP Task->Fixed issue aborting Task (VC-2124)

:white_check_mark: Server: Execute Task->Fixed execution failure with combintation Credential without stdout and stderr (VC-2021)

:white_check_mark: Client: Textboxes->Fixed issue with caret position and rendering text field content(VC-2148)

:white_check_mark: Client: Output->Better switch to window (VC-2043)

:white_check_mark: Server: HTTP Task/Trigger->Added PATCH support (VC-2145)

:white_check_mark: Server: Scan document->Fixed crash issue aborting Task (VC-2178)

:white_check_mark: Server: SFTP->Fixed 0 kb file issue (VSPS-285)

:white_check_mark: Client: Triggers->Fixed 'specified cast' error in Trigger dependency (VC-2189)

:white_check_mark: Client: Log->Fixed non-modal crash in general log window (VC-2191)

:white_check_mark: Client: Manage servers->Fixed upgrade server issue (VC-2165)

:white_check_mark: Client: Main window/result-> Added support for 'days' in Execution time (VC-2192)

:white_check_mark: Server: SFTP/FTP->Fixed performance when working with many files and Variables (VSPS-286)

:white_check_mark: Server: Cloud File Trigger->Fixed retry loop issues (VSPS-284)

:white_check_mark: Server: Email Trigger->Added file length check and fix (VC-2180)

:white_check_mark: Server: Objects->Added limitation in scanning recursive components (VC-2181)

:white_check_mark: Client: Output/Result->Fixed positioning (VC-2196)

:white_check_mark: Client: Import->Added 'Clear settings' fix only to clear all that has something to import (VC-2174)

:white_check_mark: Client: Triggers->Fixed visibility of 'Reset Trigger dependency' (VC-2136)

:white_check_mark: Client: UI->Added main font to themes file (VC-2125)

:white_check_mark: WebClient->Fixed column resizer position (VC-2108)

:white_check_mark: WebClient->Fixed Popup Task issues (VC-2102)

:white_check_mark: Server: VMWare->Fixed fetching server name (VC-1990)

:white_check_mark: Client: Server cards->Fixed style issues (VC-2204)

:white_check_mark: Server: SFTP->Fixed issue download all files when folder does not exist (VSPS-268)


### 9.6.5 [2021-03-11]

#### Features

:star: Client/Server: Certificates->Added import option from local computer (VC-1408)

:star: Client/Server: Service Trigger->Added retry options on failure (VC-1946)

:star: Client/Server: Google Cloud BigQuery->Further improvemnts on Tasks (VSPS-241)

:star: Client/Server: Output/Result->Improved limit information (VC-2005)

:star: Client/Server: Output/Result->Improved visuals (VC-2019)

:star: Client/Server: Output/result->Configured dedicated output types for each Task type (VC-1951)

:star: Client/Server: Web macro Task->Upgraded components Chromium V86 (VC-2094)

:star: Client/Server: Cloud Tasks->Azure Data lake Gen 2 is now supported (VSPS-247)


#### Bug Fixes


:white_check_mark: Client: Fixed execution time formatting according to regional settings(VC-2001)

:white_check_mark: Client: Log window->Fixed issue with reload on click on combo (VC-2016)

:white_check_mark: Client/Server: Web macro->Improved crash handling (VC-1191)

:white_check_mark: Server: PowerShell Task->Fixed issue passing parameters and starting pure script blocks (VC-2029)

:white_check_mark: Client/Server: Proxy->Better proxy handling (VSPS-263)

:white_check_mark: Client: SQL Task->Fixed split query option (VC-2060)

:white_check_mark: Server: Assembly Execute Task->Fixed issue with "tampered" error/crash (VC-2084)

:white_check_mark: Client: SQL Task->SQL jobs controls was off/shifted (VC-2083)

:white_check_mark: Client: Main window->Fixed refresh issue when importing/adding Jobs when using filter (VC-2067)

:white_check_mark: Client: Excel->Set cell: Fixed UI lock (VC-2066)

:white_check_mark: Client: Fixed UI error in AD groups (VC-2039)

:white_check_mark: Client/Server: .Assembly Execute Task->Handled "tampered" error (VC-2078)

:white_check_mark: Server: Web macro Task->Fixed issue stopping web macro (VC-2092,VC2076)

:white_check_mark: Server: Web macro Task->Fixed issue with 'object reference error' (VC-2093)

:white_check_mark: Client: Log->Job listing control - improved speed (VC-2022)

:white_check_mark: Client/Server: Crystal reports->Added missing dlls (VC-2100)

:white_check_mark: Client: Job folders->Fixed rename (update) issue (VC-2114)

:white_check_mark: Client/Server: Slack->Fixed issue with deprecated method (VC-2113)

:white_check_mark: Client: Conditions->Fixed selection/hang errors (VC-2129,VC-2107)

:white_check_mark: Server: Logging->Fixed copy Oracle database error (VC-1963)

:white_check_mark: Client/Server: Amazon->Added support for more AWS zonse (VSPS-270)

:white_check_mark: Client: Sharepoint->Fixed delete issue in folder browser (VSPS-269)

:white_check_mark: Server: VisualCron service->Fixed error message when stopping VC service (hanging MFT thread) (VC-2040)


### 9.6.0 [2021-01-27]

#### Features

:star: Client: New dark themes (VC-1794,VC-1795,VC-1796,VC-1866)

:star: Client/Server: New output/result features (VC-1915)

:star: Client/Server: New ROI features added (VC-1878)

:star: Client/Server: SQL Task->Added native support för IBM DB2 database (VSPS-228)

:star: Client/Server: Excel - Get cells Task->Added new option for column and row retrieval (VC-1826)

:star: Client/Server: AMQP->Added certificate validation option (VSPS-234)

:star: Client/Server: Import->Moved cert validation to Server instead of Client (VSPS-227)

:star: Client/Server: Cloud->Added semicolon split and regex support (VSPS-232)

:star: Client: Tasks->Change Affinity UI settings (VC-1588)

:star: Client/Server: Get AD group members Task->Added extended range support (VC-1859)

:star: Client/Server: SSH keys->Added ECDSA and EDDSA support (VSPS-238)

:star: Client: Text controls->Updated some text controls (Powershell Task, SQL Task etc) (VC-1916)

:star: Web Client: Increased grid performance (VC-1847)

:star: Client/Server: Robot Task->Now supporting VC Variables (VC-1858)


#### Bug Fixes


:white_check_mark: Client/Server: DB logging->Handled Credentials better when switching settings (VC-1738)

:white_check_mark: Client/Server: DB logging->Fixed issues copying internal DB to Oracle (VC-1823)

:white_check_mark: Server: Execute Task->Fixed standard output redirect error when using Shell execute option (VC-1846)

:white_check_mark: Server: Sync files Task->Fixed argument exception (VC-1845)

:white_check_mark: Client/Server: Global objects->Send to.. null reference error (VC-1582)

:white_check_mark: Client: SQL Event Trigger->Fixed Credential validation issue (VC-1851)

:white_check_mark: Server: Get AD Group members Task->Fixed issues parsing null entries (VC-1852)

:white_check_mark: Client/Server: Web macro->Fixed exception related to "Property accessor 'FullImageSource'" (VC-1825/VC-1854)

:white_check_mark: Client: Output window->Fixed issue opening some links (VC-1843)

:white_check_mark: Server: Credential->Fixed potential "leak" to main thread when clicking Test (VC-1856)

:white_check_mark: Client/Server: Web API->Added optional certificate (VC-1443)

:white_check_mark: Server: TaskManager->Fixed unhandled error (VC-1872)

:white_check_mark: Client/Server: Web macro->Fixed potential crash from minor errors (VC-1876)

:white_check_mark: Server: File Trigger->Fixed manual "Fire Trigger" issue (VC-1844)

:white_check_mark: Server: Execute Task->Fixed unhandled crash "System.InvalidOperationException: 'No process is associated with this object.'" (VC-1895)

:white_check_mark: Client/Server: SFTP->Fixed handling of empty files mask (VSPS-242)

:white_check_mark: Server: HTTP Trigger->Fixed potential crash with wrong settings (VC-1913)

:white_check_mark: Client: Main grid->Fixed saving some columns (VC-1936)

:white_check_mark: Server: Scan document Task->Fixed append output issue (VC-1943)

:white_check_mark: Server: Scan document Task->Fixed missing AutoMapper dll (VC-1945)

:white_check_mark: Server: Scan document Task->Fixed issue scanning in another language (VC-1957)

:white_check_mark: Server: Cloud Tasks/Triggers->Fixed issue disposing object in the end (VC-1947)

:white_check_mark: Client: Main window->Fixed a problem loading/saving window position (VC-1870)

:white_check_mark: Client/Server: Web macro Task->Fixed issue with editing step (VC-1893)

:white_check_mark: Client/Server: Cloud->Sync files: Fixed issued with All/Folders option (Access to path) (VSPS-255)

:white_check_mark: Client/Server: Azure Connection->Fixed issue with publish settings file configuration (VSPS-253)

:white_check_mark: Client/Server: Dropbox->Fixed "Bad parameters" error (VSPS-250)

:white_check_mark: Client: Connection Explorer->Filter improvement speed (VSPS-254)

:white_check_mark: Client/Server: Connections/Tasks->General TLS 1.3 support added (VSPS-244)

:white_check_mark: Server: HTTP Trigger->Fixed a potential unhandled exception (VC-1913)

:white_check_mark: Server: Startup->Fixed a potential problem determining operating system - that could cause crash (VC-1984)

:white_check_mark: Server: Logging->Fixed issue with external Oracle logging and Copy database -  ORA-01735 (VC-1963)

:white_check_mark: Server: SQL->Output->Fixed issue with locked output file on SQL errors (VC-1953)

:white_check_mark: Server: PowerShell Task->Fixed a problem executing Process section in script block (VC-1950)

:white_check_mark: Server: Global objects->Deleted old (deleted) references at startup (Time exceptions, Conditions) (VC-2004)


### 9.4.5 [2020-11-24]

#### Features

:star: Client/Server: Objects relations/search: Added SSH key global object support (VC-1617)

:star: WebClient: UI->Implemented new themes (VC-1592)

:star: Client: MFT/SSH keys->Added Export.. and Send to options (VC-1660)

:star: Client/Server: Google Cloud storage->Added support in Cloud Tasks/Triggers (VSPS-205)

:star: Client/Server: Object relations->Added name filter for Connections/Credentials (VC-1608)

:star: Client/Server: Update components for Cloud/SFTP/FTP/WebDav (VSPS-225)

:star: Client/Server: Added support for new Client events (Credential failed,SSH key not found) (VC-1781)

:star: Client: Import/Export: Added warnings when nothing selected for import/export (VC-1669)


#### Bug Fixes


:white_check_mark: Client/Server: MFT->Fixed unhandled crash of MFT Server (VC-1469)

:white_check_mark: Client/Server: MFT->Fixed update of Last access and other values (VC-1681)

:white_check_mark: Client: MFT->Handled issue with empty MFT list and enabling MFT (VC-1729)

:white_check_mark: Server: MFT->Fixed issue with wrong server status causing MFT not to start (VC-1773)

:white_check_mark: Server: MFT->Fixed Credential re-impersonate and events at startup (VC-1774)

:white_check_mark: Server: MFT->Fixed changing MFT state button behavior (VC-1757)

:white_check_mark: Client/Server: Export settings Task->Fixed an issue with MFT (VC-1717)

:white_check_mark: Client/Server: Sync->Added reconnect and error handling (VC-1720)

:white_check_mark: Server: FTP/SCP->Fixed overwrite option (if smaller) issue (VSPS-216)

:white_check_mark: Client/Server: Web macro->Fixed upload issue (VC-1723)

:white_check_mark: Server: Settings->Export->Fixed timeout issue in export when working with large files (VC-1728)

:white_check_mark: Server: SQL Task->Fixed error "There is already an open DataReader associated with this Command which must be closed first." (VC-1733)

:white_check_mark: Server: Logging->Fixed Credential load issue when using External db logging (VC-1737)

:white_check_mark: Server: Sync files Task->Fixed issue with folder deletion (VC-1647)

:white_check_mark: Server: Sync files Task->Fixed issue with source path changing to destination path (VC-1739)

:white_check_mark: Server: Users->Now blocking empty username (VC server logon) (VC-1724)

:white_check_mark: Server: Set folder permission Task->Fixed issue with adding without removing rights (VC-1732)

:white_check_mark: Client: Connection Explorer->Fixed issue using Variables in SSH host name (VC-1784)

:white_check_mark: Server: FTP/SFTP/SCP: Fixed support for semicolon in include file mask of remote file filter (VSPS-231)

:white_check_mark: Client: Group permissions->Added some missing permissions (SSH keys, Network drives, Task repository, Client connections and Server sync) (VC-1790)

:white_check_mark: Server: SNMP Tasks->Upgraded to latest library (VC-1699)

:white_check_mark: Server: SQL Task->Removed forced requirement of Load profile in Credential (VC-1809)

:white_check_mark: Server: Archive - Decompress->Fixed issue with Tar+Gzip (VC-1673)

:white_check_mark: Client/Server: Web macro->Fixed wait time saving issue (VC-1788)

:white_check_mark: Client/Server: Web macro->Fixed issue saving location for screenshots (VC-1707)

:white_check_mark: Client/Server: Web macro->Fixed issue launching new instance (VC-1824)

:white_check_mark: Client: Robot Task->Fixed null reference issue on recording (VC-1716)

:white_check_mark: Client: Robot Task->Fixed issues with resolution when DPI changed (VC-1715)

:white_check_mark: Client: VMWare->Added client warnings on vSphere API limitations (VC-1742)

:white_check_mark: Client: Job combo list (general)->Handled null reference (VC-1818)

:white_check_mark: Client: Folder/file selection/Connection Explorer->Optimized retrieving information (VSPS-233)


### 9.4.0 [2020-10-07]

#### Features

:star: Client: Connection Explorer->Added FTP data logging to output according to Connection settings (VSPS-209)

:star: Client/Server: Database->Added copy database options (VC-1577)

:star: Client/Server: SQL Task/Trigger/SSISDB: Added better Credential validation (VSPS-219)

:star: Install: Export settings Task->Added MFT and SSH keys (VC-1694)

:star: Client/Server: VMWare Tasks->Added support for vSphere 7.0 (VC-1625)


#### Bug Fixes


:white_check_mark: Client/Server: MFT->Added some public key validation (VC-1690)

:white_check_mark: Client/Server: MFT->Switched to SSH key selection control with search (VC-1664)

:white_check_mark: Client: Email - Send->Fixed issue using Job Variable in Email - Send Task (VC-1622)

:white_check_mark: Client/Server: Cloud->Added option to ignore certificate errors (VSPS-207)

:white_check_mark: Client: Conditions->Fixed issue selecting a Condition (VC-1620)

:white_check_mark: Client/Server: Informatica->Handled crash refreshing Task settings (VC-1616)

:white_check_mark: Client/Server: Informatica->Username and password was not saved correctly (VC-1637)

:white_check_mark: Server: Informatica->Updated default url and made on-premise url configurable (VC-1633)

:white_check_mark: Server: Email->Get messages->Fixed issue saving email in network share (VC-1591)

:white_check_mark: Server: Variables->Handled problem when null Variable was used (VC-1634)

:white_check_mark: API: Variables->Updated max Variable count in single field to 10.000 (VC-1638)

:white_check_mark: Client: Remote file explorer->Fixed drag and drop issues (VC-1635)

:white_check_mark: Client/Server: Web macro Task->Better handling of unhandled exceptions (VC-1648)

:white_check_mark: Client/Server: Web macro Task->Fixed Task failure if last action was download (VC-1670)

:white_check_mark: Client/Server: Web macro Task->Fixed issue saving type speed (VC-1703)

:white_check_mark: Client/Server: Web macro Task->Fixed click JS detection issue (VC-1711)

:white_check_mark: Server: Event log->Better handling of a crash (VSPS-212)

:white_check_mark: Server: Connections->Fixed issue loading/importing SFTP/SSH Connections with private keys into SSH keys (VSPS-211)

:white_check_mark: Client/Server: Email - Get messages/headers/single message->Fixed issue saving which output columns to use (VC-1653)

:white_check_mark: Client/Server: SSH Connection->Changed default timeout to 0 (infinite) for new Connections as SSH component is aborting the command at the timeout set (VC-1667)

:white_check_mark: Client/Server: MFT->Fixed various crashed related to wrong key settings. Fixed start on import issue. (VC-1658)

:white_check_mark: Client/Server: MFT->Fixed public key logon issue when no key was selected in MFT user (VC-1680)

:white_check_mark: Client/Server: MFT->Fixed flood logging at upload issue (VC-1679)

:white_check_mark: Client: MFT->Fixed SSH console access issue (VC-1663)

:white_check_mark: Client/Server: MFT->Fixed flood logging at upload issue (VC-1679)

:white_check_mark: Server: MFT Trigger->Fixed issues with Login failed/session disconnected events (VC-1666)

:white_check_mark: Client/Server: MFT->Fixed an issue with importing settings (multiple MFT) (VC-1683)

:white_check_mark: Server: Exceptions->Changed general exception handling to better catch unhandled exceptions (VC-1661)

:white_check_mark: Server: SSH Keys->Fixed issue sending SSH Key after import (VSPS-217)

:white_check_mark: Client/Server: SSH Keys->Fixed empty password prompt (VSPS-204)

:white_check_mark: Client: SQL Task->Fixed problem switching from MSSQL Job to Text option (VC-1687)

:white_check_mark: Client: Logging->Reduced logging when Extended debugging is off (VC-1688)

:white_check_mark: Client/Server: SFTP->Fixed an issue with 0 byte file download (VSPS-215)

:white_check_mark: Server: SFTP->Fixed overwrite option (if smaller) issue (VSPS-216)

:white_check_mark: Server: Output->Fixed potential random crash in output reader (Execute/ExecuteHelper) (VC-1689)

:white_check_mark: Client: SNMP Get Bulk->Fixed issue saving SNMP version (VC-1695)

:white_check_mark: Server: Settings->Fixed issue updating Server settings after import (VC-1693)

:white_check_mark: Client: Variables->Fixed issues with Archive Compress Variable (VC-1698)

:white_check_mark: Client: Time exceptions->Fixed Client crash in Job window when lacking permissions to view Time exceptions (VC-1704)

:white_check_mark: Client/Server: Azure->Fixed dll mismatch (Microsoft.IdentityModel.Tokens) (VC-1705)

:white_check_mark: Server: Sync->Fixed an issue with syncing Variables (`<string>` addition) (VC-1700)

:white_check_mark: WebClient: Handled crash in w3wp.exe on disconnect (VC-1710)


### 9.3.5 [2020-08-31]

#### Features

:star: Server: Event log Trigger->Increased performance (VC-1521)

:star: Client/Server: New Task->IBM Cognos Analytics - Run report/job (VC-1028)

:star: Client/Server: Scan document->Now storing sample document in Task instead of file reference (VC-1466)

:star: Client/Server: File/Folder browser->Better transfer and drag and drop features (VC-1356)

:star: Client/Server: Notification history->New search filters (VC-1461)

:star: Client/Server: New Job filter used in various places (VC-1355)

:star: Client/Server: Job history->New search filters (VC-1404)

:star: Client: Task manager->Threads-> Added Started column and better realtime sync (VC-1522)

:star: Client/Server: Robot Task->App property/sync mapping feature (VC-1233)

:star: Client/Server: Added Right click->Export functionlity among Global objects (VC-1456)

:star: Client/Server: SSH keys new global object (VSPS-186,VC-1570,VC-858)

:star: Client/Server: MFT->Separated MFT from settings into own settings file (VC-1342)

:star: Client/Server: MFT->Additional folder permissions (VC-1348)

:star: Client/Server: Email - Get messages->Added selectable data to include as columns (VC-1563)

:star: Client/Server: Email - Get messages/Headers->Added test filter (VC-1494)


#### Bug Fixes


:white_check_mark: Server: SharePoint - Download->Fixes for Delete/Download Task (VSPS-193)

:white_check_mark: Server: Execute/PowerShell->Fixed a memory leak of desktop/winstation handles (VC-1510,VC-1609)

:white_check_mark: Server: Touch file Task->Fixed issue not creating files if file was not found (VC-1526)

:white_check_mark: Server: Performance counter Trigger->Handled error with problems listing categories (VC-1506)

:white_check_mark: Server: Time Trigger->Fixed possible delayed execution (VSPS-194)

:white_check_mark: Server: Certificates->Fixed Add/Update event upon importing/adding Certificates (VC-1527)

:white_check_mark: Client/Server: Drag and drop->Handled objects not existing (VC-1496)

:white_check_mark: Client/Server: Web macro->Fixed issue loading certificate on demand (VC-1503)

:white_check_mark: Client/Server: Web macro->Fixed inject JavaScript issue (VC-1508)

:white_check_mark: Client/Server: HTTP REST Trigger->Handled problem adding second Trigger on same port (VC-1532)

:white_check_mark: Web Client: Fixed issue with running Jobs (VC-1546)

:white_check_mark: Client/Server: Fixed potential Foreground execution "Could not find the specified Connection for Foreground execution" (VC-1486)

:white_check_mark: Client/Server: Office 365->Added Tenant settings to fix "token was empty" (VSPS-195)

:white_check_mark: Client/Server: SCP->Fixed issue preventing using Certificate option (VSPS-197)

:white_check_mark: Client/Server: Sharepoint->Handled error "Failed to retrieve file list: Field or property "TimeLastModified" does not exist" (VSPS-196)

:white_check_mark: Client: Azure->Fixed test button message box confusion (VSPS-200)

:white_check_mark: Client/Server: HTTP proxy->Fixed a general issue with HTTP proxies in Connections (VSPS-199)

:white_check_mark: Client/Server: Variables->Added dragn drop support (VC-1497)

:white_check_mark: Client/Server: Right click->Export option right click menu added to reach Export settings window for a particular object (VC-1456)

:white_check_mark: Client: Right click->Add Job/Task null ref error (VC-1574)

:white_check_mark: Server: Loops->Fixed a loop limitation with foreground execution (VC-1566)

:white_check_mark: Client/Server: JSON JQ Filter Task->Fixed "Access Denied" error (VC-1577)

:white_check_mark: Server: Logging->Fixed external logging to Oracle through OLEDB (VC-1332)

:white_check_mark: Client: Web macro->Fixed EO runtime exception when opening Task (on some machines) (VSPS-206)

:white_check_mark: Client/Server: Web macro->Fixed issue with taking screenshot in some scenarios (VC-1558)

:white_check_mark: Client/Server: Variables->Fixed issues with Archive Compress/Decompress Task Variables (VC-1590)

:white_check_mark: Server: Logging->Fixed issue reading Notification logs from external DB (VC-1615)


### 9.3.0 [2020-06-24]

#### Features

:star: Client/Server: Robot Task->Improved recording performance (VC-1460)

:star: Client/Server: Email - Move message(s) (new Task) (VC-1477)

:star: Client/Server: Connections->FTP Connections types merged into one (VSPS-177)

:star: Client/Server: Folders->Added ability to add all Jobs in a group to a folder (VC-1484)

:star: Client/Server: Run Job->Added option to not raise Trigger events (VC-1483)

:star: Web API: Added filters on all List methods (VC-1297)


#### Bug Fixes


:white_check_mark: Server: Job report->Excel multi line export issue fixed (VC-1333)

:white_check_mark: Server: Task history->Problem reading output (switched to realtime) (VC-1462)

:white_check_mark: Client: Job dragndrop between Servers->Handled deleted Connection issue (VC-1463)

:white_check_mark: Client/Server: FTP->Changed default option to auto-accept server certificates (VSPS-180)

:white_check_mark: Client/Server: Azure Data Lake->Fixed upload path issue (VSPS-174)

:white_check_mark: Client/Server: General auto-accept for server side certificates with related error 75788 (VSPS-181)

:white_check_mark: Client/Server: Variables->Added missing parameters for PowerShell Task type in Task repository (VC-1428)

:white_check_mark: Client/Server: Cloud->Fixed Google Drive and OneDrive refresh issue (VSPS-183)

:white_check_mark: Client/Server: Web macro->Fixed cookie sharing between Jobs issue (VC-1453)

:white_check_mark: Server: Excel - Convert->Fixed problem using Variables in some fields (VC-1481)

:white_check_mark: Client: Main window->Delete Job->Fixed a reference count problem (VC-1485)

:white_check_mark: Server: WebDAV - Download->Improvements for download Task (VSPS-185)

:white_check_mark: Server: SSH Task->Handled socket error when using exit in Send text option (VC-1498)

:white_check_mark: Server: Cloud - Sync->Fixed problems with Variables not resolving (VSPS-187)

:white_check_mark: Client/Server: SSH Task->Fixed missing dlls / upgrade issue (VSPS-188)

:white_check_mark: Client/Server: WebDAV - Upload->Fixed target folder Variable resolving (VSPS-190)

:white_check_mark: Client/Server: SCP - List file(s) - fixed null reference issue (VSPS-191)


### 9.2.5 [2020-06-01]

#### Features

:star: Client/Server: Robot Task->Added custom nuget method support (VC-1248)

:star: Client/Server: Robot Task->Added wait before/after (VC-1422)

:star: Client/Server: Robot Task->Improved hover mouse selection/tracking (VC-1421)

:star: Client/Server: Robot Task->Improved specific Windows element selection (VC-1438)

:star: Client/Server: Robot Task->Improved Windows selection (VC-1449)

:star: Client/Server: Windows Failover Cluster->Added cluster status and information (VC-1361)

:star: Client/Server: HTTP REST Trigger added (VC-568)

:star: Client/Server: HTTP Task->Added response headers as Variables (VC-1416)


#### Bug Fixes


:white_check_mark: Server: SSRS Task->Now allowing Variables in parameter names (VC-1431)

:white_check_mark: Client/Server: SharePoint->Fixed missing dll OfficeDevPnP.Core.dll (VC-1435)

:white_check_mark: Client: Fixed issue with logon prompt hanging on manual password (VC-1436)

:white_check_mark: Server: Image Tasks->Fixed dll reference issue (VC-1400,VC-1444)

:white_check_mark: Server: File filter->Fixed an issue with filter on ? # wild cards (VC-1448,VC-1430)

:white_check_mark: Client: Amazon Tasks->Fixed issue with bucket selection (VSPS-174)

:white_check_mark: Client/Server: PGP - Encrypt->Changed default values for disabling sub keys to fix "No suitable OpenPGP public key for encryption found" error (VC-1447)

:white_check_mark: Server: Fixed a general Task handle leak in TaskFoundation related to AssemblyResolve (VC-1450)

:white_check_mark: Server: Loops->Fixed an issue with "Use column" value not implemented properly (VC-1458)

:white_check_mark: Client/Server: Flow->Fixed support for Job->If other value condition (VC-1446)

:white_check_mark: Client: Log->Fixed issue with showing Task log from loop (VC-1452)


### 9.2.0 [2020-05-20]

#### Notes

:memo: General: Decreased original download and added dll on-demand download. Some Tasks require additional download  Scan document) (VC-1314)

:memo: Client/Server: MFT->Security has been increased on passwords - please re-apply any passwords for MFT users (VC-1187)


#### Features

:star: Client/Server: Sync->Added Master/Slave sync features (VC-879,VC-1088,VC-1089)

:star: Client/Server: Robot Task->Added Excel awareness and cell recognition (VC-1176)

:star: Client/Server: Web macro->More screenshot settings (VC-640)

:star: Client/Server: Web macro->Added cookies sharing between Tasks (VC-596)

:star: Client/Server: Web macro->Various output improvements (VC-923)

:star: Client/Server: Web macro->Added support for local paths (VC-1263)

:star: Client/Server: Cloud Tasks->Added Azure Data Lake support (VSPS-120)

:star: Client/Server: Robot Task->Added alternate Stop method via VCTray client (VC-1255)

:star: Client/Server: SSIS Task->Added support for MSSQL 2019 (VC-1250)

:star: Client/Server: Connections->Added permission override options (VSPS-125)

:star: Client/Server: Triggers->Added the Sharepoint Trigger (VSPS-45)

:star: Client/Server: New task "Scan document" (VC-1156)

:star: Client/Server: Azure->Added Block blob support (configure in Connection) (VSPS-44)

:star: Client/Server: Azure->Added support for Azure File Shares (VSPS-168)

:star: Client/Server: File write Task->Added option to write Base64 content directly to file stream (VC-1317)

:star: Client: Notifications/Conditions->Better multi delete handling (VC-1319)

:star: Client/Server: Offline maintenance validation options extended (VC-1277)

:star: Client/Server: Email Trigger/Tasks now supporting Microsoft OAuth (VC-1206)

:star: Server: Microsoft Teams->Added more relevant output on success (VC-1228)

:star: Server: SharePoint->Added SharePoint delete after download option (VSPS-152)

:star: Server: Cloud - Sync->Added delete source file option (VSPS-145)

:star: Server: Cloud - Sync->Sync from local to cloud option added (VSPS-78)

:star: Server: Print Task->Replaced print pdf component (VC-1347)

:star: Client/Server: Sharepoint->Added claims based support (VSPS-157)


#### Bug Fixes


:white_check_mark: Server: Windows forms obfuscation has been applied on passwords in general (VC-1187)

:white_check_mark: Server: Robot Task->Fixed record panel issues (VC-1137,VC-1275)

:white_check_mark: Client/Server: Excel - Set cell->Added similar date handling as in Excel - Create (VC-1222)

:white_check_mark: Server: Wait Task->Handled issue with crash when using non-valid wait value (VC-1240)

:white_check_mark: Server: SQL Task->Handled null reference issue related to some output scenarios (VC-1241)

:white_check_mark: Client/Server: SSISDB Task->Fixed issue using Variable in Environment parameter (VC-1254)

:white_check_mark: Client/Server: SSISDB Task->Fixed double hyphen in name issue and reporting back SQL Job not found issue (VC-1248)

:white_check_mark: Server: File handling general->Fixed individual skip on permission/IO errors (VC-1252)

:white_check_mark: Client: File filter->Fixed date validation issue in file filter (VC-1253)

:white_check_mark: Server: Excel - Create->Fixed issue with option 'Different folder and use file mask' (VC-1238)

:white_check_mark: Server: Email Trigger->Fixed impersonation issue saving mail and attachments to network share (VC-1258)

:white_check_mark: Client: File filter->Fixed issue with Trigger attachment details in Trigger description (VC-1259)

:white_check_mark: Client: AD authentication->Updated Client and doc with warnings if not secure LDAP port being used (VC-1181)

:white_check_mark: Server: Assembly Execute Task->Fixed issue reloading assembly (VC-1260)

:white_check_mark: Server: Web service Task->Fixed edit parameter issue (VC-1227)

:white_check_mark: Server: Print Task->Fixed landscape printing issue (for fallback method) (VC-1270)

:white_check_mark: Client/Server: Web macro->JS injection step is now performed during recording (not just playback) (VC-650)

:white_check_mark: Client/Server: Exit codes->Fixed an issue syncing the default exit code collection for Windows (VC-1272)

:white_check_mark: Server: File filter->Fixed various issues related to multiple file mask usage (VC-1273)

:white_check_mark: Server: ForEach loop additional fix (VC-1007)

:white_check_mark: Client: Clone Job/Task now requires Read permission to show and Add permission to save (VSPS-125)

:white_check_mark: Client/Server: Permissions->Fixed 'Remove after execution' permission check issue (VC-1284)

:white_check_mark: Client: Job->Added warning about using feature 'Remove Job after execution' (VC-1278)

:white_check_mark: Client: Permissions->Various object specific permission issues fixed (VC-1250)

:white_check_mark: WebAPI: Fixed backwards compatible issue with Login with token and expire time (VC-1282)

:white_check_mark: Client/Server: Sharepoint->Handled File not found issue in Folder browser (VSPS-148)

:white_check_mark: Client: Default flows->Fixed creating default Task flow issue (VC-1288)

:white_check_mark: Client/Server: Cloud - Sync->Fixed 0 kB upload issue (VSPS-146)

:white_check_mark: Client/Server: Cloud - Sync->Fixed lower case upload issue (VSPS-151)

:white_check_mark: Server: SQL Trigger->Fixed null reference issue due to output settings, concerns ODBC, OLEDB, MySQL and Oracle (VC-1295)

:white_check_mark: Client/Server: WebDAV->Fixed upload issue with servers not supporting HEAD request (VSPS-128)

:white_check_mark: Client/Server: Conditions->Fix for problem with duplicate references being created in .NET Code Condition (VC-1322)

:white_check_mark: Client/Server: SharePoint->Fix for "GetFileByServerRelativePath does not exist" error (VSPS-153)

:white_check_mark: Client/Server: Base64 encode/decode Tasks->Fixed impersonation issue and added Credential for destination file (VC-1325)

:white_check_mark: Client/Server: Cloud - Upload->Fixed folder selection crash issue (VSPS-155)

:white_check_mark: Client/Server: FTP/Cloud/File filter->Fixed sorting on path (VSPS-139)

:white_check_mark: Server: Cloud (Google Drive)->Fixed upload issue (VSPS-156)

:white_check_mark: Client: Web macro->Fixed password field view and update (VC-1327)

:white_check_mark: Server: File filter->Date->Added support for more Task Variables (VC-1326)

:white_check_mark: Server: Archive compress->Fixed issue with using network path (folder creation instead of files) (VC-1315)

:white_check_mark: Server: MFT->Fixed Credential problem with root folder (VC-1341)

:white_check_mark: Server: Base64 - Decode Task->Added fault tolerance option (VC-1335)

:white_check_mark: Server: Sharepoint connection issue fixed (VSPS-87)

:white_check_mark: Server: Remote file Trigger->Fixed a problem downloading to relative source path (VSPS-160)

:white_check_mark: Server: Cloud- Sync->Fixed Credential issue and sync issue (VSPS-145)

:white_check_mark: Server: Tasks general->Fixed "SafeHandle cannot be null" issue in Tasks usign ExecuteHelper (VC-1303)

:white_check_mark: Client: Object references->Fixed issue with PGP key ring search (VC-1365)

:white_check_mark: Server: SSISDB Task->Improved error handling (VC-1243)

:white_check_mark: Server: Trigger->Azure Queue Storage->Added missing file (VC-1368)

:white_check_mark: Server: SQL Task->Output append issue fixed (missing last new line) (VC-1369)

:white_check_mark: Server: Telegram - Bot->Fixed time limit for sending messages, added the message text format (VC-1230)

:white_check_mark: Server: SQL Task->File output - fixed saving Credentials (VC-1382)

:white_check_mark: Server: PGP - Encrypt->Fixed issue with duplicate keys signing (VC-1376)

:white_check_mark: Server: Execution context->Remote->Fixed Credential issue and various related errors (VC-1387)

:white_check_mark: Server: Excel - Set cell->Fixed performance issue with many rows (VC-1378)

:white_check_mark: Client/Server: SharePoint->Fixed issue with Update list item Task (VSPS-169)

:white_check_mark: Client/Server: SharePoint->Fixed issue getting root folder instead of sub folder (VSPS-147)

:white_check_mark: Client/Server: SharePoint->Fixed issue adding List item (VSPS-165)

:white_check_mark: Client/Server: Cloud sync->Fixed Credential issue when syncing with local (added Credential selection) (VSPS-170)

:white_check_mark: Client/Server: PDF->Upgraded PDF component to support newer version of PDF (VC-1406)

:white_check_mark: Client/Server: Variables->Fixed issue using Time exceptions in DATENOWADD Variable (VC-1385)

:white_check_mark: Client/Server: Email Task/Trigger->Google Auth implemented (VC-1367)

:white_check_mark: Server: Excel - Get cells->Fixed too long values becoming ######## in output (VC-1407)

:white_check_mark: Client: Conditions->Fixed an issue with Condition selection (VC-1414)

:white_check_mark: Client: PGP key rings->Fixed right click menu issue with Delete key (VC-1413)


### 9.1.5 [2020-02-17]

#### Features

:star: Client/Server: Robot Task->Fixed better grouping of keystrokes (VC-1048)

:star: Server: WebDAV->Fixed Upload output (VSPS-130)

:star: Server: Email Trigger->Added attachment name and path Variables (VC-1193)

:star: Server: Added ability to update global and Job object ids (VC-1174)

:star: Server: SharePoint->List items - added items to output (VSPS-137)


#### Bug Fixes


:white_check_mark: Client/Server: SQL Task/Connection: Fixed license issue with Oracle (VC-1177)

:white_check_mark: Client: Export settings->Fixed null reference issue when lacking Certificate permissions (VC-1180)

:white_check_mark: Client/Server: Web macro->Fixed playback issue (VC-1108)

:white_check_mark: Client/Server: Web macro->Fixed object reference issue on checkbox selection (VC-1195)

:white_check_mark: Client: Web macro->Fixed slow Task opening (VC-1169)

:white_check_mark: Client/Server: Web macro/Robot Task->Fixed realtime output (VC-1168)

:white_check_mark: Server: SQL Trigger->Fixed output null reference issue (VC-1183)

:white_check_mark: Server: Office macro->Changed to password hidden field for password field (VC-1186)

:white_check_mark: Client: Server settings->Fixed license issue when testing proxy settings (VC-1188)

:white_check_mark: Server: Fixed license issue when VisualCron is installed in root directory of drive (VC-1173)

:white_check_mark: Client: Robot Task->Fixed OCR selection bug (VC-1170)

:white_check_mark: Server: Cloud->OneDrive upload fixed issue 'Index was outside the bounds of the array' (VSPS-134)

:white_check_mark: Server: Cloud->OneDrive upload fixed issue 'Object reference not set to an instance of an object' (VSPS-132)

:white_check_mark: Server: SCP->Fixed upload error 'scp: error: unexpected filename' (VSPS-131)

:white_check_mark: Client: SQL Connection->Fixed save on close issue (VSPS-136/VC-1179)

:white_check_mark: Server: Sharepoint->Fixed root folder browsing issue (VSPS-135)

:white_check_mark: Server: Cloud Connection->Fixed issue with Task succeeding even if Connection was not existing (VSPS-133)

:white_check_mark: Server: MFT->Fixed permissions issue (VC-1185)

:white_check_mark: Server: Azure->Added missing dlls to installation (RM) (VC-1208)

:white_check_mark: Server: Connections->Fixed crash issue when lacking permissions when opening Connection (VC-1184)

:white_check_mark: Server: ForEach loop additional fix (VC-1007)

:white_check_mark: Server: Crystal reports->Fixed issue with Date Variable resolving (VC-1212)

:white_check_mark: Server: SQS Trigger->Fixed issues with collecting data (VC-1137)

:white_check_mark: Server: SQL Task->Fixed Oracle component license issue (VC-1218)

:white_check_mark: Client: On error->Exit code collection management->Fixed null reference issue when no Exit code collection was selected (VC-1220)

:white_check_mark: Client/Server: Web macro->Fixed download issue (VC-1211)

:white_check_mark: WebClient: Web macro->Fixed persistence of Server Connections (VC-1213)

:white_check_mark: Server: Task repository->Fixed an issue with .NET code execution (VC-1223)

:white_check_mark: Server: Assembly Execute Task->Fixed issue refreshing assembly (VC-1224)


### 9.1.0 [2020-01-21]

#### Features

:star: Client/Server: Tasks->Auto scrolling to node in Task->Main settings->treeview (VC-917)

:star: Client/Server: SFTP/FTP/Cloud->Triggers and Tasks->Download->Added download destination file mask (VSPS-57)

:star: Client: SQL Connections->Added group support (VSPS-113)

:star: Client: SQL Connections->Title add/edit support in window (VSPS-110)

:star: Client: Connection Explorer->Realtime updates an Connection delete addition (VSPS-109)

:star: Client: Connection Explorer->Auto selection of Connection from Manage Connections (VC-1050)

:star: Client: External logging->Added tables recreation/dropping (VC-1029)

:star: Client: Export/Import settings->Group filtering (VC-1025)

:star: Client: Conditions->Added search filter (VC-1037)

:star: Client/Server: Various components updated (VC-1065,VC-1054)

:star: Client/Server: Add Connection->Added test buttons for various protocols (VSPS-114)

:star: Client: PowerShell Task->Moved parameters to tab (VC-1023)

:star: Client: EC2 Tasks->Added proxy support (VC-771)

:star: Client: Web macro->Added runtime output details when testing in Client (VC-925)

:star: Client/Server: Web macro->Update previews at playback (VC-1067,VC-1077)

:star: Client/Server: Web macro->Added "Save as PDF" step (VC-1008)

:star: Client/Server: Web macro->Added Conditional features (VC-1048)

:star: Client/Server: Web macro->Update to Chromium version 77

:star: Client: Triggers->Increased max polling interval to 9999999 (VC-1131)

:star: Client/Server: Excel->Set cell->Add option to clear worksheet before starting (VC-1166)


#### Bug Fixes


:white_check_mark: Client/Server: Slack Trigger->Added reconnection options on failure (VC-864)

:white_check_mark: Server: XML->Edit node Task->Fixed Credential issue (VC-1046)

:white_check_mark: Server: Server settings->AD test->Fixed 'Length cannot be less than zero' issue (VC-1049)

:white_check_mark: Client/Server: SharePoint->Fixed issue with upload of large files (VSPS-115)

:white_check_mark: Server: SSIS Tasks->Fixed missing VisualCronAPI.dll file (VC-1063)

:white_check_mark: Client: New registry setting was created for V9 to not conflict with side by side V8 (VC-1069)

:white_check_mark: Client/Server: Notifications->Various fixed to log window and logging functionality related to Flow (VC-1074)

:white_check_mark: Client: Web macro->Fixed null reference error during record (could not find frame) (VC-1070)

:white_check_mark: Client: Web macro->Fixed hide password issue (VC-987)

:white_check_mark: Client: Web macro->Fixed "choppy" update of step (VC-1071)

:white_check_mark: Client: Web macro->Fixed re-record append sequence issue (VC-1072)

:white_check_mark: Client: Web macro->Fixed issue going to next step from populate Task to fast (VC-1073)

:white_check_mark: Client: Web macro->Fixed issue properties in upload/download path not updated after change (VC-973)

:white_check_mark: Server: Web macro->Fixed a memory leak (VC-1079)

:white_check_mark: Server: Web macro->Click crash (VC-1083,VC-1084)

:white_check_mark: Client: Web macro->Fixed double click / right click issues in Steps (VC-914)

:white_check_mark: Client: Web macro->Fixed populate password issue (shown in cleartext) and related Enter step (VC-1111,VC-1113)

:white_check_mark: Client/Server: Web macro->Fixed issue with screenshot action (VC-1079)

:white_check_mark: Client/Server: Web macro->Fixed issue loading plugins like Flash (VC-1117)

:white_check_mark: Client/Server: Web macro->No download folder ccould result in hang (rather than failure) (VC-740)

:white_check_mark: Client/Server: Web macro->Fixed Download/Upload properties editing (VC-928)

:white_check_mark: Client/Server: Web macro->Fixed web auth null issue (VC-1152)

:white_check_mark: Client/Server: Web macro->Fixed blank steps listing issue (VC-1148)

:white_check_mark: Server: Output->Handled potential hang of Execute Tasks (VC-657,VC-1082)

:white_check_mark: Server: Handled exception related to retrieving thread CPU usage (VC-1091)

:white_check_mark: Client: Cloud->Fixed folder selection issue (VSPS-116)

:white_check_mark: Client: Certificates->Fixed a license issue exporting Certificates (VC-1103)

:white_check_mark: Client: .NET Code Task->Only some dlls are listed fix + more detailed listing (VC-921)

:white_check_mark: Server: File Trigger->Fixed retry issue on failure (at startup) (VC-1104)

:white_check_mark: Client: Task history->Fixed realtime update issue (VC-1105)

:white_check_mark: Server: SQL Task->Fixed outputting date data type as date and not datetime (VC-1106)

:white_check_mark: Server: Image Tasks->Fixed issue with image rotate on tif image with many pages (VC-1101)

:white_check_mark: Server: Now checking for free diskspace before trying to save Jobs, minimum of 50MB is currently required (VC-1114)

:white_check_mark: Server: Web API->Fixed object reference issue when Variables parameter was not supplied for Run method (VC-1116)

:white_check_mark: API: Adapted some methods to fit ASP.NET Core 3.1 - still 3.1 is not fully supported (VC-1115)

:white_check_mark: Client: Conditions->Fixed read permissions (VC-1124)

:white_check_mark: Server: Increased max allowed time for PowerShell, .NET, SSISDB Tasks (VC-1126)

:white_check_mark: Server: SSIS Task->Fixed decryption of parameters in 2017 version of this Task (Array cannot be null) (VC-1127)

:white_check_mark: Client: Notifications->Fixed read permissions (VC-1132)

:white_check_mark: Server: Email Trigger->Fixed problem with MailFolder Variable when only saving attachment and not email (VC-1130)

:white_check_mark: Server: Cloud Tasks->Fixed better cancellation of Tasks (VSPS-119)

:white_check_mark: Client: Robot Task->Fixed issue with OCR crashing (VC-892)

:white_check_mark: Server: Cloud Tasks->Adder more detailed Amazon loggging (VSPS-123)

:white_check_mark: Server: Telegram->Fixed proxy issue (VC-1125)

:white_check_mark: Server: IM/XMPP/Jabber Task fixes for Openfire (VC-952)

:white_check_mark: Client: Connections->Fixed null reference error when authentication failed (VC-1146)

:white_check_mark: Client: Connection Explorer->Fixed issue with close button and refresh of names on update (VSPS-126)

:white_check_mark: Client: Flow chart->Fixed multi page print issue (VC-905)

:white_check_mark: Server: Telegram Task->Added support for HTTP proxy (VC-1125)

:white_check_mark: Server: Archive - Extract->Fixed folder creation issue (VC-1153)

:white_check_mark: Server: Archive - Extract->Fixed issue extracting newer versions of RAR (VC-1129)

:white_check_mark: Client: File Explorer->Fixed "Illegal characters in path" error (VC-1165)

:white_check_mark: Client/Server: Variables->Fixed issues with a LOGIC Variable (VC-1167)

:white_check_mark: Client: Permissions->Fixed permissions for SQL Connection and Task manager (VC-1172)


### 9.0.0 [2019-11-26]

#### Features

:star: Client/Server: Protocol change->Due to many security changes you can no longer connect to older versions or connect with older Clients to this version. If you want to downgrade to older version without loading settings from an older backup

:star: Client/Server: Upgraded to .NET 4.8 (VC-602)

:star: Client/Server: Archive Compress->Added new Credential option to be able to store archive on network share. If you relied on Credential of content please use the same Credential (if using the same share) (VC-811)

:star: Client/Server: Active Directory->Added test button (VC-531/VC-608)

:star: Client/Server: Slack - send messages->Added support for attachments (VC-789)

:star: Client/Server: Job/Task log->Added database output search (VC-693)

:star: Client/Server: SQL Task->Support for Amazon RDS and Amazon Aurora (VSPS-76)

:star: Client/Server: Web macro Task->Upgraded UI for more complex logic (VC-695)

:star: Client/Server: Robot Task->Upgraded UI for more complex logic (VC-695)

:star: Client/Server: Updated general encryption security to AES-256 (VC-704)

:star: Client/Server: General Web Client updates

:star: Client/Server: Web API->Added ability to run Job with Job Variables set (VC-667)

:star: Client/Server: Logs->Added all Job log search based on date interval (VC-889)

:star: Client/Server: New Tasks for Amazon DynamoDB (VC-636)

:star: Client/Server: Settings->Import/Export->Added filter on name (VC-890)

:star: Client: Server manager/Main window->Added computer name (VC-932)

:star: Client: Connection Explorer/Remote file/folder browser->Improved threading for better UI experience (VSPS-83)

:star: Client/Server: Variables->Added Variable for printing special characters {STRING(Print|line1\nline2)} (VSPS-101)

:star: Client/Server: Powershell->Added command support to be able to set Execution Policy and other (VC-882)

:star: Client/Server: Box transfer optimizations (VSPS-82,VSPS-83)

:star: Client/Server: Local/Remote file filters->Added better date validation and showed accepted server format (VC-959)

:star: Server: Exit codes->Auto adding not found exit codes (VC-947)

:star: Client: Performance increase in main window when connecting/listing (getting full username) (VC-963)

:star: Server: Performance increase in Server process polling (VC-946)

:star: Client: Added setting to allow multiple Client instances on the same Server (VC-936)

:star: Client: Performance increase in Connection Explorer/remote folder browser (VSPS-83,VSPS-99)

:star: Client/Server: Sharepoint/Cloud->Added result Variables (VSPS-95)

:star: Client: Performance increase startup (VC-998)

:star: Client/Server: Powershell Task now support typed parameters (VC-898)

:star: Client: Triggers->Added Copy Trigger Id from Trigger to clipboard (VC-954)

:star: Client: Mixed GUI updates (VC-1035,VC-1031)

:star: Client/Server: Dynamics CRM->Added Connection test (VC-1005)

:star: Client: Auto selection/scroll to when clicking on Manage buttons for Notifications, Credentials and Connections (VC-918)


#### Bug Fixes


:white_check_mark: Client: Fixed issue with farsi language display (VC-802)

:white_check_mark: Client/Server: .NET Code Task->Fixed various issues refreshing, run and dll selection (VC-819)

:white_check_mark: Client/Server: Excel Create/Set->Fixed issue with Date formatting (VC-803,VC-856)

:white_check_mark: Client/Server: Log off Task->Fixed issue running Task on Windows 2016 (VC-831)

:white_check_mark: Client/Server: MFT->Variable fixes for Download/Upload path and file name (VC-580)

:white_check_mark: Client/Server: FTP/SFTP->Fixed List folders action and some GUI related stuff (VSPS-81)

:white_check_mark: Server: System - Restart Task->Fixed issue rebooting with no Credential (VSPS-93)

:white_check_mark: Server: Fixed a memory leak that appeared in VMWare systems related to Active Directory (VC-752)

:white_check_mark: Client: Fixed deselect all issue in Job permissions (VC-853)

:white_check_mark: Client/Server: Web service Task->Fixed array parameter issue (VC-852)

:white_check_mark: Client/Server: Excel - Recalculate->Fixed issue with xls files (VC-673)

:white_check_mark: Client/Server: Certificates manager->Fixed right click issue (VC-861)

:white_check_mark: Client/Server: Audit log->Versions->Fixed Task N/A issue (VC-834)

:white_check_mark: Client/Server: File filter->Fixed count issue when there was access problems (VC-833)

:white_check_mark: Client: Trigger->Fixed issue with UI issue and "Run delay" option (VC-866)

:white_check_mark: Client/Server: Sync files Task->Added support for one-way synchronization and made some changes to the propagate deletion function (VC-722)

:white_check_mark: Server: Tasks with sub exe (like SSISB) did not include all error output (VC-867)

:white_check_mark: Server: AMPQ Connection->Fixed issues related to Connections settings (port save and auth warning) (VC-862)

:white_check_mark: Server: Remote File Trigger->Fixed issue with download hwne using option "Save files relative to destination source path" (VSPS-80)

:white_check_mark: Server: SSISDB Task->Fixed a folder refresh issue (VC-872)

:white_check_mark: Client: Fixed an issue clicking on link in output (VC-859)

:white_check_mark: Server: SSIS Task->Fixed Credential validation issue (VC-874)

:white_check_mark: Server: Excel Create->Fixed performance issue when writing to Excel file (VC-885)

:white_check_mark: Server: Sharepoint Delete->Fixed null reference exception on Connection Id (VC-886)

:white_check_mark: Server: Logging->Fixed issue with cleaning up external database according to cleanup rules (VC-883)

:white_check_mark: Server: Office Macro Task->Fixed error handling for non existing file (VC-869)

:white_check_mark: Server: Sharepoint->Fixed issues downloading files with # character in it (VSPS-89)

:white_check_mark: Client: Remote folder browser->Fixed tooltip (VSPS-88)

:white_check_mark: Client: Box->Fixed issues with Test files tab not working properly (VSPS-82)

:white_check_mark: Server: FTP/SFTP Upload->Fixed multiple upload items "On error" handling to be able to ignore "No files found" (VSPS-86)

:white_check_mark: Server: Web macro Task->Fixed "Uncaught ReferenceError" (VSPS-899)

:white_check_mark: Server: VCCommand.exe->Fixed remote connection issue (VC-854,VC-855)

:white_check_mark: Server: Fixed non working date Variables in date filter i.e. {TASK(Active|LastExited|dd/MM/yyyy HH:mm)} (VC-913)

:white_check_mark: Server: SFTP->Added more clear error when preserving dates on upload fails (VSPS-96)

:white_check_mark: Server: Flow->Notifications - fixed possible duplicate Notifications when using 'On complete' events (VSPS-97)

:white_check_mark: Server: .NET Code Task->Fixed assembly load issue (cannot find the file specified) (VC-901)

:white_check_mark: API: License->Fixed license issue (switching from Pro to Basic) (VC-922)

:white_check_mark: Installer: Killed other instances of PreInstaller (preventing installation) (VC-930)

:white_check_mark: Server: MFT->Fixed folder permission issues (VC-896)

:white_check_mark: Server: Fixed "Credential not found" issue when running Task manually (in a loop) and exiting (VC-940)

:white_check_mark: Client/Server: SFTP->Fixed a possible cause for error 96273 (VC-894,VC-953,VSPS-98)

:white_check_mark: Client: SFTP->Fixed a possible cause for error 96273 (VC-894,VC-953,VSPS-98)

:white_check_mark: Client: Permissions->Fixed Trigger permissions (menu) (VC-929)

:white_check_mark: Server: SFTP/SCP Task/Trigger->Failed to download System.ArgumentException: String cannot be of zero length (VSPS-102)

:white_check_mark: Server: Remote file Trigger->Fixed stack overflow crash related to many subsequent connection failures (VC-893)

:white_check_mark: API: Web API->Fixed certificate issue when using HTTPS (VC-875)

:white_check_mark: Client: Remote folder browser->Fixed empty path issue on non-existing predefined folder (VSPS-100)

:white_check_mark: Client: Fixed a translation bug in main window right click menu (VC-839)

:white_check_mark: Client: Manage Server Connections->Handled empty hostname issue (VC-976)

:white_check_mark: Client: Variables->Fixed usage of Variables in Connection Explorer/Remote folder/file browser (VC-1000)

:white_check_mark: Server: Execute Task->Fixed problems showing error output when file was not found (VC-1002)

:white_check_mark: Client/Server: Variables->Fixed issue using User Variables in File filter (VC-1003)

:white_check_mark: Server: Loops->Fixed value "1" added to CurrentXValue when originating from Go to Task in Flow (VC-1007)

:white_check_mark: Server: Sync file(s)->Fixed issue with with sync when file is deleted in source (VC-943)

:white_check_mark: Server: PrevTask value issue in long running event for Notification (from Task) (VC-1013)

:white_check_mark: Client/Server: WebDAV->Fixed connection issue for uncommon responses (VSPS-104)

:white_check_mark: Client/Server: WebDAV->Fixed issue not uploading full folder structure (VSPS-106)

:white_check_mark: Client/Server: WebDAV->Download->Fixed issue with destination folder Variable not resolved (VSPS-107)

:white_check_mark: Client/Server: Web service Task->Fixed issue using a Variable in url (VC-978)

:white_check_mark: Server: SQL Trigger->Fixed issue when trying to deactivate Trigger when in retry mode (on error) (VC-1016)

:white_check_mark: Server: Assembly execute/Web service->Too long time loading dll issue (VC-977)

:white_check_mark: Server: Web service->Web service refresh crash issue (VC-971)

:white_check_mark: Server: Sharepoint upload issue->PropertyOrFieldNotInitializedException (VSPS-108)

:white_check_mark: Server: Email Task->Get/Delete messages/headers - fixed unread/read filter (VC-1027)

:white_check_mark: Client/Server: Excel Create->Fixed erroring out if no file is found (VC-860)

:white_check_mark: Server: Copy files Task->Fixed a potential issue when copying very large files (VC-950)

:white_check_mark: Client: Cloning Job from other Server resulted in wrong JobId in Stats class (VC-1033)

:white_check_mark: Server: Amazon S3->Fixed issue with file upload/download when requests are handled by cluster of servers (VS-PS-112)

:white_check_mark: Client: Output window->Fixed some issues related to resolving links (VC-1038)


### 8.5.5 [2019-08-28]

#### Features

:star: Client/Server: Web service Task->Added SOAP Body discovery and execution option

:star: Client/Server: Web service Task->Added support for using Variables in date fields

:star: Client/Server: Performance fixes

:star: Client: Connection Explorer->Improved dragn drop support

:star: Client/Server: Password rules->New expiration features added

:star: Client/Server: Oracle->Addes support for stored procedures retrieval and execution (within packages)

:star: Server: Archive - Compress->Added option "Always create archive" - when checked an empty archive will be created no matter if files are not found

:star: Client/Server: Cloud Tasks->Implemented Move/Copy actions

:star: Client/Server: Cloud->Added overwrite options


#### Bug Fixes


:white_check_mark: Server: Conditions->Fixed issue cleaning up duplicate Conditions in a Condition set

:white_check_mark: Server: Telegram->Fixed dll issue for Telegram Bot option

:white_check_mark: Server: Azure->Fixed dll issue for Azure virtual machines refresh

:white_check_mark: Server: Crystal reports->Fixed null reference issue when loading parameters

:white_check_mark: Server: Copy files Task->Fixed issue copying from root path

:white_check_mark: Client: Permissions->Fixed problems opening Time exceptions, Connections and Conditions with Read permission

:white_check_mark: Server: .NET Code Task->Fixed issue with delete of temporary files

:white_check_mark: Server: Archive - Compress->Fixed issues with content filters

:white_check_mark: Server: Email Trigger->Fixed problems finding folder

:white_check_mark: Server: Microsoft Teams->Fixed dll reference issue

:white_check_mark: Server: Set folder permissions->Fixed use of Credential

:white_check_mark: Server: Email->Get messages->Fixed problem with Read filter when using Exchange EWS

:white_check_mark: Client/Server: Licensing->Fixed an issue with extending trial (sync dates between Client and Server)

:white_check_mark: Server: Copy files Task->Fixed deletion of empty sub folders option

:white_check_mark: Server: PGP - Decrypt->Fixed destination file mask renaming issue

:white_check_mark: Client/Server: Firewall buttons->Fixed problems changing/identifying firewall settings

:white_check_mark: Server: Archive - Compress->Fixed issue compressing 7z archive with files from network share

:white_check_mark: Server: SFTP - Upload->Fixed problem with output when uploading from different sources

:white_check_mark: Server: File write->When not using Append we added an empty row - that has been fixed

:white_check_mark: Client: GANTT chart->Improved form load speed and experience

:white_check_mark: API/Server: Fixed some trial/pro license issues


### 8.5.4 [2019-07-31]

#### Features

:star: Client: Performance fixes in main grid (filter)

:star: Client/Server: Performance fixes for large number of Jobs (Use compression in server connection)

:star: Client/Server: MFT settings->Various improvements in settings

:star: Client/Server: PGP->Export keys now supporting newer format of OpenPGP standard

:star: Client: Credentials->Added warnings for incorrect usage

:star: Client/Server: Variables->Added quarter Variable


#### Bug Fixes


:white_check_mark: Client/Server: Job/Task Control Task->Fixed issue with permissions and Variables

:white_check_mark: Client/Server: MFT Trigger->Various variable fixes

:white_check_mark: Server: WebDAV Download->Handled issue with migrating old Task

:white_check_mark: Client: Grid->Fixed black flashing and row updating issues

:white_check_mark: Server: SSISDB Task->Fixed refresh issue

:white_check_mark: Server: Archive Compress Task->Fixed issue with 0 sized package

:white_check_mark: Server: Assembly Execute Task->Fixed issue returning output and result

:white_check_mark: Client/Server: Web macro Task->Handled a specific javascript issue (find button)

:white_check_mark: Server: Sharepoint Task->Added debugging

:white_check_mark: Server: Web macro->Fixed issue with resolving Variable in printer name

:white_check_mark: Client: SQL Task->Fixed issue refreshing stored procedures when creating Task Notification

:white_check_mark: Client/Server: Telegram Task->Fixed handling of authentication issue

:white_check_mark: Client/Server: Copy files Task->Fixed issue using wildcard in folder name

:white_check_mark: Client: Copy files Task->Fixed scanning servers crash


### 8.5.3 [2019-07-15]

#### Features

:star: Client/Server: Added Task manager with CPU usage per Job / Task / Thread / Services etc.

:star: Client/Server: SSIS Task->Added support for SQL server 2017

:star: Client/Server: WebDAV->Added List files and folders Tasks and file filters for WebDAV Tasks

:star: Client/Server: FTP/Cloud/WebDAV->Added Get folders Task

:star: Client/Server: VisualCron Trigger->Added option to ignore the current Job

:star: Client/Server: SharePoint Tasks->Optimized listing of files

:star: Client/Server: Proxy->Added test button for proxy

:star: Client/Server: Added support for AzureRM in Azure Tasks

:star: Client/Server: VisualCron Trigger->On error reconnect attempts added

:star: Client/Server: Web API->Added Task repository methods


#### Bug Fixes


:white_check_mark: Client/Server: Amazon S3->Folder selection fixes

:white_check_mark: Client/Server: SFTP/SSH default cipher changes

:white_check_mark: Server: Email Trigger->Fixed "Keep connection" issue

:white_check_mark: Server: Email Task/Notification->Fixed issues with truncating email recipient

:white_check_mark: Server: File Trigger->Fixed issue with folder exclusion and using full path

:white_check_mark: Client: Backup settings->Fixed missing option for "Task repository objects"

:white_check_mark: Client: Unlock desktop Task->Fixed Credential validation error

:white_check_mark: Server: Variables->Fixed issue with Task->Connection string Variable

:white_check_mark: Server: .NET Code Task/Assembly Execute Task->Fixed character encoding issue

:white_check_mark: Server: Job folders->Fixed issues with Job folders

:white_check_mark: Server: Output->Handled large output issues

:white_check_mark: Server: XML - Create/Edit node->Fixed Variable resolving issues

:white_check_mark: WebClient: Fixed various issues with reworked code (speed, flickering)

:white_check_mark: Server: SQL Task->Fixed stored procedures refresh issue for Oracle

:white_check_mark: Server: Variables->Fixed current executing user Variable when running Tasks manually

:white_check_mark: Server: PowerShell->Fixed a problem capturing "throw"

:white_check_mark: Client/Server: WebDAV->Fixed a problem with URI construction

:white_check_mark: Server: PDF Task->Add Header: Fixed some output issues and a Credential issue

:white_check_mark: Server: SharePoint->Fixed Connection and inner exception issues

:white_check_mark: Client: Task repository->Fixed bug adding new objects

:white_check_mark: Server: Email Trigger->Fixed issue with reading delete messages

:white_check_mark: Server: Excel - Recalculate Task->Some optimizations for Excel 2007 and over

:white_check_mark: Client/Server: Job running status - fixed potential hanging on "Running"

:white_check_mark: Server: Audit log->Limited more sensitive values from diff

:white_check_mark: Server: Service Tasks->Fixed remote Credential validation

:white_check_mark: Server: Task flow->Fixed a problem with Retry times not resetting when using multiple Tasks with retry times

:white_check_mark: Server: Fixed an issue with Test Job feature in Client

:white_check_mark: Server: Task repository->Fixed issue using Variables in parameters

:white_check_mark: Server: Cloud file Trigger->Fixed issue with downloading

:white_check_mark: Client: Main grid->Improved some speed

:white_check_mark: Client: Main grid->Added column Task->Description and removed some irrelevant columns in column selector

:white_check_mark: Server: Logoff Task->Fixed issue on newer Windows server versions

:white_check_mark: Server: Archive extract->Fixed issue with inheriting original permissions


### 8.5.1 [2019-05-15]

#### Features

:star: Client/Server: Added Task Repository - community shared code

:star: Client/Server: Remote/Cloud file Trigger->Added optional "Wait before download"

:star: Client/Server: Amazon S3->Added setting for "multi part upload size"

:star: Client/Server: SFTP->Updated default "auto"-encryption algorithms

:star: Client/Server: Added Trigger->Trigger debugging and moved Task and Trigger debugging from general Extended debugging to create less and more direct logging

:star: Client/Server: SharePoint Tasks->Added filters

:star: Client/Server: Connection Explorer->Improved performance


#### Bug Fixes


:white_check_mark: Client/Server: Credentials->Fixed an issue updating local login/load profile

:white_check_mark: Client/Server: Connection->SQL->Fixed db index error when selecting among connection strings

:white_check_mark: Client: Slack->Fixed UI issue

:white_check_mark: Client: Task schedule import issue->Fixed missing dll error issue

:white_check_mark: Server: Print Task->Fixed concurrent printing issue

:white_check_mark: Server: Twitter Tasks->Fixed dll issue

:white_check_mark: Server: MS Teams Tasks->Fixed query issue

:white_check_mark: Server: Office 365->Get calendars->Fixed output issue

:white_check_mark: Server: Get checksum->Fixed file lock issue

:white_check_mark: Server: .NET Code Task->Fixed parameter issue when not Executing in server process


### 8.5.0 [2019-04-21]

#### Features

:star: Client/Server: Added new Trigger and Task for Microsoft Teams

:star: Client/Server: SFTP Task/Trigger/Connection Explorer->Improved list speed of large folders

:star: Client/Server: Sharepoint file filter now supports Variables

:star: Client/Server: Added Task and Trigger for Amazon SQS

:star: Client/Server: Added new Task for Amazon SNS

:star: Client/Server: Added Task Notification logs


#### Bug Fixes


:white_check_mark: Client/Server: Web macro Task->Fixed support for specific listbox and ability to ignore loading timeout

:white_check_mark: Client/Server: Fixed output issue for Tasks executing very fast

:white_check_mark: Client/Server: Fixed output issue of Main grid (Task null reference)

:white_check_mark: Client: Improved performance when opening Settings window

:white_check_mark: Server: Rename file(s) - fixed relative folder issue

:white_check_mark: Server: SAP Task->Fixed issue when two SAP Jobs are being run at the same time

:white_check_mark: Client/Server: Credentials->Fixed a potential issue creating Credentials and viewing Tasks (with that Credential)

:white_check_mark: Client/Server: WebDAV Tasks->Fixed issue with relative folders

:white_check_mark: Server: Assembly Execute Task->Fixed output issue when not using local execution (mixed debug output)

:white_check_mark: Server: Unmanaged dll call Task->Fixed serialization bug and updated documentation

:white_check_mark: Server: Print Task->Fixed PDF print issue

:white_check_mark: Server: Crystal reports->Fixed import parameters isssue

:white_check_mark: Server: Execute Task->Fixed random service crash

:white_check_mark: Server: Execute Task->Fixed issue updating Last run (and more) when calling Job through Job/Task control Task

:white_check_mark: Server: Task flow->Fixed issue Notification not being sent if Retry was used in other flow


### 8.4.2 [2019-03-22]

#### Features

:star: Client: Manage Servers->Added "scan" feature

:star: Client/Server: Credentials->Added ability to override permissions

:star: Client/Server: New Task->Informatica - Run Job

:star: Client/Server: Sharepoint - Download files - added recursive mode

:star: Client/Server: Added new DB for Notifications logging so result and output can be tracked

:star: Client/Server: Execute Task->Added option for passing Standard input as text

:star: Client/Server: Copy files Task etc->Added CURRENTFILE and CURRENTPATH Variables

:star: Server: Added support for running VisualCron server in console mode (VisualCronService.exe c)

:star: Client/Server: Amazon S3->Added support for Amazon S3 compatible servers


#### Bug Fixes


:white_check_mark: Client: Grid->Fixed a Job refresh issue

:white_check_mark: Client/Server: Web macro Task->Fixed playback issue

:white_check_mark: Server: PowerShell Task->Fixed OnError->Contains error issue

:white_check_mark: Client: Failed Jobs->Fixed output window issue

:white_check_mark: Server: Sharepoint connection optimizations

:white_check_mark: Client/Server: SSH Keyboard authentication fix

:white_check_mark: Client/Server: Email Trigger->Added instant Trigger option for IMAP protocol

:white_check_mark: Client/Server: Conditions->Fixed duplicate creation issue when cloning

:white_check_mark: Server: Job/Task Control Task->Fixed issue with waiting for completion (Run synchronous)

:white_check_mark: Client: SAP Task->Fixed cloning issue

:white_check_mark: Server: Crystal reports->Fixed reference issue

:white_check_mark: Client: Email - Get messages/single message->Fixed Credential listing

:white_check_mark: Server: Execute Task (and more)->Stopped using temp output files

:white_check_mark: Server: MSMQ->Send message Task: Fixed XML serialization issue

:white_check_mark: Client: Connection Explorer->Fixed possible crash due to icon extraction

:white_check_mark: Client: Calendar->Fixed drawing issue

:white_check_mark: Client/Server: Azure->Create VM: Fixed issue with VM creation

:white_check_mark: Client/Server: Web service Task->Added support for out parameters (WCF)

:white_check_mark: Client/Server: Variables->Removed trimming of Loop Variables

:white_check_mark: WebClient: Ignored cross domain post error

:white_check_mark: Client/Server: PowerShell->Fixed triple output issue

:white_check_mark: Server: VMWare->Added missing dll

:white_check_mark: Client/Server: Sharepoint->Fixed FieldLookupValue issue

:white_check_mark: Server: Fixed a problem with DST change (iteration of Jobs and update of next run time)

:white_check_mark: Client/Server: Web macro Task->Fixed multiple frames issue


### 8.4.1 [2019-01-23]

#### Features

:star: Client->Gantt chart for better visualization of Jobs planning

:star: Client/Server: Trailing File Trigger

:star: Client/Server: MFT->Added public key authentication support

:star: WebClient: Mixed new features

:star: Client/Server: AMQP->Added Retry options

:star: MySQL->Updated MySQL dll to support newer versions with higher security. This affects both External logging and SQL Task

:star: Client/Server: Added Peoplesoft Task and Trigger

:star: Client/Server: Added more features to Robot Task and several fixes. Including OCR support

:star: Client/Server: Added real time output for specific Tasks

:star: Client/Server: Added Azure Data Storage Trigger


#### Bug Fixes


:white_check_mark: Server: Slack Connection->Fixed crash issue when no network is available

:white_check_mark: Client/Server: PDF Concatenate Task->Added option for destination Credential

:white_check_mark: Client: Job folders->Fixed refresh issue when removing a Job from a folder

:white_check_mark: Server: Rabbit MQ Trigger->Fixed an issue with durable queues

:white_check_mark: Server: Job/Task control Task->Fixed variables issue (paramaters reference)

:white_check_mark: Server: .NET Execute Task->Fixed problem capturing unhandled errors

:white_check_mark: Client/API: Triggers->Handled issue regarding creating descriptions

:white_check_mark: Server: Archive - Decompress->Fixed issues with creation of folders in System32 folder

:white_check_mark: Client/Server: WebDav Task->Fixed download issue on paths with spaces

:white_check_mark: Client: Main window->Fixed issue with right click to Run with Conditions

:white_check_mark: Client/Server: Reverted to traditional DNS resolution

:white_check_mark: Server: Fixed issue witih nested Jobs and Run synchronous issue (still marked as running)

:white_check_mark: Client: Object search->Fixed search inside Condition objects

:white_check_mark: Client: Improved AWS S3 speed when working with many sub folders with many objects

:white_check_mark: Client/Server: Sharepoint Tasks->Fixed various listing and download issues

:white_check_mark: Client: SAP Task->Fixed issue with editing SAP step causing new add of step

:white_check_mark: Client: Main window->Fixed issue with "lock" on Running status

:white_check_mark: Client: Fixed possible hang/crash in the Remote file explorer

:white_check_mark: Client: Cloud - Sync file(s) Task->Fixed switching to Task issue

:white_check_mark: Server: SAP Task->Fixed duplicate SAP Job creation

:white_check_mark: Server: Variables->Fixed issue with Trigger Variables in Notifications

:white_check_mark: Server: Variables->Fixed issue with JQ filter issue


### 8.4.0 [2018-11-07]

#### Features

:star: WebClient: Mixed new features

:star: Server: Email Task->Added communication log to output when using Task debugging

:star: Client/Server: New Trigger->Network change

:star: Client/Server: Email Trigger->Added optional forwarding

:star: Client/Server: Task CPU affinity->CPU usage on each Task can now be controlled through main settings of Task->Set affinity

:star: Client: Triggers->Added optional "auto description"

:star: Client: Connections->Added filtering

:star: Client/Server: File Trigger->Added folder exclusing mask

:star: Client/Server: Web service Task->Added security protocol selection

:star: Client/Server: Sharepoint Tasks->Added security protocol selection in the Connection

:star: Client/Server: Robot Task->Many improvements and new actions

:star: Client/Server: New Tasks->Mixed IIS Tasks


#### Bug Fixes


:white_check_mark: Server: External DB logging fixes

:white_check_mark: Client: Fixed issue with Test Job button

:white_check_mark: Server: Box->Fixed download issue

:white_check_mark: Server: Archive - Compress->Fixed issue with compressing folders

:white_check_mark: Server: Execute Task->Fixed a potential problem when checking if process is already running

:white_check_mark: Server: MFT Trigger->Fixed issue with MFT Trigger not Triggering in some situations

:white_check_mark: API: Fixed an issue with Trigger result Variables

:white_check_mark: Client/Server: Sharepoint Tasks->Fixed various listing and download issues

:white_check_mark: Server: Slack Trigger->Fixed Text equals Condition

:white_check_mark: API: Fixed issue with Count occurencies Variable

:white_check_mark: Client: Fixed a problem with adding/cloning Default flows

:white_check_mark: Server: PGP Tasks->Fixed Variable problem in password fields

:white_check_mark: Client: SAP->Fixed problem adding multiple steps of the same kind

:white_check_mark: Server: FTP Task->Fixed problem with deleting temp files (copy/move)

:white_check_mark: Server: FTP Task->Fixed problem with uploading locked files

:white_check_mark: Client: SQL Explorer->Fixed a problem showing tables for som MySQL versions

:white_check_mark: Server: Archive compress/decompress: Fixed issue aborting Task

:white_check_mark: Server: Web service API->Fixed certificate issue

:white_check_mark: Server: Slack - Send message: Fixed support for multi line

:white_check_mark: Server: MFT->Fixed issue with transferring 0 byte files

:white_check_mark: Server: Email Tasks->Fixed issues with date condition

:white_check_mark: Server: .NET Execute Task->Fixed problem stopping the Task

:white_check_mark: Client: Failed Jobs->Fixed "days back issue"

:white_check_mark: Client: Event log->Fixed wrong server name issue when connected to multiple machines

:white_check_mark: Server: REST API->Fixed issue with text output in REST API in some scenarios


### 8.3.6 [2018-08-13]

#### Features

:star: Client/Server: WevDAV Tasks rebuilt for new component

:star: Client/Server: New Task->Telnet Task

:star: Client/Server: DB logging to any database (beta)


#### Bug Fixes


:white_check_mark: Client: Fixed issue editng Job Variables in Notification

:white_check_mark: Server: SQL Task->Fixed SQL Job query issue

:white_check_mark: Server: Mail Tasks->Fixed missing Exchange EWS Connection support

:white_check_mark: Server: Kill task->Fixed a problem adding/editing Task

:white_check_mark: Server: Delete file(s) Task->Fixed issued with Secure delete

:white_check_mark: Server: Web macro Task->Better error handling

:white_check_mark: Server: SharePoint Task - Upload file(s)->Fixed # character in file name

:white_check_mark: Server: SharePoint Task - Upload file(s)->Fixed large file upload issue

:white_check_mark: Server: SharePoint Task->Fixed auth issue

:white_check_mark: Client/Server: SharePoint Task->Fixed FieldLookupValue issue

:white_check_mark: Server: Remote File Trigger->Moved treat unknown types as files to remote file filter

:white_check_mark: Server: Web service Task->Fixed a Variable translation issue on sub parameters

:white_check_mark: Client/Server: Web macro Task->Fixed proxy issue

:white_check_mark: Client/API: Fixed Job stats update issue in right click menu

:white_check_mark: Server: Image - Overlay Task->Fixed issue with writing to same file

:white_check_mark: Server: Flow->Fixed issue with Task flows when cloning Job. Goto Task was referenced wrong

:white_check_mark: Server: Fixed issue with new password rules combined with AD logon

:white_check_mark: Client: Fixed SysLog Task control issue

:white_check_mark: Server: Fixed missing dll issue for Slack Task/Trigger

:white_check_mark: Client: Client events->Fixed issue with Update failed

:white_check_mark: Server: SCP->Fixed delete file(s) issue


### 8.3.5 [2018-06-05]

#### Features

:star: Client/Server: Folders->Group your Jobs into folders

:star: Client/Server: Delete file(s) Task->Added Secure delete functionality

:star: Server: SFTP/SCP->Added debugging

:star: Server: Web macro Task->Added debugging

:star: Client/Server: Added Azure Service Bus (through AMQP) Trigger and Send message Task for that

:star: Client/Server: Added RabbitMQ (through AMQP) Trigger and Send message Task for that

:star: Client/Server: Added password rules for authentication

:star: Client/Server: Added HTTP Status Code result Variable

:star: Client/Server: SSH Connection->Added Terminal type selection

:star: Client/Server: SSH/SFTP Connection->Added MAC algorithm selection

:star: Client/Server: Added Slack Trigger and Send message Task for that

:star: Client/Server: VMWare Tasks->Added new web service API (replacement for VIX) for VMWare Server Tasks

:star: Client/Server: Remote file Trigger->Added "Treat unknown types as files" option

:star: Client/Server: Cloud Task->New Sync file(s) Task


#### Bug Fixes


:white_check_mark: Server: Interactive logon->Handled LogOut event

:white_check_mark: Server: Office365->Fixed a missing dll

:white_check_mark: Server: Execute Task->Fixed memory leak (access denied)

:white_check_mark: Server: Web macro Task->Fixed issue with playing back List item selection

:white_check_mark: Server: SSH Task->Added non-zero exception and fixed so it fails on first <<failing command

:white_check_mark: Server: SSRS Task->Fixed use of Variables in parameters

:white_check_mark: Server: Web macro Task->Fixed issue with playing back radiobox item selection

:white_check_mark: Server: Azure - web*->Fixed Connection validation issue

:white_check_mark: Client: Delete XML Node->Fixed issue typing file name manually (to use Variables)

:white_check_mark: Client/Server: SSH/SFTP Connection->Fixed issue with key exchange algorithm selection

:white_check_mark: Server: Print Task->Fixed issue printing specific page(s

:white_check_mark: Server: Rename file(s) Task->Fixed issue with long path

:white_check_mark: Server: Copy file(s) Task->Fixed a potential lock

:white_check_mark: Client/Server: Email Trigger->Fixed folder selection tree

:white_check_mark: Client/Server: Email Trigger->Fixed a potential problem with TLS security "Cannot create secure channel"

:white_check_mark: Server: SSH Task->Send text->Faster exit of Task

:white_check_mark: Server: HTTP Task->Fixed a problem with Variable translation in form parameters

:white_check_mark: Server: Fixed FIPS compliance for some algorithms

:white_check_mark: Server: Web service Task->Fixed Windows authentication issue

:white_check_mark: Server: AD - Create group->Fixed error with creating right group type


### 8.3.4 [2018-03-09]

#### Features

:star: Client/Server: New Task->Office365 - Add calendar event(s)

:star: Client/Server: New Task->Office365 - Get calendar event(s)

:star: Client/Server: New Task->Office365 - Update calendar event(s)

:star: Client/Server: New Task->Office365 - Delete calendar event(s)

:star: Client/Server: New Task->Database - Sync table(s)

:star: Client/Server: New Trigger->Printer Trigger

:star: Client/Server: New Task->Azure - Update VM

:star: Client/Server: New Task->Azure - Create VM

:star: Client/Server: New Task->Azure - Start web site

:star: Client/Server: New Task->Azure - Stop web site

:star: Client/Server: New Task->Azure - Restart web site

:star: Client/Server: New Task->Azure - Remove web site

:star: Client/Server: New Task->Azure - Create web site

:star: Client: Improved SFTP - Brute force test

:star: Client/Server: SCP->Added support for public key authentication

:star: Client/Server: SSRS Task->Fixed support for multiple (array) parameters

:star: Client/Server: New Task->Email - Get header(s)

:star: Client/Server: New Task->Email - Get message(s)

:star: Client/Server: New Task->Email - Get single message

:star: Client/Server: New Task->Email - Delete single message

:star: Client/Server: New Task->Email - Delete message(s)


#### Bug Fixes


:white_check_mark: Server: Email Trigger->Fixed issue with some Email result Variables like AttachmentFolder, MailPath and MailFolder

:white_check_mark: Server: Events->Added missing Task Notification not found event

:white_check_mark: Server: Loop->Fixed a problem with wait loop values

:white_check_mark: Server: Amazon S3->Fixed problem with creating folders in Download Task

:white_check_mark: Server: Web macro Task->Changed default location for web engine to prevent problems with temp folder

:white_check_mark: Server: Variables->Fixed Job Variable reference issue when mixing Variables from different Jobs

:white_check_mark: Server: Get AD Object property Task->Fixed converting some specific date values

:white_check_mark: Client: Connections->Fixed filter to filter on Address too

:white_check_mark: Client/Server: SCP->Fixed folder creation for download

:white_check_mark: Client/Server: SCP->Fixed drag and drop for upload issue (wrong target folder and name)

:white_check_mark: Client/Server: License->Fixed a license validation (maintenance expired + using latest possible version)

:white_check_mark: Client/Server: Web service Task->Fixed issue with supporting older versions of server certificate

:white_check_mark: Server: Image - Crop->Fixed crop issue

:white_check_mark: Server: Logging->Improved cleanup by compacting database

:white_check_mark: Server: Jobs load/sync->Fixed issue when referencing to Task in Trigger (when Task not yet has been loaded)

:white_check_mark: Server: Web macro Task->Fixed issue aborting a running macro

:white_check_mark: Server: Web macro Task->Fixed compability issue on a web site

:white_check_mark: Server: XML - Sign->Added missing dll

:white_check_mark: Server: Task->OnError: Changed logic for 'Do not raise error'

:white_check_mark: Server: Remote File Trigger->Fixed issue using Variables in Download->Destination folder

:white_check_mark: Server: Loop->Added ability to abort loops faster


### 8.3.3 [2018-02-04]

#### Features

:star: Client/Server: New Task->PDF - Add attachment(s)

:star: Client/Server: New Task->PDF - Get attachment(s)

:star: Client/Server: New Task->PDF - Delete attachment(s)

:star: Client/Server: New Task->PDF - Replace text

:star: Client/Server: New Task->PDF - Search text

:star: Client/Server: New Task->PDF - Insert pages

:star: Client/Server: New Task->Encrypt (asymmetric)

:star: Client/Server: New Task->Decrypt (asymmetric)

:star: Server: PDF - Set field(s)->Added alternate ways of setting combobox (both text and number) and checkbox (both "true" and 1 and 0)

:star: Client: Web service/Assembly execute Task->Now supporting file selection for byte arrays

:star: Server: Server communication now requiring TLS 1.2

:star: Client/Server: Loop->Added milliseconds wait support

:star: Client/Server: Print Task->Added Auto orientation for PDF

:star: Client/Server: Client events->Added Notification failed event


#### Bug Fixes


:white_check_mark: Client/Server: Web macro Task->Fixed issue with downloading without Credential

:white_check_mark: Server: PDF - Split->Fixed some issues splitting at the right page

:white_check_mark: Server: PDF - Convert->Fixed error "Cannot access a closed data stream" when trying to convert JPG to PDF

:white_check_mark: Client: PDF - Encrypt->Fixed display of permissions

:white_check_mark: Server: PDF - Encrypt->Fixed error "Security handler is not bound to PDF document"

:white_check_mark: Server: PDF - Sign->Fixed image widget not showing in some scenarios

:white_check_mark: Server: PDF - Convert->Fixed locked file issue

:white_check_mark: Client: Client events->Fixed a problem with showing the "Job failed" event

:white_check_mark: Client: Remote file Trigger->Adding missing SCP Connection

:white_check_mark: Server: Web macro Task->Fixed issue with upload and Credentials

:white_check_mark: Server: Flow->Fixed false/positive error at Job/Task startup

:white_check_mark: Server: Web API->Fixed issue with server certificate

:white_check_mark: Client: Web service/Assembly execute Task->Fixed issue with "Empty" data type

:white_check_mark: Server: Kill process->Added functionality to prevent killing vital processes

:white_check_mark: Server: Print->Fixed issue with margins (fill paper) for PDF printing

:white_check_mark: Server: Base64 - Decode->Fixed an issue with decoding

:white_check_mark: Server: Login->Fixed a problem with AD logon and groups

:white_check_mark: Client: License status->Fixed some issues concerning update license status

:white_check_mark: Client: Main window->Fixed a problem with black flickering grid


### 8.3.2 [2018-01-05]

#### Features

:star: Client/Server: Web macro->Added feature to optional store session/cookies between calls

:star: Server: Remote execute->Changed from default 4 hours timeout to 7 days

:star: Client/Server: Settings->Added firewall control button

:star: Client/Server: Export settings Task->Optional password with encryption

:star: Client/Server: Import/Export settings->Optional password with encryption

:star: Client/Server: New Task->PDF - Split

:star: Client/Server: New Task->PDF - Remove page(s)

:star: Client/Server: New Task->PDF - Convert

:star: Client/Server: New Task->PDF - Encrypt

:star: Client/Server: New Task->PDF - Decrypt

:star: Client/Server: New Task->PDF - Sign

:star: Client/Server: New Task->PDF - Clear signature(s)

:star: Client/Server: New Task->PDF - Get field value(s)

:star: Client/Server: New Task->PDF - Set field value(s)

:star: Client/Server: New Task->PDF - Get information

:star: Client/Server: New Task->File - Sync

:star: Client/Server: FTP Connection->Added support for cipher selection

:star: Client/Server: New Trigger->MFT Trigger

:star: Client/Server: Encrypt (symmetric) Task->Added AES encryption

:star: Client/Server: Decrypt (symmetric) Task->Added AES encryption

:star: Client/Server: Certificates->Creation->Added AES256 algorithm and up to 4096 bit size

:star: Client/Server: Crystal reports->Version was upgraded to version 21 (3500) - please download latest runtime


#### Bug Fixes


:white_check_mark: Server: Web service Task->Handled object reference error when using WCF in some situations

:white_check_mark: Server: SFTP Connection->Now Timeout affects CommandTimeout as well

:white_check_mark: Client: Remote file explorer->Fixed closing crash issue when nothing has been selected

:white_check_mark: Client: Connections->Fixed a filter and crash issue when opening Connection from Task

:white_check_mark: Server: SQL Task->Fixed multiple query (semi colon separated) issue with Oracle

:white_check_mark: API: Permissions->Fixed validation for Task running and changing Server status

:white_check_mark: Server: Telegram->Fixed problems with passing Telegram App Id (requesting code)

:white_check_mark: Client: SSH Task->Increased max value for Receive timeout

:white_check_mark: Server: SQL Task->Fixed issue adding extra row delimiter in the end of the output

:white_check_mark: Client/Server: Web macro Task->Handle issues uploading/downloading from network share with Credential

:white_check_mark: Client: Permissions->Added missing License permission

:white_check_mark: Server: Flow->Fixed problem with running Notifications if the Job was set to not run Tasks in order

:white_check_mark: Server: Excel->Convert->Fixed an issue converting month format in a special scenario


### 8.3.1 [2017-11-30]

#### Notes

:memo: All: New protocol version (8.3.1) for communication. Requires Server and Client version to be the same.


#### Features

:star: Server: Added better Job recovery options for incompatible Job definitions

:star: Client/Server/TrayClient: Added detailed control over client event popups

:star: Client/Server: Added grouping and search in Connections


#### Bug Fixes


:white_check_mark: Client: Client events->Fixed sorting

:white_check_mark: Server: Web macro Task->Fixed object reference error related to Extract data action

:white_check_mark: Server: SQL Task->Fixed a problem using Variables in the Task

:white_check_mark: Server: MFT->Added some missing files to installation

:white_check_mark: Server: Flow->Now not adding On success if matching On complete is existing

:white_check_mark: Server: HTTP Task->Fixed impersonation issue when doing binary upload

:white_check_mark: Server: Permissions->Fixed AD authentication issue when AD user is not inhering from group

:white_check_mark: Server: MFT->Various fixes


### 8.3.0 [2017-11-23]

#### Notes

:memo: All: New protocol version (8.3.0) for communication. Requires Server and Client version to be the same.


#### Features

:star: Client/Server: MFT Server->First release of optional built in FTP and SFTP server inside VisualCron

:star: Client/Server: Dropbox is now able to use the VisualCron registered application. Note, if you used your own application you need to uncheck "Use VisualCron application" as it is the new default value.

:star: Client/Server: GoogleDrive is now able to use the VisualCron registered application. Note, if you used your own application you need to uncheck "Use VisualCron application" as it is the new default value.

:star: Client/Server: New Task->JSON filter

:star: Client/Server: SQL Task->Generally faster executions

:star: Client/Server: SQL Task->Can now retrieve InfoMessages from database

:star: Client/Server: SQL Task->SQL Jobs are now better monitored using OLEDB and ODBC

:star: Client/Server: Image resize->Added resize based on DPI

:star: Client/Server: Image convert->Added option for setting quality on resulting JPG images

:star: Client/Server: Crystal reports->Updated engine to the latest version

:star: Server: Changed default certificate for communication to be SHA256 instead of SHA1

:star: Client/Server: New Task->System - Environment - Get Variable

:star: Client/Server: New Task->System - Environment - Set Variable

:star: Client/Server: New Task->System - Environment - Append Variable

:star: Client/Server: New Task->System - Environment - Delete Variable

:star: Client/Server: New Task->System - Environment - List Variables

:star: Client/Server: New Task->Image - Get EXIF data

:star: Client/Server: New Task->Image - Image profile change

:star: Client/Server: SQL, DTS, SSIS, SSISB Tasks->Added option to pass null value

:star: Client/Server: Variables->Added null Variable

:star: WebClient: Added the remote file explorer

:star: Server: Internal DB can now repair itself upon corruption

:star: Client/Server: New Task->XML - XML Transform

:star: Client/Server: New Task->XML - XML Validate

:star: Client/Server: New Task->XML - XML Verify

:star: Client/Server: New Task->XML - XML Sign

:star: Client/Server: Settings->Added optional default flows for Jobs/Task and mass update options

:star: Client/Server: Added "Client events" for monitoring for internal errors and other events

:star: Client/Server: Added Maintenance expiration tracking in Client

:star: Client/Server: Copy files Task->Is now allowing use of two Credentials which enables copy between two network shares

:star: Client/Server: Web service Task->Added support for XmlNode object type


#### Bug Fixes


:white_check_mark: Client: Event log write Task->Fixed a problem saving the Task

:white_check_mark: Server: Web service Task->Fixed issue with null reference error

:white_check_mark: Server: Web service Task->Now maximizing MaxReceivedMessageSize instead of default 65536

:white_check_mark: Server: SQL Task->Handled infinite loop issue when specified SQL Job was not found

:white_check_mark: Server: SQL Task->Fixed issue refreshing ODBC parameters for MSSQL

:white_check_mark: Server: Active directory logon->Handled deletion of referenced groups

:white_check_mark: Server: Handled "Only local connections allowed" problem when network is disabled

:white_check_mark: Server: SQL Task->Fixed parameter type issue when opening MySQL parameter

:white_check_mark: Server: Server diagnostics->Handled crash

:white_check_mark: Client: Cloud->Download->Fixed crash when saving Dropbox with empty bucket

:white_check_mark: Server: Image Tasks->Fixed file lock issue when writing to the same file

:white_check_mark: Server: Cloud->Fixed issues with listing files and Trigger for Google Drive

:white_check_mark: Client: Cloud->Fixed issues with Google Drive remote file/folder filter

:white_check_mark: Server: PDF->Add Header/Footer->Fixed issue writing to same file

:white_check_mark: Server: Image Tasks->Fixed general issues writing to the same file and keeping EXIF properties

:white_check_mark: Server: Web macro Task->Fixed issue with setting headers

:white_check_mark: Server: Leaving Daylight Saving no longer causes a recalculation of Triggers (which could cause duplicate runs)

:white_check_mark: Server: Flow->Fixed a problem with validation in Flow->On start

:white_check_mark: Client: Set Job Variable->Fixed crash issue when clicking on Job Variables button next to Job selection

:white_check_mark: Server: Web macro Task->Fixed problem with saving option "Save to Variable"


### 8.2.9 [2017-09-21]

#### Features

:star: Server: PowerShell->Added option to access remote drives for remote execution

:star: Client/Server: File Trigger->Added no retry attempt limit option

:star: Client/Server: New Task->Image Task - Image crop

:star: Client/Server: New Task->Image Task - Image resize

:star: Client/Server: New Task->Image Task - Image rotate

:star: Client/Server: New Task->Image Task - Image flip

:star: Client/Server: New Task->Image Task - Image adjust

:star: Client/Server: New Task->Image Task - Image filter

:star: Client/Server: New Task->Image Task - Image join

:star: Web macro Task->Added support for 'same origin policy' with new option "Disable web security" (to support Google Drive automation for example)

:star: Client/Server: Cloud Tasks->OneDrive->Added option to use existing VisualCron application (no need to register own)

:star: Client/Server: New Task->Telegram - Send Bot message

:star: Client/Server: New Task->Telegram - Send User message

:star: Client/Server: Permissions->Added Audit log permission option

:star: Client/Server: Added Description property to Task

:star: Client/Server: New Task->Twitter - Tweet

:star: Client/Server: New Task->Twitter - Reply tweet

:star: Client/Server: New Task->Twitter - Get tweet

:star: Client/Server: New Task->Twitter - Delete tweet

:star: Client/Server: New Task->Twitter - Follow/Unfollow user

:star: Client/Server: New Task->Twitter - Send direct message

:star: Client/Server: New Task->Twitter - Retweet/Undo retweet

:star: Client/Server: New Task->Twitter - Like/Undo like tweet

:star: Client/Server: New Task->Twitter - Search tweets

:star: Client/Server: New Task->Twitter - Get messages

:star: Client/Server: New Task->Twitter - Get timeline

:star: Client/Server: New Task->Twitter - Get mentions

:star: Client/Server: New Task->Twitter - Get friends

:star: Client/Server: New Task->Twitter - Get followers


#### Bug Fixes


:white_check_mark: Server: File Trigger->Added more debugging

:white_check_mark: Server: Credentials->Changing back to default API CreateProcessWithLogonW (to prevent problems with accessing network shares)

:white_check_mark: Client: Cloud filter->Fixed problem with display of Include sub folders setting

:white_check_mark: Server: Checksum Task->Fixed MD5 option issue

:white_check_mark: Client: XML Tasks->Improved namepsace resolving when creating XPath queries

:white_check_mark: Client: Azure->Stop VM Task->Fixed issue with setting Deallocate option

:white_check_mark: Server: Variables->Fixed CloudFile result Variables

:white_check_mark: Client: Cloud Tasks->Fixed a UI problem with the Upload Task that could cause a crash

:white_check_mark: Server: Excel Convert->Fixed problem saving result to the right folder if source folder was in sub folder

:white_check_mark: Client: Variables->Fixed mix of | and , parameter separators. Now only using |

:white_check_mark: Server: Set Job Variable Task->Fixed problems updating Job Variables that are used within the same Job

:white_check_mark: Server: Cloud Tasks->Fixed a problem detecting file size

:white_check_mark: Server: Job Task/Control Task->Fixed a problem re-calculating next run for Trigger->Activate method

:white_check_mark: Client/Server: Fixed issues with Variable Job->Exited and general Variable resolving

:white_check_mark: Server: Interactive logon->Handled possible long paths in GetPipeList that resulted in problems connecting to Credential provider

:white_check_mark: Server: Variables->Fixed CountOccurencies string Variable (reverted previous fix in 8.2.8)

:white_check_mark: WebClient: Fixed "Invalid character" JavaScript error

:white_check_mark: Client: Email Task->Fixed problem showing window with no read permissions on PGP key rings

:white_check_mark: Server: Web API->Fixed a problem with permission check on overridden Jobs

:white_check_mark: Server: SSIS DB Task->Fixed issue with environment folder not found

:white_check_mark: Client: Connection Explorer->Fixed local renaming issue

:white_check_mark: Client: Connection Explorer->Fixed issue with extension removed during upload

:white_check_mark: Client: Connection Explorer->Fixed folder browser issue in FTP Tasks

:white_check_mark: Client: Cloud Tasks->Fixed folder selection for Amazon S3

:white_check_mark: Client: Permissions->Fixed a problem with overridden Job permissions and right click "Run Job with options"


### 8.2.8 [2017-07-31]

#### Features

:star: Server: PowerShell->Added option to access remote drives for remote execution

:star: Server: SQL Trigger->Added reconnection settings

:star: Server: Email Trigger->Added option to mark moved email as read

:star: Server: Dropbox->Support for API V2

:star: Server: Cloud services->Added support for keeping modified/created time on upload/download

:star: Server: HTTP/Webservice Task->Added Expect 100 Continue option

:star: Client/Server: New Task: EC2 - Launch instance

:star: Client/Server: Time exceptions online - import official holidays

:star: WebClient: Various improvements


#### Bug Fixes


:white_check_mark: Server: Sharepoint Upload->Fixed some issues uploading some files to various folder combinations

:white_check_mark: Server: Variables->Fixed CountOccurencies string Variable

:white_check_mark: Client: SQL Connection guide->fixed issue with deleting keywords

:white_check_mark: Client: SQL Connection guide->fixed issue with testing Connections for Oracle and MySQL

:white_check_mark: Server: Job/Task control Task->Fixed issues with inheriting exit code from Job

:white_check_mark: Client: Audit log->Fixed selection issues

:white_check_mark: Server: Event log Trigger->Fixed problem using "'" for local monitoring

:white_check_mark: Server: Event log Trigger->Fixed proble filtering against EventID

:white_check_mark: Server: Fixed a problem deactivating Triggers on expiration

:white_check_mark: Server: Foreground execution->Handled ArgumentOutOfRangeException in LoginIfNeeded method

:white_check_mark: Server: Login->Fixed problem with case sensitive domain search when using AD login method

:white_check_mark: Server: Registry Trigger->Fixed issue with monitoring remote registry value

:white_check_mark: Server: Credentials->Fixed issue with default setting CreateProcessAsUserW + LOGON_BATCH


### 8.2.7 [2017-05-25]

#### Features

:star: Server: Web macro Task - various improvements

:star: .NET Code Task->Can now be run in separate process

:star: Archive Decompress Task->Now supporting file filter mask on compressed file content

:star: Client/Server: FTP/SFTP Task->Added Keep original dates option

:star: Client/Server: Kill Task->Added kill childs option


#### Bug Fixes


:white_check_mark: Server: SNMP Tasks->Fixed support for Variables in some fields

:white_check_mark: API: Clone Tasks issue could result in new cloned Tasks not running

:white_check_mark: Server->Print PDF->Switched printing engine for more features and better support

:white_check_mark: Server->Email Trigger->Now supporting very long paths when downloading email

:white_check_mark: Server->MSMQ->Fixed problem with setting original queue to Journal type

:white_check_mark: Client: Tasks->Fixed a problem where Delete in Tasks window deleted the Task before pressing OK

:white_check_mark: Client: Notifications->Removed some event handlers that could result in crashes in some special occations

:white_check_mark: Server->Email Trigger->Handled UIDL that was not suitable as file/folder names

:white_check_mark: Server->Sharepoint Upload->Fixed issue uploading larger files than 4096 bytes

:white_check_mark: Server->Popup Task->Fixed issue returning output from Radiobox input type

:white_check_mark: Server->Variables->Fixed a problem with referencing direct Id of Task result output in some scenarios

:white_check_mark: Server->Fixed flow order/skip problems that occured in some scenarios


### 8.2.6 [2017-04-18]

#### Features

:star: Install: Now requiring .NET 4.5.2

:star: WebClient: Various improvements

:star: Client: Added exact date expiration for PGP key creation

:star: Client: Web macro Task - click on X/Y location added


#### Bug Fixes


:white_check_mark: Server: SFTP Task->Fixed MAC algorithm compatibility

:white_check_mark: Server: Variable fix for more exact Variable references

:white_check_mark: Server: Added option to Execution context´->Foreground to use existing connection

:white_check_mark: Server: EC2 Tasks->Fixed missing dll references

:white_check_mark: Server: FTP Task->Append problem fixed

:white_check_mark: Server: HTTP Task->Fixed better parsing of Content-Disposition->Filename

:white_check_mark: Client: Fixed connection problem due to different time zones

:white_check_mark: Client/Server: Web macro->Fixed issues with setting proxy and user-agent

:white_check_mark: Server: Flow->Fixed an issue with Deactivate Job option

:white_check_mark: Client: Variables->Fixed Tasks sorting issue

:white_check_mark: Server: Remote file Trigger->Fixed issue with impersonation when downloading


### 8.2.5 [2017-03-14]

#### Features

:star: WebClient: Various improvements

:star: SQL Task: Adding support for Job Variables in Connection string

:star: Web macro Task: Now supports screen capture of specific size

:star: FTP/SFTP/SCP: Append/AppendOrSkip has been added to Download


#### Bug Fixes


:white_check_mark: Client: Job log->Fixed realtime update issue which could result in wrong result of Job when completed

:white_check_mark: Server: Event log Trigger->Improved performance and remote event log handling

:white_check_mark: Server: Cloud  Tasks->Fixed issue uploading file > 2GB

:white_check_mark: Server: MSMQ->Fixed issues with connecting to remote message queues

:white_check_mark: Server: SQL Task->Fixed issues refreshing parameters from Oracle stored procedures

:white_check_mark: Server: HTTP Task->Fixed parameter Variable

:white_check_mark: Server: Email Trigger->Fixed problem monitoring/copying to a sub folder

:white_check_mark: Server: Popup Task->Various improvements

:white_check_mark: Server: WebDav - Download Task->Handled some path problems

:white_check_mark: Server: Concatenate file Task->Fixed issue with overwrite option


### 8.2.4 [2017-02-08]

#### Features

:star: Client/Server: Desktop macro Task->general improvements and edit capability

:star: Client/Server: Web macro Task->Various improvements

:star: Client/Server: SFTP->Added KeepAlive setting

:star: Client/Server: RSS Trigger->Added auth and Credential support

:star: Client: Permissions->Added "Select all" / "Deselect all" option to override permissions window

:star: WebClient: Added realtime update of progress for Job/Task just like Windows Client

:star: WebClient: Various improvements

:star: Client: Now single instance of Windows Client per session

:star: Client/Server: Added new window "Failed Jobs"


#### Bug Fixes


:white_check_mark: Server: Foreground execution->Fixed username enumeration dictionary bug

:white_check_mark: Server: Amazon EC2 Tasks->Upgrades libraries and fixed dependencies

:white_check_mark: Client/Server: SFTP->Fixed issue with servers returning full path for name

:white_check_mark: Server: MSMQ->Fixed issue with remote MSMQ servers

:white_check_mark: Server: SFTP->Fixed compatiblity issue with GlobalScape SFTP servers

:white_check_mark: Server: Cloud Task->Fixed issue with submitting bucket from Amazon Connection

:white_check_mark: Client/Server: Email Trigger->Fixed issue with storing regex option in attachment filter

:white_check_mark: WebAPI: Allowed setting local (external) ip to comply with web service standards

:white_check_mark: Server: Fixed issue with property "Allow local connections only"

:white_check_mark: Server: Task->Excel Set cell/Create->Fixed issue using Variables in password field

:white_check_mark: Server: Foreground execution->Fixed issue with login on computers with AD

:white_check_mark: Server: FTP/SFTP disconnect->Fixed issue with sometimes lingering connections when using multiple commands

:white_check_mark: Server: FTP/SFTP/SCP->Fixed duplicate file output on upload when using multiple commands

:white_check_mark: Client: Fixed Client status update issue for Job/Task row

:white_check_mark: API: Popup Task->Fixed crash when caption count differed from value count

:white_check_mark: Client: XML - Read node Task->Handled XPath query errors better to prevent crashes in Client

:white_check_mark: WebClient: Fixed issue with Download Step dialog OK button when no description was set

:white_check_mark: Server: Fixed crash related to logging missing Credential in Task

:white_check_mark: Client: Email Trigger->Fixed mail tree issue with multiple levels and public folders

:white_check_mark: API: Variables->Fixed problem resolving Variable {DATETIME()} in file filter

:white_check_mark: Client: Remote file dialog->Fixed general failure handling with inaccessible links

:white_check_mark: Server: Web macro Task->Fixed crash

:white_check_mark: Server: SharePoint - Upload Task->Fixed problem uploading from network share


### 8.2.3 [2016-12-16]

#### Bug Fixes


:white_check_mark: Client/Server: Variables->Fixed an issue with LastWorkDay Variable

:white_check_mark: Server: Variables->Fixed issue with PrevTask (8.2.2 issue)


### 8.2.2 [2016-12-12]

#### Features

:star: Client/Server: Server monitor window (beta)

:star: Client/Server: Audit log->Can now see changes in encrypted values (please revise permissions if needed)

:star: Client/Server: New Task->Concatenate PDF

:star: WebClient: Added auto connect option to client connection settings

:star: Client/Server: VisualCron Trigger->Now supporting "All Jobs" as option

:star: Client/Server: VisualCron Trigger->Now handling more events from remote server

:star: API: VisualCron Trigger->Now handling more events from remote server

:star: Client/Server: VisualCron Trigger->New events Startup complete and Service service stop


#### Bug Fixes


:white_check_mark: Server: Delete files Task: Now removing Read only flag before deletion to prevent failure

:white_check_mark: Server: Fixed a memory leak related to result of Task processed in loops

:white_check_mark: Server: SFTP Task->Fixed issue with setting encryption algorithm

:white_check_mark: Client: Handled error when backup folder cannot be reached

:white_check_mark: Client: Email Task->Fixed a resize issue which prevented some controls from showing

:white_check_mark: Server: Delete files Task->Fixed issue with very long directory paths

:white_check_mark: Server: Set Variable Task->Fixed issue setting Job Variable when running Task directly (compared to running Job)

:white_check_mark: Server: Archive - Decompress Task->Fixed Gz extraction issue

:white_check_mark: Server: SQL Task->Fixed issue with waiting for SQL Job completion

:white_check_mark: Server: SFTP->Fixed issue with Auto adjust ciphers on Server level

:white_check_mark: Server: Task logging->Fixed issue with logging the result

:white_check_mark: Server: Output->Fixed crash issue JSON output option

:white_check_mark: Client: Connection Explorer->Fixed Modified time sorting

:white_check_mark: Client: Fixed splash screen property for customization

:white_check_mark: WebClient: Fixed cookie storage of AD settings

:white_check_mark: WebClient: Fixed error popups on authentication failure

:white_check_mark: Client: Conditions->Fixed cloning issue which could cause edit rather than clone


### 8.2.1 [2016-11-01]

#### Features

:star: Client/Server: New Task: Check port

:star: Client/Server: Web macro Task->Various features and fixes

:star: Client/Server: Email Trigger->Added support for Exchange EWS and WebDAV

:star: Client/Server: SSRS Task->Added override option for report folder

:star: Client/Server: File filter->Added exclude folder(s) with file mask support

:star: Client/Server: SSIS Task->Support for SQL Server 2016


#### Bug Fixes


:white_check_mark: Server: Variables->Fixed negative workdays issue

:white_check_mark: Client/Server: Web macro Task->Memory optimizations

:white_check_mark: Client: Fixed issues with Task progress running after Task is complete

:white_check_mark: Server: Fixed output issue for Execute Task using option "CreateProcessAsUserW"

:white_check_mark: Server: Job/Task control Task->Fixed update issue of Job Variables for Run Task option

:white_check_mark: Server: Checksum Task->Fixed issues with very large files

:white_check_mark: Server: Email Trigger->Fixes for EWS protocols

:white_check_mark: Server: Fixed Folder filter issue for folder exclusion

:white_check_mark: Client: Flow->Fixed resize and limitations in retry values

:white_check_mark: Client: Fixed problem passing some Loop Variables to remote client

:white_check_mark: Server: Fixed Server IP Variable issue

:white_check_mark: Server: SSISDB Task->Included file that was needed in some cases in installation

:white_check_mark: Server: Print Task->Fixed an issue printing from the network

:white_check_mark: Server: Crystal reports->Fixed timeout issue (not terminating report)

:white_check_mark: Client: Wait Task->Fixed 100ms limit


### 8.2.0 [2016-09-16]

#### Features

:star: Client/Server: New Task: Web macro Task

:star: Client/Server: FTP Task->Added option 'Resume SSL session' in Connection

:star: Client/Server: RSS Event->Added support for security protocol version

:star: Client/Server: Event log Trigger->Now faster and support for sub folders

:star: Client/Server: Added new Trigger MSMQ

:star: Client/Server: Added support for sending MSMQ to non-transactional messages

:star: Client/Server: Added many Variables related to working days

:star: WebClient: Now saving other client settings like Job start/stop Notifications

:star: Server: Remote Execute Task->Added support for terminating running remote process


#### Bug Fixes


:white_check_mark: API/Server: Fixed a problem with Foreground execution when using no Credential

:white_check_mark: Server: HTTP Task->Fixed issue passing data when using PUT command

:white_check_mark: Server: File filter->Fixed a problem identifying size of +3 GB files

:white_check_mark: Client: Conditions->Fixed a problem cloning Conditions in the Client

:white_check_mark: Server: Fixed problem importing HTTP Task from older version

:white_check_mark: Client: Pushbullet->Handle null/empty device name

:white_check_mark: Server: SFTP/FTP/Cloud Tasks/Triggers->Fixed issue with using regex in 'include file name'

:white_check_mark: Server: Fixed problem loading ExitCodes which could result in Task failing in special scenarios

:white_check_mark: Server: Fixed problem with not disposing Client properly when using Execute Task with remote execution context. This could lead to memory issues on Server and excessive logging.

:white_check_mark: Server: Handled null error output issue in Notifications to prevent crash

:white_check_mark: Server: Fixed issue where the Set Variable Task could interrupt items in queue of the File Trigger

:white_check_mark: Server: Fixed issue in the Remote file Trigger which could prevent download from starting

:white_check_mark: Server: SQL Task->Fixed ODBC issues (refreshing stored procedures and executing) and Direct MySQL stored procedure execution issue

:white_check_mark: Server: Excel - Set Task->Fixed permission issue when writing to network share

:white_check_mark: Server: Remote File Trigger->Fixed memory leak issue

:white_check_mark: Server: AD - Create User Task->Fixed validation and set of CN property

:white_check_mark: Server: Execution Context->Fixed a problem finding the specified or any connection

:white_check_mark: Server: Conditions->Process condition - better handling of null module names

:white_check_mark: Client/Server: Assembly Task->Fixed a problem with reflecting dll's when extended debugging was on

:white_check_mark: Server: Cloud->Upload->Fixed error 'Sequence contains no elements'

:white_check_mark: Client: Permissions->Fixed problem adding Task when Job was overridden with specific permissions

:white_check_mark: Server: Email Trigger->Fixed a problem with saving multiple attachments with the same name

:white_check_mark: Client: Web client->Fixed a problem installing / detecting installation

:white_check_mark: WebClient: Fixed a problem saving client settings (servers)

:white_check_mark: WebClient: Fixed a problem displaying empty startup popups

:white_check_mark: Server: Task->Flow->Fixed 'On running longer than' issue

:white_check_mark: Server: Crystal Reports Task->Fixed dispose/memory cleanup issue

:white_check_mark: Server: Assembly Execute Task->Fixed recursive loop making reflection hanging


### 8.1.2 [2016-07-05]

#### Features

:star: Client/Server: Execute Task->Developed alternate execution method to handle error -1073741502

:star: Client/Server: Pushbullet->Enabled proxy in Connection settings

:star: Client/Server: SFTP/SSH Connection->Added support for overriding default Key Exchange Algorithm

:star: Client/Server: FTP Connection->Added support to select which SSL/TLS versions should be allowed

:star: Client/Server: New Task->Image - Convert

:star: Client/Server: Execute options moved to Credential (to control which API is used for execution)

:star: Client/Server: Variables->Added Math.Abs and Math.Round Variables

:star: Server: Email Trigger->Now supporting multiple attachment filters through semicolon separation

:star: Client/Server: HTTP Task->Added DELETE method option

:star: Client/Server: SysLog Task->Added "Application" and TCP/UDP option

:star: Client/Server: SSRS Task->Added Open Office XML format


#### Bug Fixes


:white_check_mark: Client: Handled problem related to AD user creation and deleting Credentials

:white_check_mark: Server: Run Job with options->Fixed if no first Task is selected

:white_check_mark: Server: Custom exit codes->Fixed a problem being overridden

:white_check_mark: Server: Fixed NonZeroExitCode override issue

:white_check_mark: Client: Variables->Removed warning when trying to update Variable (Variable name already exists)

:white_check_mark: Client: Variables->Fixed Variable translating problem with special chars like HTML

:white_check_mark: API: Fixed possible crash in Job/Task progress report

:white_check_mark: Server: Excel Convert Task->Fixed problem with overwriting existing files

:white_check_mark: Server: SSH Task->Fixed a problem with returning exit code

:white_check_mark: Server: SSRS Task->Fixed a problem with timing out after 100 seconds

:white_check_mark: Server: Connection Explorer->SSH terminal->Fixed issue with connecting to SSH server from remote client (when using public key authentication)

:white_check_mark: API: Fixed a problem inheriting timeout from Connection when using Execution context->Remote in Execute Task

:white_check_mark: Client/Server: Syslog Task - fixed missing/wrong facility codes

:white_check_mark: Server: Email Trigger->Fixed issue with TO/CC Variables (only got the last email if multiple)


### 8.1.1 [2016-05-24]

#### Features

:star: Client/Server: HTTP Task->Added support for Client certificates

:star: Client: Server settings->Improved loading speed

:star: Client: Connection explorer->Improved loading speed

:star: API: Added Server.ExportSettings method


#### Bug Fixes


:white_check_mark: Client/Server: SQL Task->Removed ;1 from ODBC stored procedures

:white_check_mark: Client/Server: Several improvements to Job/Task progress

:white_check_mark: Client/Server: Desktop Macro Task->Fixed various problems related to UAC

:white_check_mark: API: Foreground execution->Execute Task->Fixed a problem killing child processes

:white_check_mark: Server: SFTP->Download->Fixed a problem with preserving Modified date

:white_check_mark: Server: Fixed convert of (old) Tasks when importing

:white_check_mark: Client: Job/Task progress update fixes

:white_check_mark: Client/Server: Fixed a lot of issues concerning Foreground execution and auto logon

:white_check_mark: Server: Execute Task->Now keeping exit code even though "Non zero exit code" is checked (to suppress errors)

:white_check_mark: Server: Archive - Compress->Fixed overwrite/append issue

:white_check_mark: Server: Connections->SQL->Fixed problem with default value "Convert data types"

:white_check_mark: Server: Archive Decompress->Fixed file lock on archive if decompress failed because of broken archive

:white_check_mark: Client: Handled crash when trying to add same Job Variable key twice

:white_check_mark: Server: Conditions->Fixed a problem with setting and using UniqueProcessId

:white_check_mark: Server: AD - Create group Task->Fixed property issues

:white_check_mark: Server: SCP Task->Fixed a problem causing multiple SCP instances running in memory


### 8.1.0 [2016-05-03]

#### Features

:star: Client: Improved connection speed for Servers with many Jobs

:star: Client: Added timeout property to Server connection

:star: Client: Progress bar and execution time is now updating in real time (beta - can be turned off in File->Client settings)

:star: Client/Server: HTTP Task has been re-worked to handle Body and Headers better

:star: Client/Server: Cloud Tasks->Added Test filter and more remote file filters

:star: Client/Server: Remote File Trigger->Added optional download support

:star: Client/Server: Added new Task: Messaging->Pushbullet - Send message

:star: Client/Server: Added new Task: Messaging->Pushbullet - Send SMS

:star: Client/Server: Added new Task: Messaging->Pushbullet - Send file

:star: Client/Server: Added new Task: Messaging->Pushbullet - Upload file

:star: Client/Server: Added new Task: Messaging->Pushbullet - Send link

:star: Server: Increased logging for auto logon functionality

:star: Client:Server: FTP/SFTP Download Task->Added 3 options to better handle destination path in relation to source path

:star: Client/Server: Added new Task: SSRS Task (SQL Server Reporting Services)

:star: Client/Server: Added new Task: Image - Overlay image

:star: Client/Server: Added new Task: SAP - R/3 Job execute

:star: Server: Triggers->Now checking Time exceptions before polling for Trigger types: Remote file, Cloud file, Email and File (polling)

:star: Server: Mail Trigger->Now checking for not read email only when polling when Delete message on server or Leave message on server (mark as read is checked) is set


#### Bug Fixes


:white_check_mark: Server: Credential provider/Auto logon->Fixed issue with not identifying architecture correctly which could cause installation problems with Credential provider

:white_check_mark: Server: Better handling for situations when default user/group was deleted

:white_check_mark: Client: Fixed Test button issue in the Add/Edit Credential window

:white_check_mark: Server: Fixed a problem with PrevTask and Flow->On start

:white_check_mark: Server: Fixed issue with some email providers (like Gmail) in Email Task

:white_check_mark: Client/API: Fixed issue with import from Task Scheduler on Windows 10

:white_check_mark: Server: Fixed text delimiter issue in loops (where delimiter contained a split character)

:white_check_mark: Client/Server: Variables->Fixed a problem with displaying new lines in User Variables

:white_check_mark: Client: Popup Task->Fixed minor target selection problem

:white_check_mark: Server: Excel Convert Task->Fixed an issue with as specific document content

:white_check_mark: Server: File write Task->Fixed duplicate file name output (from 8.0.4)

:white_check_mark: API: Fixed a hang on fast connect/disconnect at Dispose

:white_check_mark: Client: Manage PGP Key rings->Fixed a problem with incompatiblity when exporting private keys

:white_check_mark: Server: Archive->Decompress-Gz->Fixed a problem with naming of extracted files (produced .tar file)

:white_check_mark: Server: Execute Task->Fixed a problem with not deleting a temp file causing empty temp file leftover

:white_check_mark: API: When creating new Task the default exit code is now set to prevent it from stopping at first Task

:white_check_mark: Client/Server: Fixed TLS 1.1 and 1.2 support issue for FTPS

:white_check_mark: Installer: Fixed a problem detecting previous version when installing

:white_check_mark: Client: Handled a problem resolving icons in Connection Explorer

:white_check_mark: Client: Fixed problem with CTRL+A in some text fields

:white_check_mark: Client: Credentials/Connections->Optimized combos for faster loading when having many Connections or Credentials

:white_check_mark: Client: Output window->Fixed search/replace enabling issue when switching output display type

:white_check_mark: Server: Remote File Trigger->Fixed a potential stack overflow crash


### 8.0.4 [2016-03-22]

#### Features

:star: Server: SQL Task->Support for loading images into column of type Image

:star: Client/Server: PowerShell Task->Added support for controlling in "On error" if error should be raised if PowerShell contains error output

:star: Client/Server: HTTP Task->Added support for custom headers

:star: Client/Server: SFTP/SSH->Added support for selecting which encryption algorithms to use

:star: Client/Server: SQL Task->Added support for listing stored procedures from Oracle

:star: WebClient: Added cookie support for remembering Connections

:star: Server: Execute/Kill Task->Now killing child processes

:star: Client/Server: Web service Task->Improved proxy implementation


#### Bug Fixes


:white_check_mark: Client/Server: Cloud Tasks->Many fixes to all new Cloud Tasks (Box, DropBox,Google Drive, OneDrive)

:white_check_mark: Client/Server: SCP Task->Mixed fixes

:white_check_mark: WebClient: Fixed communication issue in older IE versions

:white_check_mark: Client/Server: Popup Task->Fixed input parsing errors

:white_check_mark: Client/Server: Popup Task->Changed value sent back to output (no longer true (unless input value is empty) and only true values)

:white_check_mark: Client/Server: Cloud Tasks->Fixes for Azure and S3 Tasks

:white_check_mark: Client/Server: Popup Task->Checkbox->Selected property issue

:white_check_mark: Server: Job->Timeout->Consider timeout as error did not raise error properly


### 8.0.2 [2016-02-22]

#### Features

:star: Server: FTP/SFTP/SSH - upgraded components

:star: Server: FTP/SFTP/Cloud - added folder/file browsers to Tasks

:star: Server: PowerShell Task->Added ability to control port for remote execution

:star: Server: Execute Task->Now appending output/error if using custom exit code collection

:star: Server: FTP/SFTP Task->Added SCP support

:star: Server: PDF Tasks->Added Task Add PDF Footer/Header


#### Bug Fixes


:white_check_mark: Server: Fixed general race condition/time out problems during high load

:white_check_mark: Client: Update->Fixed downloaded file name to real version name

:white_check_mark: Server: Job Variables->Fixed a problem updating a Job Variable in some scenarios

:white_check_mark: Server: Archive - Decompress->Fixed issue that could occur on some systems when extracting to UNC path

:white_check_mark: Server: Fixed build issue for 32 bit version of SSIS, PowerShell, Office macro and UnmanagedExecute Tasks

:white_check_mark: Server: Variables->Fixed workaround for Austrian WEEK Variable bug

:white_check_mark: Client: Main grid->Fixed a problem with updating some menu items

:white_check_mark: Server: PowerShell Task->Fixed Task error result issue

:white_check_mark: Server: Task Flow->Fixed a problem deactivating Task

:white_check_mark: Server: FTP->Fixed date parsing errors for custom parsing of server system of type: UNIXTypeL8

:white_check_mark: Server: SFTP->Fixed duplicate connection issue

:white_check_mark: Server: File Trigger->Fixed false/positive popup issue when editing reconnected file trigger

:white_check_mark: Client: Fixed main window startup location and size when starting on a smaller screen than last saved

:white_check_mark: Server: File->Delete Task: Added a retry for the false/positive error "The operation completed successfully"

:white_check_mark: Client/Server: Cloud Tasks->Fixed delete source file after download

:white_check_mark: Server: Cloud Tasks->Fixed output for download in various cloud services

:white_check_mark: Server: Fixed issue with Variables in Crystal reports Task


### 8.0.1 [2016-01-11]

#### Features

:star: Server: Azure->Start VM Task added

:star: Server: Azure->Stop VM Task added

:star: Server: Set Job Variable->Added output

:star: Server: SSH Task->Now stopping Task gracefully with output if Stop Job/Task is called


#### Bug Fixes


:white_check_mark: Server: SQL Task->Fixed issue with refreshing stored procedures from Connections with Variables

:white_check_mark: API: Fixed a communication issue

:white_check_mark: Server: Assembly Execute Task->Fixed a problem with the Task not marked as failed when assembly failed

:white_check_mark: Server: Fixed issue with single file recovery that could lead to resetting users on Server

:white_check_mark: Server: Handled issue with local or remote server not started dependency

:white_check_mark: Server: Archive - Decompress->Fixed issue with extraction of very large zip files

:white_check_mark: Server: Offline activation->Used new cryptoprovider to handler FIPS validation error

:white_check_mark: Server: Variables->Fixed an issue with using OnComplete PrevTask Variables in Flow/Notifications

:white_check_mark: Client/Server: Cloud->Amazon S3->Fixed support for different regions

:white_check_mark: Web Client->Fixed an issue with AD-support

:white_check_mark: Server: Fixed a memory leak in Job/Task control Task

:white_check_mark: Server: SharePoint->Upload file->Fixed issue related to local SharePoint installation

:white_check_mark: Server: Set Job Variable->Fixed cloning issue (so that it points to current Job)

:white_check_mark: Server: SSIS DB Task->Fixed error handling (previously not marked as failed when failed)

:white_check_mark: Client: Grid filter->Fixed a problem with "Clear filter" when selected "Running Task"

:white_check_mark: Client: Email Trigger->Fixed a problem saving file mask for attachments

:white_check_mark: Web Client: Various fixes related to interface

:white_check_mark: Server: Fixed a bug related to Loop and inactive Task

:white_check_mark: Server: Excel Set Task->Now creates worksheet if not existing

:white_check_mark: Server: Flow->Fixed a problem deactivating Job in Job Flow

:white_check_mark: Server: Variable->Fixed support for Job Variables in Date filter


### 8.0.0 [2015-11-24]

#### Features

:star: Client: Cloud->Added Dropbox and Box support to FTP Explorer

:star: Server: PowerShell Task->Now capturing "throw" exit codes

:star: Server: Excel - Set cell->Now it supports new (non existent) files for creation

:star: Client/Server: Import settings now supports import of older files with old Notifications


#### Bug Fixes


:white_check_mark: Server: Export settings->Fixed a problem with selective export of Exit code collections

:white_check_mark: Server: Assembly Execute Task->Fixed output issue

:white_check_mark: Server: FTP->Fixed a code page issue

:white_check_mark: Server: SharePoint->Fixed 405 error issue when uploading files

:white_check_mark: Client/Server: Trigger->Performance counter->Fixed a cloning issue

:white_check_mark: Client: SQL Explorer->Now supporting Variables in connection strings

:white_check_mark: Client: FTP->List files->Fixed a cloning issue

:white_check_mark: Server: Variables->Fixed an issue identifying Variables when using Conditions on Tasks

:white_check_mark: Client/Server: DTS Task->Fixed issue with trusted connection

:white_check_mark: Server: FTP/SFTP/SSH Task->Fixed memory leak

:white_check_mark: Server: File Trigger->Improved detection of folder not available

:white_check_mark: Server: IM->Updated expired url for Yahoo messaging

:white_check_mark: Server: Login->Fixed a login problem related to using AD and a Credential


### 7.7.8 [2015-11-02]

#### Features

:star: Client/Server: Cloud->Google Drive support

:star: Client/Server: HTTP Task->Added SSL/TLS version support

:star: Client/Server: Email Trigger->Added attachment filter settings

:star: Client/Server: SMTP->Added SASL mechanism support for controlling DIGEST-MD5 and NTLM for older email servers

:star: Client/Server: Added Set Job Variable Task

:star: Client/Server: Cloud Tasks->First beta of OneDrive Tasks

:star: Client/Server: Remote Execute->Added fallback method for buggy Windows servers


#### Bug Fixes


:white_check_mark: Client: Main grid->Fixed issue saving some columns permanently

:white_check_mark: Server: Performance counter Trigger->Fixed possible memory leak

:white_check_mark: Client/Server: Dynamics CRM->Update entity fixed problem displaying attribute values

:white_check_mark: Server: Web Client->Fixed an issue with folder extraction

:white_check_mark: Server: Cloud->Azure->Fixed upload issue

:white_check_mark: Client: Output/Test->Fixed an issue clicking on output urls with blank space in it

:white_check_mark: Server: SSH Task->Fixed an issue that no error was raised upon Connection timeout

:white_check_mark: Client: Connections->Removed duplicate confirmation

:white_check_mark: Client: Archive - Decompress->Fixed an issue decompressing 7z/zip files

:white_check_mark: WebClient: Various fixes and features

:white_check_mark: Server: File Trigger->Fixed problem with not retrying properly after error


### 7.7.7 [2015-10-08]

#### Features

:star: Client/Server: Connections->SFTP->Brute force connection test tool

:star: Client/Server: Connections->SFTP, Cloud, SSH->Now loading public key into connection object which lets you use the Explorer in the Client (remote connect)


#### Bug Fixes


:white_check_mark: Server: Archive - Compress->Fixed an issue producing file according to zip standard

:white_check_mark: Server: File Trigger (use polling)->Fixed a problem with a scenario that multiple threads could be created (when file trigger path failed)

:white_check_mark: Client/Server: Dynamics CRM Tasks->Various fixes

:white_check_mark: Server: HTTP Task->Handled error "Could not create SSL/TLS secure channel" that could occur on some servers

:white_check_mark: Server: Web service API->Fixed issue with serialization


### 7.7.6 [2015-09-29]

#### Features

:star: Client/Server: Better handling for FTP server of type V5R2M0

:star: Client/Server: Excel Set cell->Added option "Remove password when saving"

:star: Client: Permissions->Jobs and Tasks can now be opened with Read permission - still Add/Edit permission required to save

:star: Client/Server: Added MSMQ - Delete message(s) Task

:star: Client/Server: Added support for mainframe FTP server V7R2M0

:star: Server: Credential provider->Better logging and optimizations for Foreground execution


#### Bug Fixes


:white_check_mark: Server: Amazon S3->Fixed general issue about downloading sub items

:white_check_mark: Server: Amazon S3->Fixed issue with preserving modified/creation dates on min value dates

:white_check_mark: Server: Variables->Fixed a direct Id issue

:white_check_mark: Server: FTP->Download->Fixed a issue that could cause an error when using option "Delete source file after download"

:white_check_mark: Server: Dynamics CRM->Update entity->Fixed a problem using Variables

:white_check_mark: Server: Archive->Compress->Fixed Tar+Gzip issue

:white_check_mark: Server: Foreground execution->Fixed SID identifier for better matching of username

:white_check_mark: Server: Dynamics CRM->Fixed entity listing issues

:white_check_mark: Client: Remote explorer->Fixed handling of listing directories with many files (crash)

:white_check_mark: Client: Fixed next run sorting issue related to inactive Jobs

:white_check_mark: Server: Cleaned up output for PowerShell, Office Macro and .NET Execute Tasks

:white_check_mark: Server: File filter->Fixed issue using OR operator on file size


### 7.7.5 [2015-09-01]

#### Features

:star: Client/Server: Added 'On running longer than' option in Flow - the ability to control if a Task or Job runs longer than expected

:star: Client/Server: Added result Variables for File rename Task

:star: Client: XendApp Task->Added proxy settings


#### Bug Fixes


:white_check_mark: Server: File filter->Fixed an issue concerning using no date filter and OR setting on date

:white_check_mark: Server: Excel - Recalculate->Fixes issue with corrupt file creation

:white_check_mark: Server: Instant messaging->Fixed AIM thread issue

:white_check_mark: Server: HTTP Task->Now handling unhandled error override in On error tab

:white_check_mark: Server: FTP Task->Fixed issue with folder separator for some older FTP systems

:white_check_mark: Server: Variables->Fixed result Variable issue for Tasks in loops

:white_check_mark: Server: Exit codes->Fixed result setting for exit codes not found

:white_check_mark: Client: Time exceptions->Fixed issue with Time exceptions selection


### 7.7.4 [2015-08-14]

#### Features

:star: WebClient: Various improvements

:star: Variables->Various improvements to the Variables window and SQL Trigger Variables

:star: Settings->Added option to enable/disable UAC


#### Bug Fixes


:white_check_mark: Server: Settings->Web API->Fixed a link display issue (missing ampersand)

:white_check_mark: Server: Fixed a memory leak related to Put Job in queue = false

:white_check_mark: Server: Office Macro->Now creating needed folders at startup to fix issue with error 0x800AC472

:white_check_mark: Server: Fixed a problem with using some output Variables in long running Jobs

:white_check_mark: Server: Excel - Convert Task->Fixed issue converting double to date

:white_check_mark: Server: FTP Upload->Fixed an output issue where not the full path were displayed when overwriting existing file

:white_check_mark: Server: Remote File Trigger->Fixed a problem when the Job was deleted and Trigger still polling

:white_check_mark: Server: Remote File filter (test)->Fixed a problem with "Larger than size"

:white_check_mark: Server: FTP Task->Fixed Download/List/Rename/Delete/CopyMove commands to comply with new remote file filter

:white_check_mark: Server: Variables->Fixed a direct Id reference problem with Tasks

:white_check_mark: Client: Permissions->Fixed cloning issue of AD user

:white_check_mark: Client/Server: Web service Task->Fixed complex parameter issue

:white_check_mark: WebClient: Fixed installation issue (0x80070021)

:white_check_mark: Client: XML->Read node Task->Fixed issue with displaying manually added namespaces


### 7.7.3 [2015-07-22]

#### Bug Fixes


:white_check_mark: Server: File Trigger(polling)->Fixed a problem with retry settings

:white_check_mark: Server: Dynamics CRM->Fixed a problem with suppling Entity Id

:white_check_mark: Server: Remote file Trigger->Fixed issue with folder Variable

:white_check_mark: Server: Fixed a problem with Job queuing synchronization when Triggering occured in a fast rate

:white_check_mark: Server: Email Trigger->Fixed a problem with using no casesensitve string comparison

:white_check_mark: Server: Time exceptions->Fixed a problem selecting Time exceptions in Job add/edit window


### 7.7.2 [2015-07-10]

#### Features

:star: Client: FTP Connection->Did some improvements to Brute force Connection test

:star: WebClient: Various improvements


#### Bug Fixes


:white_check_mark: Server: Fixed a memory leak related to Conditions

:white_check_mark: Server: Dynamics CRM->Delete attachments->Fixed issue deleting some object types

:white_check_mark: Server: Calendar->Removed a handler leak

:white_check_mark: Client: Conditions->Actions->Fixed column that should be hidden (Task order)

:white_check_mark: Client: Flow->Fixed empty Task name when cloning a Job

:white_check_mark: Client: Explorer->SFTP->Fixed issue with AutoAdjustMACAlgorithm

:white_check_mark: Server: Service Trigger->Handled null values better

:white_check_mark: Server: SFTP Rename->Fixed a problem with source folder property


### 7.7.1 [2015-07-02]

#### Features

:star: Client/Server: SQL Task->Optional data type conversion

:star: WebClient: SQL Various improvements


#### Bug Fixes


:white_check_mark: Client: File filter issue (popup error when opening Task)

:white_check_mark: Server: Better handling of adding default flows when flow is missing

:white_check_mark: Client: Fixed a problem saving output settings of various Tasks (when output tab is clicked on directly)

:white_check_mark: Server: FTP Task->SFTP->Fixed a problem moving a file if the file was already there (and should be overwritten)


### 7.7.0 [2015-06-24]

#### Features

:star: Server: Job/Task control Task->Added option "Update Job Variables" which updates the existing Job Variables (of target Job) if set

:star: Client/Server: Added Task "Dynamics CRM - Delete attachment(s)"

:star: Client/Server: New Web API for accessing VisualCron

:star: WebClient: Group support and real time Job log


#### Bug Fixes


:white_check_mark: Server: Excel - Create Task->Fixed a problem with using no text qualifier (empty string)

:white_check_mark: Server: Job/Task control Task->Fixed issue with Jobs being queued (Variables and other Job parameters)

:white_check_mark: Server: Excel - Get->Fixed a problem parsing dates

:white_check_mark: Server: Web service Task->Fixed issue reloading assembly (serialization error) resulting in Server disconnect in Client

:white_check_mark: Server: Test connection->Fixed a bug where Oracle connections were lingering

:white_check_mark: Client/Server: Variables->Fixed a problem using alternate parameters like this: {FILE(@Content@c:\textfile.txt)}

:white_check_mark: WebClient: Fixed an issue with installing on IIS in Windows 2008

:white_check_mark: Server: Remote file filter->Fixed a Sort + Limit bug - names were previously limited then sorted instead of sorted then limited

:white_check_mark: Server: Excel - Create->Fixed a problem accessing files on network shares

:white_check_mark: Server: Fixed a memory leak in communication object (WCF)

:white_check_mark: Server: Now stopping Job if a Task produces and exit code that is not found in list

:white_check_mark: Client: SQL Task->Fixed sorting of stored procedures

:white_check_mark: Server: Export settings Task->Fixed a bug which could result in Connections not being exported

:white_check_mark: Server: Variables->String.TrimStart->Now behaving like TrimEnd (exact match on start needed)

:white_check_mark: Client: Variables->Fixed problems with methods using Credential (Credential not found error)

:white_check_mark: Server: SQL Task->Changed how parameters are converted to the correct type (required for some databases) when using ODBC/OLEDB


### 7.6.6 [2015-05-28]

#### Features

:star: Web Client: AD login support added

:star: Tray Client: Updated interface

:star: Server/API: Exit codes->Improved handling of Windows default exit codes

:star: Client->File and hyperlink support in output and filter result text boxes

:star: Client->General interface updates

:star: Added Task "MSMQ - Send message"


#### Bug Fixes


:white_check_mark: Client: Task scheduler->Import: Minor fixes concerning converting start time

:white_check_mark: Install: Web Client->Dll reference fixes for Windows 2012R2

:white_check_mark: Client: FTP Task->Deleting commands in grid now updates order for remaining commands

:white_check_mark: Server: Settings->Fixed real time update of database when output folder is changing

:white_check_mark: Server: Now cleaning up VisualCron temp folder more often

:white_check_mark: Server: File filter->Now handling names containing character #

:white_check_mark: Client/Server: Fixed a problem with using Job Variables and other in date Variables sections like filters

:white_check_mark: Server: Fixed a memory cleanup bug (TaskProcesses)

:white_check_mark: Client: Fixed a memory cleanup bug related to FTP Explorer window

:white_check_mark: Client: Fixed a problem filling signers in PGP encrypt Task

:white_check_mark: Client: Fixed a problem with Import settings window concerning Exit codes and selection of specific nodes

:white_check_mark: Server: Email Trigger->If Move + Delete is used then Move command is used instead of Copy + Delete

:white_check_mark: Client: Credentials->Prevented a hang issue when adding/updating Credentials sometimes

:white_check_mark: Server: SSH Task->Fixed a problem sending multiple texts commands in one Task

:white_check_mark: Client: Popup Task->Fixed a bug previewing Popup when no Input were used

:white_check_mark: Server: FTP Task->Upload->Fixed a problem with uploading when relative path was exact as upload destination path

:white_check_mark: Server: Dynamics CRM->Fixed issue resolving entity id:s

:white_check_mark: Server: Fixed a problem with reference to PrevTask when using Notifications with high rate of execution

:white_check_mark: Client: SQL Explorer->Fixed Oracle issues

:white_check_mark: Server: Changed flow behavior when no matching flow is found. Now creating default flows and update Task

:white_check_mark: Server: Excel - Create Task->Handled split of content better that has the separator inside text qualifier

:white_check_mark: Server: Popup Task->Fixed dialog result handling


### 7.6.5 [2015-05-01]

#### Notes

:memo: All: New protocol version (7.6.5) for communication. Requires Server and Client version to be the same.


#### Features

:star: Client/Server: Introducing the first version of the Web Client - installation through Server settings dialog

:star: Client/Server: Improved communication security between Client and Server

:star: Client/Server: FTP/SFTP->Added result filter (sorting and limit)

:star: Client: Output window->Added line numbers, search/replace and goto line features

:star: Client/Server: Added support for using Variables in Size in Remote file filter

:star: Client/Server: Assembly Execute Task->Added support for loading configuration settings from dll/exe

:star: Server: Excel - Convert->Better treatment and formatting of dates when converting to text files

:star: Client: Settings->Added option to turn off/on Tray client startup at start

:star: Client/Server: Added support for importing Tasks from Windows Task Scheduler

:star: Client/Server: Added new Trigger "Session change" which can detect logon, logoff, lock etc from any or specified user

:star: Client/Server: Popup Task->Now supporting Variables for dynamic controls


#### Bug Fixes


:white_check_mark: Client: Trial registration->Handled an error

:white_check_mark: Client: File filter->Increased timeout for Testing file filter

:white_check_mark: Client: Main grid->Fixed a problem with updating Job count when auto connecting to multiple servers

:white_check_mark: VCCommand: Fixed build issue with VCCommand.exe

:white_check_mark: Client/Server: Fixed issue with popup when connecting to multiple servers at once and one is off

:white_check_mark: Client/Server: Fixed communication issue when properties where mismatching between Client and Server

:white_check_mark: Client/Server: Fixed communication issue related to disconnect

:white_check_mark: Server: Permissions->Now deleting unused temp groups at startup

:white_check_mark: Server: Folder - List->Fixed folder filter to include first level sub folders as default

:white_check_mark: Server: XML Read node->Fixed an issue related to creating duplicate namespaces when editing namespace


### 7.6.4 [2015-04-08]

#### Features

:star: Client: Oracle Connection->Added unicode support and Service Name connection string parameter

:star: Client/Server: SFTP Tasks->Fixed support for treating unknown types as files for testing in remote file filter and List files command

:star: Client: Main grid->Job count is now reflecting grid filter and hidden Jobs


#### Bug Fixes


:white_check_mark: API: Removed a NewtonSoft reference

:white_check_mark: Server: FTP Task->Fixed parsing issue for FTP server of type: V6R1M0

:white_check_mark: Server: Copy files Task->Better handling of long file names

:white_check_mark: Server: SFTP Explorer/Task->Now using local time instead of UTC

:white_check_mark: Client: Event log - Read Task->Fixed problem with saving remote host name

:white_check_mark: Server: SQL Task->Fixed Unicode issue for Oracle connections without direct connection

:white_check_mark: Client: Fixed multiple, same time, connection issue "Object reference error"

:white_check_mark: Server: Flow->Fixed a bug that could trigger other flows on start

:white_check_mark: VCTray: Connection->Fixed "too often ping issue"

:white_check_mark: Client: GridFilter->Fixed "Clear filter" issue

:white_check_mark: Server: Foreground execution->Better logging, testing and minor bug fixes

:white_check_mark: Client: Remote folder dialog->Fixed a crash concerning drawing icons

:white_check_mark: Client/Server: Job/Task control Task->Fixed various issues concerning setting Job Variables


### 7.6.3 [2015-03-19]

#### Features

:star: Client/Server: Assembly execute Task->Added "local execution" option

:star: Client/Server: Added permissions for Object finder


#### Bug Fixes


:white_check_mark: Server: Print Task->Handled an error not supporting orientation setting

:white_check_mark: Server: Excel - Create Task->Fixed two bugs concerning duplicate row creation and fields containing split character

:white_check_mark: Server: Fixed a bug concerning Job running status when not using "Run Tasks in order"


### 7.6.2 [2015-03-17]

#### Notes

:memo: All: New protocol version (7.6.2) for communication. Requires Server and Client version to be the same.


#### Features

:star: Client/Server: SMTP Task->Added support for setting supported SSL/TLS versions

:star: Client/Server: XML Read Node Task->Added support for code page

:star: Client/Server: Add List permission to prevent users from seeing certain Jobs


#### Bug Fixes


:white_check_mark: Client/API: Assembly Execute Task->Increased timeout for assembly reflection

:white_check_mark: Client/API: Assembly Execute Task->Increased quota for array length

:white_check_mark: Client: SQL Connection->Fixed issue with testing Connection that could prevent later saving of the Connection

:white_check_mark: Client: SQL Connection->Fixed testing issue for Oracle

:white_check_mark: API: Processes->Fixed a bug that could result in problems listing running processes

:white_check_mark: Client: Login->Fixed a problem pasting password into password field at login phase

:white_check_mark: Server: Excel Convert->Fixed a problem handling empty rows

:white_check_mark: Client: Grid filter->Improved sorting & expansion of rows

:white_check_mark: Client: PowerShell Task->Fixed a problem selecting Authentication type

:white_check_mark: API: Popup Tasks and more->Fixed a problem resolving Job/loop Variables

:white_check_mark: Client/Server: Fixed a hang when trying to open the log window while having extended debugging on


### 7.6.1 [2015-03-02]

#### Features

:star: Client: Grid filter->Now hiding parent row if no object is found in child row

:star: Server: SSIS Tasks->Added more output from package execution

:star: Client/Server/API: Added csv import functionality for Time exceptions

:star: Client: Main grid->Added "Conditions icon" for Jobs and Tasks containing one Condition or more

:star: Client: Main grid->Added grid filter for Task type

:star: Client: Main grid->Added grid filter for Active/Inactive Job or Task

:star: Client: Main grid->Added support for combining grid filters

:star: Client: PGP->Sub keys can now be deleted from parent key


#### Bug Fixes


:white_check_mark: Server: Web service Task->Fixed problems viewing XML output in output window (XML)

:white_check_mark: Client: Service Tasks->Now handling Variables in host name field

:white_check_mark: Server: Permissions->Handled AD user import better from older versions

:white_check_mark: API: Merged file CommServer.dll into VisualCronAPI.dll

:white_check_mark: Client/Server: Solved some communication issues on W2003 servers

:white_check_mark: Server: Archive decompress->Handled an error disposing an object

:white_check_mark: Server: Variables->Handled a problem with user variables starting with a non-letter character

:white_check_mark: Server: Jobs->Fixed a problem with loading/saving Job settings for Jobs containing Service event Triggers

:white_check_mark: Client/API: Job/Task control Task->Fixed a timeout problem

:white_check_mark: Client/Server: Fixed a communication problem leading to Client crash


### 7.6.0 [2015-02-13]

#### Notes

:memo: All: New protocol version (7.5.2) for communication. Requires Server and Client version to be the same.


#### Features

:star: Server: HTTP Task->Now resolving "Content-Disposition" to get name of file attachments downloaded

:star: API/Client/Server: Changed the way VisualCron communicates to improve speed and stability

:star: Client/Server: Connections->SQL Connection test is now performed from Server instead of Client giving more exact result (also with Credential option)

:star: Client/Server: Connections->WebDAV->Added support for SSL/TLS version support

:star: Client/Server: FTP/SFTP->Download->Added support for replacing unsupported Windows characters

:star: Client/Server: Variables->Any non-letter character can be used as parameter split character. Start by using the first character in argument that you want to use, for example: {FILE(@Content@c:\textfile.txt)}

:star: Client/Server: Web service Task->Added custom endpoint option to override any existing endpoint


#### Bug Fixes


:white_check_mark: Server: PowerShell Task->Handling large output error "The maximum string content length quota (8192) has been exceeded while reading XML data."

:white_check_mark: Client: Import settings->Fixed a problem when trying to import all settings when only some settings selected

:white_check_mark: Client: FTP Explorer->Fixed handling of Binary/ASCII setting

:white_check_mark: Client: Credentials->Fixed alphabetical sorting in combos

:white_check_mark: Client: Grid filter->Handled a problem with backslashes in the grid filter

:white_check_mark: Server: Excel - Create Task->Fixed a problem with creating password encrypted file

:white_check_mark: Server: Archive - Decompress->Fixed a memory leak while extracting

:white_check_mark: API/Client/Server: Fixed a problem calculating next run of Trigger on invalid dates

:white_check_mark: Server: Web service Task->Fixed a problem executing certain web services

:white_check_mark: Server: PowerShell Task->Fixed a problem with Variables not resolving in parameters

:white_check_mark: Client: Variables->Fixed a problem changing name of cloned Variable

:white_check_mark: Server: Delete files Task->Fixed a problem with deleting empty sub folders

:white_check_mark: API: AD->Timeout increased on AD queries

:white_check_mark: Server: Job report Task->Fixed encoding and various issues

:white_check_mark: Server: SSISDB Task->Now translating Connection string Variables properly


### 7.5.1 [2014-11-17]

#### Features

:star: Server: Notifications->Can now access in-loop Variables

:star: Server: Export settings->Added Deselect all button

:star: Server: SQL Task->Now including SqlException data in error output


#### Bug Fixes


:white_check_mark: Server: Logon->Fixed a problem which could cause some old AD groups not to convert to new logon type

:white_check_mark: Server: General file search->Handled problems with abnormal dates in files

:white_check_mark: Server: FTP Task->Copy/Move->Fixed a problem overwriting files

:white_check_mark: Server: FTP Task->Fixed another convert old settings problems (from version 6 to 7)

:white_check_mark: Client: Variables->Fixed unwanted User Variable window when clicking on scrollbar

:white_check_mark: Server: PowerShell Task->Handling error "Mixed mode assembly is built against version 'v2.0.50727' of the runtime and cannot be loaded in the 4.0 runtime without additional configuration information."


### 7.5.0 [2014-11-05]

#### Notes

:memo: All: New protocol version (7.5.0) for communication. Requires Server and Client version to be the same.

:memo: All: If you get problems with AD logon type then please logon with normal VC user and delete the AD user and add it again - or use the new AD group features


#### Features

:star: All: New logo and graphical profile

:star: Client: Added Job count to main window

:star: Client/API: Added more advanced and selective import of settings

:star: Client/Server: Popup Task->Now you can send to executing user

:star: Client/Server: Email Trigger->Optionally create folder tree for emails (and attachments)

:star: Client/Server: Email Trigger->Added case sensitive option

:star: Client/Server: File filter->Added result limit

:star: Client/Server: File filter->Added result sorting

:star: Client/Server: File filter->Added support for Variables in file size filter

:star: Client/Server: PowerShell Task->Added x86 execution mode

:star: Client/Server: Excel - Get cell->Added password support

:star: Client/Server: Excel - Get cell->Added support for parsing dates

:star: Client/Server: Excel - Set cell->Added support for old Excel formats

:star: Client/Server: Excel - Create->Added support for old Excel formats

:star: Client/Server: Rename methods in various Tasks->Added option to choose between VisualCron and REN implementation in Server settings

:star: Client/Server: Added support for AD group logon with options to assign specific VisualCron permissions group

:star: Client/Server: Web service Task->Added client Certificate support


#### Bug Fixes


:white_check_mark: Server: Delete files Task->Fixed a false positive error that was not raised properly when a file could not be deleted

:white_check_mark: Server: Email Trigger->Fixed an issue with not firing when using Timeout option on Trigger.

:white_check_mark: Server: SharePoint->Update list item->Fixed Variable resolving issue

:white_check_mark: Server: FTP Task->Fixed a problem overriding Transfer type

:white_check_mark: Server: Settings import->Fixed issue with importing Exit code collections

:white_check_mark: Server: SSISDB Task->Added more debugging and error handling

:white_check_mark: Server: HTTP Task->Fixed parameter type handling for PUT method

:white_check_mark: Server: Minor adjustments in Rename functionality

:white_check_mark: Client: PGP Encrypt->Removed the need for setting password when using conventional encryption

:white_check_mark: Server: Handled a crash related to Flow and Notifications

:white_check_mark: Server: PowerShell Task->Improved exit code and error handling

:white_check_mark: Server: Excel Create/Set cell Tasks->Fixed a problem with row splitting

:white_check_mark: Client: Excel Create->Fixed a problem with validating form

:white_check_mark: Client/Server: Variables->Now handle more complex input (for example JSON which could break the Variable parser)

:white_check_mark: Server: Fixed a potential crash that could occur when handling Variables at execution

:white_check_mark: Server: PowerShell Task->Fixed issue with x86 execution and execution from file issue

:white_check_mark: Server: Fixed general crash issue related to Flow

:white_check_mark: Client: FTP Task->Fixed display issue of Connection used

:white_check_mark: Server: Archive Decompress Task->Fixed a problem with destination folder and error handling

:white_check_mark: Server: FTP Task->Download->Fixed a problem converting old settings which could lead to a reset in Remote file filter settings

:white_check_mark: Server: Assembly execute Task->Fixed a problem reflecting x86 assemblies

:white_check_mark: Server: SQL Task->Handled an error in SQL Job execution related to null messages in result at completion


### 7.2.1 [2014-09-19]

#### Features

:star: Client/Server: SSIS Task->Added support for MSSQL 2014 SSIS package execution

:star: Client/Server: Added Task->Amazon EC2 - Create snapshot

:star: Client/Server: Added Task->Amazon EC2 - List snapshots

:star: Client/Server: Added Task->Amazon EC2 - Delete snapshot

:star: Client/Server: Added Task->Amazon EC2 - List addresses

:star: Client/Server: Added Task->Amazon EC2 - List key pairs

:star: Client/Server: Added Task->Amazon EC2 - List security groups

:star: Client/Server: Added Task->Amazon EC2 - List volumes

:star: Client/Server: Added Task->Amazon EC2 - Reboot instance

:star: Client/Server: Added Task->Amazon EC2 - Start instance

:star: Client/Server: Added Task->Amazon EC2 - Stop instance

:star: Client/Server: Added Task->Amazon EC2 - Terminate instance

:star: Client/Server: Added Task->Amazon EC2 - List instances


#### Bug Fixes


:white_check_mark: Client/Server: Popup Task->Fixed input handling problem with radio boxes

:white_check_mark: Server: Fixed a problem with renaming strings which could come up in different Task types

:white_check_mark: Server: Dynamics CRM general->Fixed a general returning description for some entity types

:white_check_mark: API: Fixed issue with Adding/Updating Job Variables

:white_check_mark: Client: Loops->Fixed resizing error in window

:white_check_mark: Server: Email Task/Notification->Fixed error "User authentication failed: No SASL mechanisms supported by both the client and the server (error code is 0)"

:white_check_mark: Client: Desktop Macro Task->Fixed a problem which could occur when saving the macro

:white_check_mark: Server: Fixed a small database cleanup issue

:white_check_mark: Server: FTP Task->Fixed Copy/Move files sub folders issue


### 7.2.0 [2014-08-29]

#### Features

:star: Client/Server: Loop->Added option to start from a specific row when using For each (to exclude headers etc)

:star: API: Loop->Added methods for adding and deleting Job Variables

:star: Client/Server: SQL Task/Trigger: Now prefixing with schema in front of stored procedures

:star: Client: .NET code Task->Added option to add direct file reference


#### Bug Fixes


:white_check_mark: Server->Crystal reports Task->Fixed a problem using certain Variables in this Task

:white_check_mark: Server->Hyper-V List Task->Fixed an issue where a property name could be different in some systems resulting in SID instead of Name is returned - further fixes

:white_check_mark: Client->Manage PGP key rings->Fixed issue when importing private key only

:white_check_mark: Server->WebDAV Tasks->Fixed an issue transferring files to and from some WebDAV servers

:white_check_mark: Server->Task Flow->Fixed issue with On start - Run Job

:white_check_mark: Server->PowerShell Task->Fixed an issue that could cause problems with blank spaces in paths to scripts

:white_check_mark: Client->.NET code Task->Handled test Run of scripts that uses the API better so they do not conflict with the Client

:white_check_mark: Server->SQL Task->Removed an extra newline that was added accidentally with the support for multiple query result

:white_check_mark: Server->Office macro->Fixed a false postive error when no macro file was found

:white_check_mark: Client->FTP Tasks->Fixed issue referencing to the right Job Variable in Variables window

:white_check_mark: Server->Database->Fixed minor issues cleaning up local database

:white_check_mark: Server->File Trigger->Added different Reconnect handling in case of connection problems to avoid impersonation errors

:white_check_mark: Server->Variables->Fixed a problem with TrimStart and TrimEnd function

:white_check_mark: Client->DTS Task->Fixed problem with updating parameters in the UI

:white_check_mark: Server->SSISDB Task->Fixed a problem returning failed result

:white_check_mark: Server->Checksum Task->Fixed a problem with zeroes in the checksum

:white_check_mark: Server->Crystal reports Task->Fixed a problem cloning parameters

:white_check_mark: Server->SSISDB Task and more->Fixed a problem with timeout of connection generating error

:white_check_mark: Server->Microsoft CRM Task->Fixed an issue filling some entity ids

:white_check_mark: Server->Running processes->Fixed a rounding issue when calculating number of hours


### 7.1.9 [2014-07-15]

#### Features

:star: Server->SQL Task->Now including output from multiple tables

:star: Client/Server->Added Run Job X with options right click functionality

:star: Client/Server->PowerShell Task->Modified to be more independent and support impersonation better

:star: Client/Server->VisualCron Trigger->Created new types for just "Inactivated Trigger" and "Inactivated by error"

:star: Client/Server->Job/Task control Task->Added support for all actions in remote mode


#### Bug Fixes


:white_check_mark: Server->Job Variables->Fixed a scenario which handling Job Variables could cause a crash

:white_check_mark: Server->Email Task->Fixed a problem with sending using an anonymous account

:white_check_mark: Client->Job/Task Control Task->Fixed issue not displaying some properties right when using remote Connection

:white_check_mark: Server->SSISDB->Filtered out variables from project and package parameters

:white_check_mark: Client->Time exceptions->Fixed new date sorting issue

:white_check_mark: Client->Fixed a Disconnect Server and Connect Server and multiple connect issue which could resulted in a message like "You are not connected to any Server"

:white_check_mark: Client/Server->Export settings->Fixed a problem exporting specific Users to a specific path

:white_check_mark: Server->Hyper-V List Task->Fixed an issue where a property name could be different in some systems resulting in SID instead of Name is returned


### 7.1.8 [2014-06-27]

#### Features

:star: Client/Server: New translation engine for delivering faster and more translations to other languages

:star: Server->Performance counter Trigger->More efficient code that now supports remote performance counter


#### Bug Fixes


:white_check_mark: Server: SFTP->Upload->Fixed a problem with that source file was deleted even though nothing was uploaded

:white_check_mark: Logging->Events->Fixed an issue with logging problems with SQL Connections

:white_check_mark: Client->Editing Task->Fixed an issue with Previous and Next button and saving some Task information

:white_check_mark: Server->Fixed an issue with On Task error->Do not raise error setting

:white_check_mark: Server->File Trigger (Samba)->Fixed a reconnect issue (not re-setting properties)

:white_check_mark: Server->FTP->Fixed a problem retrieving current folder too many times

:white_check_mark: Server->Remote file filter test->Fixed an issue with multiple source folders split by semicolon

:white_check_mark: Client->Remote file Trigger->Fixed issue with selecting "Delete files" only

:white_check_mark: Client->Manage PGP key rings->Fixed an issue deleting keys

:white_check_mark: Client->Fixed an unhandled exception when doing Object search

:white_check_mark: Server->Amazon S3->Added support for uploading < 5GB files

:white_check_mark: Server->VisualCron Trigger->Fixed an issue with Job Variables

:white_check_mark: Server->Powershell->Fixed a Credential issue (accessing network files)

:white_check_mark: Server->Variables->Fixed a problem using certain strings in the DATENOWADD Variable in file filter

:white_check_mark: Server->Notifications->Fixed issue with not (directly) saving TaskNotifications.xml after importing

:white_check_mark: Client->Time exceptions->Fixed date sorting

:white_check_mark: Server->Fixed a general renaming issue when working with string (for example calculating destination name with file masks) that in some cases could cause problems


### 7.1.7 [2014-05-21]

#### Features

:star: Client/Server: Connections->Added test button for SMTP,POP3 and IMAP

:star: Client: Connections->Added protocol filter and Connection selection in Connections window

:star: Server: Increased startup performance

:star: Server: Audit log->Increased performance on object comparisons

:star: Client/Server: XML Delete Node->Added namespace support

:star: Client: Updated UI controls

:star: Client/Server: PowerShell Task->Added remote execution

:star: Client/Server: New Task: Base64 - encode

:star: Client/Server: New Task: Base64 - decode


#### Bug Fixes


:white_check_mark: API: Variables->Fixed a problem with loop Variables in foreground execution

:white_check_mark: API: Variables->Fixed a problem parsing Variables

:white_check_mark: Server: Office Macro->Now setting appropriate permissions before macro execution

:white_check_mark: Client: Job/Task control Task->Fixed a problem with cloning Job Variables

:white_check_mark: Client: Web service Task->Fixed a problem handling simple arrays

:white_check_mark: Client: Manage PGP Key rings->Fixed a problem with deleting key rings

:white_check_mark: Server: SharePoint - Add list item->Fixed an issue with multiple columns

:white_check_mark: Server: Excel - Create->Handled empty strings differently

:white_check_mark: Server: Audit log->Fixed some minor bugs in object comparison

:white_check_mark: Server: Loop->Fix waiting time of last loop iteration


### 7.1.6 [2014-04-16]

#### Bug Fixes


:white_check_mark: Client: Permissions->Fixed a UI problem with Cloning a Group

:white_check_mark: Server: Permissions->Fixed a problem with updating a cloned Group

:white_check_mark: API: Variables->Fixed a problem parsing Variables

:white_check_mark: API: Job report Task->Fixed issue preventing calculation of next run resulting error:  Object reference not set to an instance of an object

:white_check_mark: Server: .NET Code Task->Fixed an issue with compiling assemblies leading to dlls not found (in some situations)

:white_check_mark: Server: SQL Task->Fixed a problem parsing and adding parameter values to result

:white_check_mark: Client: SQL Task->Fixed a problem viewing parameters with MAX as input

:white_check_mark: Client: SQL Task->Fixed a problem refreshing Job list (old list was not cleared)

:white_check_mark: Server: Execute Task->Handled -1073741502 error (related to Load profile option)

:white_check_mark: API: Popup Task->Fixed an issue not being able to return result/output from other Tasks within the Popup Task


### 7.1.5 [2014-04-09]

#### Features

:star: Client: Email Task->Updated HTML editor

:star: VCCommand: Added support for activate/deactivate license

:star: Installer: Now prompting with original path when installing

:star: Client: FTP Task->Added Copy/Move command

:star: Time exceptions: Add Clone option for collections

:star: Client/Server: New Task->Event log - Read


#### Bug Fixes


:white_check_mark: API: Variables->Fixed problem parsing Task Variable with direct Id

:white_check_mark: API/Server: Popup Notification->Fixed problem with PrevTask Variable

:white_check_mark: Server: Processes->Fixed issue that could cause problems with "Running Jobs window" and keeping track of running Jobs

:white_check_mark: API: Variables->Fixed a problem parsing Variables

:white_check_mark: Server: Database->Fixed a problem deleting old entries in the Audit log

:white_check_mark: Client: Running jobs->Fixed a display problem when Jobs were running more than 24 hours

:white_check_mark: Server: Handled an issue with copying SQL CE files

:white_check_mark: Client: Main window->Handled an issue with the GridFilter becoming inactive

:white_check_mark: Server: SQL Trigger->Fixed an issue with storing and comparing the last value

:white_check_mark: Server: Folder filter->Fixed a problem parsing the right folder when using regular expressions

:white_check_mark: Server: Run missed Jobs (because of Time change etc) did not take Time exceptions into account - fixed

:white_check_mark: Server: Impersonation: added check if profile directory exists before loading it to avoid profile directory creation by VisualCron

:white_check_mark: Client: Popup Task Notification: Fixed an issue with preview button

:white_check_mark: Client/Server: Handled sanitation of output/result that could interrupt communication

:white_check_mark: Client: .NET Code Condition->Handled a problem with saving parameters

:white_check_mark: Client: Connections->Fixed a problem editing address of VisualCron Connection type


### 7.1.4 [2014-03-17]

#### Notes

:memo: Database: New version of database for logging. Historic events will be cleared from this version.


#### Features

:star: Client/Server: Introducing Audit logs

:star: Client/Server: Introducing Version logs

:star: Client: Assembly Task->Added support for using Variables in date time data type

:star: Client: Object relations->Search updated

:star: Client: FTP Task->Added override options for Transfer type in Connection for Download/Upload commands

:star: Client/Server: HTTP Task->Added different authentication types


#### Bug Fixes


:white_check_mark: Client: Tasks->Fixed a problem with non-responsive Edit button

:white_check_mark: Server: Folder delete Task->Fixed a problem converting old settings to new

:white_check_mark: Client: Calendar->Fixed another bug where the calendar - calculcating next executions

:white_check_mark: Server: SSIS DB Task->Fixed a problem with supplying project parameters

:white_check_mark: Client: Attachments->Fixed problems accessing some Job Variables in Email Task/Notification

:white_check_mark: Client: Log->Fixed an issue in the realtime log when open over night

:white_check_mark: Client: Calendar->Fixed an issue with showing scheduled Jobs in the future

:white_check_mark: Server: Variables->Fixed an issue with using File Conent Variable with Credentials

:white_check_mark: API: Sync->Now sending permissions if sync is off

:white_check_mark: API: Variables->Fixed parsing issue of Variables with no parameters


### 7.1.3 [2014-03-03]

#### Features

:star: Client/Server: New Variable translation which should allow more ways of entering characters

:star: Client/Server: Office Macro Task->Added more debug logging

:star: Client/Server: Office Macro Task->Added password support for Excel documents

:star: Client/Server: Office Macro Task->Added update file after execution support

:star: Client/Server: Copy files->Added option to copy all files to destination directory without creating sub directories

:star: Client/Server: SQL Task->Added better ways to capture errors when running SQL Job and redirecting back some basic output

:star: Client/Server: List file(s) Task->Added options to control output and separator

:star: Client/Server: List folder(s)->New Task

:star: Client: Variables->Added search function

:star: Installer: Added option to re-use same user for the VisualCron service

:star: Client/Server: SSIS DB Task->Added "environment" property support

:star: Client: Variables->Added multiple delete


#### Bug Fixes


:white_check_mark: Server: AS/400 Command Task->Fixed an issue with execution result

:white_check_mark: Server: Assembly Execute Task->Fixed an issue with training and execution (timeout)

:white_check_mark: Client: SQL Task->Fixed a validation problem when refreshing SQL Jobs

:white_check_mark: Server: Excel Convert Task->Removed empty rows in resulting file

:white_check_mark: Client: SSIS DB Task->Fixed a problem editing parameters

:white_check_mark: Server: Delete file(s) Task->Now deleting all empty sub folders (not just those that had files that were deleted)

:white_check_mark: Server: SSIS DB Task->Fixed a problem executing with parameters

:white_check_mark: Client: Calendar->Fixed a bug where the calendar, in some scenarios, could hang on "Refreshing data"


### 7.1.2 [2014-02-11]

#### Features

:star: Client/Server: SSIS DB Task->Added 32 bit execution mode

:star: Server: FTP Task->Delete folder command->Improved it so it can delete folders that are not empty (from files are folders)

:star: Client/Server: PGP Decrypt->Added support for basing destination name on source file (encrypted file) instead of "inner" file name

:star: Client/Server: PGP Decrypt->Added "post process" Variable support

:star: Client/Server: PGP Decrypt->Added overwrite option

:star: Client/Server: Crystal Reports->Added multiple datasource support

:star: Client/Server: Added Task AS/400 Command Task


#### Bug Fixes


:white_check_mark: Server: Crystal reports Task->Fixed datetimevariable issue when using discrete values

:white_check_mark: Server: SSIS DB Task->Fixed false positive result error

:white_check_mark: Server: Remote File Trigger->Fixed issue deactivating Trigger when error occurs

:white_check_mark: Server: Remote File Trigger->Fixed issue saving retry settings

:white_check_mark: Server: Email Task->Fixed error 'User authentication failed: No SASL mechanisms supported by both the client and the server (error code is 0)' which could occur on some Exchange servers

:white_check_mark: Server: Assembly Task->Fixed issue with really large assemblies preventing communication

:white_check_mark: Server: Assembly Task->Fixed a problem setting Variables on parameters

:white_check_mark: Client/Server: FTP Task->Now treating dates as local time when MSLT is not supported

:white_check_mark: Server: Email Trigger->Fixed a problem where the match process on conditions could produce wrong result in some scenarios

:white_check_mark: Server: Web service Task->Fixed a problem retrieving WSDL information

:white_check_mark: Client: SSIS DB Task->Fixed a problem re-saving the Task with parameters


### 7.1.1 [2014-01-29]

#### Features

:star: Client/Server: Added 32 bit execution mode for Assembly Execute Task

:star: Server: Fixed issues with reloading and executing assembly in Assembly Execute Task (prevented lock of files)


#### Bug Fixes


:white_check_mark: Server: Fixed duplicate On complete - Notification issue

:white_check_mark: Server: Fixed an issue where the Email Task ignored code page property

:white_check_mark: Server: Fixed a file mask in combination with Variable issue in FTP download/list files Task

:white_check_mark: Client: Fixed issue with not displaying FTP Delete settings properly

:white_check_mark: Client: Fixed saving of variable bindings in SNMP * Tasks

:white_check_mark: Server: Now setting correct codepage (from Task) on FTPS Tasks


### 7.1.0 [2014-01-17]

#### Notes

:memo: Installer: Removed "Allow service to interact with desktop" option. If you for some reason need that you need to enable it after installtion.

:memo: Client/Server: Transfer type has been moved from Upload/Download Tasks to Connection. Manual adjustment needed.

:memo: Client/Server: ASCII mode property in Connection has been replaced by Transfer type. Manual adjustment needed.

:memo: Client/Server: Remote File Trigger has been redefined. Manual adjustment needed.


#### Features

:star: Client/Server: SQL Task->added Jobs refresh from server

:star: Client/Server: SQL Task->added Jobs steps refresh from server

:star: Client/Server: SQL Task->added stored procedure parameter(s) load and refresh

:star: Client/Server: SQL Task->added column displaying data type among stored procedure parameters

:star: Client/Server: FTP/SFTP Task-> added remote file filter for Download file(s) command

:star: Client/Server: FTP/SFTP Task-> added remote file filter for Delete file(s) command

:star: Client/Server: FTP/SFTP Task-> added remote file filter for List file(s) command

:star: Client/Server: FTP/SFTP Task-> added remote file filter for Rename file(s) command

:star: Client/Server: FTP/SFTP Task-> various improvements

:star: Client/Server: FTP/SFTP Task-> Resume and Append has been added

:star: Client/Server: Added support for semi colon separated values in Parameter values


#### Bug Fixes


:white_check_mark: Server: Fixed an issue with Crystal reports Task and DateTimeVariable type

:white_check_mark: Client/Server: Fixed various filter issues in Remote file Trigger. Any existing Remote file Trigger needs to be edited and defined again manually.

:white_check_mark: Server: Fixed a problem with Task Flows not continuing "On complete" event


### 7.0.9 [2014-01-07]

#### Features

:star: Client: Fixed sorting of encoding info in Task

:star: Client/Server: Added support for specifying SFTP version in Connections

:star: Client: Added the CAML query browser for Sharepoint Tasks

:star: Client: Added option to Deselect/Select all Jobs in the Calendar tool

:star: Client/Server: Added parameter/argument support for PowerShell Task

:star: Client/Server: SharePoint - Get list item(s) Task updated with CAML browser, field selection and output control

:star: Client/Server: Added Task SharePoint - Add list item(s)

:star: Client/Server: Added Task SharePoint - Update list item(s)

:star: Client/Server: Added Variables for SQL output parameters


#### Bug Fixes


:white_check_mark: Client: Fixed sorting in Clone menu (main window)

:white_check_mark: Server: Fixed errors that were raised when trying to filter out more than 50.000 files

:white_check_mark: Server: Fixed issue with executing MSSQL Job with OLEDB

:white_check_mark: Client/Server: Fixed a bug concerning cloning of Jobs->Tasks->Flow->TaskId

:white_check_mark: Client/Server: Fixed a bug concerning cloning of Jobs->Tasks->Job/Task control Task->TaskId

:white_check_mark: Client/Server: Fixed a problem with the new Variable {TASK(orderId,property)}

:white_check_mark: Server: Fixed a problem with duplicate Attributes list when using the File filter in FTP Task->Upload

:white_check_mark: Client: Fixed issue with saving settings (Description->Condition) in RSS Trigger

:white_check_mark: Client: Fixed an issue in Task log not reflecting the Exit code collection propertly

:white_check_mark: Server: Fixed an issue in Task SharePoint - Delete list item(s)

:white_check_mark: Server: Fixed a problem with storing AttachmentFolder Variable in Email Trigger

:white_check_mark: Server: Fixed an issue with output parameters in SQL Task


### 7.0.8 [2013-12-06]

#### Features

:star: Client/Server: Added Dynamics CRM - Get Entity Task

:star: Client/Server: Added Dynamics CRM - Create Entity Task

:star: Client/Server: Added Dynamics CRM - Update Entity Task

:star: Client/Server: Added Dynamics CRM - Download attachment Task

:star: Client/Server: Added Dynamics CRM - Upload attachment Task

:star: Client/Server: Added Dynamics CRM - Get entity Task

:star: Client/Server: Added Dynamics CRM - Delete entity Task

:star: Client/Server: Added Dynamics CRM - List entities Task

:star: Client/Server: Added Dynamics CRM - Upload attachment Task

:star: Client/Server: Added Dynamics CRM - Get audit status Task

:star: Client/Server: Added Dynamics CRM - Set audit status Task

:star: Client/Server: Added Dynamics CRM - Start work flow Task

:star: Client/Server: Added group icons to menus

:star: Client/Server: Added "Logic" Variable functions

:star: Server: Added support for stopping remote Job/Task started through Job/Task Control Task


#### Bug Fixes


:white_check_mark: Server: Fixed a bug with deleting folder in Delete folder Task when folder was not empty

:white_check_mark: Client: Fixed general problems of realtime update of Job history window

:white_check_mark: Server: Fixed a problem using VisualCron Variables in a Powershell file

:white_check_mark: Client: Fixed duplicate button rows in the Popup Task

:white_check_mark: Client/Server: Fixed various issues with Job/Task Control Task

:white_check_mark: Server: Fixed issues with Set file/folder permission Tasks

:white_check_mark: Client/Server: Fixed issue with a new, unknown, restore point type for System restore Tasks


### 7.0.7 [2013-11-08]

#### Features

:star: Client/Server: Added the File - Get checksum Task

:star: Client/Server: Added the File - Set file attributes Task

:star: Client/Server: Added the File - Set folder attributes Task

:star: Client/Server: Added the File - Change owner Task

:star: Client/Server: Added Variables for retrieving a certain column on a certain row in content

:star: Client/Server: Updated Folder delete Task to use new folder filter

:star: Server: Added support for Variables in parameters of Crystal reports Task

:star: Client: Updated Flow chart to support new "flow" with various improvements

:star: Client: Added Trigger Activate/Deactivate to main right click menu on Job/Task

:star: Client/Server: Added Trigger Add and Delete event to VisualCron Trigger


#### Bug Fixes


:white_check_mark: Client: Fixed a problem which could occur when refreshing remote Jobs in Job/Task Control Task

:white_check_mark: Server: Fixed a problem with changing Server status from Tray Client

:white_check_mark: Server: Fixed a problem with duplicate files and split of folders using semicolon in File filter

:white_check_mark: Server: Fixed issues with Trigger inactivation/expire events

:white_check_mark: Client: Fixed a problem with not displaying running status correctly

:white_check_mark: Server: Fixed a problem aborting SQL Tasks

:white_check_mark: Client: Fixed a problem selecting various combinations when adding/editing a Credential

:white_check_mark: Server: Fixed a problem where Variables were not resolved in Header of Web service Task

:white_check_mark: Server: Fixed a problem with uploading files via Sharepoint - Upload Task


### 7.0.6 [2013-10-07]

#### Features

:star: Client: Various improvements to UI of Notifications and Flows


#### Bug Fixes


:white_check_mark: Client/Server: Fixed a permissions problem

:white_check_mark: Server: Fixed an issue in the Archive - compress Task

:white_check_mark: Server: Fixed a problem with Oracle DirectMode and "License error"

:white_check_mark: Server: Fixed a problem with Excel Create Task and using Variables as input (could result in no file creation)

:white_check_mark: Server: Fixed a problem with Set Variable Task (XML error) when containing "forbidden" characters like &

:white_check_mark: Client: Fixed a wrong message when exporting all settings


### 7.0.5 [2013-09-13]

#### Features

:star: Client/Server: Added 30 VMWare Tasks

:star: Client/Server: Added Activate/Inactivate Trigger in Job/Task control Task

:star: Client/Server: Added Content-type option based on file type

:star: Client/Server: Added option to run Execute Task on remote Server without creating Job or Task at remote Server

:star: Server: Performance fixes in the Excel - Create Task


#### Bug Fixes


:white_check_mark: Client: Fixed an issue causing crash in Running Jobs window

:white_check_mark: Install: Handled some possible install problems

:white_check_mark: Client: Fixed a problem with Client not storing Add new line property in File write Task - added new line break options

:white_check_mark: Server: Fixed a issue with SQL Trigger raising wrong events (inactivated) when updated

:white_check_mark: Server: Fixed a problem with updating status for Jobs that were started throught he Job/Task control Task.


### 7.0.4 [2013-08-15]

#### Bug Fixes


:white_check_mark: Client/Server: Fixed a problem with next run calculation for interval time trigger (hours) which could change the base start hour in special situations

:white_check_mark: Client: Fixed a bug where backup settings file could become empty when exporting to default directory from Client

:white_check_mark: Server: Fixed various minor issues in Sharepoint Tasks

:white_check_mark: Client/Server: Fixed various minor issues related to Job history window

:white_check_mark: Client: FIxed issues selecting and searching in the Notifications window

:white_check_mark: Install: FIxed an issue with VixCOM.dll which could cause installation problems on some x86 servers


### 7.0.3 [2013-08-12]

#### Bug Fixes


:white_check_mark: Server: Fixed a problem with Stop Job flow and Notifications where Notifications could be skipped when Stop Job appeared first (appeared first in 7.0.1)

:white_check_mark: Client/Server: Fixed a problem with using the Variable {TASK(Active,ExitCodeDesc)} (appeared first in 7.0.1)

:white_check_mark: Server: Fixed a problem SFTP downloading from root folder (/) (appeared first in 7.0.1)

:white_check_mark: Server: Fixed a problem with the polling File Trigger and Credentials

:white_check_mark: Server: Fixed a problem with sending emails with Email Task when special recipient type was empty


### 7.0.2 [2013-08-07]

#### Bug Fixes


:white_check_mark: Client: Fixed a problem with deleting SQL parameters

:white_check_mark: Server: Fixed an issue that could cause Decompress (zip) Task to fail (appeared first in 7.0.1)

:white_check_mark: Client: Fixed an issue with storing parameters in DTS and SSIS Tasks

:white_check_mark: Server: Fixed an issue that ending semicolon was deleted in SQL queries (appeared first in 7.0.1)


### 7.0.1 [2013-08-02]

#### Notes

:memo: Client/Server: Protocol has been updated - server and client needs to be on same version 7.0.0

:memo: Client/Server: Notifications tabs have been removed - Notifications are now set in the Flow tab

:memo: Client/Server: Parts of On error functionality have now been moved to Flow tab

:memo: Client/Server: Existing logs will be cleared with this version


#### Features

:star: Client/Server: Added custom Exit code handling for Tasks

:star: Client/Server: Added option to control auto negotiation of ciphers in SSH Connection

:star: Client/Server: Added SysLog Task

:star: Client/Server: Notifications are now based on Tasks so you can use any Task type as Notification

:star: Client/Server: Notifications can now be sent on 4 events; on start, on success, on complete and on error where on success is the new one. Also, additional conditions can be applied, like output

:star: Client/Server: The Flow tab now controls what happen when Task or Job events occur (i.e. on success/on error) and also based on basic conditions, like output

:star: Client/Server: On error handling now supports generating success or failure based on output and any Variable at runtime

:star: Server: Added support for multiple queries separated by semicolon in SQL Task

:star: Client/Server: Added several File Variables (Exist,Content,Size,CreatedTime,Modifiedtime) with Credential support

:star: Client/Server: Added SSISDB Task

:star: Client/Server: Added overwrite option for Rename file Task

:star: Client/Server: Added SendKeepAlive option in SSH Task

:star: Client/Server: Added optional environent variables when sending command in SSH Task

:star: Client/Server: Added Trigger.RSS.PubDate Variable

:star: Client/Server: Added string Variables "Get first line", "Get last line","GetLineByRowNumber"

:star: Client/Server: Added support for selecting and executing multiple Jobs in the Client

:star: Client/Server: Added support for increased length in output in Task history

:star: Client: Performance optimizations of start time and Add/Edit Job window

:star: Server: RSS, Remote file, SQL and Email Trigger are no longer polling if a Time exception exists at poll moment - previously only checked at "fire"-moment


#### Bug Fixes


:white_check_mark: Client: Fixed non-working menu buttons in the Job permissions override

:white_check_mark: Client: Fixed sorting in Object relations window

:white_check_mark: Client: File Trigger->On error reconnect attempts was saved but not displayed correctly

:white_check_mark: Server: Fixed problems exporting to other formats than PDF in the Crystal reports Task

:white_check_mark: Server: Fixed a problem with the VisualCron Trigger->Inactivated+Expired not triggering

:white_check_mark: Client/Server: Handled parsing for V6R1M0 server

:white_check_mark: Client: Fixed a problem with Job log history and expanding Job (remembering which Tasks has been loaded)

:white_check_mark: Client: Fixed correct handling of proxy settings for SFTP in Explorer

:white_check_mark: Client: Fixed a crash in the Remote file explorer

:white_check_mark: Server: Fixed issue in Email Trigger performing actions even though Conditions not met

:white_check_mark: Server: Fixed issues with Loop and Smaller or Smaller than

:white_check_mark: Server: Fixed issue with Cloud upload Tasks not closing the filestream properly resulting in locked upload file

:white_check_mark: Server: Fixed a problem with not being able to stop running Powershell Task

:white_check_mark: Client/Server: Fixed update of Windows process id in "Running Jobs" window

:white_check_mark: Server: Fixed a bug in updating result objects from Triggers (when Job came from queue)

:white_check_mark: Client: Fixed a bug in the Remote registry viewer concerning certain string types and Cancel option

:white_check_mark: Server: Fixed a bug concerning detection of encryption in S/MIME emails in Email Trigger

:white_check_mark: Client/Server: Fixed issues running Job on other Server (through Job/Task Control Task) with Job Variables

:white_check_mark: Client: Fixed a problem showing the right Variable key in Job Variables window


### 6.2.2 [2013-04-08]

#### Bug Fixes


:white_check_mark: Client/Server: Fixed a problem with Sharepoint Delete files Task

:white_check_mark: Client/Server: Fixed a problem with saving settings in Sharepoint - list files Task

:white_check_mark: Client/Server: Fixed a problem with saving settings in Sharepoint - list items Task

:white_check_mark: Server: Fixed a statistics logging error (InternalWorkerThread->OutputStatistics)


### 6.2.1 [2013-04-03]

#### Features

:star: Client: Event info description added

:star: Server: Added support for x86 execution of SSIS with SQL server 2012


#### Bug Fixes


:white_check_mark: Server: Fixed an error in the Remote Kill Task (object nullreference error)

:white_check_mark: Client: Fixed some issues in Edit XML node Task

:white_check_mark: Server: Fixed a DST bug which could cause some Jobs that should run during a DST change not to be recalculated for next run time

:white_check_mark: Server: Fixed a problem in the date filter of general file filter. Date comparison used UTC time instead of local file time

:white_check_mark: Server: Fixed a problem with importing settings


### 6.2.0 [2013-03-19]

#### Features

:star: Client: 20% faster startup time

:star: Client/Server: Added date Variable support in Crystal reports Task

:star: Client/Server: Added Hyper-V - Check VM Task

:star: Client/Server: Added Hyper-V - List VM Task

:star: Client/Server: Added Hyper-V - Start VM Task

:star: Client/Server: Added Hyper-V - Stop VM Task

:star: Client/Server: Added Hyper-V - Pause VM Task

:star: Client/Server: Added Hyper-V - Suspend VM Task

:star: Client/Server: Added Hyper-V - Resume VM Task

:star: Client/Server: Added Hyper-V - Reset VM Task

:star: Client/Server: Added Hyper-V - Apply snapshot Task

:star: Client/Server: Added Hyper-V - Create snapshot Task

:star: Client/Server: Added Hyper-V - Delete snapshot Task


#### Bug Fixes


:white_check_mark: Server: Fixed a problem with downloading sub folders (SFTP/FTP) when using On error "No file(s) downloaded"

:white_check_mark: Server: Fixed a problem with creating destination folders when downloading sub folders (SFTP)

:white_check_mark: Client/Server: Fixed a problem with returning the right output for Tasks in loops

:white_check_mark: Server: Fixed a compatibility issue with some older Crystal reports documents

:white_check_mark: Client: Fixed an issue with maximum number length in Crystal reports Task

:white_check_mark: Client: Fixed an issue with default value in Crystal reports Task

:white_check_mark: Server: Fixed long path issue in various Tasks

:white_check_mark: Server: Fixed an issue with Date condition in Email Trigger

:white_check_mark: Server: Additional fix for 'retry times' in Email Trigger corrected in 6.1.9


### 6.1.9 [2013-02-26]

#### Features

:star: Client/Server: Added Virtual Server - Start VM Task

:star: Client/Server: Added Virtual Server - Save VM state Task

:star: Client/Server: Added Virtual Server - Pause VM Task

:star: Client/Server: Added Virtual Server - Reset VM Task

:star: Client/Server: Added Virtual Server - Turn off VM Task

:star: Client/Server: Added Virtual Server - List VM Task

:star: Client/Server: Added Virtual Server - Check VM Task

:star: Client/Server: Added support for controlling SFTP/SSH authentication in more detail

:star: Client/Server: Added Excel - Set cell(s) Task

:star: Client/Server: Added Job Variables (parameters) functionality and added parameter settings to Job/Task control Task

:star: Client/Server: Added error control in FTP/SFTP Task about raising error when no files were found, downloaded or uploaded

:star: Client: Faster startup of Client

:star: Client: Faster Task search

:star: Client: Added mail folder selection for Email Trigger


#### Bug Fixes


:white_check_mark: Client/Server: Various small fixes with Crystal reports

:white_check_mark: Client: Fixed a problem with remote file explorer (crash)

:white_check_mark: Server: Fixed an issue with Powershell in some environments

:white_check_mark: Client/Server: Removed obsolete SSL2 protocol from FTP Explorer/Task (in TLS mode) as it could cause issues

:white_check_mark: Server: Fixed a problem resetting "retry times" on successful Email Trigger connection.

:white_check_mark: Server: Fixed issues with uploading documents to Google (finding destination folder)

:white_check_mark: Server: Fixed issues moving a mail to other folder (Email Trigger)


### 6.1.8 [2013-01-12]

#### Features

:star: Client/Server: Added support for return error if no files are found in the List files Task. Please note that the default behavior is returning error.

:star: Client/Server: Added basic support for custom branding VisualCron. Contact sales for more information.

:star: Client/Server: Added content-type header support for the HTTP Task

:star: Client/Server: Added "duplicate file delay" property for File Trigger

:star: Client/Server: Added Excel - Recalculate Task


#### Bug Fixes


:white_check_mark: Server: Fixed and issue where Logoff User Task reported error even though it succeeded

:white_check_mark: Server: Fixed a problem with adding parameters in DTS and SSIS Task

:white_check_mark: Server: Fixed an issue connection and executing against Oracle (SQL Task)

:white_check_mark: Server: Fixed with Sharepoint file upload and commit

:white_check_mark: Server: Fixed and issue with high session value and the execution context dialog

:white_check_mark: Server: Fixed a problem preventing negative values in the Crystal reports Task

:white_check_mark: Server: Fixed an issue with WebDAV Download Task and .NET 4.0

:white_check_mark: Server: Fixed a problem with remote execute reporting back (reverting to a previoius solution)

:white_check_mark: Installer: Fixed an issue pointing to wrong version of .NET

:white_check_mark: Client: Added missing SQL Explorer permission


### 6.1.7 [2012-12-27]

#### Notes

:memo: VisualCron is now using and requires .NET 4.0


#### Features

:star: Client/Server: Added the Popup Task

:star: Client/Server: Added the Create Excel Task

:star: Server: Added wait for completion support in SQL Task->MSSQL->Job

:star: Client/Server: Added support for Direct mode with Oracle (no need for installed Oracle Client)

:star: Client/Server: Added the Crystal reports Task

:star: Client/Server: Added the SQL event Trigger

:star: Client/Server: Added support for MSSQL 2012 SSIS package execution


#### Bug Fixes


:white_check_mark: Server: Fixed an issue where File Trigger could hang on waiting for file to be released (if Triggered by other Task which uses same Credential)

:white_check_mark: Client: Fixed an issue when cloning Email Tasks with attachments

:white_check_mark: Server: Fixed issue with Job/Task Control Task not being able to stop itself

:white_check_mark: Client: Fixed a decimal and Guid validation in Web service Task

:white_check_mark: Client: Fixed an issue when Validate was deselected in Web service Task

:white_check_mark: Server: Fixed an issue when Kill Task reported an error even though it succeeded (introduced in 6.1.5 and only when having Extended debugging on)

:white_check_mark: Server: Fixed an issue related to uploading large files through Sharepoint Task

:white_check_mark: Client: Sorting fixes in order change

:white_check_mark: Server: Fixed Variable handling in the Registry Task


### 6.1.5 [2012-11-08]

#### Features

:star: Client/Server: Added XendApp Task which lets you send messages directly to phones and devices

:star: Client/Server: Added JobReport Task

:star: Client/Server: Added VCCommand - a command line alternative for various actions (requires .NET 4.0)

:star: Client/Server: Added support for offline Trial extension


#### Bug Fixes


:white_check_mark: Server: Fix for Variable problem in Copy files Task

:white_check_mark: Server: Fix for authentication issue in Sharepoint (Sharepoint 2010)

:white_check_mark: Server: Fix and import issue in SSIS Task

:white_check_mark: Client: Fixed a permission issue which could crash the Client

:white_check_mark: Server: Variables were not set on the Remote file trigger

:white_check_mark: Server: Fixed duplicate File Trigger issue (for applications that might create twice within a short time period)

:white_check_mark: Client/Server: Fixed some memory leaks in Client and Server

:white_check_mark: Server: Fixed a problem with writing to file in Excel Convert Task

:white_check_mark: Client: Fixed a bug with exporting User groups

:white_check_mark: Client: Fixed a time zone bug (when scheduling against a server in another time zone)


### 6.1.4 [2012-10-10]

#### Features

:star: Client/Server: Added Sharepoint - Create list Task

:star: Client/Server: Added Sharepoint - Update list Task

:star: Client/Server: Added Sharepoint - Delete list(s) Task

:star: Client/Server: Added Sharepoint - Describe list Task

:star: Client/Server: Added Sharepoint - Get lists Task

:star: Client/Server: Added Sharepoint - Get list item(s) Task

:star: Client/Server: Added Sharepoint - Delete list item(s) Task

:star: Client/Server: Added Sharepoint - Download file(s) Task

:star: Client/Server: Added Sharepoint - Upload file(s) Task

:star: Client/Server: Added Sharepoint - Delete file(s) Task

:star: Client/Server: Added Sharepoint - Get file(s) Task

:star: Client: Added password character when viewing existing SQL connection strings

:star: Client/Server: Added support for specifying initialization vector in Symmetric encryption/decryption Tasks

:star: Client/Server: Added padding options in Symmetric encryption/decryption Tasks


#### Bug Fixes


:white_check_mark: Client: Handled an issue when Adding a Task (potential crash)

:white_check_mark: Client: Windows 8 compatibility fix

:white_check_mark: Server: Fixed an issue of double execution of SSIS (using MSSQL2008)

:white_check_mark: Client/Server: Handled a problem with ForeignKeyException in Client

:white_check_mark: Client: Handled a scenario which could crash Client when new Task was added

:white_check_mark: API: Handled a reconnection problem when wrong password was specified


### 6.1.3 [2012-09-04]

#### Features

:star: Client/Server: Added Remote File Trigger for FTP/SFTP

:star: Server: Optionally added way to not override HTTP maximum connections

:star: Client/Server: Added NTLM authentication for WebDAV


#### Bug Fixes


:white_check_mark: Server: Fixed some error handling in Remote Execute Task

:white_check_mark: API: Fixed a reference problem with Settings object. Affected Server->folder settings

:white_check_mark: Server: Fixed an issue in Trigger where they were not removed correctly after RunOnce option on Job

:white_check_mark: API: Fixed issue with displaying name in Modified/Created when AD user had no firstname/lastname specified from the beginning. If so, we show username instead.

:white_check_mark: API: Fixed a permission issue when activating many Tasks

:white_check_mark: Client: Fixed issue when trying to open output from Job log->Task

:white_check_mark: Client: Fixed issue 'disappearing namespace issue' in XML Read Node Task

:white_check_mark: Server: Fixed an issue when Jobs listing in VisualCron Trigger could not be refreshed

:white_check_mark: Server: Fixed various issues with SSIS Task including support for Trusted connections

:white_check_mark: Client: Fixes issues with performance and sorting when changing sort in Jobs->Tasks

:white_check_mark: Client: Fixes issue with parameters types in SSIS Task

:white_check_mark: Client: Fixed issue with switched DB logging parameters

:white_check_mark: Server: Add error handling for unhandled exceptions in SQL Task

:white_check_mark: Server: Handled an error when no Task was selected in Job/Task control Task

:white_check_mark: Client: Fixed Job Test button issue that could cause reference problems in Client (foreign key errors)


### 6.1.2 [2012-06-26]

#### Notes

:memo: Backwards compatibility. This version uses new protocol and cannot connect to older versions. If you downgrade then new permissions created will not be seen in older versions.


#### Features

:star: Client: Added support for Azure/Amazon S3/Google drive/SkyDrive and WebDav in FTP explorer

:star: Client/Server: Support for the Web client

:star: Client/Server: Added group permissions

:star: Client/Server: Added permissions on Job level


#### Bug Fixes


:white_check_mark: Server: Fixed a folder creation issue in Amazon/Azure upload

:white_check_mark: Server: Added a fix for Email Trigger when using POP3 (could previously cause an error if you do not use default folder or had extended debugging on)

:white_check_mark: Client/Server: Handled some errors in Set Variable Task  when using "late binding"

:white_check_mark: Server: Fixed printer selection issue in when printing images (removed Word dependency)

:white_check_mark: Client/Server: Fixed issues with web services parameters of type output in Web service Task

:white_check_mark: Client/Server: Fixed an issue with Variables and testing Job

:white_check_mark: Client: Fixed sorting issue in FTP explorer

:white_check_mark: Server: Fixed WebDAV multiple files upload issue

:white_check_mark: Server: Fixed image printing issue when All pages was selected

:white_check_mark: Server: Fixed a temporary folder location issue for Office Macro Tasks


### 6.1.1 [2012-05-17]

#### Features

:star: Client/Server: Added Zipx format support


#### Bug Fixes


:white_check_mark: Client: Fixed a problem with scheduling across time zones

:white_check_mark: Client: Fixed Task order issue

:white_check_mark: Server: Fixed Web service Task Credential issues

:white_check_mark: Server: Fixed and issue with the Service Condition and remote computers

:white_check_mark: Server: Fixed Variable issue referring to a specific TaskProcess.Result

:white_check_mark: Client: Fixed "Get full output" issue (button disabled even though more output existed)

:white_check_mark: Server: Fixed an issue with loading referenced libraries in Unmanaged dll call Task


### 6.1.0 [2012-04-27]

#### Notes

:memo: Client/Server: If you have any Web service Tasks of type WCF you need to refresh those urls in the Task edit window


#### Features

:star: Server: Added SFTP/SSH settings for controlling packet size, download/upload block size and ASCII/binary transfer

:star: Client/Server: Added multiple Trigger dependency support

:star: Client/Server: Added support for multiple file mask inclusion and exclusion in File Trigger

:star: Client: Task search/filter in Add/Edit Task window added

:star: Client/Server: Added support for Variables in the path for Assembly execute or Web service

:star: Client/Server: Added Job completed (successfully and failed) Trigger event in VisualCron Trigger

:star: Client/Server: Added option to switch 32/64 bit execution in Office macro Task

:star: Client/Server: Added Job Reset option in right click on Job listing

:star: Client/Server: Added Unmanaged dll call Task

:star: Client/Server: Added optional 'Create relative Server folder structure' in FTP/SFTP->Download Task


#### Bug Fixes


:white_check_mark: Server: Fixed an issue with wild cards (i.e. matching a*.txt with a.txt)

:white_check_mark: Client/Server: Fixed an issue with Windows security/authentication in Web service Task (wcf mode)

:white_check_mark: Server: Fixed a bug regarding finding TaskProcesses in Variables. Could cause wrong references in Loop context Variables in certain cases

:white_check_mark: Client: Fixed a Task order display problem in the add/edit Loop window

:white_check_mark: Server: Fixed an issue with the XML - Create node Task

:white_check_mark: Client: Fixed an issue with method selection in Assembly execute Task

:white_check_mark: Client: Fixed an issue with path storage in Assembly execute Task

:white_check_mark: Server: Fixed an issue with Remote execution and waiting for process to finish

:white_check_mark: Client: Fixed a date display problems in main grid when connecting across time zones

:white_check_mark: Server: Issued proper quit command after FTP transfer

:white_check_mark: Server: Fixed an issued with Amazon S3 download

:white_check_mark: Server: Added support and better workaround for non-standard unix listing FTP's

:white_check_mark: Server: Fixed a bug concerning result Variables from Triggers

:white_check_mark: Client: Fixed a problem showing stored procedures in SQL Explorer for MySQL

:white_check_mark: Client: Fixed a problem with changing Task order in Task listing


### 6.0.9 [2012-03-29]

#### Features

:star: Client/Server: Added some kill conditions in the Kill Task: Memory and CPU usage

:star: Client/Server: Added support for plain Send Text command in SSH Task for ssh servers that do not support command channels for some reason


#### Bug Fixes


:white_check_mark: Client/Server: Fixed a .NET 3.5/4.0 conflict that could cause problems with referenced libraries in .NET Code Task

:white_check_mark: Server: Fixed a problem using output from another Task in Email Task

:white_check_mark: Server: Fixed a problem with package password in SSIS Task

:white_check_mark: Client: Fixed a gui issue with "Use shell execute" in Execute Task

:white_check_mark: Server: Fixed a problem with case sensitivity in FTP Task

:white_check_mark: Client: Fixed an issue with generating the Job/Task report

:white_check_mark: Server: Fixed an issue with a reference to System.Data in Web service Task


### 6.0.8 [2012-03-02]

#### Notes

:memo: If you use version 6.0.7 this version contains a critical update - we strongly suggest upgrading


#### Features

:star: Client: Opened up the Remove Variable Task for manual editing

:star: Client/Server: Added pipe | and tab as optional Y value (new line) in Loop


#### Bug Fixes


:white_check_mark: Server: Fixed a 'Handled invalid' bug which was related to Credentials and impersonation

:white_check_mark: Server: Fixed a problem with desktop unlock (used in Foreground Tasks) when trying to logon to domain

:white_check_mark: Server: Fixed an output problem in the Execute script Task


### 6.0.7 [2012-02-28]

#### Notes

:memo: Client/Server/API: A lot of changes have been applied to Execute Tasks. Credentials now hold information about "With profile" option. Credentials should have been converted with settings from Execute Tasks. Please verify that your Tasks works.

:memo: Server: Log database has been updated. This new installation will clear current database log history.


#### Features

:star: Server: New PDF engine - support for more pdf types and password printing

:star: Client: Now saving Tasks when clicking on Previous/Next buttons

:star: Client/Server: Added "impersonation" options like "local login" and "load profile" to Credentials. These settings are now removed from Execute Task. Please check/test your execute Tasks

:star: Client: Credentials added to the .NET Execute Task

:star: Installer: The installer has been updated

:star: Client: .NET Execute Task has been improved with better error reporting and built in references to the VisualCron API dlls

:star: Client/Server: Added "Not contains" in VisualCron and File Condition

:star: Client/Server: Added standard output check in VisualCron Condition

:star: Client/Server: Cloud Task added: Upload file(s) - for Amazon S3, Windows Azure, Google Docs and Microsoft SkyDrive

:star: Client/Server: Cloud Task added: Download file(s) - for Amazon S3, Windows Azure, Google Docs and Microsoft SkyDrive

:star: Client/Server: Cloud Task added: List item(s) - for Amazon S3, Windows Azure, Google Docs and Microsoft SkyDrive

:star: Client/Server: Cloud Task added: Delete item(s) - for Amazon S3, Windows Azure, Google Docs and Microsoft SkyDrive

:star: Client/Server: Cloud Task added: Create folder - for Amazon S3, Windows Azure, Google Docs and Microsoft SkyDrive

:star: Client/Server: Task added: Encrypt (symmetric)

:star: Client/Server: Task added: Decrypt (symmetric)

:star: Client/Server: Added "Wait for completion" and remote exit code to Remote execute Task

:star: Client: Added Exit code columns to Task and Job level

:star: Client: Added filter above the main grid for easier accessibility. Added filter options Exit code, Result and Status as well which lets you filter on failed Jobs for example.

:star: Client: Improved Job history. Now with realtime update and Task history in sub node. Filter on failed/successful Jobs.

:star: Client/Server: Added support for password only (symmetric) PGP encryption in PGP Encrypt/Decrypt Tasks

:star: Client/Server: Added Windows update Task

:star: Client/Server: Added System restore - Perform system restore Task

:star: Client/Server: Added System restore - List restore points Task

:star: Client/Server: Added System restore - Create restore point Task

:star: Client/Server: FTP action->List files


#### Bug Fixes


:white_check_mark: API: Removed a Timeout on Job/Task Control which could prevent long running remote Jobs

:white_check_mark: Server: Fixed a change folder problem with mainframe FTP servers

:white_check_mark: Client: Fixed an issue with right click option "Run with Conditions"

:white_check_mark: Client: Fixed a problem with a modal popup dialog "New version"

:white_check_mark: Client: Fixed a problem with displaying the Server settings->Log->Log to event log setting right

:white_check_mark: Server: Fixed issue with executing Access macro

:white_check_mark: Server: Fixed last modified and modified value in grid when updating a single Task

:white_check_mark: Server: Fixed an issue with creating folders (if they do not exist) in FTP Task

:white_check_mark: Client: Fixed a cloning issue with Job->Task listing->Clone button

:white_check_mark: Server: Fixed a bug preventing duplicate Triggers from the File Trigger when using "Changed"

:white_check_mark: Server: Handled previously unhandled WebDAV errors

:white_check_mark: Server: Handled an infinite loop of logging if any problem should occur to local database

:white_check_mark: Server: Fixed handling of large output from Web service Task (WCF mode)

:white_check_mark: Server: Fixed and issue with deleting empty sub folders when using /*/ in File delete Task

:white_check_mark: Server: Fixed an issue with Retry and on error which could cause Retry to fail (TaskProcess.Active == false)

:white_check_mark: Server: Fixed an issue with reading some files in Excel Tasks


### 6.0.6 [2012-01-13]

#### Notes

:memo: If you have a WebDAV Upload Task you need to edit the Task again. WebDAV now uses Connections


#### Features

:star: Client/Server: Added "On error" option "Found no process(es) to kill" to Kill Task

:star: Client/Server: Added WebDAV - Download Task

:star: Client/Server: Added WebDAV - Create folder Task

:star: Client/Server: Added WebDAV - Copy/Move files Task

:star: Client/Server: Added WebDAV - Delete files/folders Task


#### Bug Fixes


:white_check_mark: Client/Server: Fixed a problem with attachments in Email Notification

:white_check_mark: Client/Server: Fixed a problem with Credentials in attachments in Email Notification

:white_check_mark: Client: Fixed a problem with viewing Credentials in attachment listing

:white_check_mark: Server: Fixed a bug which could cause problems listing items in Task history

:white_check_mark: Client: Fixed a problem with the Client scrolled to top after sort in main window

:white_check_mark: Server: Fixed a problem concerning SFTP download and calculating out the destination folder

:white_check_mark: Client: Fixed a cloning issue with .NET execute Task which could cause parameter values to be "forgotten"

:white_check_mark: Server: Fixed a problem turning an int User Variable to string

:white_check_mark: Client/Server: Fixed a problem with exporting specific settings manually

:white_check_mark: Client: Fixed some minor issues in the Variable browser window

:white_check_mark: Server: Increased a limit for number of concurrent HTTP connections from the Server. Affects HTTP Tasks and RSS Trigger.

:white_check_mark: Server: Fixed a cloning issue with SQL parameters. Affect SQL/SSIS/DTS Tasks

:white_check_mark: Server: Fixed temp folder issue with SSIS Task


### 6.0.5 [2011-12-20]

#### Notes

:memo: If you have used the header field in the Web service you need to re-enter it. The reason is that we are, from now, encrypting this value. You also need to open each parameter that you want to use and set it again by pressing Ok.


#### Features

:star: Client: Added Clone Task option in Task listing of Job edit

:star: Client/Server: Added optional XML output to Webservice, assembly execute and .NET Execute Task

:star: Client/Server: Added post Variable processing to Copy files Task

:star: Client/Server: Added Variable support in Web service parameters

:star: Client/Server: Added Contains/Not contains to string comparision in Loop settings


#### Bug Fixes


:white_check_mark: Client: Fixed a problem with enabling "Run with Conditions" in the right click menu

:white_check_mark: Server: Fixed a problem with resolving sub-properties in the Web service Task

:white_check_mark: Server: Fixed a Credential problem in the Stand by Task

:white_check_mark: Server: Fixed a problem in the Web service Task affecting complex objects that could not be serialized properly

:white_check_mark: Server: Fixed a problem with communication failing after running a Web service Task

:white_check_mark: Server: Fixed date parsing for some non-standard FTP:s

:white_check_mark: Server: Fixed some problems with inactivated Tasks in beginning and end of loops

:white_check_mark: Client: Handled a crash that could occur given file in a XML Read Node Task does no longer exist

:white_check_mark: Server: Handled a web service proxy generation problem when a Task has been exported to other server

:white_check_mark: Server: Fixed an issue with password when signing an email with PGP key


### 6.0.4 [2011-11-16]

#### Features

:star: Client/Server/API: Updated documentation

:star: Client: Added Timeout property to RSS Trigger

:star: Client: Added Ignore errors property to RSS Trigger

:star: Client/Server: Added 'Run from here' to right click options to run the Job from a specific Task - and forward

:star: Server: Added support for dependency assemblies in the Assembly execute Task

:star: Client/Server: Added "No file(s) found" error handling for Rename Task


#### Bug Fixes


:white_check_mark: Client: Fixed a problem with removing attributes in the Create node Task

:white_check_mark: Client: Fixed a dialog problem when using File Triggers in the Job edit dialog

:white_check_mark: Client: Fixed a bug in the Variable Condition related to displaying condition type

:white_check_mark: Client: Handled an error in the Print Task dialog (regarding Variables in path)

:white_check_mark: Client: The import settings dialog is now using the local browser instead of remote because import is always done from the local computer

:white_check_mark: Server: Fixed a problem with setting lastwrite time on FTP files even though they were not downloaded

:white_check_mark: Server: Added some better error handling for RSS Trigger

:white_check_mark: Server: Fixed a problem with "time changed" that could potentially Jobs even though server is Off

:white_check_mark: Server: Now sending server time changed to Client - if connected

:white_check_mark: Server: Impersonation (credentials) could fail when using more than one "archive item" in the Compress Task

:white_check_mark: Server: DB logging improved - older versions could cause lag in insert

:white_check_mark: Client/Server: Fixed a FTP parsing issue which could result in items not displaying the correct type (file/dir)


### 6.0.3 [2011-10-20]

#### Features

:star: Client/Server: Added TriggerForEachItem property to RSS Trigger


#### Bug Fixes


:white_check_mark: Client/Server: Convert remote FTP time to local in FTP browser and download comparison - part 2

:white_check_mark: Client: Fixed some Trigger Variables in the Variables browser

:white_check_mark: Server: Fixed a problem with report back Task completion which occured on some machines - if you are using 6.0.x we strongly suggest that you upgrade


### 6.0.2 [2011-10-18]

#### Bug Fixes


:white_check_mark: API: Fixed a problem with setting the AD server property

:white_check_mark: Client: Fixed a bug which could occur when trying to delete a User

:white_check_mark: Server: Fixed a Variable bug which could cause the Internal VisualCron Trigger to fail in some situations

:white_check_mark: Install: Fixed an uninstall problem of previous version 6.x.x

:white_check_mark: Server: Fixed a problem with WCF execution and timeout - causes WCF execution to fail

:white_check_mark: Client/Server: Convert remote FTP time to local in FTP browser and download comparison


### 6.0.0 [2011-10-17]

#### Features

:star: Client/Server: Added Loop support for Tasks in Jobs

:star: Client/Server: Added the .NET code execute Task

:star: Client/Server: Added the .NET Condition

:star: Client/Server: Added List files Task

:star: Client: Some new features in the Variable window. Helps you pick up the Active and PrevTask Variables.

:star: Client/Server: Added support to base FTP upload on size comparison

:star: Client/Server: Added support for selecting multiple nodes in the XML Read Task

:star: Client/Server: Added support for loading a Variable instead of File in XML Read Task

:star: Client/Server: Added option to "post process" new name with a Variable in File Read Task

:star: Client: Added Task re-ordering through buttons in the grid (Edit Job->Tasks)


#### Bug Fixes


:white_check_mark: Server: Fixed a bug where files were not deleted in the Archive - Compress Task

:white_check_mark: Client: Fixed a crash when opening the web service Task

:white_check_mark: Server: Fixed a problem with VisualCron event deactivation

:white_check_mark: Server: Fixed a Credential problem in the XML Read Task

:white_check_mark: Server: Handled a potential crash when no Connection was specified in SQL Notification

:white_check_mark: API: Fixed a permission problem concerning multiple connections against the same Server (with same Client)

:white_check_mark: API: Fixed a problem where Allow AD logon settings where overwritten when stopping the VisualCron Server

:white_check_mark: Server: Fixed a possible synchronization problem in the core scheduling. Could cause scheduling to fail in some scenarios.

:white_check_mark: Server: Improved database logging performance - Tasks do no longer hang if db (disk performance) is slow

:white_check_mark: Client: Fixed a problem with closing tabs in the “FTP Explorer”

:white_check_mark: Client: Fixed a problem in the “Remote save files dialog”. The dialog could crash in some situations.


### 6.0.1 [2011-10-17]

#### Bug Fixes


:white_check_mark: Server: Fixed a problem with "Run Tasks in order". If you are using 6.0.0 we strongly suggest that you upgrade.


### 5.8.1 [2011-08-30]

#### Notes

:memo: This version requires that you install new version of both Client and Server


#### Features

:star: Client: Added options to change Client settings-,log- and backup folder

:star: Client/Server: Added options to change Server settings-,log-,output, temp and backup folder

:star: Client: Added optional confirmation dialog for Server->Stop action in Client settings

:star: Client/Server: Added detached signing option in PGP Encrypt Task

:star: Client/Server: Added support for multiple folders in all file filters. Separate folders with semi colon ";"

:star: Server: Treated powershell error output as VisualCron error


#### Bug Fixes


:white_check_mark: Server: Fixed a Variable problem in the Office Macro Task (Variables converted to static after first run)

:white_check_mark: API: Fixed some bugs related to internal events which could cause the test API project (among other things) to go beserk

:white_check_mark: Server: Fixed a problem with printing HTML documents

:white_check_mark: Server: Fixed a timezone bug - could potentially affect Interval triggers scheduled a longer time ahead


### 5.8.0 [2011-08-22]

#### Notes

:memo: This version requires that you install new version of both Client and Server

:memo: Please review your existing Archive Tasks as they have been upgraded


#### Features

:star: Client/Server: Archive Task was split into "Archive - Compress" and "Archive - Extract" Tasks

:star: Client/Server: Added support for extracting the following file types in the Archive - Compres Task:  7z, Gzip, Bz2, Xz

:star: Client/Server: Added support for extracting the following file types in the Archive - Extract Task:  7z, Gzip, Bz2, Xz, ARJ, CAB, CHM, CPIO, DEB, DMG, HFS, ISO, LZH, LZMA, MSI, NSIS, RAR, RPM, UDF, WIM, XAR and Z.

:star: Client/Server: Archive - Decompress now has option to extract several files according to file filter

:star: Client/Server: Added Timeout property to web/wcf Task

:star: Client/Server: Added destination file mask for the Copy file Task


#### Bug Fixes


:white_check_mark: Client: Fixed crash in main window that could happen if new server was selected while a Job was updating

:white_check_mark: Server: write-error command for writing to std error output in Powershell Task did not properly transfer output to the standard error value of the Task


### 5.7.9 [2011-08-12]

#### Features

:star: Client/Server: Added the Service Condition

:star: Client: Fixed better sorting of Conditions and Notifications


#### Bug Fixes


:white_check_mark: Client: Fixed a copy file issue with the Remote file explorer tool

:white_check_mark: Client: Handled an error in the trial registration window

:white_check_mark: Server: Fixed a Variable resolution error in the Web service Task

:white_check_mark: Server: Handled a .NET bug causing file filter to fail in special occasions


### 5.7.8 [2011-07-29]

#### Bug Fixes


:white_check_mark: Server: Fixed a infinite loop problem with "Go to Task" in combination with "Run following Tasks"

:white_check_mark: Server: Fixed an output reference problem in Task log

:white_check_mark: Server: Removed some debug logging

:white_check_mark: Client: Enabled a field in the XML Node Read Task

:white_check_mark: Client: Fixed a copy file issue with the Remote file explorer tool


### 5.7.7 [2011-06-23]

#### Features

:star: Client: Added the "Brute force" test connection tool for figuring out FTP connection settings


#### Bug Fixes


:white_check_mark: Client: Fixed a checkbox that prevented to change to Stop Job » Synchrous = false in Job/Task Control

:white_check_mark: Server: Removed new line in output of HTTP Task

:white_check_mark: Server: Fixed a potential server crash problem with the Kill Task


### 5.7.6 [2011-06-14]

#### Features

:star: Client/Server: Added remote server (VisualCron) execution in Job/Task control for Run Job/Task

:star: Client/Server: Added remote server (VisualCron) Trigger


#### Bug Fixes


:white_check_mark: Client/API: Fixed an issue with listing remote services in Service Trigger


### 5.7.5 [2011-05-27]

#### Notes

:memo: This version requires that you install new version of both Client and Server

:memo: This version requires at least .NET Framework version 3.5


#### Bug Fixes


:white_check_mark: Client: Fixed a bug in the Condition set list when moving between Tasks

:white_check_mark: Server: Fixed a license issue (problem with remembering activation)

:white_check_mark: Server: Fixed an issue with Credentials in Print Task

:white_check_mark: Server: Fixed an issue with exit code for Tasks in the Task history

:white_check_mark: Server: Fixed a Credential issue in the Office Macro Task

:white_check_mark: Server: Fixed a bug where a file could be delete even though it was not successfully copied

:white_check_mark: Server: Fixed an issue with System startup Trigger that could prevent VisualCron service to start if Job ran for a long time

:white_check_mark: Server: Added support for RunSynchrous on Job/Task Control->Stop Job

:white_check_mark: Client/Server: Fixed a time zone issue when working with a client and server in different time zones

:white_check_mark: Client: Fixed an issue with reloading parameters in Assembly/Web service Execute Task

:white_check_mark: Client/API: Fixed an issue with showing output Variables for the first time in the Variables browser


### 5.7.4 [2011-04-07]

#### Features

:star: Client/Server: Added the PowerShell Task

:star: Server: VisualCron now executes Jobs (once) that *should* have been executed within a DST change period, i.e. 2:01 AM when change goes from 2 AM to 3 AM

:star: Server: Added On/Off setting for database logging


#### Bug Fixes


:white_check_mark: Server: Fixed 64 bit issue in Office Macro Task

:white_check_mark: Client: Illegal characters in Execute Task command caused crash

:white_check_mark: Client: Fixed compatibility issue with old Web service Tasks

:white_check_mark: Client: Fixed crash in Set Variable Task when wrong type was used


### 5.7.3 [2011-04-01]

#### Bug Fixes


:white_check_mark: Client/Server: Fixed a FTP parsing problem with gene6 FTP server

:white_check_mark: Client: Fixed a crash when trying to re-order Copy File items after deleting one

:white_check_mark: Client: Improved speed when right clicking on a Task in a list of many Jobs

:white_check_mark: Server: Fixed a Credential problem on the Web service Task

:white_check_mark: Server: Handled an error in Execute output

:white_check_mark: Server: Fixed an installation problem

:white_check_mark: Server: Fixed a problem with Execute Task hanging in some situations

:white_check_mark: Server: Fixed a Credential problem in the Archive->Extract method


### 5.7.2 [2011-03-28]

#### Features

:star: Client/Server: Historic general/Job/Task log functionality

:star: Client/Server: Added exit code Variable to Job

:star: Server: Added list of file to Touch file Task Output

:star: Server: IPV6 support on server port

:star: Client/Server: Added Credential support for Mail Trigger

:star: Client/Server: Added net.tcp and other alternate protocols for WCF execution


#### Bug Fixes


:white_check_mark: Client: Fixed a parsing problem with some FTP servers

:white_check_mark: Server: Fixed a bug in the FTP Delete files when using file mask in the path

:white_check_mark: Server: Fixed a problem with deleting empty sub folders in Delete File Task

:white_check_mark: Client/Server: Fixed a parsing bug in FTP file listing

:white_check_mark: Server: Handled an error that could arise in the Event Service Trigger

:white_check_mark: Server: Fixed problem with ODBC Job execution in SQL Task

:white_check_mark: Client/Server: V6R1M0 ftp parsing error fixed

:white_check_mark: Client/Server: Fixed a client certificate bug in FTP Task and FTP Explorer

:white_check_mark: Client: Fixed a Variable validation problem in SQL Task when adding a parameter with Variable

:white_check_mark: Server: Fixed PDF printing issue


### 5.7.0 [2010-11-23]

#### Features

:star: Client: Added support for Contains, Not contains, Regex match, Regex - no match in Variable Condition

:star: Client/Server: Added Job Group Variable


#### Bug Fixes


:white_check_mark: Client/Server: Added String.WordWrap function

:white_check_mark: Client: Fixed some cloning bugs in the Connection window (cloning SQL connections)

:white_check_mark: Client: Fixed a problem with saving settings in Excel - Get cell Task

:white_check_mark: Server: Fixed internal VisualCron event "Server status changed to On" which did not work properly

:white_check_mark: Server: Fixed PDF printing problems on x64 systems

:white_check_mark: Server: Fixed a problem with update of Job status when using the Job Control Task

:white_check_mark: Server: Fixed a bug in the Restart server Task

:white_check_mark: Server: Fixed PrevTask and Active Task Variable so they can be used in Job Notification (will be the last run Task)

:white_check_mark: Client/Server: Fixed an API deadlock that could occur when calling methods within events

:white_check_mark: Server: Fixed an issue with expire after number of times in Trigger

:white_check_mark: Server: Default working directory changed to current directory when running with Credentials

:white_check_mark: Server: Fixed a bug in SQL parameter values when using Variables (length problem)


### 5.6.9 [2010-09-21]

#### Bug Fixes


:white_check_mark: API/Server/ClientI: Fixed a license problem (maintenance expired)

:white_check_mark: Client/Server: Fixed a security issue with Active Directory logon method


### 5.6.8 [2010-09-15]

#### Bug Fixes


:white_check_mark: Client/Server: Fixed a weeknumber Variable bug

:white_check_mark: Client/Server: Fixed a next run calculation bug

:white_check_mark: Server: Fixed a log problem with user name when using AD

:white_check_mark: Client/Server: Fixed a Run Job bug when using Job/Task control Task

:white_check_mark: API/Server: Fixed a problem which could cause a crash when using the Foreground Task

:white_check_mark: Server: Fixed a problem with SSIS Task when executing package in database


### 5.6.7 [2010-09-02]

#### Features

:star: Client/Server: Added Excel - Convert Task

:star: Client/Server: Added Excel - Get row count Task

:star: Client/Server: Added Concatenate files Task

:star: Server: Added runtime Variables for unique runtime Job Id and runtime Job Counter


#### Bug Fixes


:white_check_mark: Client: Fixed a a crash when cloning SQL Notifications

:white_check_mark: Client/Server: Fixed some bugs in Excel - Read cell Task


### 5.6.6 [2010-08-20]

#### Features

:star: Client/Server: Added Excel read cell Task

:star: Client/Server: Added namespace support for XML Read Task


#### Bug Fixes


:white_check_mark: Client/API: Fixed a bug where a user could update her/his own permissions

:white_check_mark: Client: Fixed a problem with SSH/Terminal Explorer being slow

:white_check_mark: Client: Fixed a UI problem with the Event log Trigger and Category operator

:white_check_mark: Server: Fixed a problem with the Event log Trigger where Event type was not matching correctly


### 5.6.5 [2010-08-03]

#### Features

:star: Client: Added Active Directory filter for searching groups/users


#### Bug Fixes


:white_check_mark: TrayClient: Settings are now saved in Local application data folder

:white_check_mark: Server: Fixed a problem deleting empty sub folders in File Delete Task

:white_check_mark: Client: Fixed some issues in Permissions (Add) created in 5.6.4.


### 5.6.4 [2010-07-23]

#### Features

:star: Client/Server: Added Active Directory integration

:star: Client/Server: Added Event log Task

:star: Client/Server: Added error that is raised when no files are copied in Copy files Task. Change this new behavior in On error tab.


#### Bug Fixes


:white_check_mark: Client/Server: Fixed minor generic decryption problem

:white_check_mark: Server: Fixed V5R4M0 FTP raw interpretation

:white_check_mark: Server: Fixed problem with overwriting files in WebDAV Upload Task


### 5.6.3 [2010-07-14]

#### Features

:star: Client/Server: Added synchronous operation option in Job/Task control Task


#### Bug Fixes


:white_check_mark: Server: Fixed a bug concerning Custom filter in Activate Directory List Object Paths Task

:white_check_mark: Client: Fixed a display problem with the interval of the Mail Trigger

:white_check_mark: Server: Handled error 105 in SFTP Task

:white_check_mark: Server: Fixed a Credential bug in FTP download Task

:white_check_mark: Server: Fixed a problem when using Variables in the destination file mask of PGP Decrypt Task


### 5.6.2 [2010-06-29]

#### Bug Fixes


:white_check_mark: Server: Fixed a Variable problem with Working directory property in Execute Task

:white_check_mark: Server: Fixed a problem which could cause a crash if a Connection was not found at start


### 5.6.1 [2010-05-31]

#### Features

:star: Client/Server: Credential is moved to the File filter (where available)

:star: Client/Server: Added support for wild cards (*?) in File filter (where available)

:star: Client/Server: Added support for multiple file inclusion/exclusion file masks in File Filter (where available). Use semicolon ; to separate

:star: Client/Server: Added "Create full folder structure" for Copy files Task:  If folder structure from drive letter should be created in destination folder

:star: Client/Server: Credential support for Rename Task

:star: Client/Server: Credential support for Print document Task

:star: Client/Server: PGP Task split into two Tasks, Encrypt and Decrypt

:star: Client/Server: Added SSIS execution in 32 bit mode setting

:star: Client/Server: Added Serial Send Task

:star: Client/Server: Added WebDAV - Upload (SharePoint) Task

:star: Client/Server: Added WebDAV - Delete (SharePoint) Task

:star: Client: Added list of event log names to Event log Trigger


#### Bug Fixes


:white_check_mark: Server: Fixed an update problem with the Set Variable Task

:white_check_mark: Server: Fixed a problem with auto detection of document in Print Task.


### 5.6.0 [2010-05-23]

#### Bug Fixes


:white_check_mark: Client: Fixed an UI error in the Interval time trigger - specific days of the month

:white_check_mark: Client: Fixed a bug in the UI of HTTP Task preventing saving content when using POST method

:white_check_mark: Client: Fixed a crash when switching between Condition types

:white_check_mark: Server: Handled a problem in PGP Task that could occur if original file name for decryption is empty

:white_check_mark: Server: Handled a problem in PGP Task. End of data error.

:white_check_mark: Server: Fixed a bug in folder check Condition (null reference error)

:white_check_mark: Server: Fixed a startup problem connected to running missed Jobs


### 5.5.9 [2010-05-10]

#### Features

:star: Client/Server: Added optional event log logging of server events

:star: Client/Server: Added Tasks to Active Job node in Variables

:star: Client/Server: Added support for paranthesis () in Variables


#### Bug Fixes


:white_check_mark: Client: Fixed an error when trying to import certificates in the Manage Certificates window

:white_check_mark: Client: Fixed a display problem of the new work day Trigger from last version

:white_check_mark: Server: Fixed a problem with translating Variable to constant in Set Variable Task

:white_check_mark: Server: Fixed some issues with PrevTask combinations with the new result Variables from FTP and Copy file Task

:white_check_mark: Server: Fixed a Variable problem with SFTP change folder Task


### 5.5.8 [2010-04-23]

#### Features

:star: Client/Server: Added support for 1st to 22th workday


#### Bug Fixes


:white_check_mark: Server: Fixed a timeout problem when starting the VisualCron service


### 5.5.7 [2010-04-22]

#### Features

:star: Client: Added a lot of internal Trigger events to the VisualCron Trigger


#### Bug Fixes


:white_check_mark: Client: Handled path error in attachment of Email Task when using "illegal characters" in the path

:white_check_mark: Client: Fixed a crash when an assembly with no method was selected in the Assembly Execute Task

:white_check_mark: Server: Fixed a problem with replacing dll's used by the Assembly Execute Task

:white_check_mark: Server: SSH Task - port property was not set properly

:white_check_mark: Server: Fixed a problem with HELO/EHLO message in SMTP where remote address was sent instead of local


### 5.5.6 [2010-04-07]

#### Features

:star: Server: Added SNMP Tasks: Get, Get Next, Get Bulk, Walk and Set

:star: Client/Server: Added Variables for files downloaded/uploaded for FTP Task

:star: Client/Server: Added Variables for files copied for Copy files Task

:star: Client/Server: Added PrevTask Variable

:star: Client/Server: Added comma for line break in SQL Task (output)


#### Bug Fixes


:white_check_mark: Server: Fixed a COM problem with the SSIS Execute Task


### 5.5.5 [2010-03-04]

#### Bug Fixes


:white_check_mark: Client: Fixed a problem showing file properties in local browser in FTP Explorer on 64 bit systems

:white_check_mark: Client: Fixed a problem showing the object relations window

:white_check_mark: Client: Fixed a problem with deselecting Notifications when moving between Tasks

:white_check_mark: Client: Fixed a problem with deselecting Conditions when moving between Tasks

:white_check_mark: Server: Fixed a problem with Task output on Set Variable Task (which was one change behind when updating)


### 5.5.4 [2010-02-25]

#### Features

:star: Server: Added custom parsing for GSX FTP servers

:star: Server/Client: Added support for retrieving XML from Event log entry and using that result Variable

:star: Client: Added PGP key paste when creating PGP key rings

:star: Client: Added private key export to Manage PGP key rings

:star: Client: Added right click option to Execute Job with Conditions (default no Conditions are being checked when run manually)


#### Bug Fixes


:white_check_mark: Client: FTP Explorer was not totally cleaned up (when closing the window using Telnet/SSH)

:white_check_mark: Client: Fixed some minor issues like problems with home dir and UNIX listing in FTP Explorer

:white_check_mark: Client: Fixed a problem showing set PGP recipients and signers in PGP Task when a license key was not set

:white_check_mark: Client: Re-added security settings for SMTP connection which was accidently removed in earlier version

:white_check_mark: Client: Handled an error in the log viewer

:white_check_mark: Server: Fixed a problem reading some XML files with namespaces in XML Read Node Task


### 5.5.3 [2010-02-08]

#### Bug Fixes


:white_check_mark: Client: Fixed a bug in saving stored procedures for Direct MySQL and Direct Oracle

:white_check_mark: Client: Fixed a problem with re-ordering Tasks

:white_check_mark: Client: Fixed a problem with displaying the "destination filemask" on the PGP Task

:white_check_mark: Client: Fixed some connection issues in the FTP Explorer

:white_check_mark: Server: Fixed a problem with return ExitStatus in SSH Task

:white_check_mark: Server: Fixed a performance problem in SSH Task (during wait process could experience high load)

:white_check_mark: Server: Fixed a timeout problem in SSH Task (timeout property was not set and it was using default 30 seconds)


### 5.5.2 [2010-01-29]

#### Features

:star: Client/Server: Added proxy setting "Use Proxy For Data Channel" option

:star: Client/Server: Added FTP PASV setting "AdjustPasvAddress"

:star: Client: Added proxy support for FTP in FTP Explorer

:star: Client: Added support for FTP servers with uncommon format


#### Bug Fixes


:white_check_mark: Server: Fixed a memory leak in the SSH Task

:white_check_mark: Server: Fixed a problem with proxy settings for FTP connection (all settings were not fully applied)

:white_check_mark: Server: Fixed a problem with uncommon FTP servers in FTP Task

:white_check_mark: Client/Server: Fixed a minor calculation problem in the Custom Time Trigger

:white_check_mark: Client: Fixed a bug in Desktop Macro Task when recording twice


### 5.5.1 [2010-01-22]

#### Notes

:memo: This version breaks previous protocol and requires upgrade of both Client and Server


#### Features

:star: Client/Server: New Task "Assembly execute" - execute methods within .NET exe's or dll's

:star: Client/Server: New Task "Web service/WCF execute" - execute methods in web or WCF services

:star: Client/Server: Added separate proxy support for HTTP Task


#### Bug Fixes


:white_check_mark: Client: Fixed a problem with displaying the condition in the Performance Trigger

:white_check_mark: Client: Fixed a problem with displaying correct data type in SQL Task (parameter)

:white_check_mark: Client: Fixed a validation problem against correct data type in SQL Task (parameter)

:white_check_mark: Client: Fixed a problem saving the SQL parameter the first time in SQL Task

:white_check_mark: Client: Fixed a problem with Copy/Paste Jobs/Task when this was done twice with same object

:white_check_mark: Server: Fixed some issues with the File Trigger and "Trigger when released" when working against a drive on the network


### 5.5.0 [2010-01-16]

#### Features

:star: Client/Server: Added field separator "None" to SQL output Task

:star: Client/Server: Added option to Set Variable Task: Translate to constant Variable


#### Bug Fixes


:white_check_mark: Server: Fixed a null reference error at xFTPx.Disconnect

:white_check_mark: Server/TrayClient: Fixed an issue with Desktop Macro Task on x64 systems

:white_check_mark: Server: Fixed an issue with auto logon on x64 systems

:white_check_mark: Server: Some further cleanup in SSH Task

:white_check_mark: Client: Fixed a problem with highlighting and performance in SQL highlighter in SQL Task

:white_check_mark: Client: Fixed a problem which could prevent the button "Get full output" in output window being enabled


### 5.4.9 [2009-12-22]

#### Features

:star: Client/Server: Added Get button to retrieve Stored procedures in SQL Task


#### Bug Fixes


:white_check_mark: Client/Server: General fixes to Exchange Tasks

:white_check_mark: Client: Fixed a cloning bug when Job status was not reset (if Job was running)

:white_check_mark: Server: Handled desktop lock/logoff bug when no Connection is found

:white_check_mark: Client/Server: Fixed support for MAX in SQL Task


### 5.4.8 [2009-12-17]

#### Features

:star: Client/Server: New Task "Create Exchange Object"

:star: Client/Server: New Task "Get Exchange Object(s)"

:star: Client/Server: New Task "Modify Exchange Object"

:star: Client/Server: New Task "Delete Exchange Object"

:star: Client/Server: New Task "Delete Exchange Object(s)"

:star: Client/Server: Added On error option for Unhandled FTP reply

:star: Server: Added support for very simple custom FTP parsing

:star: Server/API: Added exit code to JobEnded event


#### Bug Fixes


:white_check_mark: API: Fixed Modified by and Created by properties when adding/updating a Job

:white_check_mark: Client: Fixed an update problem of Next run in the Job add dialog

:white_check_mark: Client: Fixed a problem in Server edit dialog (when not connected)

:white_check_mark: Client: Fixed a cloning bug in Conditions

:white_check_mark: Server: Fixed a problem with killing process tree (Execute/Kill Task)

:white_check_mark: Server: Fixed a problem with Retry waiting one too many times

:white_check_mark: Server: Fixed a problem with Retry return success on Job on last failing Task

:white_check_mark: Server: Fixed a problem with Previous Job (Auto) in VisualCron Condition

:white_check_mark: Server: Fixed a problem with Desktop Lock and User Logoff (foreground execution) for Windows 2003

:white_check_mark: Client/Server/API: Fixed TempPath Variable

:white_check_mark: Client: Fixed a problem in Guide (StyleAPI)


### 5.4.7 [2009-11-28]

#### Features

:star: Client/Server: Added Trigger "System start/shutdown"

:star: Client/Server: Added Trigger "Performance counter"

:star: Client/Server: Added TLS and explicit/implicit method for SMTP (Google SMTP requirements TLS+implict+port 465). Note, if you previously used SSL in IMAP/POP3/SMTP you need to select SSL in Encryption tab of Connection settings and press update on your Connection


#### Bug Fixes


:white_check_mark: Client/Server: Fixed a problem updating Server off status for inactive Jobs

:white_check_mark: Server: Now ignoring FTP reply 250

:white_check_mark: Server: Now ignoring FTP reply 257


### 5.4.6 [2009-11-25]

#### Features

:star: Client/Server: Added Trigger "RSS Trigger"

:star: Server: Added auto error reporting for Server


#### Bug Fixes


:white_check_mark: API: Fixed RegAsm problem when preparing for COM

:white_check_mark: Server: Fixed an unhandled error in Output

:white_check_mark: Server: Fixed an unhandled error in FTP


### 5.4.5 [2009-11-18]

#### Features

:star: Client: Added support for Credentials when using "Test file filter"


#### Bug Fixes


:white_check_mark: Client: Optimized height of Job items in Calendar

:white_check_mark: Client: Moved Client and VCTray settings to localapplicationfolder/settings. Moved log files for those to localapplicationfolder/log

:white_check_mark: Client: Fixed Variable display in Set-,Remove-,Calculate Variable Tasks

:white_check_mark: Client: Small UI error when going from week->day or month->day (selected button)

:white_check_mark: Server: Fixed a problem with destination file name in PGP Task (encryption)

:white_check_mark: Server: Fixed a problem with network drive mapping

:white_check_mark: Server: Now ignoring FTP reply 200

:white_check_mark: Server: Now ignoring FTP reply 553


### 5.4.4 [2009-11-15]

#### Bug Fixes


:white_check_mark: Server: Handled missing Notifications and Conditions in Flowchart

:white_check_mark: Server: Now ignoring FTP reply 426

:white_check_mark: Server: Now ignoring FTP reply 502

:white_check_mark: Server: Fixed reset of failure when Task first failed and then retried with success

:white_check_mark: Client: Fixed Object search not returning all objects

:white_check_mark: Client: Fixed and issue with Standard error in the output window

:white_check_mark: Server: Fixed a problem with Execute task "Handle is invalid"


### 5.4.3 [2009-11-11]

#### Bug Fixes


:white_check_mark: Server: Fixed a bug when reading null output

:white_check_mark: Server: Fixed a memory problem in output


### 5.4.2 [2009-11-10]

#### Features

:star: Client: Grouping->Dragging Jobs locally does no longer Clone but Move to group

:star: Client: Grouping->Clone/Copy will now move the Job to the targer group


#### Bug Fixes


:white_check_mark: Client: Fixed an icon problem in Windows 7 for the FTP Explorer

:white_check_mark: Server: Fixed a bug when saving null output

:white_check_mark: Server: Fixed a memory problem in output


### 5.4.0 [2009-11-09]

#### Features

:star: Client/Server/API: Optimized output handling

:star: Client: Choose from Text, HTML, XML in output window

:star: Client/API: Added Clone function to Notifications

:star: Client/Server: Added timeout and retry function for Mail Trigger


### 5.4.1 [2009-11-09]

#### Features

:star: Client: Grouping->Added context sensitive "Add Job" so that new Job gets the group depending in which group you click "Add Job"

:star: Client: Grouping->Added multiple selection

:star: Client: Grouping->Multi selection when clicking on group

:star: Client: Grouping->Added group rename when right clicking at group

:star: Client: Grouping->Added multiple selection delete Jobs/Tasks

:star: Client: Grouping->Added multiple selection activate/inactivate Jobs/Tasks


### 5.3.9 [2009-11-06]

#### Features

:star: Client: Added the FTP/SSH/Telnet explorer


#### Bug Fixes


:white_check_mark: Server: Fixed a Job deadlock in the API


### 5.3.8 [2009-11-04]

#### Features

:star: Client: Added the schedule calendar


#### Bug Fixes


:white_check_mark: Server: Fixed a Job deadlock in the API


### 5.3.7 [2009-10-28]

#### Bug Fixes


:white_check_mark: Server: Fixed a problem with Event log Trigger when using event type

:white_check_mark: Server: Fixed a problem with changing FTP path

:white_check_mark: Server: Now ignoring FTP reply 226

:white_check_mark: Server: Fixed "size type" problem in file filter (kB etc.)

:white_check_mark: Client: Fixed sort order in Job/Task control to Order instead of Name


### 5.3.6 [2009-10-23]

#### Bug Fixes


:white_check_mark: Server: Fixed a in file filter regarding regexp


### 5.3.5 [2009-10-22]

#### Bug Fixes


:white_check_mark: Server: Fixed an unhandled error when no source folder was specified in PGP Task

:white_check_mark: Server: Fixed and unhandled FTP reply (425 and 150)


### 5.3.4 [2009-10-09]

#### Features

:star: Client/Server: Changed support from 3 to 4 levels of Variable searching


#### Bug Fixes


:white_check_mark: Server: Fixed and unhandled FTP reply (213)

:white_check_mark: Server: Fixed a exit code handling problem in Execute Task

:white_check_mark: Server: Fixed date Variable parsing


### 5.3.3 [2009-10-03]

#### Features

:star: Server: Added ftp support for: V5R4M0, V6R1M0, V5R3M0, VMS MultiNet


#### Bug Fixes


:white_check_mark: Client: Handled a flow chart bug

:white_check_mark: Server: Handled UNIX Type: L8 parse error

:white_check_mark: Server: Fixed handling of more than one Variable in File Filter

:white_check_mark: Server: Mixed fixes for File Trigger with polling

:white_check_mark: Server: Fixed that Export settings is overwriting old file

:white_check_mark: Server: Fixed a disconnection problem in SFTP/FTP

:white_check_mark: Server: Handled an unhandled error in Event log Trigger


### 5.3.2 [2009-08-23]

#### Features

:star: Client: Added Jabber protocol support in Instant Messenger Task


#### Bug Fixes


:white_check_mark: Server: Fixed a bug regarding closing objects in Office Macro Task

:white_check_mark: Server: Fixed a bug regarding result objects in Mail Event

:white_check_mark: Client: Fixed some minor bugs in the flow chart


### 5.3.1 [2009-08-03]

#### Bug Fixes


:white_check_mark: Client: Fixed a GUI bug that appeared when selecting Tasks


### 5.3.0 [2009-07-31]

#### Features

:star: Client: Added Job flow chart (beta)

:star: Client: Added object search dialog

:star: Client: Added object relations dialog

:star: Client: Now sorting Jobs in Report dialog


#### Bug Fixes


:white_check_mark: Server: Fixed a bug saving Server log settings

:white_check_mark: Server: Fixed a bug regarding private key in SSH Task

:white_check_mark: Server: Fixed a bug in Instant messaging Task regarding proxy

:white_check_mark: Server: Fixed a bug regarding transferring Email Notification Attachment settings from 4 -> 5

:white_check_mark: Server: Ignored Reply error on MVS servers (FTP)

:white_check_mark: Client: Fixed a bug regarding cloning SQL Connections

:white_check_mark: Client: Handled a bug in Remote file browser


### 5.2.2 [2009-07-19]

#### Features

:star: Client/Server: Added Active Directory Task - Create group

:star: Client/Server: Added Active Directory Task - Create object

:star: Client/Server: Added Active Directory Task - Create user

:star: Client/Server: Added Active Directory Task - Delete object

:star: Client/Server: Added Active Directory Task - Get group members

:star: Client/Server: Added Active Directory Task - Get object path

:star: Client/Server: Added Active Directory Task - List object paths

:star: Client/Server: Added Active Directory Task - Modify group

:star: Client/Server: Added Active Directory Task - Modify user

:star: Client/Server: Added Active Directory Task - Move object

:star: Client/Server: Added Active Directory Task - Rename object

:star: Client/Server: Added Active Directory Task - Set object property

:star: Client/Server: Added Foreground support to Send Keys Task


#### Bug Fixes


:white_check_mark: Server: Fixed issue with Credentials in Execute Script Task

:white_check_mark: Server: Fixed issue encoding in FTP Task

:white_check_mark: Server: Fixed support for MVS servers (FTP Task)


### 5.2.1 [2009-07-09]

#### Features

:star: Client/Server: Added Instant Message Task for Yahoo, GTalk, ICQ, AIM and MSN


#### Bug Fixes


:white_check_mark: Client: Fixed a GUI problem with the SSH Task

:white_check_mark: Client: Fixed sort order of Tasks in Variables

:white_check_mark: Server: Fixed from with email time encoding in Email Task


### 5.2.0 [2009-06-30]

#### Features

:star: Client/Server: Added XML Read Node Task

:star: Client/Server: Added XML Edit Node Task

:star: Client/Server: Added XML Delete Node Task


#### Bug Fixes


:white_check_mark: Server: Fixed a problem where exit code on Copy Files Task was not reported correctly on error


### 5.1.9 [2009-06-25]

#### Bug Fixes


:white_check_mark: Server: Fixed a problem with deleting sub empty sub folders in Delete Files Task.

:white_check_mark: API: Removed some warnings

:white_check_mark: Client: Fixed some GUI bugs in HTTP Task

:white_check_mark: Client: Fixed a problem with testing a Job (unique Id in grid)

:white_check_mark: Server: Fixed a bug in Email Trigger with custom folder

:white_check_mark: Client: Fixed a problem with downloading latest version and max version (according to license)


### 5.1.8 [2009-06-24]

#### Bug Fixes


:white_check_mark: Server: Handled a crash in the SysLog Notification

:white_check_mark: Server: FileNotFound error is now raised in Execute script (if file is not found)


### 5.1.7 [2009-06-03]

#### Bug Fixes


:white_check_mark: Server: Fixed an problem intepreting UNIX Type: L8 FTP servers

:white_check_mark: Server: Changed behavior with Job.Exited Variable. This Variable is now set before Notifications are sent

:white_check_mark: Server: Fixed double incremental of Variable NoExecutes in Archive and Copy files Task


### 5.1.6 [2009-06-02]

#### Features

:star: Client: Added CC and BCC to Email Task (please update all Email Tasks that referred to a file)

:star: Client: Added Job Result to Report generator

:star: Client: Added more decriptive "Next run" (when using Event Triggers)

:star: Client/API: Added optional Condition Check when running manually. From now on Conditions are not checked when Jobs or Tasks are being run manually.


### 5.1.5 [2009-05-25]

#### Features

:star: Client: Added File/HTTP Upload to HTTP Task


#### Bug Fixes


:white_check_mark: Client: Fixed some GUI errors in HTTP Task

:white_check_mark: Client: Fixed a missing print dll which could cause printing problems on some systems

:white_check_mark: Client/API/Server: Fixed last trigger Variable for Time triggers


### 5.1.4 [2009-05-24]

#### Features

:star: Client: Added Job/Task printing/report

:star: Client/Server: Added support for ACCT for FTP Connections

:star: Client: Added confirmation boxes to drag/drop of Jobs/Tasks


#### Bug Fixes


:white_check_mark: Client/Server: Fixed issue with 1 hour time interval trigger

:white_check_mark: Client: Fixed issue when using c:\ or d:\ etc as source folder in file filter

:white_check_mark: Client: Fixed issue when cutting Task from one server to another (source Task was not removed)

:white_check_mark: Client: Handled an error in Background/Foreground selection (if no Credential was selected)

:white_check_mark: Client: Handled an error in the SQL syntax control

:white_check_mark: Client/Server/API: Fixed an error in DATEFORMAT in FileFilter


### 5.1.3 [2009-05-10]

#### Features

:star: API: Server.Import function for import of server settings in API

:star: Client: Added services listing at different places

:star: Client: Added users listing at different places

:star: Client: Added computers listing at different places


### 5.1.2 [2009-05-03]

#### Features

:star: Server: Added NonZeroExit code handling for foreground and background Execute


#### Bug Fixes


:white_check_mark: Server/Client: Fixed a calculation problem 3 hour Interval

:white_check_mark: Client: Fixed a problem in the Variables window with cloned Tasks

:white_check_mark: API: Fixed {DATE(Month.Name)} Variable

:white_check_mark: Server: Ending semicolon in email Notification could cause problems

:white_check_mark: Client: Optimized the SQL query text box

:white_check_mark: Server: Fixed problem with relative paths within zip file in Archive Task


### 5.1.1 [2009-04-19]

#### Features

:star: Server: Kill and Timeout now kills whole process tree (child processes)

:star: Server: Added support for DATEFORMAT Variable in date comparison

:star: Server: Added PermissionDenied error handling for File delete Task

:star: Server: Added IOException error handling for File delete Task

:star: Server: Added PermissionDenied error handling for Copy files Task

:star: Server: Added UnahandledException error handling for Copy files Task

:star: Server: Added IOException error handling for Copy files Task

:star: Server: Added String.GUID Variable


#### Bug Fixes


:white_check_mark: Server: Fixed a problem with anonymous FTP servers

:white_check_mark: Client/Server/API: Fixed a problem with editing and changing own password in Permissions

:white_check_mark: Client: Fixed a GUI error with SSL switching in Connections

:white_check_mark: Client/Server: Reverted back to original handling of public key authentication in SFTP


### 5.1.0 [2009-04-01]

#### Bug Fixes


:white_check_mark: Server: Fixed a mail Trigger Variable

:white_check_mark: Server: Fixed a problem with sourcefolder being creating in SFTP (upload) destination folder (instead of content of source folder)


### 5.0.8 [2009-03-31]

#### Bug Fixes


:white_check_mark: Server: Fixed a problem which could occur when creating folders in FTP task

:white_check_mark: Server: Fixed a problem with sourcefolder being creating in FTP (upload) destination folder (instead of content of source folder)

:white_check_mark: Server: Added support for custom parsing of FTP: Windows_NT version 5.0


### 5.0.9 [2009-03-31]

#### Bug Fixes


:white_check_mark: Server: Further tuning on FTP folder creation

:white_check_mark: Server: Removed trailing slash in Copy files Task which could cause compatibility issues between version 4 and 5


### 5.0.7 [2009-03-26]

#### Bug Fixes


:white_check_mark: Server: Fixed a problem with Copy files Task

:white_check_mark: Client: Changed to SaveFileDialog from OpenFileDialog in Export settings Task


### 5.0.6 [2009-03-24]

#### Bug Fixes


:white_check_mark: Server: Fixed parsing issues in FTP


### 5.0.5 [2009-03-21]

#### Features

:star: Server: Added a custom FTP parser for DDS FTP

:star: API: Added GetUserName function in API to get decrypted user name


#### Bug Fixes


:white_check_mark: API: Fixed problem with activating through the API

:white_check_mark: Server: Fixed a problem in Conditions concerning Run Task

:white_check_mark: Server: Fixed a problem with Retry in On Error

:white_check_mark: Server/API: Better connection handling


### 5.0.4 [2009-03-10]

#### Bug Fixes


:white_check_mark: Client/API/Server: Improved handling of characters when using RegEx functions

:white_check_mark: Server: Handled an unhandled FTP error

:white_check_mark: Installation: Fixed a problem of a missing file that could cause installation errors


### 5.0.3 [2009-03-07]

#### Features

:star: Client: Improved loading of Job Variables in Variables window

:star: Client/Server/API: Added RegExp Match and Replace functions in Variables

:star: Client/Server/API: Added the following String Variables: TrimStart, TrimEnd , Left, Right, Length, IndexOf, IsEmptyOrNull, RowCount, CountOccurencies


#### Bug Fixes


:white_check_mark: Client: Fixed some issues with deleting SQL connections from the SQL Explorer window


### 5.0.2 [2009-02-23]

#### Bug Fixes


:white_check_mark: Client: Fixed a FileFilter initialization problem.

:white_check_mark: Client: Fixed a problem with rename/new folder in remote folder browser dialog


### 5.0.1 [2009-02-19]

#### Bug Fixes


:white_check_mark: Install: Fixed some minor installation problems


### 5.0.0 [2009-02-17]

#### Bug Fixes


:white_check_mark: Install: Now installing in \VisualCron\ folder instead of \VisualCron 4\. Service is now named "VisualCron" and not "VisualCron 4". Settings are moved through guide.

:white_check_mark: Server: Fixed a problem with reading large files (File read Task) even though limit output was used

:white_check_mark: Client: Fixed a SQL Connection clone bug

:white_check_mark: Server: Fixed a possible codepage problem in FTP/S

:white_check_mark: Server: Handled an error when stopping (already stopped service) or when starting (already started service)


### 4.9.58 [2009-02-11]

#### Bug Fixes


:white_check_mark: Server: Fixed a problem with displaying modified by / created by

:white_check_mark: Client: Fixed a problem with loading SQL connection data

:white_check_mark: Client/Server: TimeTrigger->Last day in month had an update problem


### 4.9.57 [2009-02-01]

#### Features

:star: Client/Server: Added File Filter to Copy files Task

:star: Client/Server: Added File Filter to PGP Task

:star: Client/Server: Added better support for encrypting/decrypting to a destination folder with rename file mask


#### Bug Fixes


:white_check_mark: Client: Fixed a problem adding a new Server


### 4.9.55 [2009-01-29]

#### Bug Fixes


:white_check_mark: Install: Fixed problem on x64 systems with starting VC Tray application after install

:white_check_mark: Server: Fixed a bug in FTP upload concerning upload path


### 4.9.56 [2009-01-29]

#### Bug Fixes


:white_check_mark: Client: Fixed a UI bug concerning Delete source files in FTP upload

:white_check_mark: Server: Fixed a bug with Variables in Notification


### 4.9.54 [2009-01-27]

#### Bug Fixes


:white_check_mark: Server: Fixed Job Variables bug in File Filter


### 4.9.53 [2009-01-26]

#### Features

:star: Client/Server/API: Added test filter function (does not work with Credentials yet)

:star: Server: Added cookie handling support in HTTP Task


#### Bug Fixes


:white_check_mark: Client/Server/API: Fixed JulianYearDay and JulianDay Variable

:white_check_mark: Server: Fixed a bug in the exclusion filter of the File Filter

:white_check_mark: Client/Server/API: Fixed some Variables that were moved because of the File Filter

:white_check_mark: Client: Fixed an UI problem in Archive Task (password saving)

:white_check_mark: Client: Fixed an UI bug in export settings


### 4.9.52 [2009-01-22]

#### Features

:star: Client/Server: Added File Filter to FTP upload Task

:star: Client/Server: Added File Filter to Archive Task

:star: Client/Server: Added File Filter to Email attachments

:star: Client/Server: Added File Filter to File Touch Task

:star: Client/Server: Added File Filter to File Print Document Task

:star: Client/Server: Added File Filter to File Rename Task

:star: Client/Server: Added rename "mask" ?* to Rename Task

:star: Client/Server: Added File Filter to File Delete Task

:star: Client/Server: Added "Delete sub folders" property to File Delete Task

:star: Server: Added default Job for deleting old log files


#### Bug Fixes


:white_check_mark: API: Handled problem: "Port busy. All pipes are busy."


### 4.9.47 [2009-01-02]

#### Bug Fixes


:white_check_mark: Server: FTP/S password is now hidden in communication

:white_check_mark: Server: Fixed issues where Retry loops prevented stopping Job manually

:white_check_mark: Server: Fixed a problem where the "Trial period is over" could popup at startup


### 4.9.45 [2008-12-31]

#### Features

:star: Client/Server:  Connections are now connected to Certificates, i.e. SSH uses Certificates

:star: Client/Server:  SQL Task and Notification now uses Connections

:star: Client: SQL Explorer added


#### Bug Fixes


:white_check_mark: Server: Timeout issue on FTP upload is fixed

:white_check_mark: Server: Fixed problem with LastTrigger Variable in Conditions


### 4.9.44 [2008-12-23]

#### Bug Fixes


:white_check_mark: Server: Fixed issue with not handling multiple attachments well in the Email Trigger

:white_check_mark: Server: Fixed issue with IsSigned property on Email Trigger

:white_check_mark: Server: Increased connection timeout from 60 seconds to 180 seconds in Email Trigger

:white_check_mark: Server: Handled error in SSH Task


### 4.9.43 [2008-12-17]

#### Bug Fixes


:white_check_mark: Client/Server: Fixed issue with exporting server settings

:white_check_mark: Client/Server: Fixed issue with ftp certificate approval

:white_check_mark: Server: Fixed issue Windows XP and mail decryption


### 4.9.42 [2008-12-08]

#### Bug Fixes


:white_check_mark: Server: Fixed Variable resolving for Condition.Contains


### 4.9.41 [2008-12-05]

#### Features

:star: Client:  Added permissions for Remote File browser


#### Bug Fixes


:white_check_mark: Server: Fixed the File Trigger Name Variable. It was relative before when file was found in a sub folder.

:white_check_mark: Server: Fixed export certificates problem

:white_check_mark: Server: Fixed a problem with S/MIME decryption in mail trigger

:white_check_mark: Client: Fixed a bug when saving EmailSaveAction in mail trigger

:white_check_mark: Server: Fixed append bug in archive Task

:white_check_mark: Server/Client/API: Fixed a problem with Stop/Start Server from API


### 4.9.40 [2008-11-23]

#### Bug Fixes


:white_check_mark: Client: Fixed a problem with the Connections window


### 4.9.38 [2008-11-13]

#### Bug Fixes


:white_check_mark: Installer: Fixed a bug in the Tray launcher

:white_check_mark: Server: Did some optimizations in the Server regarding the File Trigger


### 4.9.36 [2008-11-11]

#### Bug Fixes


:white_check_mark: Client: Fixed a dialog problem (showing OpenFileDialog and FolderDialog in some windows)


### 4.9.37 [2008-11-11]

#### Bug Fixes


:white_check_mark: Client: Fixed Credential check in Execute Script Task

:white_check_mark: Client: Fixed User permission delete problem

:white_check_mark: Server: Fixed login check in some Tasks using Credential


### 4.9.35 [2008-11-09]

#### Features

:star: Client: Enabled empty Condition and File content


### 4.9.34 [2008-11-04]

#### Features

:star: Server: Added debugging for mail trigger


#### Bug Fixes


:white_check_mark: Client/Server: Fixed calculation of Julian Day


### 4.9.33 [2008-10-31]

#### Features

:star: Client: Added custom Export of objects

:star: Client/API: Added server info window/values


#### Bug Fixes


:white_check_mark: Client: Fixed a problem with right click for cut/copy


### 4.9.31 [2008-10-30]

#### Bug Fixes


:white_check_mark: Server: Fixed mail trigger thread exit problem

:white_check_mark: Server: Fixed custom save location problem (mail trigger)

:white_check_mark: Server: Fixed a triggering problem with AnyMatch (mail trigger)

:white_check_mark: Server: Fixed a triggering problem with counter (mail trigger)

:white_check_mark: Server: Fixed attachment folder Variable


### 4.9.32 [2008-10-30]

#### Bug Fixes


:white_check_mark: Client: Fixed a problem with Cut Task (did not delete source Task)

:white_check_mark: Client: Handled a null reference error in the Calculate Variable Task

:white_check_mark: Server: Fixed a Retry problem in the On Error functionality


### 4.9.30 [2008-10-22]

#### Features

:star: Client: Added mail trigger variables


#### Bug Fixes


:white_check_mark: Client: Fixed a validation problem which could lead to a crash in the Calculate Variable Task


### 4.9.29 [2008-10-21]

#### Features

:star: Client/Server: Added first beta of the mail trigger

:star: Client: Added confirmation box when trying to stop the Server

:star: Server: Kill/Stop now stops queued Jobs


#### Bug Fixes


:white_check_mark: Server: Fixed a saving problem of Notifications which could disturb NewLine character

:white_check_mark: Server: Fixed a second verification bug since last beta

:white_check_mark: Server: Fixed a problem with created and modified date being reset at import and restart


### 4.9.28 [2008-10-17]

#### Features

:star: Server: Added support for time exceptions in event Triggers


#### Bug Fixes


:white_check_mark: Client: Fixed a SelectionStart bug which could cause a client crash

:white_check_mark: Server: Fixed a saving problem of Jobs which could disturb NewLine characters


### 4.9.27 [2008-10-15]

#### Features

:star: Client: Added drag'n drop support for Jobs and Tasks

:star: Client: Added optional showing of Server messages


#### Bug Fixes


:white_check_mark: Client: Fixed a bug where a messagebox from Server could block other messages

:white_check_mark: Client: Fixed a cloning bug in Condition set window

:white_check_mark: Client: Fixed a null reference problem in HTTP Task


### 4.9.26 [2008-09-28]

#### Features

:star: Client/Server: Added SSL support to Email Task

:star: Client/Server: Added single/separate recipient support for Email Task


#### Bug Fixes


:white_check_mark: Client: Fixed a bug with previous columns in main grid

:white_check_mark: Client/API: Fixed some Time exception bugs


### 4.9.25 [2008-09-27]

#### Features

:star: Client/API/Server: Added Execute script Task


#### Bug Fixes


:white_check_mark: Client: Fixed a bug concerning showing a setting Archive Task (Overwrite)

:white_check_mark: Client: Fixed a bug in the Send Keys Task (mouse down)

:white_check_mark: Client: Fixed a bug giving the right Explorer type (remote/local)

:white_check_mark: Client: Fixed column sort save

:white_check_mark: Client: Fixed a sort bug on Modified date

:white_check_mark: Client: Fixed proper show of extended debug logging setting


### 4.9.24 [2008-09-23]

#### Features

:star: Client: Added File Explorer dialogs for remote Connections


#### Bug Fixes


:white_check_mark: Client: Fixed a recording bug in Desktop Macro

:white_check_mark: Client: Fixed a problem with saving settings for the Custom WMI Trigger

:white_check_mark: Server: Fixed a problem causing Client to hang when adding a Certificate

:white_check_mark: Server: Fixed a problem causing Client to hang when editing a Condition

:white_check_mark: Client: Fixed a bug with missing Tasks in Active Job


### 4.9.23 [2008-09-18]

#### Bug Fixes


:white_check_mark: Client: Fixed a freeze bug in the Print Task

:white_check_mark: Client: Fixed a grid sort problem

:white_check_mark: API: Fixed internal sort problem


### 4.9.22 [2008-09-17]

#### Features

:star: API: Added strong name to dll:s


#### Bug Fixes


:white_check_mark: Client: Fixed a refresh issue with network drives


### 4.9.21 [2008-09-14]

#### Features

:star: Client: Major performance optimizations in interface

:star: Client/API: Added Excel macro Task


#### Bug Fixes


:white_check_mark: Client: Fixed a null reference problem

:white_check_mark: API: Fixed a problem in GetUserName function

:white_check_mark: Server: Fixed an exit code problem with SSH Task

:white_check_mark: Server: Fixed a directory problem with SFTP

:white_check_mark: Client/API/Server: Fixed some issues with Network drives


### 4.9.20 [2008-09-09]

#### Bug Fixes


:white_check_mark: Client: Fixed a null reference problem

:white_check_mark: Client: Fixed a Task stepping problem


### 4.9.18 [2008-09-04]

#### Features

:star: Client/Server: Added package password support to SSIS Execute Task

:star: Client/API: Added Job.Result Variable


#### Bug Fixes


:white_check_mark: Client/API: Fixed a bug when adding time exception collections

:white_check_mark: Client/API: Fixed a textbox cast bug

:white_check_mark: Client: Fixed a bug concerning GUI updates of Connections


### 4.9.19 [2008-09-04]

#### Features

:star: Client/API: Enabled possibility to skip validation against datatype in SQL parameters (good when using Variables)


#### Bug Fixes


:white_check_mark: Client/API: Fixed server state change permissions

:white_check_mark: Server: Fixed a problem with allowing local connections only

:white_check_mark: API: Fixed a problem with trigger update


### 4.9.17 [2008-09-03]

#### Features

:star: Client/Server: Added option to keep existing dates on SFTP download


#### Bug Fixes


:white_check_mark: Client: Fixed a bug concerning opening client settings when no Server is connected

:white_check_mark: Client/API: Fixed a bug that occured when trying to run a single Task

:white_check_mark: Client/API: Fixed a bug in the SFTP Task when using / folder


### 4.9.14 [2008-09-01]

#### Features

:star: Client: Added a startup guide

:star: Client: Added error reporting


#### Bug Fixes


:white_check_mark: Client: Fixed a problem with closing the Execution context window


### 4.9.15 [2008-09-01]

#### Bug Fixes


:white_check_mark: Client/API/Server: Fixed a problem with retrieving PGP key rings

:white_check_mark: Client/API/Server: Fixed a problem with deleting PGP key rings


### 4.9.12 [2008-08-23]

#### Features

:star: Client/API: Client now supports many connections simultaneously

:star: API: API has been extended so it can do whatever the Client can do

:star: Client: Client now supports local connection type which is 10x faster than normal connection - please update your server connections

:star: Client: Major changes in UI

:star: Client: Added theme support

:star: Client: Proxy settings are now separated from Server proxy settings. Please review your proxy settings.


#### Bug Fixes


:white_check_mark: API: Many smaller bugfixes has been done in the API

:white_check_mark: Client: Desktop macro Task was not recording upper case correctly

:white_check_mark: Client: Removed some unwanted columns in Excel export of log

:white_check_mark: Client: Fixed a bug with Task stepping

:white_check_mark: Server: Fixed a problem where FTPSSSLImplicit connections where sorted out

:white_check_mark: Server: Fixed a Job timeout bug concerning threating it as error


### 4.9.11 [2008-07-25]

#### Bug Fixes


:white_check_mark: Server: Fixed a build error causing network drive mapping to fail

:white_check_mark: Server: Fixed SQL Trigger timeout bug


### 4.9.10 [2008-07-24]

#### Bug Fixes


:white_check_mark: Server: Fixed SQL output settings for ODBC/OLEDB

:white_check_mark: API: Fixed various problems with Remove methods


### 4.9.9 [2008-07-10]

#### Features

:star: Client/Server: Added SQL Output settings


#### Bug Fixes


:white_check_mark: API/Client/Server: Fixed a problem with running a Job synchrously

:white_check_mark: Client/Server: Fixed a with linefeed/carriage return in File write task and File Notification


### 4.9.8 [2008-07-09]

#### Bug Fixes


:white_check_mark: Server: Fixed a problem with reconnecting to a remote server in the file trigger

:white_check_mark: API: Fixed a problem with Jobs.Remove function

:white_check_mark: Client: Corrected some minor issues concerning Variables GUI


### 4.9.7 [2008-07-08]

#### Features

:star: Client/Server: Added error handling (OnError) in Task

:star: Client/Server: Added File Trigger support for Samba shares

:star: Client: Added Task stepping within Task editing


#### Bug Fixes


:white_check_mark: Server: Fixed a problem with WatcherChangeType "Delete" and TriggerWhenReleased setting


### 4.9.6 [2008-06-25]

#### Features

:star: Client/Server/API: Added Variables support


### 4.9.5 [2008-06-11]

#### Bug Fixes


:white_check_mark: Client: Fixed correct form validation of Conditions->VisualCron


### 4.9.4 [2008-06-04]

#### Features

:star: Client/Server: Added support for PGP/MIME and S/MIME support in Email Task


#### Bug Fixes


:white_check_mark: Client: Fixed an gui issue concerning non-army time in Time Exceptions


### 4.9.3 [2008-05-20]

#### Features

:star: Client/Server: File trigger values are now updated dynamically


### 4.9.2 [2008-05-14]

#### Features

:star: Client/Server: New Task: Restart service

:star: API: Added Tasks.Run function


#### Bug Fixes


:white_check_mark: Server: Result was not correctly set for VisualCron Trigger result object

:white_check_mark: Server: Fixed an FTP download issue


### 4.9.1 [2008-05-09]

#### Bug Fixes


:white_check_mark: API: Fixed a synchronization problem


### 4.9.0 [2008-05-01]

#### Features

:star: Client/Server: Added 3 levels of variable stepping


#### Bug Fixes


:white_check_mark: Server: Fixed a time zone calculation bug

:white_check_mark: Server: Fixed SFTP transfer 2 gb limit


### 4.8.9 [2008-04-15]

#### Features

:star: Client/Server: Added wildcard support for PGP Task

:star: Client/Server: Added wildcard support for attachments in Email Task


### 4.8.8 [2008-04-05]

#### Features

:star: Tray: Added Job Started/Completed popups


#### Bug Fixes


:white_check_mark: Server: Fixed a printing bug


### 4.8.7 [2008-03-30]

#### Bug Fixes


:white_check_mark: Tray: Fixed an issue when the tray window was visible when switching between windows


### 4.8.6 [2008-03-25]

#### Bug Fixes


:white_check_mark: Server: Fixed a path problem in FTP task


### 4.8.5 [2008-03-20]

#### Bug Fixes


:white_check_mark: Server: Fixed a Condition issue with Action Run Task

:white_check_mark: Server: Fixed argument problem with Remote Execute

:white_check_mark: API: Fixed a IndexOutofBounds error when removing a TaskPid

:white_check_mark: Server/API: Added optimization flag and debug info


### 4.8.4 [2008-02-24]

#### Bug Fixes


:white_check_mark: Server: Fixed a UserAgent problem in the HTTP Task

:white_check_mark: Server: Fixed a PDF printing problem

:white_check_mark: Server: Added PROT P commmand to secure FTP connections


### 4.8.3 [2008-02-19]

#### Features

:star: Server: Fixed a better implemenation of PDF printing

:star: Client/Server/API: Added more Date and Math functions/variables


#### Bug Fixes


:white_check_mark: Client: Fixed a bug in the Execution Context window

:white_check_mark: Client/Server: Fixed a problem with the RunOnce property


### 4.8.2 [2008-02-07]

#### Features

:star: Server: Added support for interactive logon for Windows 2008

:star: Client/Server: Expanded documentation and F1 support on all windows


#### Bug Fixes


:white_check_mark: Server: Fixed a trigger activation problem

:white_check_mark: Client: Now handling copy to clipboard error

:white_check_mark: API: Fixed a problem with adding Time exception collections


### 4.8.1 [2008-01-26]

#### Bug Fixes


:white_check_mark: Client/Server: Fixed a logon problem on Windows XP


### 4.8.0 [2008-01-24]

#### Features

:star: Client/Server: Logon/Unlock function now supports Vista

:star: Client/Server: New task: Registry

:star: Client/Server: Added more options to Foreground execution

:star: Client/Server: Added UserAgent property to HTTP task


#### Bug Fixes


:white_check_mark: Client: Fixed a problem with multiple copy task/ftp items

:white_check_mark: Client: Fixed a problem with editing email attachments in task

:white_check_mark: Server: Removed KeepAlive which caused some ftp tasks to timeout

:white_check_mark: Client: Fixed a UI bug in HTTP task concerning "Save content"

:white_check_mark: Client: Fixed a UI bug in SQL task rconcerning swithing between SP and Job

:white_check_mark: Server: Fixed a loading bug of proxy settings


### 4.9.39 [2008-01-21]

#### Bug Fixes


:white_check_mark: API: Fixed a bug in Use compression parameter at connection

:white_check_mark: Client: Fixed Use compression check box in server manager

:white_check_mark: Server: Fixed a problem with Time exceptions


### 4.7.8 [2008-01-05]

#### Features

:star: Client/Server/API: Added Julian date variables


#### Bug Fixes


:white_check_mark: Client: Fixed error check of Export settings task

:white_check_mark: Client: Fixed a save settings problem of the Print task

:white_check_mark: Server: Fixed a problem with PDF in the Print task

:white_check_mark: Server: Fixed an unhandled exception in Execute task


### 4.7.7 [2007-12-03]

#### Bug Fixes


:white_check_mark: Server: Fixed a bug in new Variables

:white_check_mark: Client: Fixed an import problem in PGP (delete old keys)


### 4.7.5 [2007-11-26]

#### Features

:star: Client/Tray/Server: Added Desktop macro task

:star: Client/Tray/Server: Added Play sound task


#### Bug Fixes


:white_check_mark: Server: Fixed a timeout dispose problem

:white_check_mark: Server: Fixed connection time in Client connections


### 4.7.4 [2007-11-22]

#### Features

:star: Client: Added Job result to main window


#### Bug Fixes


:white_check_mark: Client: Now correctly remember maximized/minimized state when starting client

:white_check_mark: Client: Fixed a loading bug in the Execution context window


### 4.7.3 [2007-11-17]

#### Bug Fixes


:white_check_mark: Server: Fixed Job status change issue


### 4.7.2 [2007-11-16]

#### Features

:star: Server: Added a lot of string functions to Variables


#### Bug Fixes


:white_check_mark: Server: Fixed a compatibility issue with Archive task and XP built-in zipping

:white_check_mark: Client: Fixed a GUI bug in the Print task

:white_check_mark: Client: Fixed some validation checks in Print task and Export settings task

:white_check_mark: Server: Fixed a bug in FTP download


### 4.7.1 [2007-11-15]

#### Features

:star: Client/Server: Added Job/Task control task

:star: Client/Server: Added Ping task

:star: Client/Server: Added File write task

:star: Client/Server: Added File touch task

:star: Client/Server/TrayClient: Added VisualCron Tray Client

:star: Client/Server/TrayClient: Added support for foreground execution

:star: Client/Server: Added option to specify armor boundary (PGP)


#### Bug Fixes


:white_check_mark: Client: Fixed a bug in key generation (PGP)


### 4.6.29 [2007-10-15]

#### Features

:star: Client/Server: Added support for viewing client connections

:star: Client/Server: Added TimeOut property for connections


#### Bug Fixes


:white_check_mark: Client: Fixed a compability bug in PGP task

:white_check_mark: Client: Fixed a SQL job (OLEDB/ODBC)


### 4.6.27 [2007-09-05]

#### Features

:star: Client/Server: Added wildcard support for file condition

:star: Client/Server: Fixed support for some older FTP servers


#### Bug Fixes


:white_check_mark: Server: Fixed a logical error in Condition check

:white_check_mark: Server: Fixed an error concerning closing of a file when FTP downloading (when an error occured)

:white_check_mark: Server: Fixed a certificate error in FTPS connection

:white_check_mark: Server: Fixed a potential lock in File Trigger


### 4.6.17 [2007-09-01]

#### Bug Fixes


:white_check_mark: Server: Fixed a case when users was not correctly saved


### 4.6.16 [2007-08-27]

#### Features

:star: Client/Server: Added true domain support for Remote Execute and Remote Kill

:star: Client/Server: Added permissions for Export and Import settings

:star: Client/Server: Added direct support for MSSQL job execution

:star: Client/Server: Added support for native MSSQL connection in Database task

:star: Client/Server: Improved connection speed further

:star: API: Added optional logging

:star: Client/Server: Added support for drive mapping

:star: Client/Server: Added Print document task


#### Bug Fixes


:white_check_mark: Client/Server: Fixed a bug concerning multiple time triggers

:white_check_mark: API: Fixed some obfuscation problems

:white_check_mark: Client/Server: Corrected some API error handling

:white_check_mark: API: Corrected some problems with the remote job execution

:white_check_mark: Server: Fixed some problems with SQL job execution


### 4.6.9 [2007-06-20]

#### Features

:star: Client/Server: Added new task: SystemUnLock/Desktoplogin


#### Bug Fixes


:white_check_mark: Client/Server: Fixed a variable bug

:white_check_mark: Client: Fixed a bug which could appear in main window when settings file was locked

:white_check_mark: Server: Handled an exception that could occur when wrong notify filters where used in the file trigger

:white_check_mark: Client: Fixed a bug in the file trigger gui


### 4.6.8 [2007-06-16]

#### Features

:star: Client/Server: Added new task: Remote Execute

:star: Client/Server: Added new task: Remote Kill


### 4.6.7 [2007-06-14]

#### Bug Fixes


:white_check_mark: Client/Server: Fixed a calculation bug in SpecificDaysOfTheWeek

:white_check_mark: Client: Fixed gui bug in event log event trigger


### 4.6.6 [2007-06-10]

#### Bug Fixes


:white_check_mark: Server: Fixed a bug in the Email task with attachments


### 4.6.4 [2007-06-06]

#### Features

:star: Client/Server: Added some new encryption algorithms in the PGP task


#### Bug Fixes


:white_check_mark: Client/Server: Fixed password problem in PGP task

:white_check_mark: Server: Fixed a bug regarding running randomly

:white_check_mark: Client/Server: Fixed a calculation bug in SpecificDaysOfTheWeek


### 4.6.3 [2007-04-28]

#### Features

:star: Client/Server: Added Execute DTS package Task

:star: Client/Server: Added Execute SSIS package Task

:star: Client/Server: Added FTP Explicit SSL connection option


#### Bug Fixes


:white_check_mark: Server: Fixed a bug in the local Restart/Shutdown task when using W2003

:white_check_mark: Client: Fixed UI error when deleting SQL param when no row was selected

:white_check_mark: Server: Fixed reconnect problem in File trigger

:white_check_mark: Server: Fixed variable problem with encrypted PGP file

:white_check_mark: Server: Fixed obfuscation problem with API


### 4.6.1 [2007-04-27]

#### Features

:star: Server: Added user tracking in log (who did what..)


#### Bug Fixes


:white_check_mark: Client: Fixed sorting bug in Client main grid

:white_check_mark: Client: Handled a connection error (data transfer thread)

:white_check_mark: Server: Fixed a nullreference error in Email task when foreign characters where used

:white_check_mark: Server: Corrected a DST bug


### 4.6.0 [2007-04-27]

#### Features

:star: API: First Beta of the VisualCron API

:star: Server: FTP speed improved

:star: Server: Added support for "non valid" certificates in HTTP task


#### Bug Fixes


:white_check_mark: Client: Behavior changed when importing keys, old keys are not cleared anymore

:white_check_mark: Server: Fixed trigger result behavior

:white_check_mark: Client/Server: Fixed last workday calculation bug

:white_check_mark: Client: Handled null reference error in empty task names

:white_check_mark: Server: Handled more FTP errors (GetFiles)

:white_check_mark: Server: Handled more FTP errors (Unhandled exception at connection)

:white_check_mark: Server: Fix for HTTP task (unsafeheaders)

:white_check_mark: Server: Fixed unhandled error when saving Jobs


### 4.5.8 [2007-03-25]

#### Bug Fixes


:white_check_mark: Server: Fixed an output problem with the HTTP task and SQL task

:white_check_mark: Server: Fixed the variable replacement in of attachment file name in Email task


### 4.5.6 [2007-03-19]

#### Features

:star: Client/Server: Added alternate credential execution on Execute task


#### Bug Fixes


:white_check_mark: Client: Fixed bug in Connection dialog concerning SFTP/SSH task


### 4.5.4 [2007-03-13]

#### Features

:star: Client: Updated Variables with new task types


#### Bug Fixes


:white_check_mark: Server: Added Credentials to Reconnect in File Trigger

:white_check_mark: Client: Fixed some GUI errors in the File Trigger


### 4.5.1 [2007-03-03]

#### Features

:star: Client/Server: Added Start service task

:star: Client/Server: Added Stop service task

:star: Client/Server: Added Logoff task

:star: Client/Server: Added Shutdown task

:star: Client/Server: Added Restart task

:star: Client/Server: Added Wake up on LAN task

:star: Client/Server: Added Standby/Sleep task

:star: Client/Server: Added Hibernate task

:star: Client/Server: Added Lock workstation task

:star: Client/Server: Added Wake up task

:star: Client/Server: Added Control monitor task

:star: Added reconnection interval at file trigger


#### Bug Fixes


:white_check_mark: 	Added some extra locks to prevent task run problems

:white_check_mark: 	Added some exception handling in the FTP task

:white_check_mark: 	Fixed as sort bug in the main window


### 4.4.18 [2007-02-23]

#### Bug Fixes


:white_check_mark: Server: Fixed a problem with the SSH task when it was aborting

:white_check_mark: Client: Fixed a cloning bug


### 4.4.16 [2007-02-21]

#### Bug Fixes


:white_check_mark: Client: Fixed a credential interface bug at File Read task


### 4.4.15 [2007-02-19]

#### Features

:star: Client/Server: Added Read File task

:star: Server: Added Reconnect for File Event if connection was lost

:star: Client/Server: Added Email task

:star: Client/Server: Added SSH task


#### Bug Fixes


:white_check_mark: Client: Fixed problems with the Manage credentials permissions

:white_check_mark: Client: Fixed an interface bug with the Create Folder task

:white_check_mark: Server: Fixed encoding problem at the FTP task


### 4.4.6 [2007-02-10]

#### Features

:star: Client: Jobs are now sorted in the VisualCron Event


#### Bug Fixes


:white_check_mark: Client: Fixed problems with the Conditions permissions


### 4.4.4 [2007-01-17]

#### Features

:star: Client/Server: New file result variable - path to folder where file was triggered

:star: Client/Server: File mask delete and case sensitive option in SFTP Delete file


#### Bug Fixes


:white_check_mark: Client: Bug appeared when changing task type and pressing Cancel

:white_check_mark: Client: Fixed Cancel behavior in the select working directory dialog


### 4.4.0 [2007-01-14]

#### Features

:star: Server: Added support for credentials in Windows 2000

:star: Client: Optional UNC path auto naming

:star: Client/Server: New functionality in the SendKeys task - drag/select window

:star: Client: Optimizations in the task dialogs - reduced loading speeds

:star: Client/Server: New task: PGP

:star: Client/Server: New task: Folder create

:star: Client/Server: New task: Folder delete

:star: Client/Server: New task: Folder rename

:star: Client/Server: New task: File rename

:star: Client/Server: New task: File delete

:star: Client/Server: New task: Wait

:star: Client/Server: New task: Export settings

:star: Client/Server: Import settings

:star: Client/Server: Export settings

:star: Server: Settings auto recovery


#### Bug Fixes


:white_check_mark: Client: Fixed a bug in the version control

:white_check_mark: Client: Fixed time exception bug

:white_check_mark: Server: Fixed bug in Conditions concerning "Next"

:white_check_mark: Server: Fixed credential bug in HTTP task

:white_check_mark: Server: Fixed bug in "Run missed jobs"


### 4.3.23 [2006-12-09]

#### Features

:star: Server/Client: Automatic, quiet network install support


### 4.3.22 [2006-12-03]

#### Bug Fixes


:white_check_mark: Server: Adjust for time change bug

:white_check_mark: Client: Fixed Network Credentials bug (when adding NC)


### 4.3.20 [2006-11-27]

#### Features

:star: Server/Client: Added HTTP file content download option

:star: Server/Client: Consider timeout as error option

:star: Server: Server recovery alternative

:star: Server/Client: Added Last Executed variable

:star: Server/Client: Trigger file on release


#### Bug Fixes


:white_check_mark: Server: Fixed time exception bug

:white_check_mark: Server: Fixed error which could occur on some FTP servers: An error occurred while reading from or writing to the data channel.

:white_check_mark: Server: Fixed a bug concerning sub folders of FTP

:white_check_mark: - Client: Fixed FTP GUI error

:white_check_mark: Server: Active trigger variable fix

:white_check_mark: Server: Last day in month fix, part 2


### 4.3.8 [2006-11-13]

#### Bug Fixes


:white_check_mark: Client/Server: Fixed a copy files bug in "order"

:white_check_mark: Server: Threadfix stopped high cpu usage

:white_check_mark: Server: Copy files task -> last modified bug fixed

:white_check_mark: Server: Time re-calculation at time change fix

:white_check_mark: Server: Last day in month fix

:white_check_mark: Server: Output optimization

:white_check_mark: Server: Fixed a time exception bug


### 4.3.0 [2006-11-02]

#### Bug Fixes


:white_check_mark: Fixed a GUI error in time exceptions

:white_check_mark: Fixed a memory leak in Windows 2000 Server

:white_check_mark: Fixed a bug in the date format variable

:white_check_mark: Fixed a bug in ftp task which could occur when file did not exist at download destination

:white_check_mark: Cloned job statistics are now cleared correctly

:white_check_mark: Fixed a bug which appeared when no computer name was given in any event

:white_check_mark: Log is cleaned more often

:white_check_mark: Fixed a design error in SQL task

:white_check_mark: Fixed an error in the Manage variables window


### 4.2.2 [2006-10-13]

#### Features

:star: Added case sensitivity option to file mask in FTP upload/download task

:star: Added credentials support for file notification


### 4.2.0 [2006-10-12]

#### Bug Fixes


:white_check_mark: Fixed a bug which occured in the client when no ftp client or credential was selected when adding a task

:white_check_mark: The correct exit code is now returned when using credentials

:white_check_mark: When service is stopped all child processes are now correctly killed

:white_check_mark: Fixed a in copy files task which could cause error when copying


### 4.1.6 [2006-10-09]

#### Features

:star: Extended Variable functionality

:star: Added variable permissions

:star: Added last execution time to job row at main grid

:star: Added output limitation setting

:star: Added SQL output to SQL task

:star: Added "delete source file after copy" to FTP upload/download


#### Bug Fixes


:white_check_mark: Fixed a timeout bug in the execute task

:white_check_mark: Fixed a bug which could skip jobs if the server was really busy

:white_check_mark: Fixed a sort problem in the main grid

:white_check_mark: Fixed an update problem in the archive item list

:white_check_mark: Fixed some cloning bugs

:white_check_mark: Fixed a bug which could occur in the VisualCron condition

:white_check_mark: Fixed a problem with from email and from name in Notifications

:white_check_mark: Fixed a problem with changing from SFTP to FTP protocol type

:white_check_mark: Fixed with a problem with FTP (overwrite if newer)

:white_check_mark: Fixed a problem with clearing and loading FTP connections when switching server

:white_check_mark: Fixed a memory leak

:white_check_mark: Fixed a bug in Copy files regarding read only files when overwriting

