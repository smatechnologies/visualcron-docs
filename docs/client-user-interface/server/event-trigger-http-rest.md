---
sidebar_label: 'Event Trigger - HTTP REST'
hide_title: 'true'
---

## Event Trigger - HTTP REST

The HTTP REST Trigger runs an HTTP (or HTTPS) server on the VisualCron Server computer. It listens on the address and port you set and fires when a request matches one of the methods and paths on the ***Request methods*** sub tab and meets that request's header conditions. A request that matches none gets the status "404" and does not fire the Trigger. The details of the request, such as query parameters, headers and the body, are available as result Variables (see [Result Variables](#result-variables)).

If another Trigger or program already uses the address and port when the Trigger starts, the Trigger is deactivated and the error is written to the log.

The *Polling interval* on the Trigger's ***Main settings*** tab (not the ***Main settings*** sub tab of the ***HTTP REST*** tab) is an internal wait in milliseconds (default 1000). Requests are handled as they arrive, so you do not need to change it.

This Trigger fires once per request. With *Immediately* under *Response*, the caller has already received the *Status code* when the Job is due to start, so if the run of the Job is skipped, for example because *Do not start if job is already running* is selected (the default), the request is lost although the caller got a success status. See *Triggers that fire once per item* in [Event Triggers](event-triggers#triggers-that-fire-once-per-item).
 
The settings are on the ***HTTP REST*** tab, ***Main settings*** sub tab.

![Main settings sub tab of the Add/Edit event window for the HTTP REST Trigger with Address, Port, Use SSL, Certificate, Authorization (Auth type, Realm, Credential) and Response options](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20HTTP%20REST.png)

**Parameters**

**Address**

The IP address or host name of the VisualCron Server computer that the server listens on. "0.0.0.0" (the default) or an empty value listens on all network interfaces. For a host name, the server listens on the first address the name resolves to. You can use Variables.

**Port**

The TCP port to listen on (default "9990"). You can use Variables. A port is required.

**Use SSL**

Check to accept HTTPS instead of HTTP. You must then select a *Certificate*.

**Certificate**

Select the [Certificate](../server/global-certificates) that the server presents to callers. The field is available only when *Use SSL* is checked.

**Authorization**

**Auth type**

The authentication the server asks callers for: check *Basic*, *Digest* or both, or leave *Not specified* for no authentication. With an authentication type, you must also select a Credential.

:::warning

With *Basic* or *Digest*, the Trigger compares the password in the request with the password of the selected Credential. If the Credential has no password or has been deleted, every request is rejected. Use *Use SSL* with *Basic*, which sends the password in clear text.

:::
 
**Realm**

The field is available when *Digest* is checked (default "VisualCron"). The Trigger does not use this value: it sends the *Address* as the realm.

**Credentials**

Select the [Credential](../server/global-credentials) whose password callers must send. The field is available when an authentication type is checked.

**Response**

Choose when the server answers the request:

* *Immediately* (default): as soon as the request is accepted
* *Job complete*: after the Job that this Trigger starts has finished
* *Task complete*: after the Task you select in the list below has finished

With *Job complete* or *Task complete*, the *Content* of the request (***Request methods*** sub tab) and, if it contains Variables, the *Status code* are evaluated again after the Job or Task has finished, so they can contain Variables with its results, for example the output of a Task.

:::warning

The server handles one request at a time, and with *Job complete* or *Task complete* it waits without a time limit. The wait ends when that Job, or that Task, finishes in any run, also a run that this request did not start.

* If the Job does not start, for example during a time exception or because *Run after the trigger has been triggered* is above 1, or the selected Task does not run, or *Task complete* is selected without a Task, the request gets no answer and every later request waits behind it
* If the Job or Task finishes while no request is waiting, the next request is answered at once, with values from that earlier run

Use *Immediately* unless the caller needs the result, and make sure the Job always runs the selected Task.

:::
 
***HTTP REST*** tab, ***Request methods*** sub tab

![Request methods sub tab of the Add/Edit event window listing a POST and a GET request on the path /, both with status 200, and the Add, Edit and Delete buttons for requests and header conditions](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20HTTP%20REST%20Request.png)

On this sub tab you list the requests the Trigger accepts. Each request has a method and a path; the Trigger fires when a request matches both. In the screenshot, the Trigger accepts POST and GET requests on the path `/`, for example `http://<server>:9990/` with the default port.

To read a query parameter in the Job's Tasks, use a result Variable, for example `{TRIGGER(Active|LastTrigger|HTTPREST.Result.QueryParameters.Value|name)}` for the value of `name` in `http://<server>:9990/?name=John`.

Click *Add*, *Edit* or *Delete* under the list to manage requests. In the *Add/Edit http request* window:

* *Method*: "GET", "POST", "PUT", "DELETE", "HEAD", "CONNECT", "OPTIONS" or "TRACE"; you can also type another method name in capital letters
* *Path*: the path of the request, for example `/orders`, without the query string; without *Use Regex*, the path must match exactly, including case
* *Use Regex*: check to treat *Path* as a regular expression; the expression matches anywhere in the request path unless you anchor it, for example `^/orders$`
* *Status code*: the HTTP status code returned when the request matches (default "200"); it must be a whole number, or Variables that return one when the request arrives, otherwise the request gets "404"
* *Content*: the text returned as the response body; you can use Variables

:::warning

If the *Status code* of a matching request, or the *Value* of a yes/no or number header condition, cannot be converted when a request arrives, that request gets "404". After that, the Trigger answers later requests with "404" as well, some of them only after a wait of up to 2 minutes. Correct the value, then deactivate and activate the Trigger.

:::

**Placeholders in the path**

Square brackets and braces in *Path* are always read as placeholders, so they cannot be used for regular expression character classes such as `[a-z]` or counts such as `{2}`. Placeholders work only with *Use Regex* checked; without it, a path that contains them never matches.

* `[name]`: a part that follows the `/` before it, for example `/orders/[id]`; the part can be empty, and at the end of the path it takes the rest of the path
* `{name}`: the same, but the part and the `/` before it can be missing

The value of each placeholder, and of each named group in your expression, is available in the `Parameters` result Variable under its name.

**Header conditions**

Select a request and click *Add* next to *Header condition* to add a condition that the request must also meet. The condition appears under the request, with the columns *Header*, *Condition*, *Value* and *CaseSesitive* (as spelled in the Client). In the *Add/Edit http header condition* window:

* *Header name*: the request value to check, selected from a fixed list, for example *ContentType*, *UserAgent*, *Authorization*, *Host*, *Referer*, *ContentLength* or *KeepAlive*; other header names cannot be entered
* *Condition*: the comparison; date headers offer *Equal*, *Not equal*, *Larger*, *Larger or equal*, *Smaller* and *Smaller or equal*, all other headers *Equal*, *Not equal*, *Contains* and *Not contains*; *Do not check* is selected when you pick a header, and a condition left at *Do not check* is not checked
* *Value*: the value to compare with; you can use Variables; for a yes/no header such as *KeepAlive*, enter "True" or "False", and for a number header such as *ContentLength* a whole number, otherwise matching requests get "404"
* *Case sensitive*: for text headers, check to compare with regard to case

*Contains* and *Not contains* never match a yes/no or number header.

:::warning

Header conditions have these limits:

* Conditions on *Cookies*, *CustomHeaders* and *AcceptRanges* are not checked, so they always pass
* A header that the request does not send is compared as an empty value: empty text, 0, False or an empty date
* When a request has several header conditions, only the result of the last condition that is checked counts

Do not rely on header conditions to protect the Trigger; use *Auth type* with a Credential.

:::
 
***HTTP REST*** tab, ***Save content*** sub tab

![Save content sub tab of the Add/Edit event window with Save content to file, Credentials, Folder, Auto name file, File name and Overwrite options set to Overwrite](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20HTTP%20Save.png)

**Save content to file**

Check to save the body of each request that fires the Trigger to files in *Folder*. The body is read only for POST, PUT and methods that you type yourself in *Method*. For a `multipart/form-data` request sent with POST or PUT, each part is saved as its own file: each uploaded file, and also each text field that is not empty. A `multipart/form-data` body sent with another method is not saved. For any other request with a body, the whole body is saved as one file. The saved files are listed in the `SavedFiles` result Variable.

**Credentials**

Select a [Credential](../server/global-credentials) to write the files as, for example for a network folder. Click the settings button next to the list to open the *Manage credentials* window, where you can add a Credential.

**Folder**

The folder to save to. Click the browse button to select a folder, or type or drag a path. You can use Variables. Required when *Save content to file* is checked.

**Auto name file**

Check to name the files automatically. An uploaded file keeps the file name sent with it, a text field is saved under its value, and any other body is saved under the last part of the request path, for example `order.json` for the path `/upload/order.json`. The path of such a request must end in a file name. *File name* is unavailable while *Auto name file* is checked.

**File name**

The file name to save to. For the parts of a `multipart/form-data` request it is a mask applied to the file name sent with each uploaded file (for a text field, to its text), not to the field name; for example `*` keeps the file name. For any other body it is used as the file name itself, so a mask such as `*` causes an error and nothing is saved. You can use Variables. Required unless *Auto name file* is checked.

**Overwrite options**

What to do when a file with the same name exists: *Overwrite* (default), *Append*, *Skip*, *Auto number*, *Overwrite on size diff*, *Append if smaller or overwrite*, *Append if smaller or skip*, *Append or skip* or *Resume on*. *Resume on* overwrites the file, and *Append or skip* saves only when the file already exists. *Overwrite on size diff*, *Append if smaller or overwrite* and *Append if smaller or skip* save nothing when no file with that name exists yet, and an error is written to the log. *Auto number* saves `<name>2<extension>`, `<name>3<extension>` and so on; it needs a file name with an extension, otherwise nothing is saved.
 
### Result Variables

In the *Variables* window, the result Variables are under the Job's Trigger, *Result*. Click *Variables* at the bottom of the window to open it. See [Variables](global-variables). In a run that this Trigger started, `{TRIGGER(Active|LastTrigger|HTTPREST.Result.ContentString)}` returns the body of the request that started the run.

When the Trigger fires, it sets these result Variables:

* `HTTPREST.Result.ContentString`: the request body as text; not set for a `multipart/form-data` body
* `HTTPREST.Result.Content`: the request body as Base64; not set for an `application/json` body
* `HTTPREST.Result.QueryParameters.Value|<name>`: the value of the query parameter with that name (`HTTPREST.Result.QueryParameters|<name>` returns the same)
* `HTTPREST.Result.QueryParameters.Key|<index>` and `HTTPREST.Result.QueryParameters.Value|<index>`: the name and value of the parameter at that position, counting from 0; `HTTPREST.Result.QueryParameters|<index>` returns `<name>=<value>`; without a name or number, the number of parameters
* `HTTPREST.Result.Parameters.Value|<name>`: the value of a form field (`application/x-www-form-urlencoded` body, not URL-decoded), of a value in a JSON body, or of a path placeholder; the same forms as for query parameters
* `HTTPREST.Result.SavedFiles.Value|<index>`: the path of a file saved by *Save content to file* (`HTTPREST.Result.SavedFiles|<index>` returns `<name>=<path>`)
* `HTTPREST.Result.Headers.<header name>`: the value of a request header from the *Header name* list, for example `HTTPREST.Result.Headers.UserAgent`
* `HTTPREST.Result.Headers.CustomHeaders|<index>` and `HTTPREST.Result.Headers.Cookies|<index>`: other headers and the cookies
* `HTTPREST.Result.Part.Value|<index>` and the other `HTTPREST.Result.Part` Variables: the parts of a `multipart/form-data` body
* `HTTPREST.Result.Response`: the response the Trigger sent; it is set after the response is built, so a Job started with *Immediately* may not see it
* `HTTPREST.Trigger.Address` and `HTTPREST.Trigger.Port`: the address and port of the Trigger

Names are case-sensitive. In a JSON body, a nested value is named by its path with dots, and the name of a value inside a nested object starts with a dot, for example `.customer.name`; array items include their position, for example `items.[0].name`. A name that does not exist returns error text instead of a value.

![Add/Edit event window with the Variables button at the bottom highlighted and the Variables window it opens](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20HTTP%20REST%20Variables.png)
