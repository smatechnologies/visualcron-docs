---
sidebar_label: 'Settings - Proxy'
hide_title: 'true'
---

## Settings - Proxy

The **_Proxy_** tab sets the proxy server that the Server uses to reach VisualCron about its license. The Server uses it when it checks its license online, at service start and regularly after that, and when the license is activated or deactivated through the Web API. Only the license check, activation and deactivation use this proxy. Tasks, Connections, error reporting and the download of missing component files do not use it: set a proxy on each Connection that needs one. This tab is one of the tabs of the Server settings window (see [Main - Settings](main-settings)).

When you activate or deactivate the license from the Client, the computer where the Client runs contacts VisualCron itself, through the proxy on the **_Proxy_** tab of the Client settings (see [Settings - Client Settings](../file/client-settings)). The Client reads that setting when it connects to the Server, so connect again after you change it.

_Server_ -> _Main settings_ -> _Settings_ -> **_Proxy_** tab

![The Proxy tab with Proxy type No proxy; the Address, Port, Test url, Use credentials, Domain, Username and Password fields and the Authentication list are unavailable](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Proxy.png)

- _Proxy type_: "No proxy" (default), "HTTP Proxy", "SOCKS4" or "SOCKS5". With "No proxy" the other fields are unavailable
- _Address_: the host name or IP address of the proxy server. The field is prefilled with the VisualCron website address: replace it with your proxy server
- _Port_: the port of the proxy server. The field is prefilled with "8080"
- _Use proxy for data channel_: also uses the proxy for the data channel. Shown when a proxy type is selected
- _Test url_ and _Test_: click _Test_ to request the _Test url_ through the proxy. VisualCron shows "Proxy is available" when the request succeeds, and "Proxy is not available" when it does not. The test runs on the computer where the Client runs, so run it on the Server computer to test the Server's connection
- _Authentication_: for "HTTP Proxy" only: "Basic" (default), "Digest", "NTLM" or "Not set"
- _Use credentials_: check this if the proxy server needs a logon, and enter _Domain_, _Username_ and _Password_