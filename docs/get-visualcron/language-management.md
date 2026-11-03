---
sidebar_label: 'Language Management'
hide_title: 'true'
---

## Language Management

The Client user interface can be shown in a language other than English, and the Server has its own language setting for the text it writes. The VisualCron website, the documentation, and the texts in the demo Jobs and Tasks created at installation are in English only.

### Choose the Client language

When the Client starts for a Windows user who has not chosen a language yet, it asks for one. If you close the window without choosing, English is used. The choice is saved in that user's Client settings, so each Windows user on a machine can use a different language.

To change the Client language later, complete the following steps:

1. Go to _File_ -> _Settings_ -> _Client settings_.
2. On the ***Language*** tab, select a language in *Choose client language*.

   A message tells you that the Client must be restarted.

3. Click *Apply settings*.
4. Restart the Client.

   The Client shows the selected language.

Captions that have no translation in the selected language are shown in English. See [Settings - Client Settings](../client-user-interface/file/client-settings).

### Server language

*Server language*, on the ***Main settings*** tab of _Server_ -> _Main settings_ -> _Settings_, sets the language of the text that the Server writes, for example some log entries. Server text that has no translation stays in English. See [Main - Settings](../client-user-interface/server/main-settings).

### Translation files

The language files are in the `lang` subfolder of the installation folder, one file for each language.

- To get the latest translation for the current Client language, go to _File_ -> _Translation_ -> _Update translation files_. See [Translation - Update Translation Files](../client-user-interface/file/update-translation-page)
- To help translate VisualCron, go to _File_ -> _Translation_ -> _Open translation page_. See [Translation - Open Translation Page](../client-user-interface/file/open-translation-page)

*Update translation files* saves the files in the `lang` subfolder of the Client installation folder, and it updates the Client only. The Server's translation files do not change. When the Client is installed under Program Files, start the Client with *Run as administrator* before you use this command.
