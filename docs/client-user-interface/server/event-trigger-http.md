---
sidebar_label: 'Event Trigger - HTTP'
hide_title: 'true'
---

## Event Trigger - HTTP

The HTTP event trigger calls a web page or URL at a regular interval and fires when the response matches the conditions you set. Use it to monitor a web page or service, for example to start a Job when a page returns a certain status code or contains a certain text.

The URL is called at the *Polling interval* set in the *Main settings* tab. The default is 3600 seconds (1 hour).

This Trigger is different from the [HTTP REST](../server/event-trigger-http-rest) event trigger, which waits for incoming requests instead of calling a URL.

**Triggers > Add > Event Trigger > HTTP > Main settings** tab

**Endpoint/URL**

This is the remote page or script to be called. Use the following format: [http://www.yourwebpage.com/yourscript.php](http://www.yourwebpage.com/yourscript.php). If you use a GET you can add parameters like ```?mykey1=myvalue1&mykey2=myvalue2``` or use the Parameters/Body tab to input parameters.

**Proxy..**

Select if you want to use a proxy.

**Method**

Select the HTTP method to use when calling the page. Available options are POST, PUT, GET (default), DELETE, and PATCH.

**Version**

Select which HTTP version to use: 1.1 (default) or 1.0.

**UserAgent**

Optional. If the page requires a certain UserAgent you can use this field to let VisualCron pretend to be a certain UserAgent. Default is *VisualCron*.

**Timeout in seconds**

This is the timeout of the web request.

**KeepAlive**

Set this property to true to send a Connection HTTP header with the value Keep-alive, to indicate a preference for persistent connections.

**AllowAutoRedirect**

Set AllowAutoRedirect to true if you want the request to automatically follow HTTP redirection headers to the new location of the resource.

**Expect 100 Continue**

Enable this if you get HTTP error 417.

**Triggers > Add > Event Trigger > HTTP > Headers** tab

**Content-type header**

This header controls the content type of the HTTP request. In the drop down most common headers can be found. This setting is also related to the Parameters/Body tab as it affects the way the body is posted.

**Base on file type**

When checked (default), VisualCron automatically sets the content-type header based on the type of file being sent. Uncheck to use the content-type header value set manually above.

**Other headers**

Custom headers can be added by pressing the Add button.

**Triggers > Add > Event Trigger > HTTP > Conditions** tab

The conditions decide when the Trigger fires. Each time the URL is called, the response is checked against the conditions you have set. The Trigger only fires when all of them match. If no conditions are set, the Trigger fires on every call.

**Title**

Compares the title of the returned page (the text inside the `<title>` tag) with a value. Available conditions are *Don't check* (default), *Equal (=)*, *Not equal (!=)*, *Contains (=%)* and *Not contains (!=%)*.

* **Ignore case** — When checked, the comparison is not case sensitive.

**Body**

Compares the body of the returned page (the text inside the `<body>` tag) with a value. The same conditions as for *Title* are available.

* **Ignore case** — When checked, the comparison is not case sensitive.

**Status code conditions**

Compares the HTTP status code of the response (for example 200 or 404) with one or more values. Add a row for each status code and select a condition: *Don't check*, *Equal (=)*, *Not equal (!=)*, *Smaller than (<)*, *Smaller than or equal (<=)*, *Larger than (>)* or *Larger than or equal (>=)*. The status code condition matches if any of the rows match.

**Triggers > Add > Event Trigger > HTTP > Parameters/Body** tab

**Parameters/body**

Depending on content-type header you can send various content in the body. By selecting a tab you choose how the body is sent - please note that you need to set a matching content-header as well. Different body options:

**x-www-form-urlencoded** - use this for simple key/value pairs

**form-data** - use this if form-data content-type header is required and if you want to send multi-part data like files (and maybe text).

**raw** - use this for sending body text raw - for example when sending a Json request

**binary** - use this for sending a stream of binary data like one file

**Triggers > Add > Event Trigger > HTTP > Security** tab

**Supported security protocols**

Set the supported security protocols (by your web server) to use the maximum security. Available options (all enabled by default): SSL 3, TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3.

**Credentials**

Optional. If the page requires authentication you can select a credential from the combo box. By clicking on Manage credentials you can add or edit current credentials.

**Auth type**

What kind of authentication method that is used. No authentication method is used if no Credential is selected. Available options:

* *Basic* — sends credentials as a Base64-encoded username/password pair.
* *NTLM* — Windows NT LAN Manager challenge-response authentication (default).
* *Digest* — MD5-based challenge-response authentication.
* *Negotiate* — automatically selects between Kerberos and NTLM.
* *Kerberos* — ticket-based authentication for domain environments.
* *OAuth* — OAuth 2.0 token-based authentication.

**Triggers > Add > Event Trigger > HTTP > Certificates** tab

Client certificates can be managed here. Add a client certificate to present to the remote server when requested.

**Triggers > Add > Event Trigger > HTTP > Save content/response** tab

**Save content to file**

When checked, the content of the response is saved to a file each time the Trigger fires.

**Credentials**

Optional. If you want to save the content in a folder which requires network credentials then select a valid credential for that folder. By clicking on Manage credentials you can add or edit current credentials.

**Folder**

Specify a path where you want to save the content/file.

**Auto name file**

When checked (default), the file is named after the file name in the response headers, or after the last part of the URL if the response does not include one.

**File name**

The name of the file to be saved. Only used when *Auto name file* is unchecked.

**Overwrite options**

Select how VisualCron should handle existing files:

* *Overwrite if existing* — replace the existing file (default).
* *Overwrite if newer* — only replace the existing file if the content on the server is newer.
* *Append to file* — add the content to the end of the existing file.
* *Skip* — do not save the content if the file already exists.
