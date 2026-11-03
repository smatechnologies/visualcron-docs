---
sidebar_label: 'Connection - PeopleSoft'
hide_title: 'true'
---

## Connection - PeopleSoft

The PeopleSoft Connection stores the address, sign-in and security settings that the following PeopleSoft Tasks and the PeopleSoft Trigger use to connect to the PeopleSoft process scheduler web service:

- PeopleSoft - Process Schedule
- PeopleSoft - Find Processes
- PeopleSoft - Process Request
- PeopleSoft - Process Report
- PeopleSoft - Process Update
- PeopleSoft - Schedule PSQuery
- PeopleSoft - Schedule BI Publisher
- PeopleSoft - Schedule ConQuery

### Common settings

![PeopleSoft Connection, Common settings tab with the Test button](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/PeopleSoft/PeopleSoft.png)

The ***Common settings*** tab is the same for every Connection type that has it; see [Common settings](global-connections#common-settings).

For a PeopleSoft Connection, _Timeout_ and _Code page_ are not used. _Test_ runs on the Server. It calls the process scheduler service for its list of process types, through the web service description (WSDL) that VisualCron reads from _Schema_, _Address_, _Port_ and _Path_. A message shows the result.

### Main settings

![PeopleSoft Connection, Main settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/PeopleSoft/Settings.png)

These fields are on ***Connection settings*** -> ***Main settings***. _Address_ and _Username_ are required.

:::warning

_Schema_ is "http" for a new Connection. With "http", the user name and the password are sent without encryption when _Authentication type_ is "Basic", and by the PeopleSoft - Schedule PSQuery, Schedule BI Publisher and Schedule ConQuery Tasks. Use "https" if your PeopleSoft server supports it, and check that the service address in the WSDL also uses "https". With "https", the Server does not check the certificate of the PeopleSoft server on its web service calls. It checks the certificate only when it first downloads the WSDL. While a PeopleSoft call runs, the Server accepts any server certificate for HTTPS calls in the Server process, and each call sets the SSL and TLS versions for the Server process to the operating system default. Make sure that the Server reaches PeopleSoft only through networks that you trust.

:::

- _Address_: the host name or IP address of the PeopleSoft server, without a scheme or a port. Set those in _Schema_ and _Port_
- _Port_: the port of the PeopleSoft web server. The default is "8000"
- _Authentication type_: the HTTP authentication that the Server uses with the web server:
  - "Default": no HTTP authentication
  - "Basic": HTTP Basic authentication with _Username_ and _Password_
  - "Digest": HTTP Digest authentication with _Username_ and _Password_
  - "Windows": Windows authentication
  - "Certificate": certificate authentication, with no setting to select a client certificate
- _Username_: the PeopleSoft user name. Whatever the authentication type, the PeopleSoft - Schedule PSQuery, Schedule BI Publisher and Schedule ConQuery Tasks also send _Username_ and _Password_ in the header of the web service message
- _Password_: the password for that user
- _Schema_: the scheme of the WSDL address, "http" or "https". The default is "http". When it is empty, "http" is used
- _Path_: in the _Additional parameter_ group. The path of the WSDL on the PeopleSoft server. The default is "/PSIGW/PeopleSoftServiceListeningConnector/PROCESSREQUEST.1.wsdl". VisualCron reads the WSDL from `<schema>://<address>:<port><path>`
