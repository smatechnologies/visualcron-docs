---
sidebar_label: 'VisualCron Web API'
hide_title: 'true'
---

## VisualCron Web API

The VisualCron Web API is an alternative way to interact with VisualCron and extract information.
 
**Server > Settings > Web API** tab

![](../../static/img/Using%20VisualCron/Interacting%20with%20VisualCron/Web%20API.png)

**Allow Web API**

When checked VisualCron open ports for Web API.
 
**Unencrypted/Encrypted ports**

The Web API uses two ports for communication. The encrypted one uses a certificate created by VisualCron to enable a secure communication channel.
 
**Permissions**

The Web API uses the same permission system as in VisualCron which means that you need to add a user in [Manage user permissions](../client-user-interface/server/main-user-permissions) window first.
 
**Available methods**

Once the WebAPI is allowed you can see available methods here:
[http://localhost:8001/VisualCron/text/Docs](http://localhost:8001/VisualCron/text/Docs)
 
Calling the Web API
There are two ways of requesting information:
 
1. REST
The VisualCron [REST](https://en.wikipedia.org/wiki/REST) service communicate through the HTTP protocol. By making simple HTTP calls against the VisualCron service you can easily extract information and interact with VisualCron. The REST service is able to return 3 different result outputs:
Text - plain text output
XML - XML output
JSON - JSON output
 
The output method is controlled through the url:
[https://localhost:8002/visualcron/text/job/list?token=[token]](https://localhost:8002/visualcron/text/job/list?token=[token])
[https://localhost:8002/visualcron/xml/job/list?token=[token](https://localhost:8002/visualcron/xml/job/list?token=[token])]
[https://localhost:8002/visualcron/json/job/list?token=[token]](https://localhost:8002/visualcron/json/job/list?token=[token])
 
**Output result**

By default, if you use text as output headers are added (property names). If you want to exclude these you can set &includeheaders=false in the query. By default available properties will be listed but you can also set which properties (columns) to include like this:
[http://localhost:8001/visualcron/text/job/List?id=1&token=[token]&columns=id,name,runmissed,tasks](http://localhost:8001/visualcron/text/job/List?id=1&token=[token]&columns=id,name,runmissed,tasks)
 
It is possible to control the field separator, text qualifier and line break like this:
[http://localhost:8001/visualcron/text/job/List?id=1&token=[token]=59&textQualifier=34&lineBreak=10](http://localhost:8001/visualcron/text/job/List?id=1&token=[token]=59&textQualifier=34&lineBreak=10)
 
**Tokens and authentication**

It is possible to authenticate once and use a token that will work for 24 hours (and will be renewed for each call). The token is then used in each call. You can also authenticate each time you call a method. Using token and a method requires at least 2 calls instead of supplying user name and password in each call. However, using tokens is faster in the long run and generally more secure.
 
**Get token**

To get a token you authenticate against the the logon method:
[http://localhost:8001/visualcron/text/logon?username=admin&password=qwerty123](http://localhost:8001/visualcron/text/logon?username=admin&password=qwerty123)
 
This call returns a token that you can used in following calls like:
[http://localhost:8001/visualcron/text/job/List?token=[token]](http://localhost:8001/visualcron/text/job/List?token=[token])
 
Authenticate in call
By adding user name and password parameters you can work directly with the method without using tokens:
[http://localhost:8001/visualcron/text/job/List?username=admin&password=qwerty123](http://localhost:8001/visualcron/text/job/List?username=admin&password=qwerty123)
 
**2. Web service/SOAP**

It is also possible to communicate with VisualCron through the web service API. The wsdl URL can be found in the Web API tab in Server settings.
 
There is the following example in the API folder (sample TestClient project):

``` 
                 var binding = new BasicHttpBinding()
                 {
                         MaxBufferPoolSize = int.MaxValue,
                         MaxReceivedMessageSize = int.MaxValue,
                         ReaderQuotas =
                                 new XmlDictionaryReaderQuotas()
                                 {
                                         MaxArrayLength = int.MaxValue,
                                         MaxStringContentLength = int.MaxValue,
                                         MaxNameTableCharCount = int.MaxValue
                                 },
                         Security = new BasicHttpSecurity()
                         {
                                 Mode = BasicHttpSecurityMode.TransportCredentialOnly,
                                 Transport = new HttpTransportSecurity()
                                 {
                                         ClientCredentialType = HttpClientCredentialType.Basic
                                 }
                         }
                 };
 
                 var client = new WebServiceClient(binding, new EndpointAddress("http://localhost:8001/VisualCron"));
                 //or just:
                 //
                 //var client = new WebServiceClient();
                 //
                 //but better setup binding
 
                 if (client.ChannelFactory.Credentials != null)
                 {
                         //set Credentials
                         client.ChannelFactory.Credentials.UserName.UserName = txtUserName.Text;
                         client.ChannelFactory.Credentials.UserName.Password = txtPassWord.Text;
                 }
                 try
                 {
                         //just call methods
                         var jobs = client.Job_List();
 
                         foreach (var job in jobs)
                         {
                                 Console.WriteLine(job.Name);
                         }
                 }
                 catch
                 {
 
                 }

``` 
 
### Troubleshooting

*Can't connect securely to this page (outdated TLS security settings)*

Install .NET 4.7.1 and reboot.