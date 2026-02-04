---
sidebar_label: 'Objects - Object Search'
hide_title: 'true'
---

## Objects - Object Search

The main menu **Tools > Objects > Object search** option performs search for a string within all internal objects of VisualCron. All properties that matches this string will be listed in the result grid. it is possible to replace these strings with other value.
 
**Tools > Objects > Object search** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Tools/Objects/Object%20text%20search-replace.png)

**Object(s) type**

Select the internal object type in VisualCron which the Search and Replace should be based on.
 
**Search**

**Search text**

Text string that is used for the Search.
 
**Use exact search**

Check if you want an exact search and not on wild cards around the Search text.
 
**Search encrypted values**

Some values are encrypted in VisualCron. Searching these takes longer time. It is possible to optionally exclude these values.
 
**Search result**

The search result table shows the object name, the internal class in VisualCron, the property name of the object in the class and the Property value which is the string it was matched to. You can double click on an object to edit the information. Check the checkbox to the left to include it in the *Replace*.
 
**Replace**

Enter the text that you want to replace with. Clicking Replace will replace all selected values from *Search*. A good example can be found below: 

Current String Value = This is a test

We want to update "This is a test" to "This is a test example". To do that, we need to input the whole new string

New String Value = This is a test example

This will convert every "This is a test" to "This is a test example". 
