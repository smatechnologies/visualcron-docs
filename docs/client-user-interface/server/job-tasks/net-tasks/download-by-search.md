---
sidebar_label: 'Download By Search'
hide_title: 'true'
---

## Download By Search

The Download action of the [Task Net - Web Macro](web-macro) is created automatically when you download a file while recording. This page shows how to choose between a direct download and a download started by clicking an element. For each field, see [Download Step](download-step) and [Element Path](element-path).

### Direct download or click

- Direct download: on the ***Download*** tab, select _Force download_ and enter the file's URL in _Original file/path_; use this when the URL points straight to the file
- Download by click: clear _Force download_, then use the ***Element*** tab, which becomes available, to set the element that is clicked to start the download, such as a link or a button

  The ***Element*** tab offers _Relative_, _By position_ and _By search_.

### Choose a method

| Method | Use when |
|---|---|
| _Force download_ with a fixed URL | The file URL never changes. |
| _Force download_ with a Variable in the URL | The URL changes in a known pattern, and a Variable can hold the part that changes. |
| Click, _Relative_ | A fixed CSS selector or XPath finds the element. |
| Click, _By search_ | The element must be picked from several matches, such as the first link whose address matches a pattern. |

A URL with a Variable looks like this, with your own host and Variable:

```text
https://<host>/downloads/product-{USERVAR(Version)}.exe
```

The Variable must hold the right value before each run. If the next value cannot be predicted, for example the next version number, use a click method instead.

### Example: download the newest file in a list

A page lists its downloads in a table, newest first, below a header row.

**By relative path.** On the ***Element*** tab, select _Relative_ and enter this CSS selector in _Element path_:

```css
table > tbody > tr:nth-child(2) a
```

The selector finds the table body, takes its second row (the first row is the header), and clicks the link in that row.

**By search.** To find the same link by search, complete the following steps on the ***Element*** tab:

1. Select _By search_.
2. In _Selector_, enter `a` to find every link on the page. The selector is passed to the JavaScript function `document.querySelectorAll()`.
3. In _Attribute_, select `href` to test each link's address.
4. In _Regex value_, enter a regular expression that matches the download links, for example `^https://<host>/downloads/`.
5. In _Position_, select "First".

The action clicks the first matching link, which is the newest file. In _Position_, "First" is 0 and "Last" is -1. "Specific" takes an index that you enter, such as -2 for the second last.

The ***Element*** tab settings are also used by other actions, such as the Click action.

### More information

- [document.querySelector()](https://www.w3schools.com/jsref/met_document_queryselector.asp)
- [document.querySelectorAll()](https://www.w3schools.com/jsref/met_document_queryselectorall.asp)
- [W3C Selectors Level 3](https://www.w3.org/TR/selectors-3/#selectors)
- [XPath syntax](https://www.w3schools.com/xml/xpath_syntax.asp)
- [JavaScript regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)
- [Chrome DevTools: CSS](https://developer.chrome.com/docs/devtools/css/)
