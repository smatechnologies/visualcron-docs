---
sidebar_label: 'Task Net - HTTP'
hide_title: 'true'
---

## Task Net - HTTP

The HTTP Task sends an HTTP or HTTPS request to a URL and returns the response, for example to call a REST API, run a script on a web server or download a file. The response body is the output of the Task, so later Tasks can use it, save it to a file or send it by email.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The HTTP settings are on the ***HTTP*** tab of the Task window, which has its own inner tabs: ***Main settings***, ***Headers***, ***Parameters/Body***, ***Security***, ***Certificates***, ***Save content/response*** and ***OAuth parameters***. The inner ***Main settings*** tab is not the Task window's shared ***Main settings*** tab.

### HTTP: Main settings tab

![Main settings tab of the HTTP Task, with the Endpoint/URL, Method and HTTP version, and Request groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/HTTP.png)

- _Endpoint/URL_: the URL to call, for example `https://<host>/<path>`

  With GET, you can add query parameters to the URL, as in `?<key1>=<value1>&<key2>=<value2>`, or enter them on ***Parameters/Body***. With POST, enter the parameters on ***Parameters/Body*** only.

- _Proxy.._: opens the proxy settings for the request
- _Method and HTTP version_: the method, "POST", "PUT", "GET", "DELETE" or "PATCH", and the HTTP version, "1.1" or "1.0"

  A new Task has "GET" and "1.1". Many servers write URLs to their logs, so send values that should not be logged in the body of a POST rather than in a GET URL.

- _UserAgent_: the User-Agent header of the request, "VisualCron" on a new Task

  Change it if the server expects a particular user agent.

- _Timeout in seconds_: how long the request can take

  "0", the default, means no time limit. To limit how long the whole Task can run, use the Task's ***TimeOut*** tab (see [Task - Timeout](../../task-timeout)).

- _KeepAlive_: selected by default, so the request asks the server to keep the connection open for later requests

  If you clear it, the request may send a `Connection: Close` header.

- _AllowAutoRedirect_: selected by default, so the request follows HTTP redirects to the new location

  Clear it to get the redirect response itself.

- _Expect 100 Continue_: selected by default, so the request sends an `Expect: 100-continue` header

  If the server returns HTTP error 417, clear this check box.
 
### HTTP: Headers tab

![Headers tab of the HTTP Task, with the Content-type header list, the Other headers grid and the cookie option](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/HTTP%20headers.png)

- _Content-type header_: the Content-Type of the request

  The list has the most common types, and "application/x-www-form-urlencoded" is the default. Choose the type that matches the body type on ***Parameters/Body***.

- _Base on file type_: used only with PUT and PATCH, and selected by default

  While it is selected, the content type is taken from the file extension of the ***binary*** body file. Any other body type has no file, so the content type becomes "text/plain". To send the _Content-type header_ you chose, clear this check box. With POST and GET, the Task always sends the _Content-type header_; with DELETE, only when the request has a body.

- _Other headers_: custom headers

  Click _Add_, _Edit_ or _Delete_ to change the list.

- _Use cookies from headers only_: sends only the cookies of a `Cookie` header that you added

  The HTTP and Web Macro Tasks of one Job run share one cookie store. The HTTP Task sends the cookies in it, and adds the cookies that servers set. Web Macro Tasks use the store when _Pass cookies between Tasks in Job session_ is selected (see [Task Net - Web Macro](web-macro)), so a session that a Web Macro Task signed in to can be used by a later HTTP Task in the same run, and the other way round. When _Use cookies from headers only_ is selected and you have added a `Cookie` header under _Other headers_, the Task sends only the cookies in that header. It does not send the stored cookies, and it does not store the cookies from the response. The check box is selected automatically when you add a `Cookie` header.
 
### HTTP: Parameters/Body tab

![Parameters/Body tab of the HTTP Task, with the x-www-form-urlencoded, form-data, raw and binary body tabs](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/HTTP%20parameter.png)

Click the tab of the body type to send, and set a matching _Content-type header_ on ***Headers***:

- _x-www-form-urlencoded_: key/value pairs, for simple form posts
- _form-data_: a multipart body of text parts and file parts, for example to upload files

  Each file part selects its file with a file filter, which must match exactly one file.

- _raw_: text sent as it is, for example a JSON body
- _binary_: the content of one file, selected with a file filter that must match exactly one file

  If the filter matches no file, or more than one, the Task records an error, but the request is still sent, with an empty body; see the warning below.

With GET, the x-www-form-urlencoded and raw bodies are added to the URL as a query string.

:::warning

A form-data file part whose file filter matches no file, or more than one file, is left out of the request, and the Task does not fail. The request is sent without that file. To make sure the file is there, check for it in an earlier step, for example with a [Condition - File](../../condition-file).

When the file filter of a _binary_ body matches no file, or more than one, the Task records an error and fails, but it still sends the request, with an empty body. POST, PUT and PATCH then send no content, which can replace the server's resource with empty content, and DELETE still runs. Check for the file in an earlier step in the same way.

:::
 
### HTTP: Security tab

![Security tab of the HTTP Task, with the Supported security protocols group and the Credentials group with the Auth type list](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/HTTP%20security.png)

