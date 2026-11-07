---
sidebar_label: 'Task Net - Serial Send'
hide_title: 'true'
---

## Task Net - Serial Send

The Serial Send Task writes text to a device on a serial (COM) port of the VisualCron Server computer. It only sends: it does not read a reply from the device.

![Serial Send Task settings, with the Connection group and the Send text group](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/Serial%20-%20Send.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

In the _Connection_ group:

- _Serial port_: the COM port, "COM1" by default

  The list shows the COM ports of the VisualCron Server.

- _Baud rate_: the speed in bits per second: "150", "300", "600", "1200", "2400", "4800", "9600", "19200", "38400", "57600" or "115200"

  The default is "9600".

- _Data bits_: the Task always uses 8 data bits

  A value you choose here is not saved.

- _Handshake_: the flow control: "None" (default), "XOnXOff", "RequestToSend" or "RequestToSendXOnXOff"
- _Parity_: "None" (default), "Odd", "Even", "Mark" or "Space"
- _Stop bits_: "One" (default), "Two" or "OnePointFive"

  "None" is also listed, but the serial port does not accept it, and the Task fails.

In the _Send text_ group:

- _New line_: what is added after the text: "None" (default), "Cr" (a carriage return) or "CrLf" (a carriage return and a line feed)

  Choose the one the device expects.

- _String to write_: the text to send to the device. The field is required.
