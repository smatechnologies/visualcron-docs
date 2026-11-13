---
sidebar_label: 'Event Trigger - RSS'
hide_title: 'true'
---

## Event Trigger - RSS

The RSS Trigger reads an RSS or Atom feed at every *Polling interval* (default 300 seconds) and starts the Job once for each new feed item that meets its conditions. The first read is made when the Trigger starts.

VisualCron remembers the IDs of the last 100 items that fired the Trigger. When the Trigger starts, for example when the VisualCron Server starts or the Job is saved, it checks every item in the feed again and fires for each matching item that is not among those 100. In a feed with more than 100 matching items, older items can therefore fire again after a restart.

The settings are on the ***RSS*** tab, ***Main settings*** sub tab.

![The Main settings sub tab of the RSS tab in the Add/Edit event window: Feed address with the Fetch button and Feed version: Unknown (click Fetch to update), Trigger for each item - no conditions, Reset checked RSS items, Ignore parse and load errors and Timeout in seconds set to 60](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20RSS.png)

**Feed address**

The URL of the RSS or Atom feed. Variables in the address are replaced once, when the Trigger starts.

Click *Fetch* to read the feed and show its version below the box: *RSS 0.90*, *RSS 0.91*, *RSS 0.92*, *RSS 1.0*, *RSS 2.0* or *ATOM*. *Fetch* reads the feed from the computer that runs the Client and uses the address as typed, without replacing Variables. After *Fetch*, an error icon marks each condition box for a part that this feed version may not have.

:::warning

The Trigger currently cannot read *RSS 0.90* and *RSS 1.0* (RDF) feeds, even though *Fetch* shows their version. Each read fails, and the Trigger is deactivated unless *Ignore parse and load errors* is checked. If the site offers the feed as RSS 2.0 or Atom, use that address.

:::

**Trigger for each item - no conditions**

When checked, the Trigger fires for every new feed item, and the *Feed conditions* on the ***Conditions*** sub tab are unavailable. When cleared, set at least one condition: with every condition at *Don't check*, the Trigger never fires.

**Reset checked RSS items**

Check this box and click *OK* to clear the list of items that already fired the Trigger. Saving restarts the Trigger, so every matching item in the feed fires again at its first read. The box is not saved checked: it clears the list once, when you save the Trigger.

**Ignore parse and load errors**

When cleared (the default), the Trigger is deactivated when the feed or a linked page (see *Link content*) cannot be read or parsed, and the error is written to the log. When checked, the error is written to the log and the Trigger tries again at the next *Polling interval*.

**Timeout in seconds**

How many seconds to wait for the feed before the read fails (1 to 10000; default 60).

:::warning

When several new items are found in one read, the Trigger fires once for each. A run that is skipped because the Job is still running loses its item. See [Event Triggers](event-triggers#triggers-that-fire-once-per-item) for how to queue the runs instead. To read the item that started each run, use the *Last trigger* form of the result Variables (see [Result Variables](#result-variables)).

:::

The conditions are on the ***RSS*** tab, ***Conditions*** sub tab.

![The Conditions sub tab of the RSS tab: Feed conditions for Title, Description, Link, Author, Comment, Content and Link content, each set to Don't check with an empty text box](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20RSS%20Condition.png)

Under *Feed conditions*, each part of the item has a list to choose the check and a text box for the value. The Trigger fires for an item when **any** checked condition matches; the conditions are not combined with AND. The checks are:

* *Equal (=)* / *Not equal (!=)*: the value is (or is not) exactly the text
* *Contains (=%)* / *Not contains (!=%)*: the text appears (or does not appear) anywhere in the value
* *Regex - match*: the regular expression matches the value
* *Regex - no match*: currently works the same as *Regex - match*. To fire when a pattern is absent, use *Regex - match* with a negative lookahead, for example `(?s)^(?!.*draft)`
* *Don't check*: the condition is not used (the default)

All checks are case-sensitive. The text is used as typed: Variables are not replaced in it.

**Title**

The title of the item (`title`).

**Description**

The description of the item: `description` in an RSS feed, `summary` in an Atom feed.

**Link**

The link of the item: the text of `link` in an RSS feed, the `href` of `link` in an Atom feed.

**Author**

The author of the item. For an Atom entry, the author's name and email address are joined into one text.

**Comment**

The `comments` element of an RSS item. Atom entries do not have it, so for an Atom entry the value is empty: *Not equal* and *Not contains* with any text match every Atom entry, and *Equal* and *Contains* match none.

**Content**

The `content` element of an Atom entry. RSS feeds do not fill it; RSS `content:encoded` is not read.

**Link content**

The page at the item's link, read as UTF-8 each time this condition is checked. The page is read without the Trigger's Credential and timeout. If it cannot be read, the Trigger is deactivated unless *Ignore parse and load errors* is checked. When it is checked, that item is not checked again until the Trigger restarts, for example when the Job is saved.

The security settings are on the ***RSS*** tab, ***Security*** sub tab.

![The Security sub tab of the RSS tab: SSL 3, TLS 1.0, TLS 1.1 and TLS 1.2 checked under Supported security protocols; under Credentials, Auth type NTLM and No Credential](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20RSS%20Security.png)

**Supported security protocols**

Check the SSL and TLS versions that the Trigger may use to connect to the *Feed address*. All four are checked by default.

* _SSL 3_
* _TLS 1.0_
* _TLS 1.1_
* _TLS 1.2_

**Credentials**

**Auth type**

The HTTP authentication used when a Credential is selected: *Basic*, *NTLM* (default), *Digest*, *Negotiate*, *Kerberos* or *OAuth*.

**Credential**

The [Credential](global-credentials) whose user name and password are sent to the feed. Select it in the list, or click the icon next to it to open *Manage credentials*. With no Credential, no authentication is sent.

### Result Variables

When the Trigger fires, it sets these result Variables for the item that fired it:

* `RSS.Result.Id`: the item ID (`guid` or `id`; when the item has none, a value calculated from the item)
* `RSS.Result.Title`, `RSS.Result.Description`, `RSS.Result.Link`, `RSS.Result.Author`, `RSS.Result.Comments`, `RSS.Result.Content`: the item's parts, as for the conditions
* `RSS.Result.PubDate`: the publication date (`pubDate`, or `updated` for Atom). For another format, use `RSS.Result.PubDate|<date format>`, for example `{TRIGGER(Active|LastTrigger|RSS.Result.PubDate|yyyy-MM-dd)}`
* `RSS.Result.Item`: the whole item as XML

`RSS.Result.LinkContent` and `RSS.Result.Category` are offered in the *Variables* window but are currently always empty.

For example, `{TRIGGER(Active|LastTrigger|RSS.Result.Title)}` returns the title of the item that fired the Trigger that started the run. *Last run*, `{TRIGGER(Active|LastTrigger|LastRun)}`, returns the time the Trigger fired. See [Variables](global-variables) for how *Last trigger* and the other keys work.
