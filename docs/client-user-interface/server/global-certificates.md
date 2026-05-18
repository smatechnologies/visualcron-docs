---
sidebar_label: 'Global - Certificates'
hide_title: 'true'
---

## Global - Certificates

A certificate is a digitally signed statement from one entity (person, company, etc.) that states that the public key of another entity has a particular value. Trusting the certificate's signature implies that you trust that the association in the certificate between the specified public key and the other entity are authentic.
 
VisualCron can handle standard X509 certificates. These can be stored at the server location and be available for reuse in Tasks like the [Email Task](../server/job-tasks/messaging-tasks/email). The Manage certificates dialog is available in the main menu **Server > Global objects > Certificates**.
 
**Global > Certificates**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Certificates/Global%20-%20Certificates.png)

The Manage certificates window lets you view currently stored Certificates and their properties. The grid shows the following columns:

* **Common name** — the subject common name from the certificate
* **Self signed** — whether the certificate is self‑signed
* **Private key** — whether the certificate includes a private key
* **Can encrypt** — whether the certificate can be used for encryption
* **Can sign** — whether the certificate can be used for signing
* **Key valid** — whether the certificate's private key is valid
* **Issuer name** — the name of the certificate issuer
* **Email** — the email address from the subject information
* **Name** — the VisualCron friendly name used to identify the certificate inside VisualCron

The toolbar at the top of the window provides the following buttons (left to right): **Import certificate**, **Export certificate**, **Create certificate**, **Delete certificate**, **Audit log**, **Get from Windows** (imports certificates from the local Windows certificate store).

Right‑clicking a row in the certificate grid opens a context menu with the following commands:

* **Set name** — edit the VisualCron friendly name of the certificate
* **Copy Certificate Id** — copy the certificate's internal identifier to the clipboard
* **Change Certificate Id** — change the certificate's internal identifier
* **Audit log** — open the audit log entries related to this certificate
* **Versions** — view the version history of the certificate
* **Object relations** — view other VisualCron objects that reference this certificate
* **Export…** — open the export dialog for the selected certificate
 
### Import certificate

You can currently import certificates from files with the following format:
* PFX
* CER/DER/KEY
* PEM
* SPC/PVK
 
You import certificates by clicking the Import certificate icon. Remember to change the file filter to see your particular certificate file format.
 
### Export certificate

You can export in the following formats:
* PFX
* PEM
* CER/KEY
 
You export certificates by clicking the Export certificate icon. Change file filter to change file saving format.
 
### Create certificate

To start the Generate certificate wizard click on the Create certificate icon.
 
**Global > Certificates > Create**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Certificates/Manage%20Certificates.png)

Step 1 of the wizard. Enter the VisualCron **Name** that will be used to identify the certificate inside VisualCron, then select the type of certificate (currently only **Self-signed certificate** is selectable).
 
**Global > Certificates > Create 2**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Certificates/Certificate%20Creation%202.png)

**Hash algorithm**

A set of radio buttons that selects the signature/hash algorithm used by the certificate. The available options are:

* **md2 / RSA**
* **md5 / RSA**
* **sha1 / RSA**
* **sha256 / RSA**
* **sha1 / DSA**
* **sha256 / DSA**
 
**Public key strength**

A dropdown that controls the strength of the public key in bits. The available values are **256**, **512**, **768**, **1024**, **2048**, and **4096**.
 
**Global > Certificates > Create 3**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Certificates/Certificate%20Creation%203.png)

Enter the subject information for the certificate. All fields below are required except _Email_. Remember to set the **Email** property if you are going to use the Certificate in the [Email Task](../server/job-tasks/messaging-tasks/email):

* **Country**
* **State/Province**
* **Locality**
* **Organization**
* **Organization unit**
* **Common name**
* **Email** (optional)
 
**Global > Certificates > Create 4**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Certificates/Certificate%20Creation%204.png)

Enter the validity period for the certificate using two date pickers:

* **Valid From** — the date from which the certificate is valid. Can be left blank to use the current date
* **Valid To** — the date until which the certificate is valid. Defaults to one year from today
 
**Global > Certificates > Create 5**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Certificates/Certificate%20Creation%205.png)

Last step. Click on **Next** to generate the Certificate. The wizard notes that the generation process may take some time, depending on the key length selected on step 2.
 
**Delete certificate**

Select a certificate row and click on the Delete certificate icon.
 
### Certificate file formats supported by VisualCron

**PFX (PKCS#12)**: Binary file format, which allows storing of one or more certificates and associated private keys in one file in encrypted form. The keys are encrypted with password. Microsoft's implementation of PFX loader doesn't support TripleDES encryption, so you need to care about this issue when you save the certificate for further use with Microsoft software.
 
**PEM**: Certificate and private key format, which includes base64-encoded DER data and optional text headers , enclosed into special begin and end marks. Private keys can be encrypted using DES (tripleDES) agorithm. Certificate and key can be saved to one file. The file can even contain several certificates and keys. PEM format is used by OpenSSL package.
 
**SPC**: Binary file format, which allows storing of certificates only (no private keys). Several certificates can be saved in one file. Private keys are usually saved to a separate file in DER or PVK format. Some implementations encode the PKCS#7 format to base64 text encoding (and sometimes even with UTF16), but this is not standard-compliant.
 
**PVK**: Binary file format for storing private keys with password-based encryption.
 
**CER/DER/KEY**: Basic certificate and key format, which represents pure certificate and key data in binary ASN.1 notation. Certificates and keys are stored separately. Some implementations encode the DER format to base64 text encoding (and sometimes even with UTF16), but this is not standard-compliant.
