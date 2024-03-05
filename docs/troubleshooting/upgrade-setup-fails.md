---
sidebar_label: 'Upgrade/Setup Fails'
hide_title: 'true'
---

## Upgrade/Setup Fails

When you are doing an upgrade the previous version is first uninstalled and then the new version is installed. If something should go wrong here you can end up with the error messages that says "The specified service does not exist as an installed service.". In this case you get nowhere because the program is installed but the service for VisualCron is not. The solution for this are the following steps (your settings will remain):
 
1. Download and install Microsoft Cleanup Utility from this page: [https://support.microsoft.com/en-us/help/17588/windows-fix-problems-that-block-programs-being-installed-or-removed](https://support.microsoft.com/en-us/help/17588/windows-fix-problems-that-block-programs-being-installed-or-removed)
2. Run the "Windows Install Clean Up" that was installed
3. Locate VisualCron in the list and click on Remove
4. Remove all files in the VisualCron main folder but keep all sub folders (and their content)
5. Install the latest version VisualCron again