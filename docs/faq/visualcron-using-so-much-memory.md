---
sidebar_label: 'Why Is VisualCron Using So Much Memory?'
hide_title: 'true'
---

## Why Is VisualCron Using So Much Memory?

VisualCron is written in a .NET language. Programs that run under the .NET Framework handle memory through garbage collection, which the .NET Framework manages automatically. When a .NET application starts, the .NET Framework reserves some memory, often more than the application needs. Memory that the application no longer needs is freed automatically. Freeing memory uses system resources, so it does not happen all the time.

Memory is often freed only when it is needed elsewhere, so a .NET application can appear to use more memory than it really does. This is normal. It can be a problem only if the memory use keeps growing at regular intervals, which can point to a memory leak.