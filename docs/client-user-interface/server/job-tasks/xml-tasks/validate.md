---
sidebar_label: 'Task XML - Validate'
hide_title: 'true'
---

## Task XML - Validate

The XML - Validate Task validates that an XML file is well-formed, schema compliant or DTD compliant.
 
A XML document with correct syntax is called "Well Formed". An XML document validated against a DTD or a Schema is both "Well Formed" and "Valid".
 
**XML Validate > File filter** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/XML%20Tasks/Validate.png)

The XML Validate Task uses the standard VisualCron [File filter](../../../server/job-tasks-file-filter) to define the properties of the listed files.
 
**XML Validate > Destination** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/XML%20Tasks/Validate%20Destination.png)

**XML validate parameters**

**Validation type**

Select how the XML file should be validated. Options:

* **WellFormed** — Validates that the XML file is syntactically well-formed, with no schema or DTD checking.
* **Schema** — Validates the XML file against an external schema file (*.xsd). When selected, the **Schema(s)** tab becomes available to specify the schema file.
* **DTD** — Validates the XML file against a Document Type Definition. Expands default attributes and entities, but general entities are loaded and parsed only if they are used.
 
**Namespaces**

A list of namespace prefix/namespace URI items, to uniquely identify an element, to be used for validation.
 
**XML Validate > Schema(s)** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/XML%20Tasks/Validate%20Schema.png)

This tab is only visible when **Validation type** is set to **Schema**. Use the standard VisualCron [File filter](../../../server/job-tasks-file-filter) to specify the external schema file (*.xsd) to validate against.
