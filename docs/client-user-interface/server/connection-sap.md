---
sidebar_label: 'Connection - SAP'
hide_title: 'true'
---

## Connection - SAP

The SAP Connection stores connect and logon properties for SAP R/3 instances.
 
The SAP Connection is used in the SAP Task:
* [SAP - R/3 Job execute](../../client-user-interface/server/job-tasks/sap-tasks/r3-job-execute)
 
**Manage Connections > Add > SAP > Common settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SAP/SAP.png)

**Protocol type**

Text

**Name**

The unique name for the Connection
 
**Group**

The group that the connection is a part of.

**Timeout**

The connection timeout in seconds. Connection will fail after this time period.
 
**Code page**

Code page being used.
 
**Manage Connections > Add > SAP > Connection settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SAP/Settings.png)

**Address**

The IP or DNS name to SAP server.

**Username**

User name for the SAP instance.
 
**Password**

Password for the SAP instance.

**System ID**

The SAP System Identifier (sapsid) is a unique identification of a SAP System Instance. Within a SAP Customer Landscape it is essential to have each SAP instance
 
**System number**

The SAP server system number. This is mandatory if no value is supplied for Optional RFC Connection Parameters.
 
**Client**

The Client is a 'Customer'. We can say that each customer maps to one client. Within one SAP instance, a number of Clients can be created. No need to install separate software's for each and every customer.It provides isolation ,one client cannot see the data of other client..
 
**External user name**

The name of the user in the external system who caused the method call. The entry is of a documentary nature and should verify who made the call.
 
**Language**

The language ISO identifier to be used by the adapter. Default English.
 
**Pool size**

Max number of connections.
 
### Troubleshooting

*"Password logon no longer possible", "No RFC authorization for function module BAPI_XMI_LOGON", "You have no authorization to log on to interface XBP"*

This is caused by incorrect user permissions in SAP. 1) Check with the SAP Administrator and make sure the user on the SAP side (from the Connection Profile being tested in the CCM) is not locked or having any issue related to authorizations/privileges. 2) Verify the authorizations of the user in the Connection Profile meet the minimums as documented in the Control-M for SAP Administrator Guide under the section "SAP Authorizations"