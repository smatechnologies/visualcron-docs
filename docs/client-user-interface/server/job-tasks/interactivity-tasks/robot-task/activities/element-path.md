---
sidebar_label: 'Element Path'
hide_title: 'true'
---

## Robot Task Activities - Element Path

Many [Web Macro](web-macro) activities include a tab on their settings form for specifying the path to the target HTML element. There are three ways to specify that path:

- **Relative**
- **By position**
- **By search**

---

### Relative mode

**Element path** specifies the path to the element to be detected. Both a CSS selector and an XPath expression are supported. Specifying only a CSS selector is enough, but the full format of the path string is:

```
pathCss[%]pathHtml[%]pathXPath
```

| Part | Description |
|---|---|
| pathCss | A CSS selector. |
| pathHtml | An additional internal format for representing the path to the element. |
| pathXPath | An XPath expression. |
| `[%]` | The separator between parts. |

#### How the path is resolved

The full path format is used in recording mode for increased dependability. When configuring activities manually, the path does not need to be specified in its entirety.

At runtime the path is split on the `[%]` separator and the element is searched for in this order:

1. By the third part (**pathXPath**), if one exists after the split.
2. If not found by XPath, by the second part (**pathHtml**).
3. If still not found, by the CSS selector (**pathCss**).

If no `[%]` separator is present, the whole value is interpreted as a CSS selector.

To find an element using XPath only, provide the expression after two separators:

```
[%][%]/HTML/BODY/APP-ROOT[1]/DIV[2]/APP-RPA1[1]/DIV[1]/DIV[2]/FORM[1]/INPUT[1]
```

#### CSS selector examples

Given this HTML:

```html
<html>
  <head>
    <title>Title</title>
  </head>
  <body>
    <span id="rX8Qvb-cnt" class="toolbarbutton-content">Hello, World!</span>
  </body>
</html>
```

Any of these selectors will find the span element:

| Selector type | Example |
|---|---|
| Class selector | `.toolbarbutton-content` |
| ID selector | `#rX8Qvb-cnt` |
| Type selector | `span` |
| Attribute selector | `span[id="rX8Qvb-cnt"]` |
| Child selector | `html > body > span` |

#### XPath examples

```
[%][%]//*[@id="rX8Qvb-cnt"]
[%][%]/HTML/BODY/SPAN[1]
[%][%]//span[contains(., "Hello")]
```

#### Frame path

**Frame path** specifies the path to the HTML `frame` tag containing the element, as a valid CSS selector string.

In most cases this field is optional. It only needs to be filled in when the web page uses HTML frames, that is when the page contains a `<frame>` tag. For example, a frame path of `FRAME:nth-child(2)` with an element path of `#ddlCustomer`.

Further reading:

- [HTML frames tutorial](https://www.tutorialspoint.com/html/html_frames.htm)
- [W3C frames specification](https://www.w3.org/TR/html401/present/frames.html)

---

### By position

A mode for locating an element by its coordinates on the page.

> This mode is currently out of date and upgrades are planned. Prefer **Relative** or **By search** for new work.

---

### By search

This mode searches for elements using a CSS selector, which is passed to the JavaScript `querySelectorAll` function. It is useful when an element's path changes between runs.

| Setting | Description |
|---|---|
| Selector | The CSS selector passed to `querySelectorAll`, defining the candidate list of elements. |
| Attribute | The element attribute whose value is matched. Element properties `innerHTML`, `outerHTML`, `innerText`, and `outerText` can also be used. |
| Regex value | A regular expression the attribute value is tested against, filtering the candidate list. |
| Position | The ordinal position within the filtered results that identifies the element to return. |

The search runs in three steps:

1. Build a list of HTML elements matching the CSS selector.
2. Filter that list by testing the specified attribute or property value against the regular expression.
3. Select the element at the ordinal position given in the settings.

For example, a Selector of `span`, an Attribute of `innerText`, a Regex value of `Hello`, and a Position of `First` returns the first span on the page whose visible text contains `Hello`.

Further reading:

- [JavaScript querySelector and querySelectorAll](https://www.javascripttutorial.net/javascript-dom/javascript-queryselector)
- [Regular expression test method](https://www.w3schools.com/jsref/jsref_regexp_test.asp)
- [CSS type selectors](https://www.w3.org/TR/CSS21/selector.html#type-selectors)
- [XPath expressions and CSS selectors](https://www.qafox.com/xpath-expressions-css-selectors)

---

### Additional notes

When setting activity settings manually, the fastest way to determine the correct CSS selector or XPath expression is to use the web browser's Inspector mode.

Some selectors include quotes. It is important to make sure that in paths they are specified as double quotes and not single quotes.

For a practical walkthrough of using the Inspector to build a selector for a form field, see [Web Input - Element Path](../web-input-element-path).

---

### Tips

- Prefer selectors built on `id` and `name` attributes. They are the most stable and least likely to change when a page is updated.
- Avoid purely positional XPath such as `/HTML/BODY/DIV[3]/INPUT[1]`. It breaks as soon as the page structure changes.
- Test a selector in the browser console with `document.querySelector('your-selector')` before using it in VisualCron, to confirm it returns the element you expect.
- Use **By search** when several similar elements exist and the one you want is distinguished by its text or an attribute value rather than by its position in the document.
