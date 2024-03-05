---
sidebar_label: 'I Forgot My Server Password'
hide_title: 'true'
---

The password is located at the computer where the VisualCron Server is installed.

* Exit the VisualCron client

* On the computer where the VisualCron server is installed, open the Windows _Control Panel -> Administrative Tools -> Services_. Mark the "VisualCron Service" in the list, right click and select "Stop service"

* Delete the file called "users.xml". By default, the file is installed in the "C:\Program\VisualCron\settings" folder

* Go back to the Services window and select "Start service" for the "VisualCron Service"

* Start the VisualCron Client. Login with username "admin" and a blank/empty password. Remember to update the username and password when you have logged in