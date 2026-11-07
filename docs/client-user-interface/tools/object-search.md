---
sidebar_label: 'Objects - Object Search'
hide_title: 'true'
---

## Objects - Object Search

The ***Object text search/replace*** tab of the ***Object finder*** window searches the properties of VisualCron objects for a text and can replace it.

To open it, click ***Tools*** -> ***Objects*** -> ***Object search***.

![Object finder window on the Object text search/replace tab with the object type list open and search results](../../../static/img/Client%20User%20Interface/Main%20Menu/Tools/Objects/Object%20text%20search-replace.png)

### Search

- _Object(s) type_: the object types to search. The list has Certificate, Condition, Connection, Credential, Job, Notification, PGPKeyRing, SSHKey, Task, TimeException and Variable
- _Search text_: the text to search for
- _Use exact search_: when checked, a property matches only when its whole value is the search text. When unchecked, a value that contains the text matches
- _Case sensitive_: when checked, upper and lower case must match
- _Search encrypted values_: when checked, encrypted values, such as passwords, are also searched. This takes longer
- _Text is the name of the user variable_: when checked, the search text is treated as the name of a user Variable

Click ***Search*** to start. ***Cancel*** stops a running search.

### Search result

The grid shows _Name/Description_, the object class, _Property Name_ and _Property Value_ for each match. Each row has a check box that marks it for replacement. Double-click a row to open the object. The _Filter:_ field narrows the list.

### Replace

:::warning

Replace changes the objects on the Server as soon as you confirm, and cannot be undone here; use [Versions](audit-log-versions) to revert an object. Every row is marked by default, including rows hidden by the _Filter:_ field. Replace searches the Server again with the current search text and options; when most rows are marked, it changes every match except the unmarked rows, so a search text or option changed after the search changes values that are not in the list. If you click ***Replace*** before running a search, or when the list is empty, every value on the Server that matches the search text is replaced; the confirmation then says "all objects". With _Partial replacement_ unchecked, each marked value is replaced as a whole, so an empty replace text clears the whole value.

:::

The _Replace text (in all marked entries in the list)_ group replaces values in the marked rows.

- _Partial replacement_: when checked, only the matched text in each value is replaced, at its first occurrence. When unchecked (the default), the whole value is replaced by the new text

1. Run a search.
2. Clear the check box of each row that must not change.
3. Enter the new text.
4. Click ***Replace***.
5. Click ***Ok*** in the confirmation.

For example, a search for `test` with the new text `test example` changes `This is a test` to `test example` when _Partial replacement_ is unchecked. With _Partial replacement_ checked, `This is a test` becomes `This is a test example`.