- _Supported security protocols_: the protocols the request can use with an "https://" URL: "SSL 3", "TLS 1.0", "TLS 1.1", "TLS 1.2" and "TLS 1.3"

  All are selected by default.

- _Credentials_: optional. The Credential with the user name and password to sign in with (see [Global - Credentials](../../global-credentials))

  Without a Credential, the request uses no authentication, except with _Auth type_ "OAuth", which needs no Credential.

- _Auth type_: the authentication method:
  - "Basic": sends the user name and password with the first request, Base64 encoded. Base64 is an encoding, not encryption
  - "NTLM" (default): Windows NT LAN Manager challenge-response authentication
  - "Digest": MD5-based challenge-response authentication
  - "Negotiate": chooses Kerberos or NTLM
  - "Kerberos": ticket-based authentication for domain environments
  - "OAuth": an OAuth 2.0 access token, set up on the ***OAuth parameters*** tab

:::warning

With "Basic", the Task sends the user name and password with the first request, before the server asks for them, and anyone who can see the traffic can read them. Use "Basic" only with "https://" URLs. Because the Task does not check server certificates (see [HTTP: Certificates tab](#http-certificates-tab)), "https://" protects them only on a network path that you trust.

:::
 
### HTTP: Certificates tab

Add a client certificate here for the request to present when the server asks for one. The certificates come from [Global - Certificates](../../global-certificates).

:::warning

The HTTP Task accepts every server certificate, including expired, self-signed and mismatched ones, and has no setting to check them. It cannot tell the real server from another server that answers at the same address. Use it only with servers that you trust, and do not send credentials over a network path that you do not trust.

:::
 
### HTTP: OAuth parameters tab

This tab is available only when _Auth type_ is "OAuth". It holds the settings to get an OAuth 2.0 access token. _Client ID_, _Client secret_ and _Refresh token_ are required.

- _Token endpoint/URL_: the token endpoint of the OAuth provider
- _Client ID_: the client identifier issued when the application was registered with the provider
- _Client secret_: the secret issued with the Client ID, stored encrypted
- _Refresh token_: the refresh token that VisualCron uses to get a new access token for each run, stored encrypted
- _Authenticate_: opens the _OAuth - Authorize_ window, to get a refresh token from the provider

  Enter the provider's _Authorize endpoint/URL_, _Redirect URI_ and _Scope_, and any optional parameters for the authorization code request and the token request. Select _Use internal browser_ to sign in in a browser inside the Client. When the sign-in succeeds, _Refresh token_ is filled in.

- _Additional parameters_: key/value pairs sent with the token request

  Click _Add_, _Edit_ or _Delete_ to change the list.

:::note

If the token request fails, the Task fails, but the request is still sent, without a token. If the provider returns no access token, the request is sent without one, and the Task does not fail because of the token.

:::

### HTTP: Save content/response tab

![Save content/response tab of the HTTP Task, with the Save content check box, the Credentials, Folder path, Auto name file and File name fields and the Exist options list](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/HTTP%20save%20content%20response.png)

By default, the response body is the output of the Task, as text. To save the response to a file instead, for example to download a file, select _Save content_. This tab is available only with the GET and POST methods.

:::warning

The response is kept, as output or as a file, only when _Store standard output_ is selected on the Task window's shared ***Main settings*** tab (see [Task - Main Settings](../../job-tasks-task-main-settings)). It is selected by default. If it is cleared, the Task saves nothing and still succeeds.

:::

- _Save content_: writes the response body to a file instead of the output
- _Credentials_: optional. The Credential to write the file with, for example for a network folder (see [Global - Credentials](../../global-credentials))
- _Folder path_: the folder to save the file in
- _Auto name file_: selected by default, so the Task names the file

  The file gets the name in the response's `Content-Disposition` header. When the response has no such header, it gets the last part of the URL, including any query string. A query string can make the save fail, so for a URL with a query string, clear _Auto name file_ and enter a _File name_.

- _File name_: the name of the file, used when _Auto name file_ is cleared
- _Exist options_: what to do when the file exists:
  - "Overwrite if existing" (default): replaces the file
  - "Overwrite if newer": replaces the file when the response's `Last-Modified` date is later than the file's modified date. When the response has no `Last-Modified` header, the file is replaced on every run
  - "Append to file": adds the response to the end of the file
  - "Skip": keeps the file and writes a message to the output

:::warning

With the default "Overwrite if existing", a file with the same name in _Folder path_ is replaced. "Overwrite if newer" also replaces it on every run when the server sends no `Last-Modified` header, which is common for generated responses. To keep existing files, choose "Skip".

:::

### Output and result

The Task result shows the HTTP status code and the response headers. Both are available as Task result Variables for later Tasks (see [Task - Output and Result](../../task-output-and-result)).

If the server returns an error status code, such as 404 or 500, the Task fails, unless its ***On error*** settings exclude the error (see [Task - On Error](../../task-on-error)). The response body is then written to the standard error output.
 
### Troubleshooting

If the Task fails with the error `The requested security protocol is not supported.`, the Windows version of the VisualCron Server does not support one of the protocols selected in _Supported security protocols_. Clear "SSL 3" first. If the error remains on an older Windows version, also clear "TLS 1.3". Keep "TLS 1.2" selected.
