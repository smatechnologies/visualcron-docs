---
sidebar_label: 'Task System - Wakeup On Lan'
hide_title: 'true'
---

## Task System - Wakeup On Lan

The Wake up on LAN Task can wake a remote computer.
 
**Introduction**

Wake on LAN (WOL) support is implemented in the motherboard of the computer. The motherboard must have a WAKEUP-LINK header onboard and be connected to the network card via a special 3-pin cable. However, systems supporting the PCI 2.2 standard coupled with a PCI 2.2 compliant network adapter, typically do not require a WOL cable as the required standby power is relayed through the PCI bus. Most modern mother boards with an embedded Ethernet controller also support WOL.
 
Wake on LAN must be enabled in the Power Management section of the motherboard's BIOS. It may also be necessary to configure the computer to reserve power for the network card when the system is shut down.
 
In addition to get WOL to work, it is sometimes required to flash this feature to the card. You can do this in Windows from the properties of the network card in the device manager, on the Power Management tab. Check O*nly allow management stations to wake up the computer*, to make sure it does not wake up on every single network activity that occurs.
 
**How it works**

The general process of waking a computer up remotely in a LAN is: The target computer is shut down, with power reserved only for the network card. The network card listens for a specific packet, called the "Magic Packet". The Magic Packet is broadcast on the broadcast address for a particular subnet or the entire LAN. The listening computer receives this packet, checks it for the correct information, and then boots if the Magic Packet data is matching.
 
**Magic Packet**

The Magic Packet is a broadcast frame, transmitted over port 0 (historically the most common port used), 7 or 9 (becoming the most common ports used). It can be sent over a variety of connectionless protocols (UDP, IPX) but UDP is most commonly used. The data that is contained in a Magic Packet is the a constant represented in hexadecimal: FF FF FF FF FF FF, followed by sixteen repetitions of the target computer's MAC address, possibly followed by a four or six byte password.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Wake%20up%20on%20LAN.png)

**MAC Address**

Enter the MAC address of the remote network card. Click on *Scan/Find MAC* to search for MAC's in your network.
 
**Scan/Find MAC**

Enter a host name or range like 192.168.1.1 to 192.168.1.100. Click on *Search* to start finding MAC's. Double click on row to use the MAC found.
 
:::info Note

**Remark on Wake Up**

Some computers can wake up from standby and not from hibernation, some work for both, and some for none. It all depends on the BIOS and the APM/ACPI capabilities, your motherboard, and your ATX power supply version.

:::