---
sidebar_label: 'Element Path'
hide_title: 'true'
---

## Robot Task Activities - Element Path

The element path settings tell a [Web Macro](web-macro) activity which HTML element on the page to act on. Many Web Macro activities have a ***Source*** tab for this, with three ways to specify the element:

- _Relative_
- _By position_
- _By search_

---

### Relative

_Element path_ specifies the path to the element. Both a CSS selector and an XPath expression are supported. A CSS selector on its own is enough, but the full format of the path string is:

```text
pathCss[%]pathHtml[%]pathXPath
```

- `pathCss`: a CSS selector
- `pathHtml`: an additional internal format for the path to the element
- `pathXPath`: an XPath expression
- `[%]`: the separator between the parts

#### How the path is resolved

A recorded action may store the path in the full format. When you configure an activity yourself, the path does not need all three parts.

At runtime the path is split on the `[%]` separator and the element is searched for in this order:

1. By the third part (`pathXPath`), if there is one.
2. If it is not found by XPath, by the second part (`pathHtml`).
3. If it is still not found, by the CSS selector (`pathCss`).

If there is no `[%]` separator, the whole value is treated as a CSS selector.

To find an element by XPath only, put the expression after two separators:

```text
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

Any of these selectors finds the span element:

- Class selector: `.toolbarbutton-content`
- ID selector: `#rX8Qvb-cnt`
- Type selector: `span`
- Attribute selector: `span[id="rX8Qvb-cnt"]`
- Child selector: `html > body > span`

#### XPath examples

```text
[%][%]//*[@id="rX8Qvb-cnt"]
[%][%]/HTML/BODY/SPAN[1]
[%][%]//span[contains(., "Hello")]
```

#### Frame path

_Frame path_ specifies the path to the HTML `frame` element that contains the element, as a CSS selector.

In most cases this field can be left empty. Fill it in only when the element is inside a frame, that is when the page contains a `<frame>` or `<iframe>` element. For example, a _Frame path_ of `FRAME:nth-child(2)` with an _Element path_ of `#ddlCustomer`.

Further reading:

- [HTML frames tutorial](https://www.tutorialspoint.com/html/html_frames.htm)
- [W3C frames specification](https://www.w3.org/TR/html401/present/frames.html)

---

### By position

Locates the element by its _X_ and _Y_ coordinates on the page. A position stops matching as soon as the page layout changes, so prefer _Relative_ or _By search_.

---

### By search

Searches for elements with a CSS selector, which is passed to the JavaScript `querySelectorAll` function. Use it when an element's path changes between runs.

- _Selector_: the CSS selector passed to `querySelectorAll`, which defines the list of candidate elements
- _Attribute_: the element attribute whose value is tested; the element properties `innerHTML`, `outerHTML`, `innerText` and `outerText` can also be used
- _Regex value_: the regular expression the attribute value is tested against, which filters the list of candidates
- _Position_: which of the filtered elements to use

The search runs in three steps:

1. Build a list of the HTML elements that match the CSS selector.
2. Filter the list by testing the attribute or property value against the regular expression.
3. Take the element at the position given in the settings.

For example, a _Selector_ of `span`, an _Attribute_ of `innerText`, a _Regex value_ of `Hello` and the first position returns the first span on the page whose visible text contains `Hello`.

Further reading:

- [JavaScript querySelector and querySelectorAll](https://www.javascripttutorial.net/javascript-dom/javascript-queryselector)
- [Regular expression test method](https://www.w3schools.com/jsref/jsref_regexp_test.asp)
- [CSS type selectors](https://www.w3.org/TR/CSS21/selector.html#type-selectors)
- [XPath expressions and CSS selectors](https://www.qafox.com/xpath-expressions-css-selectors)

---

### Additional notes

When you configure an activity yourself, the fastest way to find the right CSS selector or XPath expression is the web browser's inspector.

Some selectors include quotes. In paths, use double quotes, not single quotes.

For a walkthrough of using the inspector to build a selector for a form field, see [Web Input - Element Path](../web-input-element-path).

---

### Tips

- Prefer selectors built on `id` and `name` attributes. They are the most stable and the least likely to change when a page is updated
- Avoid purely positional XPath such as `/HTML/BODY/DIV[3]/INPUT[1]`. It breaks as soon as the page structure changes
- Test a selector in the browser console with `document.querySelector('your-selector')` before you use it in VisualCron, to confirm it returns the element you expect
- Use _By search_ when several similar elements exist and the one you want is set apart by its text or an attribute value rather than by its position in the document
- If the element may be missing, check _Allow to ignore the element_ on the ***Source*** tab, so that the sequence is not stopped when the element is not found. See [Error Handling](error-handling)
