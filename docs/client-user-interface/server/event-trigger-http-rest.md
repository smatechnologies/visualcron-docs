---
sidebar_label: 'Event Trigger - HTTP REST'
hide_title: 'true'
---

## Event Trigger - HTTP REST

The HTTP REST Trigger is able to host a local HTTP server, on a certain path and be able to receive requests through GET and POST through that path. The Trigger will capture all details about the request including parameters received. These parameter values, among other information about the request, can be accessed as Variables for the Trigger.
 
 
**Main settings**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20HTTP%20REST.png)

**Address**

Use this property to set the authentication realm. All pages in the same realm share authentication credentials.Realm parameter refers to Digest authorization and is not a required parameter.
 
**Realm**

Use this property to set the authentication realm. All pages in the same realm share authentication credentials.Realm parameter refers to Digest authorization and is not a required parameter.
 
**Request methods tab**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20HTTP%20REST%20Request.png)

In this tab you specify the paths and methods supported. Above you can access [http://localhost:9991/go2](http://localhost:9991/go2) with POST and [http://localhost:9991/go3?name=John(http://localhost:9991/go3?name=John) with GET. To get the parameter value you can use this Variable in follow up Tasks: `{TRIGGER(Active|LastTrigger|HTTPREST.Result.QueryParameters.Value|name)}`
 
**Save content tab**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20HTTP%20Save.png)

In this tab you can control File uploads and choose how to name the files.
 
**Variables**

As other Triggers, this Trigger produces Variables that contain various information about the request.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20HTTP%20REST%20Variables.png)

