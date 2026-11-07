---
sidebar_label: 'Web Macro'
hide_title: 'true'
---

## Robot Task Activities - Web Macro

The Web Macro activities drive a web browser from a Robot Task: they navigate, click, fill in fields, extract data, and download and upload files.

![The Web Macro category in the activity list, with Checked Element, Click Element, Copy Link, Copy Value, Create Tab, Download File, Extract Data, Extract Table, Inject JS Script, Key Event, Launch New Instance, Navigate to URL, Open Browser, Populate Field, Print Page, Respond to JS Dialog, Save Page Source, Set Proxy, Take Screenshot and Upload File](../../../../../../../static/img/RPA/Robot%20Tasks/Web%20Macro/Web%20Macro.png)

These activities use the same browser and the same step settings as the Web Macro Task. See [Task Net - Web Macro](../../../net-tasks/web-macro).

### Required nesting

Web Macro activities run only when they are nested correctly:

- Every Web Macro activity, including _Launch New Instance_, must be inside an _Open Browser_ activity
- Every other Web Macro activity must also be inside a _Launch New Instance_ activity

```text
Sequence
  Open browser
    Do
      Launch new instance
        Actions
          Create tab
          Navigate to URL
          Click element
          ...
```

Rather than building this by hand, record the actions in a Web Macro Task and copy them into the Robot Task. See [Recording Web Macro for Robot Task](../recording-web-macro-for-robot-task).

Each Web Macro activity has its own settings window, with a ***Wait*** tab:

- _Wait before execute_: the wait in milliseconds before the activity runs
- _Wait after execute_: the wait in milliseconds after the activity runs

---

### Open Browser

Opens the browser window. This is the outermost Web Macro activity.

- Click _Edit action_ in the shortcut menu to record Web Macro actions
- Click _Browser settings_ in the shortcut menu to open the browser settings window, which has the same options as the Web Macro Task

The browser settings include:

- _Load images_: load the images on the page. Clearing it makes pages load faster
- _Store cookies_: keep cookies between runs
- _Block popups_: block popup windows
- _Lite mode_: run the browser with fewer features
- _Disable WebSecurity_: turn off the browser's web security restrictions
- _Override User-Agent_: send a custom User-Agent string
- _Override referer_: send a custom referer value
- _Accept-Language_: the Accept-Language header sent with requests, for example `en-US`
- _Google API_: the _GoogleClientID_, _GoogleAPIKey_ and _GoogleClientSecret_ values

---

### Launch New Instance

Launches a new web instance. All other Web Macro activities go inside this activity's _Actions_ body.

Click _Edit action_ to open the settings window.

---

### Click Element

Clicks a web element.

- _Allow to ignore the element_: continue the sequence if no element is found at the path, instead of failing
- _Wait element_: how long, in seconds, the activity waits for the element to appear
- _Relative_: find the element by its path
- _Frame path_: the CSS selector of the frame that holds the element, when the element is inside a frame
- _Element path_: the path to the element, as a CSS selector or XPath
- _By position_: click the element at its X and Y position
- _By search_: find the element by searching, which helps when the element's path changes between runs

**How By search works:** all elements that match the _Selector_ are collected, the _Attribute_ value of each is read and tested against the _Regex value_, and the element at the _Position_ in the filtered results is used.

For all three ways to find an element, see [Element Path](element-path).

:::note

_Allow to ignore the element_ is the error handling option for Web Macro activities. Web Macro activities do not have the _Error settings_ property. See [Error Handling](error-handling).

:::

---

### Checked Element

Checks or clears a web element, such as a check box. The settings are the same as for _Click Element_, plus:

- _State_: the state to set

---

### Copy Link

Copies the link of a web element to the clipboard. The ***Source*** tab has the same element settings as _Click Element_.

To save the link to a variable instead, use the ***Variable*** tab:

- _Job Variable_: save the link to this Job Variable
- _User Variable_: save the link to this User Variable
- _Variable type_: the data type of the variable, for example "String"

---

### Copy Value

