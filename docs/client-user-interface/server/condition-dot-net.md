---
sidebar_label: 'Condition - .NET'
hide_title: 'true'
---

## Condition - .NET

The _.NET_ condition runs a method you write in C# or VB.NET and uses the boolean it returns as the result. Use it when no other condition type can make the check you need.

This page describes the **_.NET_** tab of the _Add/Edit condition_ window. For the **_Main settings_** tab of the window (_Condition type_, _Description_, _Active_), see [Conditions - Conditions](conditions-conditions).

_Server_ -> _Global objects_ -> _Conditions_ -> _Add_ -> **_Conditions_** tab -> _Add_ -> _Condition type_ ".NET" -> **_.NET_** tab

![Add/Edit condition window with the .NET tab open, showing Language set to "C#", the Edit references.. button, and the Code editor with the sample class Test and its method MyCustomCondition](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Conditions/Condition%20-%20.NET.png)

### Requirements for the method

- Inside a class
- Declared public and static: `public static` in C#, `Public Shared` in VB.NET
- Returns a boolean: `bool` in C#, `Boolean` in VB.NET

The code can contain other classes and methods. The condition calls only the method you select. The result is:

- "true": the condition matches
- "false": the condition does not match
- Any other return type, a compile error, a method that cannot be found, or an exception thrown by the code: Match Error

:::warning

A Match Error from a _.NET_ condition is written to the log only when the Condition Set has _Extended debug logging_ checked (see [Conditions - Main Settings](global-main-settings)). Without it, a condition that fails to compile or throws an exception leaves no log entry, and the Condition Set takes its _On Match Error_ action. Test the method with _Run_, and check _Extended debug logging_ while you set up the condition.

:::

### Language

Select "C#" or "VB.NET". The code is compiled in the selected language, and the editor's syntax highlighting follows it. The default is "C#".

### Edit references..

Opens a window where you add or remove the assemblies the code needs. "mscorlib.dll" and "System.dll" are always included. When the condition is evaluated, the Server compiles the code with the same list, so an assembly referenced by path must exist at that path on the Server computer.

### Code

The code editor. A new condition starts with a sample C# class `Test` whose method `MyCustomCondition(int valueX, int valueY)` returns "true" when the two values are equal. You can use Variables in the code, see [Global - Variables](global-variables). They are replaced each time the condition is evaluated, before the code is compiled.

### Method and parameters

The combo box lists the public static methods in the code, with their parameter types, for example "MyCustomCondition(System.Int32,System.Int32)". Select the method the condition calls. The window does not let you save the condition without a method.

- _Compile_: compiles the code and shows the first error, or a message that the code compiled without errors
- _Refresh methods_: compiles the code and fills the list again, and selects the last method found if no method is selected
- _Run_: compiles the code, calls the selected method with the values in _Parameters (double click to edit)_, and shows the value it returned, or a message if it did not return a boolean

The condition stores the method together with its parameter types. After you rename the method or change its parameters, click _Refresh methods_ and select the method again. Otherwise the Server cannot find the method, and the condition returns a Match Error.

:::note

_Compile_, _Refresh methods_ and _Run_ work on the computer where the Client runs, under your Windows account. _Compile_ and _Refresh methods_ do not replace Variables in the code. _Run_ replaces them, but without the values of a Job or Task. When the condition is evaluated, the code runs inside the VisualCron service on the Server computer, under the account the service runs under. File paths, permissions and available assemblies can differ between a test and a real run.

:::

### Parameters (double click to edit)

Lists the parameters of the selected method, with _Parameter name_, _Data type_ and _Value preview_. Double-click a row to enter a value. The editor that opens depends on the data type, for example a list of names for an enumeration, or a date and time editor. When the condition is evaluated, the Server replaces any Variables in the values and converts each value to its parameter's type. A value that cannot be converted gives a Match Error.
