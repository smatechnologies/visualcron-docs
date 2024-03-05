---
sidebar_label: 'Task Social - Twitter - Get Timeline'
hide_title: 'true'
---

## Task Social - Twitter - Get Timeline

The Twitter - Get timeline Task retrieves own or specified user timeline in Twitter.

![](../../../static/img/tasksocialtwittergettimeline.png)

**Connection**

To use Twitter Tasks you need to create a Connection first. You do that in the [Twitter Connection](connection-twitter) dialog.
 
**Home/User**

Select own or specified user time-line.
 
**Max count of tweets to retrieve**

Specifies the number of Tweets to try and retrieve, up to a maximum of 200 per distinct request.
 
**Since ID**

Returns results with an ID greater than (that is, more recent than) the specified ID.
 
**Max ID**

Returns results with an ID less than (that is, older than) or equal to the specified ID.
 
**Include entities**

The entities node will not be included when not checked.
 
**Exclude replies**

This setting prevents replies from appearing in the returned timeline.
 
**Trim user**

When checked, each Tweet returned in a timeline will include a user object including only the status authors numerical ID.
 
See Twitter Developer Documentation for detailed [GET timeline](https://developer.twitter.com/en/docs/api-reference-index) information.
