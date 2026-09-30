---
sidebar_label: 'Global - PGP Key Rings'
hide_title: 'true'
---

## Global - PGP Key Rings

**What is PGP?**

Pretty Good Privacy (PGP) is a strong encryption program used to encrypt files and e-mail. PGP is similar to PKI (Public Key Infrastructure) and is based on asymmetric (open-key) cryptography. The OpenPGP standard was originally derived from PGP.
 
**How PGP encryption works**

PGP encryption uses public-key cryptography and includes a system which binds the public keys to user identities. PGP message encryption uses asymmetric key encryption algorithms that use the public portion of a recipient's linked key pair, a public key, and a private key. The sender uses the recipient's public key to encrypt a shared key (a.k.a. a secret key or conventional key) for a symmetric cipher algorithm. That key is used, finally, to encrypt the plaintext of a message. Many PGP users' public keys are available to all from the many PGP key servers around the world which act as mirror sites for each other.
 
The recipient of a PGP encrypted email message decrypts it using the session key for a symmetric algorithm. That session key is included in the message in encrypted form and was itself decrypted using the recipient's private key. Use of two ciphers in this way is sensible because of the very considerable difference in operating speed between asymmetric key and symmetric key ciphers (the differences are often 1000+ times). This operation is completely automated in current PGP desktop client products.
 
**The VisualCron implementation of PGP**

In VisualCron you are able to encrypt/decrypt PGP files using the OpenPGP standard. Encryption and decryption is part of the PGP Task. You are also able to sign your files and manage public and private keys.
 
**Manage PGP Key Rings**

The PGP key rings are managed in the main menu **Server > Global objects > PGP Key Rings** dialog. Instead of pointing to public or private key files, VisualCron lets you generate or import this data and then centrally store it in VisualCron. A key ring is a set of keys, public or private. VisualCron wraps key rings in the manager. At a later stage, when you want to encrypt a file, you first select a VisualCron key ring and then the recipients or signers key from the same key ring.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20PGP%20Key%20Rings/PGP%20Key%20Rings.png)

**Name/Description of VisualCron key ring**

Choose a proper name for the VisualCron key ring so you later can distinguish it from other.
 
**Create a key ring**

You can either create an empty key ring or create a key ring from already existing public or private key ring files.
 
**Import key(s)** 

Mark the key ring and click on the Import key(s) icon to select a path to a key ring file.
 
**Create key**

Mark the key ring and click on the Create key icon. The *Generate PGP key* window opens.
 
**Select encryption**

Select the key algorithm:

* *RSA (encrypt or sign)* - creates a single RSA key that can be used for both encryption and signing
* *RSA (encrypt only)* - creates an RSA signing key with a separate RSA encryption sub key
* *ElGamal (encrypt only)* - creates a DSA signing key with a separate ElGamal encryption sub key

All keys are created as version 4 OpenPGP keys. Elliptic curve (ECC) keys are not available.
 
**Strength**

Select bit strength: 512, 1024, 1536, 2048 or 4096. The default is 512, which is not considered secure today. Select 2048 or 4096 for new keys.
 
**Expiry date**

Select the date the key expires. The default is one year from today. The date cannot be earlier than today. Check *Never* to create a key that does not expire.
 
**Username**

Enter your name.
 
**Email**

Enter your email address.
 
**Password**

Enter password.
 
Click *OK* to generate the key.

**Algorithms used when a key is created**

The Generate PGP key window does not let you select the algorithms below. They are set automatically:

* *Private key protection* - the private key is protected with your password using the CAST5 (128-bit) cipher and an iterated and salted SHA-1 hash
* *Self-signature* - the signature that binds the username, email and expiry date to the key uses SHA-1
* *Preferred algorithms* - the key does not list preferred ciphers or hashes. Software that encrypts files for this key uses its own default settings

The encryption algorithm used for your files is selected separately in the [PGP Encrypt Task](job-tasks/encryption-tasks/pgp-encrypt), where AES-256 is available.

:::tip Tip

If you need a key where the private key is protected with AES-256 and SHA-2, create the key in a dedicated PGP tool such as GnuPG or Kleopatra and then import it into a VisualCron key ring with *Import key(s)*.

:::
 
**Signing and revoking** 

Mark a user in the key and click on either *Sign selected* or *Revoke selected*. Select a private key and then your password to continue signing/revoking.
