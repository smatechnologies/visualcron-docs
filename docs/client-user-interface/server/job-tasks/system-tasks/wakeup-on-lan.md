---
sidebar_label: 'Task System - Wakeup On Lan'
hide_title: 'true'
---

## Task System - Wakeup On Lan

The Wake up on LAN Task sends a Wake on LAN packet from the VisualCron Server computer to wake a remote computer.

**Introduction**

Wake on LAN (WOL) support is implemented in the motherboard of the computer. The motherboard must have a WAKEUP-LINK header onboard and be connected to the network card through a special 3-pin cable. However, systems supporting the PCI 2.2 standard together with a PCI 2.2 compliant network adapter typically do not need a WOL cable, because the standby power is relayed through the PCI bus. Most modern motherboards with an embedded Ethernet controller also support WOL.

Wake on LAN must be enabled in the Power Management section of the motherboard's BIOS. It may also be necessary to configure the computer to reserve power for the network card when the system is shut down.

In addition to get WOL to work, it is sometimes required to flash this feature to the card. You can do this in Windows from the properties of the network card in the device manager, on the Power Management tab. Check O*nly allow management stations to wake up the computer*, to make sure it does not wake up on every single network activity that occurs.

**How it works**

The target computer is shut down, with power reserved only for the network card. The network card listens for a specific packet, called the "Magic Packet". When it receives a Magic Packet that contains its own MAC address, the computer starts.

**Magic Packet**

The data in a Magic Packet is the hexadecimal constant FF FF FF FF FF FF, followed by sixteen repetitions of the MAC address of the target computer. The Task sends it over UDP as a broadcast to the address 255.255.255.255, port 12287. A broadcast to that address stays on the local network of the VisualCron Server computer, so the target computer must be on the same network, or the routers must forward the packet.

![Wake up on LAN Task settings, with the MAC Address field and the Scan/Find MAC button](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Wake%20up%20on%20LAN.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Wake up on LAN tab

- _MAC Address_ (_Wake up on lan_ group): the MAC address of the network card of the remote computer, with its six parts separated by ":" or "-", for example `00-11-22-33-44-55`. Any other format makes the Task fail
- _Scan/Find MAC_: opens the _Find MAC_ window, to find a MAC address on the network

To find a MAC address:

1. Click _Scan/Find MAC_.
2. Select _Search single IP or hostname_ or _Search IP range_.
3. Enter the host, or the first and last address of the range.
4. Click _Search_.
5. Double-click a row in the result to use its MAC address.

On success, the output is "Wake up on lan sent.". The Task reports success once the packet is sent; it does not check that the remote computer woke up.

:::info Note

**Remark on Wake Up**

Some computers can wake up from standby and not from hibernation, some work for both, and some for none. It all depends on the BIOS and the APM/ACPI capabilities, your motherboard, and your ATX power supply version.

:::
