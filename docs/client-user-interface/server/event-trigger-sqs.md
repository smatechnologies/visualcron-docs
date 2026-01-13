---
sidebar_label: 'Event Trigger - SQS'
hide_title: 'true'
---

## Event Trigger - SQS

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS eliminates the complexity and overhead associated with managing and operating message oriented middleware, and empowers developers to focus on differentiating work. Using SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available. Get started with SQS in minutes using the AWS console, Command Line Interface or SDK of your choice, and three simple commands.
 
The Amazon SQS Trigger in VisualCron is using the [Amazon Connection](../server/connection-amazon).
 
**Amazon SQS Trigger settings**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20SQS.png)

**Queue**

Filter on one or more queue names. If not set it will watch all.
 
**SenderId**

Filter on SenderId. If not set it will watch for all.
 
**Message text**

Filter on message text. If not set it will watch for all.
 
**Min created DateTime**

Filter on min created time. If not set it will watch for all.
 
**Max created DateTime**

Filter on max created time. If not set it will watch for all.
 
**Attribute name**

Filter on attribute name. If not set it will watch for all.
 
**On error reconnect attempts**

How many times it will try to reconnect on error.
 
**On error reconnect interval (_seconds_)**

How often it will try to reconnect.