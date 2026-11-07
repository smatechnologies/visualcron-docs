---
sidebar_label: 'Settings - Web API'
hide_title: 'true'
---

## Settings - Web API

The **_Web API_** tab turns the VisualCron Web API on or off and sets its ports and certificate. The Web API lets other programs work with the Server through a REST service and a web service. To learn how to call it, see [VisualCron Web API](../../using-visualcron/visualcron-web-api). This tab is one of the tabs of the Server settings window (see [Main - Settings](main-settings)).

_Server_ -> _Main settings_ -> _Settings_ -> **_Web API_** tab

![The Web API tab with Allow Web API checked, the Unencrypted box with port 8001 and its Web service, REST service and REST service documentation links, and the Encrypted box with port 8002, Use self signed certificate, Use user certificate and Force Windows Authentication](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Web%20API.png)

- _Allow Web API_: turns the Web API on. Unchecked by default. When it is on, the Server opens both the unencrypted and the encrypted port
- _Unencrypted_ -> _Port_: the HTTP port. The default is "8001"
- _Encrypted_ -> _Port_: the HTTPS port. The default is "8002"
- _Use self signed certificate_ (default) or _Use user certificate_: the certificate of the encrypted port. With _Use user certificate_, select a certificate from the global Certificates (see [Global - Certificates](global-certificates)). If you click _Apply settings_ without one, VisualCron shows "You must specify a certificate!". The self signed certificate is created by VisualCron, so programs that call the encrypted port must be set to trust it. Use a certificate they already trust if they cannot
- _Force Windows Authentication_: on the encrypted port, users log on with their Windows account instead of a VisualCron user name and password. Available only while _Allow Active Directory Logon_ is checked on the **_Users/Logon_** tab (see [Settings - Users/Logon](settings-users-logon)). If you uncheck _Allow Active Directory Logon_, this option is unchecked too

Each box shows links to the _Web service_ description, the _REST service_ and the _REST service documentation_ for its port; click a link to open it in your browser. The _REST service_ link of the _Unencrypted_ box is an example logon address with a sample user name and password. In the _Encrypted_ box, the _REST service_ link opens the documentation address.

Changes take effect when you click _Apply settings_: the Server restarts the Web API with the new ports, certificate or authentication. VisualCron does not open the Web API ports in Windows Firewall.

:::warning

The unencrypted port is always open while _Allow Web API_ is checked, and it does not use Windows authentication, even when _Force Windows Authentication_ is checked. A REST logon sends the user name and password in the address, so on the unencrypted port they travel in clear text. To protect them:

- Use only the encrypted port in your scripts and programs
- Allow only the encrypted port through Windows Firewall, and do not add an inbound rule for the unencrypted port
- After logon, use the token that the logon returns for later calls (see [VisualCron Web API](../../using-visualcron/visualcron-web-api))

Most examples on the VisualCron Web API page use the unencrypted port with "http" and port "8001". Use "https" and the encrypted port instead.

:::
