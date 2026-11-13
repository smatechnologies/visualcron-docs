---
sidebar_label: 'Variables'
hide_title: 'true'
---

## Robot Task Activities - Variables

The Variables activity writes a value to a VisualCron User Variable or Job Variable from inside a Robot Task.

![The Variables category in the activity list, with the Set variable activity](../../../../../../../static/img/RPA/Robot%20Tasks/Variables/Variables.png)

---

### Set variable

Sets the value of a User Variable or Job Variable. The activity is shown as _Set Variable_ once it is in the sequence.

![The Set Variable activity with the Variable and Value fields](../../../../../../../static/img/RPA/Robot%20Tasks/Variables/Set.png)

- _Variable_: the name of the variable
- _Value_: the value to set. Accepts variables, so the value can be built from other variables, an RPA Result variable or a variable function
- _TypeOfVR_: in the Properties pane, the kind of variable to write to: "User" or "Job". Default: "User"

The value that was set and the variable name are written to the Task output.

---

### Variables in a Robot Task

A Robot Task can read and write the same variables as any other VisualCron Task:

- **Job Variable**: belongs to one Job. See [Job Variables](../../../../job-variables)
- **User Variable**: shared across Jobs, created in the Variables window or by an activity such as _Set variable_. See [Global - Variables](../../../../global-variables)
- **List Variable**: a User Variable that holds rows and columns, created and changed by the [List Variable](list-variable) activities
- **RPA variable**: the value an activity writes to its _Result_ property. It exists only while the Robot Task runs and is read as `{RPA(VariableName)}`

VisualCron also has many built-in variables that need no setup, such as server, date, file and Job variables. Browse them with the _Variables_ button at the bottom left of the Edit Job and Edit Task windows.

:::note

The variables for a Job or Task are available only after the Job or Task has been created.

:::

---

### RPA result variables are not Job or User Variables

An activity's _Result_ property does not create a Job Variable or User Variable. It creates an RPA variable that exists only while the Robot Task runs, read as `{RPA(VariableName)}`.

To use a value from a Robot Task in a later Task of the same Job, copy the RPA value into a Job Variable with a _Set variable_ activity:

- _TypeOfVR_: "Job"
- _Variable_: `jvFileFound`
- _Value_: `{RPA(Exists)}`

---

### Naming convention

Put the kind of variable, abbreviated in lowercase, in front of the name:

- Job Variable: `jv`, for example `jvInputPath`
- User Variable: `uv`, for example `uvRecordCount`
- List Variable: `lv`, for example `lvCustomerRecords`

A server can soon hold fifty or more variables, and a consistent prefix makes the right one much faster to find.

---

### Tips

- Turn fixed paths, user names and connection details into variables rather than typing them into activities. Moving a process from test to production then means changing one variable instead of every activity that used the old value
- Use a User Variable when the value is shared across Jobs, and a Job Variable when it belongs to one Job only
- Do not pass a password through _Set variable_: the value is written to the Task output
- Nest variable functions to change a value in place rather than adding extra Set variable activities, for example `{STRING(Trim|{USERVAR(lvData|GetCell|1|Name|false)})}`
- Use the _Variables_ button at the bottom of the Edit Task window to insert variable references. The preview shows what an expression resolves to before you use it
