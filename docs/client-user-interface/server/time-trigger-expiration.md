---
sidebar_label: 'Time Trigger - Expiration'
hide_title: 'true'
---

## Time  Trigger - Expiration

**Time Trigger Expiration**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Time%20Triggers/Time%20Trigger%20Expire.png)

**Event Trigger Expiration**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Expires.png)

Configure when the time/event trigger should be removed or deactivated.

**Use trigger expiration**

A master checkbox that enables the expiration controls. When unchecked, the date/time fields and the action radio buttons below are disabled.

**Expiration**

The expiration date and time. The field is split into a date picker and a separate time picker. When the configured moment is reached, the action selected below is performed on the Trigger.

On the **Time Trigger Expiration** form, this is the only expiration mode available — Time Triggers always expire at a specific date and time.

On the **Event Trigger Expiration** form (see [Event Triggers](../server/event-triggers)) an additional radio mode is available that lets the Trigger expire after it has fired a given number of times.

**Expiration action**

Choose what should happen to the Trigger when it expires using the two radio buttons:

* **Deactivate trigger** — the trigger will still remain in the Job but is inactive and cannot be triggered until it is set to active again
* **Delete trigger** — the trigger will be deleted from the Job and will never be seen again (default)
