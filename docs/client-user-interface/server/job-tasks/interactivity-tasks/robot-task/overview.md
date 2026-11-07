---
sidebar_label: 'Task Interactivity - Robot Task'
hide_title: 'true'
---

## Task Interactivity - Robot Task

The Robot Task automates desktop applications, web browsers, Excel workbooks, files and folders by running a sequence of activities that you build or record.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../../job-tasks).

The Robot Task is available in the Pro edition.

With the Robot Task, you can:

- Automate repetitive desktop workflows
- Work with web applications and browser-based systems
- Read data from applications, web pages, files and Excel workbooks
- Enter and change data
- Work with older applications that have no API
- Combine several applications into one workflow

![The Robot Task window with the Robot tab and its Designer tab open, showing the activity list, a sequence with a New Excel activity, and the Properties pane](../../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Robot%20Task.png)

### How the Robot Task runs

The Robot Task always runs in the foreground. The VisualCron Server hands it to a connected [VisualCron Tray Client](../../../../../using-visualcron/visualcron-tray-client), chosen by the Task's [execution context](../../../task-main-settings-execution-context): by default the Tray Client of the user set there, and with any foreground user, the first Tray Client connected. The activities run in that desktop session, as the user logged on to it. That user's permissions apply to every file, folder, application and Excel workbook the activities use.

If no matching Tray Client is connected to the Server, the Task fails.

### Robot tab

The ***Robot*** tab has three tabs: ***Designer***, ***Settings*** and ***Mapping***.

#### Designer tab

The ***Designer*** tab is where you build the sequence.

- **Activity list**: on the left, the activities grouped by category, with a _Search_ box. Drag an activity into the sequence to add it. See [Robot Task Activities](activities/overview) for the categories and activities
- _Select element_: pick a control on the screen, and get a list of activities that suit it
- **Sequence**: the workflow in the middle. Activities in a sequence run in order, one after another, and a sequence can contain other activities that have their own bodies, such as conditions, loops and Excel containers. _Expand All_ and _Collapse All_ open or close every activity in the view
- **Properties pane**: on the right, the properties of the selected activity, such as _Display name_, _Error settings_, _Wait before_ and _Wait after_, and the activity's own settings
- _Variables_ and _Imports_: below the sequence, the workflow variables and the imported namespaces
- _Runtime errors_: the errors from the last test run
- _Scan windows_: scans the open windows for controls and lists them on the ***Mapping*** tab
- _Clear actions_: removes all activities from the sequence, or all controls from the ***Mapping*** tab when that tab is open, after you confirm
- _Test run_: runs the sequence from the Client, so that you can check it
- _Start recording_: records your mouse and keyboard actions as activities

#### Settings tab

**Record settings**

- _Use cache request to search UI elements_: checked by default; also used when the Task runs
- _Auto move recorder panel if it blocks interaction_: checked by default
- _Draw rectangles_ and _Draw interval_: draw a rectangle around each element as it is found, every 300 milliseconds by default

**Activities settings**

- _Set wait for all_: sets the wait time of all activities at once
- _Activities repository_: opens the repository of additional activities

**Playback settings**

- _Playback speed_: how fast the activities are played back
- _Execution mode_: "StepMode" (default) runs the sequence on the ***Designer*** tab; "MapMode" runs the controls on the ***Mapping*** tab instead
- _Show progress during playback_: shows a progress panel during a test run
- _Sequence transparency level_: how transparent the playback panel is

**Web browser settings**

- _Settings_: the browser settings used by the web activities

When the Task runs in a Job, no rectangles and no progress panel are shown.

#### Mapping tab

The ***Mapping*** tab lists the controls found with _Scan windows_, with the value to set or read for each. It is used when _Execution mode_ is "MapMode".

### Output tab

The ***Output*** tab can record what happens on the screen while the Task runs.

- _Output type_: "None", "Images", "GIF" (default) or "Video"; a new Robot Task records a GIF of every run unless you set "None"
- _Frame rate_ and _Quality_: the recording frame rate and quality
- _Image format_: the file format for "Images"
- _Open settings_: the video compression settings for "Video"
- _Save output to file_: also save the recording to a file
- _Output folder_ and _File name_: where the recording is saved
- _Credentials_: the Credential used to write the file

### Output and errors

The Task fails, with exit code 77777, when an activity raises an error that no Try Catch activity or _Error settings_ rule handles, or when anything is written to the Task's error output. The errors are in the Task's error output.

:::warning

An error that a Try Catch activity catches, or that an _Error settings_ rule ignores, is written only to the Task output, and the Task reports success. The same applies to a _Wait For File_ or _Wait For Folder_ that times out with _Throw exception_ cleared, to a _Set Focus_ that cannot set the focus, and to a _Search Text and Click_ or _Search Text and Hover_ that does not find its text. Test the result of steps that must succeed, and log what was skipped.

:::

### Key features

- **Desktop recording**: capture mouse clicks and keyboard input as activities
- **Web automation**: work with web browsers and web-based applications
- **Activity-based workflow**: build sequences of well-defined activities
- **Variable support**: use Job and User Variables in the activities
- **Data extraction**: read data from screens, controls, web pages and files into variables
- **Error handling**: add conditions and error handling to sequences

### Common use cases

1. **Web data entry**: fill out and submit web forms
2. **Older application integration**: automate applications that have no modern API
3. **Document processing**: read text from the screen with OCR
4. **Excel automation**: create, change and save Excel workbooks
5. **E-mail automation**: send e-mail with Outlook, with data from other sources, and handle incoming messages
6. **Cross-application workflows**: move data between applications

### Best practices

- **Keep sequences simple**: break complex workflows into smaller, manageable sequences
- **Use Variables**: store reusable data in Variables rather than typing values into each activity
- **Add waits**: add suitable waits between actions so that applications have time to respond
- **Test thoroughly**: test with _Test run_ in a controlled environment before you schedule production Jobs
- **Document steps**: describe complex parts of the sequence for later maintenance
- **Monitor runs**: check the Task output and the Job log to make sure the Task runs reliably
- **Handle errors**: add error handling for critical steps that might fail
- **Name every activity**: set the _Display name_ property of each activity so that the sequence is readable at a glance; you should be able to tell what an activity does from its name
- **Avoid collisions**: Robot Tasks, Web Macro Tasks and every other foreground Task share the desktop session they run in, and interfere with each other if they run at the same time; schedule such Jobs so that they do not overlap, or run them in separate sessions or on separate machines

### Error handling notes

The _Try Catch_ activity does not work with Web Macro activities. When a Web Macro activity raises an error, the sequence is stopped before Try Catch can catch it. Two workarounds are available:

- **Allow to ignore the element**: in the Web Macro activity's settings, check _Allow to ignore the element_, so that the sequence is not stopped when the element is not found
- **Error settings on the activity**: the other activities have an _Error settings_ property in the Properties pane, where you can choose to ignore an error rather than stop the sequence

See [Error Handling](activities/error-handling).

### Tips for recording

- Make sure the target application is stable and responsive before you record
- Move slowly and deliberately during recording, so that actions are captured accurately
- Switch between windows as little as possible during recording, so that elements are detected properly
- Close applications you do not need, to reduce the load and improve capture accuracy
- Use clear, recognizable screen positions for consistent playback
- Test recordings in the same environment where they will run
