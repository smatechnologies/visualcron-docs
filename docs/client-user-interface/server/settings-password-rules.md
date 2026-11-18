---
sidebar_label: 'Settings - Password Rules'
hide_title: 'true'
---

## Settings - Password Rules

The **_Password rules_** tab sets password requirements for VisualCron users: password length and complexity, password expiry, reuse of old passwords and account lockout. It also sets an idle time-out for Client connections. This tab is one of the tabs of the Server settings window (see [Main - Settings](main-settings)). You create users in [Main - User Permissions](main-user-permissions).

The password settings apply to VisualCron users that log on with a VisualCron user name and password, not to Active Directory users. The idle time-out applies to every Client connection to the Server while the rules are on, also for Active Directory users.

The desktop Client checks password expiry, the expiry warning and the forced change at first logon when it connects to the Server. It checks length, complexity and re-use when a password is set in the Client. Logons that do not go through the desktop Client, for example through the Web API, are not checked for expiry. The account lockout applies to every logon.

_Server_ -> _Main settings_ -> _Settings_ -> **_Password rules_** tab

Check _Implement password rules_ to turn the rules on, set the values, and click _Apply settings_. The other settings are available only while _Implement password rules_ is checked. The rules are off by default.

:::warning

On a Server where the rules have never been saved, the tab shows "35" for _Maximum password age_, "1" for _Prompt user to change password_, "600" for _Idle Session time-out minimum_ and "0" for every other value. A length or complexity value of "0" accepts any password, and _Lock account for_ "0" minutes does not lock the account. After you check _Implement password rules_, set each value before you click _Apply settings_.

:::

### General

- _Maximum password age_: the number of days after which a password expires, from "35" to "365". When a user connects with an expired password, the Client asks for a new password. If the user cancels, the Client disconnects (see [Login](../../using-visualcron/login))
- _Minimum password length_: the minimum number of characters

### Complexity

The minimum number of characters of each kind that a new password must contain.

- _Minimal alphabet lowercase character_: letters a to z
- _Minimal alphabet uppercase character_: letters A to Z
- _Minimal numeric character_: digits 0 to 9
- _Minimal special character_: any other character

### Behavior

- _Prompt user to change password_ `<n>` _days before expiration_: when a user connects within this many days of the expiry date, the Client shows the date the password expires. From "1" to "1024"
- _Not possible to re-use last_ `<n>` _passwords_: a user cannot set one of this many previous passwords again
- _Lock account for_ `<n>` _minutes when 3 successively failed log-on attempts_: when a user enters a wrong password more than three times in a row, the account is locked for this many minutes. The count is reset only when the user logs on successfully. Until then, each further wrong password locks the account again for the full time, also after an earlier lock has ended
- _Idle Session time-out minimum_ `<n>` _seconds_: when there is no keyboard or mouse input on the computer where the Client runs for this many seconds, the Client disconnects from the Server. From "600" to "100000"
- _Force user to change the password the first login_: users you create must set a new password the first time they connect. Unchecked by default
