---
sidebar_label: 'Maintenance Expiration'
hide_title: 'true'
---

## Maintenance and subscription expiration

This page shows where the Client displays the maintenance or subscription expiration date of a Server, what each state means, and how to refresh the date after you renew. For what stops when the date passes, see [Maintenance and subscription](maintenance).

### Where the expiration date is shown

The *Expiration* column on each Server row in the main grid shows the state of that Server's license:

| The *Expiration* column shows | When |
| --- | --- |
| "Maintenance expires `<date>`" or "Subscription expires `<date>`" | More than 45 days remain |
| "Maintenance expires In `<n>` day(s)" or "Subscription expires In `<n>` day(s)", on an orange background | 45 days or fewer remain |
| The same text on a red background | Fewer than 7 days remain |
| "Maintenance has expired" or "Subscription has expired", on a red background | The date has passed |
| "Not validated yet" or "Unable to verify maintenance expiration" (or "subscription expiration"), on a red background | The Client does not have an expiration date for the Server yet |

On a Server in trial, the column shows the trial days instead. See [Trial time](trial-time).

![Main grid with the Expiration column of a Server row highlighted, showing the subscription expiration date](../../static/img/Using%20VisualCron/Maintenance%20Expiration/License%20Expiration.png)

### The days-left button

When 45 days or fewer remain, a days-left button appears in the *Information* group of the ***Server*** tab. It shows the number of days left, or "0" after the date has passed. Select it to open a renewal reminder. The *View license(s)* button in the reminder opens your licenses on the VisualCron website.

The button is not shown for licenses that renew automatically, or for a Server in trial. If the Server's license has not been validated yet, the button shows "0"; select *Refresh license data*.

### Refresh the expiration date

The date updates when VisualCron validates the license (see [License validation](license-validation)). After you renew, the new date might not show right away.

To refresh the expiration date now, complete the following steps:

1. In the main grid, right-click the Server row.
2. Select *Refresh license data*.

You can also select *Server* -> *Information* -> *License* -> *Refresh license data*. The Client checks the license with VisualCron at once, from this computer. The *Expiration* column then shows the new date.

If the date is not refreshed please make sure you have associated the Maintenance code online that you purchased with the license you wanted to renew. Then select *Refresh license data* again. If the date still does not refresh, contact [support@visualcron.com](mailto:support@visualcron.com).
