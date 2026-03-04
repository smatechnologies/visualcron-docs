---
sidebar_label: 'Web Input - Element Path'
hide_title: 'true'
---

## Web Input - Element Path

When automating web forms, recording a click on an input field captures the element by its position on the page at the time of recording. If the application later repositions those fields — which is common in dynamic or single-page web applications — recorded positional clicks will land in the wrong place and the automation will fail.

A more reliable approach is to target input fields by their **element path** (CSS selector or XPath), which identifies the element by its attributes rather than its screen position.

### Finding the Element Path with Browser Inspector

1. Open the web page in your browser
2. Right-click the input field you want to target and select **Inspect** (or press `F12` and click the element picker)
3. In the Inspector panel, look at the highlighted HTML element for stable attributes such as:
   - `id` — unique identifier (most reliable)
   - `name` — common on form input fields
   - `class` — useful if the class is specific and not shared by many elements
4. Build your CSS selector from those attributes

**Example — HTML element:**
```html
<input name="labelAddress" ng-reflect-name="labelAddress" type="text">
```

**Resulting CSS selector:**
```
input[ng-reflect-name="labelAddress"]
```

This selector will find the field regardless of where it appears on the page.

### Applying the Element Path in a Populate Field Action

In the **Populate Field** action settings, enter your CSS selector in the **Element path** field on the Source tab, then use the **Populate** tab to set the value to insert.

Using an attribute-based selector instead of a recorded positional path means the action will continue to work correctly even if the page layout changes.

### CSS Selector Quick Reference

| Selector type | Example | Matches |
|---|---|---|
| ID | `#myField` | `<input id="myField">` |
| Name attribute | `input[name="address"]` | `<input name="address">` |
| Class | `.form-input` | Any element with class `form-input` |
| Type + attribute | `input[type="email"]` | Any email input |
| Child path | `form > div > input` | Input directly nested inside form > div |

### XPath Alternative

If a CSS selector is not specific enough, XPath can be used instead. To use XPath in the Element path field, prefix it with two separators:

```
[%][%]//*[@id="myField"]
[%][%]//input[@name="address"]
[%][%]//span[contains(., "Submit")]
```

The `[%]` separator tells VisualCron to interpret the path as XPath rather than a CSS selector.

### Tips

- **Prefer `id` and `name` attributes** — they are the most stable and least likely to change when a page is updated
- **Avoid positional XPath** like `/HTML/BODY/DIV[3]/INPUT[1]` — these break easily when the page structure changes
- **Test your selector in the browser console** using `document.querySelector('your-selector')` before using it in VisualCron to confirm it returns the right element
- If an element is inside an HTML `<frame>` or `<iframe>`, also fill in the **Frame path** field with the CSS selector for that frame
