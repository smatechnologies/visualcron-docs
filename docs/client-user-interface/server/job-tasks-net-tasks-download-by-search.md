---
sidebar_label: 'Download By Search'
hide_title: 'true'
---

## Download By Search

The webmacro task has a download step that is added automatically when you download something while recording a webmacro. You can edit this step after recording by right-clicking and choosing “Edit Action”.
 
The download step contains a forced download, or download by action, for example, a mouse click on a button.
When forced download, the user must check the “Force download” checkbox. A forced download is downloading from a direct link.
 
When the direct download is impossible, for example, downloading occurs only after clicking on the button, then the user needs to uncheck the “Force download”. After the user unchecked, the “Element” tab will be available.
 
In this tab, the user can select three options: Relative, By Position, By Search.
 
The relative option allows you to access an element by a relative path. The user must specify the path to the HTML element. This element will be clicked for further download.
 
The path to the HTML element can be written in the CSS selector and XPath formats.
 
The position option allows you to access an element by X, Y coordinates. The user must specify the X, Y values. This element will be clicked by position for further download.
 
The search option allows you to find the html element by selector, attribute, regex value, and position. This element will be clicked for further download.
 
For example, take the test site [https://www.visualcron.com/oldversions.aspx](https://www.visualcron.com/oldversions.aspx), where there is a list of VisualCron versions that can be downloaded, or by direct link (forced), writing: [http://neteject.com/download/VisualCron/ VisualCron9.6.5.exe](http://neteject.com/download/VisualCron/ VisualCron9.6.5.exe), or by pressing the mouse button (uncheck “ForceDownload” and specifying the options to access to the element in the “Element” tab).

For example, a user wants to always download the latest version. At the moment it is 9.6.5
 
There are several options for achieving this:
1.Forced download with a static link [http://neteject.com/download/VisualCron/VisualCron9.6.5.exe](http://neteject.com/download/VisualCron/VisualCron9.6.5.exe)
2.Forced download with a "static" link using VC variables [http://neteject.com/download/VisualCron/VisualCron{USERVAR(VCVersion)}.exe](http://neteject.com/download/VisualCron/VisualCron{USERVAR(VCVersion)}.exe)
3.Downloading by clicking on the element by relative path.
4.Downloading by searching and clicking to the founded element.
 
The first option is only suitable for links that will not change and have direct access to the downloaded file via the link.
The second option is suitable for links that change and have direct access via the link to the download file.
The third and fourth options are more interesting in the sense that the user can find more complex elements in the DOM tree and click on it to download.
 
Since we always need to download the latest version of the file, the first option will not work for us, because the link will change when a new version of the file appears.
 
We can use the second option to download a specific version using the VisualCron variables, we will somehow change the variable to the latest version of VisualCron for a successful download. For example, increment the variable ```{USERVAR(VCVersion)}```.
VCVersion = 9.6.5
 
After a successful download, we update the version (variable) to 9.6.6
But in this case, it may turn out that the version will not be released 9.6.6, but 9.7.0, and we cannot guess for sure. This is very specific and not reliable.
 
In such cases, the third or fourth options are suitable for us. Downloading by clicking on the element.
 
By relative: We need to find an element using one of the CSS selector or XPath formats.
We will use the simple selector: “table> tbody> tr: nth-child (2) a”
First, we find the “table” element, inside it we find the “tbody” element, then since the first “tr” element is the head of the table, we take the second row of the “tr: nth-child (2)” table (second row), further inside the row we find the element “a”.
On this element “a” the “click” action will be performed for further download.
This way we can always download the latest version of the file.
 
By search: This option is more flexible than just accessing the element by relative path. We can more accurately find the desired element. And from all matches, we can take the first, last element, or specify the exact index. (first: 0, last: -1, pre last: -2 and etc)
First, we should fill the selector field to find all elements by specific ```selector. (document.querySelectorAll()``` native function is used)
Then we can fill the attribute field to select the elements which contain the specified attribute only.
Then we can fill the regex value field to select all elements which match the selected attribute value.
Then we can set the position field to get the specific element from all found elements.
 
Selector: We write ‘a’ to find all ‘a’ tags on this page.
Attribute: We write ‘href’ to check the regex value with this attribute value. We will get ‘href’ attribute value like ‘[http://neteject.com/download/VisualCron/VisualCron9.9.6.exe](http://neteject.com/download/VisualCron/VisualCron9.9.6.exe)’ and check this value with regex. (In this field you can set any attribute which supported by this element)
Regex: We write ‘^[http://neteject.com/download/VisualCron/VisualCron](http://neteject.com/download/VisualCron/VisualCron)’. This means that we get all elements whose the href attribute value starts with the string ‘[http://neteject.com/download/VisualCron/VisualCron](http://neteject.com/download/VisualCron/VisualCron)’. We found all download links.
Position: We write First, 0. Because we need to get the first link (latest VC version).
 
On this element “a” the “click” action will be performed for further download.
This way we can always download the latest version of the file.
 
Element tab options are also available for other steps. like ‘ClickLink’ step.
 
More information:

[https://www.w3schools.com/jsref/met_document_queryselector.asp](https://www.w3schools.com/jsref/met_document_queryselector.asp)
[https://www.w3schools.com/jsref/met_document_queryselectorall.asp](https://www.w3schools.com/jsref/met_document_queryselectorall.asp)
[https://www.w3.org/TR/selectors-3/#selectors](https://www.w3.org/TR/selectors-3/#selectors)
[https://www.w3schools.com/xml/xpath_syntax.asp](https://www.w3schools.com/xml/xpath_syntax.asp)
[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)
[https://developer.chrome.com/docs/devtools/css/](https://developer.chrome.com/docs/devtools/css/)
