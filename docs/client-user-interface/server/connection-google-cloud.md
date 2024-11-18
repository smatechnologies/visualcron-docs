---
sidebar_label: 'Connection - Google Cloud'
hide_title: 'true'
---

## Connection - Google Cloud

The Google Cloud Connection is used in the following Tasks:

* BigQuery - Run query
* BigQuery - Fill table
* Google Storage Tasks

![](../../../static/img/bigqueryconnection.png)

**Project ID**

Can be bigquery_public_data (when working on public data available in Google Bigquery) or user’s project. Can be found in BigQuery Console (see screenshot).

![](../../../static/img/googlebigqueryprojectid.png)


**JSON Key**
JSON auth file for service account. Should be in JSON format and can be downloaded as JSON file right when adding it to the account. There’s no way of getting it from the console once again, you will need to disable the previous key and add a new one. See information below how to retrieve the JSON file.
 
**How to create JSON file**
 
1. Go to Google Console IAM & Admin for specific project

![](../../../static/img/googleiam1.png)

2. Press + Create Service Account and fill account details

![](../../../static/img/googleiam2.png)

3. Select the proper role for this service account (under Cloud Storage group)

![](../../../static/img/googleiam3.png)

4. Open created service account and add key (I added new key, key type should be JSON)

![](../../../static/img/googleiam4.png)

5. As soon as key will be created, it will be downloaded automatically. This JSON file should be used to setup a *Google Cloud Storage Connection*.