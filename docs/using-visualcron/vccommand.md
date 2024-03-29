---
sidebar_label: 'VCCommand'
hide_title: 'true'
---

## VCCommand

VCCommand.exe is a command line tool residing in the install folder\VCommand folder. The VCCommand is an alternate way, just like the API to interact with a local or remote server. This command line tool is based on command line switches that can perform the following actions at the moment:

* Run a Job
* Activate a Job
* Deactivate a Job
* Stop a Job
* Run a Task
* List Jobs
* Activate license
* Deactivate license
 
*You can see existing command switches and examples by running VCCommand.exe without any parameters:*

*Example: VCCommand --action runjob --connectionmode local --username admin --password xyz --name "Job Id or Name"*

*Example: VCCommand --action activatejob --connectionmode local --username admin --password xyz --name "Job Id or Name"*

*Example: VCCommand --action deactivatejob --connectionmode local --username admin --password xyz --name "Job Id or Name"*

*Example: VCCommand --action stopjob --connectionmode local --username admin --password xyz --name "Job Id or Name"*

*Example: VCCommand --action runtask --ip 127.0.0.1 --connectionmode remote --username admin --password xyz --name "Job Id or Name"*

*Example: VCCommand --action runjob --ip 127.0.0.1 --connectionmode remote --username admin --password xyz --name "Job Id or Name"*

*Example: VCCommand --action listjobs --connectionmode local --username admin --password xyz*

*Example: VCCommand --logontype ad --action listtasks --connectionmode local*

*Example: VCCommand --logontype ad --upn username@domain.com --action listtasks --ip 127.0.0.1 --connectionmode remote --port 16444*

*Example: VCCommand --logontype ad --spn HOST/hostname.domain.com --action listtasks --ip 127.0.0.1 --connectionmode remote --port 16444*

*Example: VCCommand --action activate --r xxxxx-xxx-xxxx-xxxx --connectionmode local --username admin --password xyz*

*Example: VCCommand --action deactivate --connectionmode local --username admin --password xyz*