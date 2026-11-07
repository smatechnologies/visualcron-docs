---
sidebar_label: 'Web Input - Element Path'
hide_title: 'true'
---

## Web Input - Element Path

This page shows how to target a web form field by its element path, so that a Robot Task keeps finding the field when the page layout changes.

When you automate web forms, a recorded click on an input field captures the element by its position on the page at the time of recording. If the application later moves the fields, which is common in dynamic or single-page web applications, recorded positional clicks land in the wrong place and the automation fails.

A more reliable approach is to target input fields by their **element path** (a CSS selector or XPath), which identifies the element by its attributes rather than its screen position. See [Element Path](activities/element-path) for the full syntax.

### Finding the element path with the browser inspector

1. Open the web page in your browser.
2. Right-click the input field you want to target and select _Inspect_, or press `F12` and click the element picker.
3. In the inspector, look at the highlighted HTML element for stable attributes such as:
   - `id`: a unique identifier, the most reliable
   - `name`: common on form input fields
   - `class`: useful if the class is specific and not shared by many elements
4. Build the CSS selector from those attributes.

**Example HTML element:**

```html
<input name="labelAddress" ng-reflect-name="labelAddress" type="text">
```

**Resulting CSS selector:**

```css
input[name="labelAddress"]
```

This selector finds the field wherever it appears on the page.

Attributes that start with `ng-reflect-` are added only by development builds of Angular applications, so they may be missing in production. Build the selector on `id` or `name` instead.

### Applying the element path in a Populate Field activity

In the [Populate Field](activities/web-macro) activity settings, enter the CSS selector in _Element path_ on the ***Source*** tab, then set the value to insert on the ***Populate*** tab.

Using an attribute-based selector instead of a recorded positional path means the activity keeps working when the page layout changes.

### CSS selector quick reference

- ID: `#myField` matches `<input id="myField">`
- Name attribute: `input[name="address"]` matches `<input name="address">`
- Class: `.form-input` matches any element with the class `form-input`
- Type and attribute: `input[type="email"]` matches any e-mail input
- Child path: `form > div > input` matches an input directly inside a `div` directly inside a `form`

### XPath alternative

If a CSS selector is not specific enough, use XPath instead. To use XPath in _Element path_, put two separators before it:

```text
[%][%]//*[@id="myField"]
[%][%]//input[@name="address"]
[%][%]//span[contains(., "Submit")]
```

The `[%]` separator tells VisualCron to read the path as XPath rather than as a CSS selector.

### Tips

- **Prefer `id` and `name` attributes.** They are the most stable and the least likely to change when a page is updated
- **Avoid positional XPath** such as `/HTML/BODY/DIV[3]/INPUT[1]`. It breaks easily when the page structure changes
- **Test the selector in the browser console** with `document.querySelector('your-selector')` before you use it in VisualCron, to confirm it returns the right element
- If the element is inside an HTML `<frame>` or `<iframe>`, also fill in _Frame path_ with the CSS selector for that frame
