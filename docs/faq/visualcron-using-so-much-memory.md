---
sidebar_label: 'Why Is VisualCron Using So Much Memory?'
hide_title: 'true'
---

## Why Is VisualCron Using So Much Memory?

VisualCron is written in a .NET-language. Programs, which run under the .NET Framework have different memory handling. The memory handling is called Garbage Collection and it's handled automatically by the .NET Framework. When starting a .NET-application, the .NET-Framework allocates some memory, often more than needed. Memory is automatically freed when no longer needed by the application. Freeing memory takes system resources and is nothing that you want to do all the time.
 
Often only memory is freed when it's really needed. This may result in that the .NET application may appear to use more resources than it really does. The bottom line is that you don't have to worry about this as long as an application does not increase in memory in regular intervals - then it may be a problem (memory leak).