Copies the value of a web element to the clipboard. The element settings are the same as for _Click Element_.

---

### Download File

Downloads a file from a URL, or clicks a web element that starts a download.

- _Force download_: download the file straight from a URL
- _Original file/path_: the URL of the file
- _Credential_: the Credential used to reach the folder the file is saved to
- _Folder_: the folder the file is saved to
- _File mask_: the file name to save as
- _Overwrite options_: what to do if the file already exists

Without a direct URL, clear _Force download_ to turn on the ***Element*** tab, then fill in the element settings for the link or button that starts the download.

---

### Extract Data

Extracts data from a web element.

### Extract Table

Extracts an HTML table from the page. Use this to put a table straight into a [List Variable](list-variable) for row-by-row processing.

---

### Inject JS Script

Runs JavaScript code in the page. Type the code on the ***Inject JS*** tab.

Use this for actions the other activities cannot do, such as scrolling an element into view or reading a value the page calculates.

---

### Key Event

Sends a key event to the page.

---

### Respond to JS Dialog

Responds to a JavaScript alert, confirm or prompt window.

- _Input dialog_: the text to enter when a prompt window opens
- _Button dialog_: the button to click when the window opens: "Yes/Ok" or "No/Cancel"

Click _Mask value_ to hide the text, for example when it is a password.

---

### Populate Field

Fills in a web element with a value. The element is set on the ***Source*** tab and the value on the ***Populate*** tab.

- _Value_: the value to fill in
- _Mask value_: hide the value, for example when it is a password
- _Milliseconds per character_: the wait in milliseconds between characters, which simulates typing
- _Is Enter_: press Enter after filling in the field

For help with finding form fields when a page changes their order, see [Web Input - Element Path](../web-input-element-path).

---

### Print Page

Prints the web page.

- _Select printer_: the printer to use, from the printers installed on the computer
- _Printer settings_: the page range, number of copies, duplex and orientation

---

### Save Page Source

Saves the source of the web page to a variable. Choose the Job Variable or User Variable that receives the page source.

---

### Navigate to URL

Goes to a URL.

- _URL_: the URL to go to

---

### Create Tab

Creates a new tab. The settings window has only the ***Wait*** tab.

---

### Take Screenshot

Takes a screenshot of the web page and saves it to a file.

- _Credential_: the Credential used to reach the folder
- _Folder_: the folder the image is saved to
- _File name_: the file name of the image
- _Overwrite options_: what to do if the file already exists
- _Screenshot type_: "Window" captures the visible part of the page, and "Page" captures the whole page

---

### Upload File

Clicks a web element and uploads a file. Fill in the **File filter** fields to choose the files to upload.

The file filter has the tabs ***Location***, ***Content***, ***Date***, ***Size***, ***Attributes***, ***Result*** and ***Test***. Its settings include:

- _Credentials_: the Credential used to reach the folder
- _Folder_: the folder to look for files in
- _Include sub folders_: search the subfolders too
- _Exclude folder(s)_: folders to skip
- _Include file mask_: the mask for the files to upload, with the _Is regex_ and _Case sensitive_ options
- _Use file exclusion_: turn on an exclusion mask, with its own _Is regex_ option

---

### Set Proxy

Uses the proxy server set in the activity to reach the web page.

---

### Tips

- Record the sequence in a Web Macro Task first, then copy it into the Robot Task. That is much faster than building the nesting by hand, and the structure is always right. See [Recording Web Macro for Robot Task](../recording-web-macro-for-robot-task)
- Replace recorded position-based paths with attribute-based CSS selectors before the Task goes into production. Recorded positions stop working the first time the page layout changes
- Set _Wait element_ rather than adding fixed waits between activities. The activity continues as soon as the element appears
- Check _Allow to ignore the element_ on activities where a missing element is acceptable, such as closing a cookie banner that may or may not be shown
- Use _Mask value_ on any _Populate Field_ or _Respond to JS Dialog_ activity that handles a password, so that the value is hidden
- Clearing _Load images_ in the browser settings makes pages with many images load noticeably faster
