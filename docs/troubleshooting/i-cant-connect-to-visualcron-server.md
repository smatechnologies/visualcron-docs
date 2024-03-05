---
sidebar_label: 'I Cannot Connect to the VisualCron Server'
hide_title: 'true'
---

Please check the following:

* Is the port and address correct?

* Open the _Windows Control Panel -> Administrative Tools -> Services_. In the list of services, locate VisualCron Service. Is the "VisualCron Service" started?
 
 
Open the log file server_startup.txt. If it contains:

_ComService() exception (System.ArgumentException: It is likely that certificate 'CN=vc' may not have a private key that is capable of key exchange or the process may not have access rights for the private key._

Perform these steps:
 
1. Stop the VC server
2. Go to VisualCron installation folder
3. Start VisualCronService.exe manually right clicking on that and choose _Run as->Administrator_
4. Click on Delete Certificates button
5. Click on the Create Certificates button
6. Exit application
7. Start VisualCron service
8. Try to connect again