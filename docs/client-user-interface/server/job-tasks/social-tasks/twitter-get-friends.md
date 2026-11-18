---
sidebar_label: 'Task Social - Twitter - Get Friends (deprecated from VisualCron v13.2.1)'
hide_title: 'true'
---

:::warning

**Deprecated**

Twitter integration described on this page is deprecated from **VisualCron v13.2.1**.

:::

## Task Social - Twitter - Get Friends

The Twitter - Get friends Task retrieves a user's friends in Twitter.

![Twitter - Get friends tab with the Connection, the User Id and Only IDs check boxes and the User name box](../../../../../static/img/tasksocialtwittergetfriends.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Twitter - Get friends tab

- _Connection_: the Twitter Connection to use; see [Twitter Connection](../../../server/connection-twitter)
- _User Id_: when checked, _User name_ holds the numeric user ID instead of the screen name
- _Only IDs_: return only the ID numbers of the friends
- _User name_: the screen name, or with _User Id_ the user ID, of the user whose friends to return

See Twitter Developer Documentation for detailed [GET friends](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-ids) information.
