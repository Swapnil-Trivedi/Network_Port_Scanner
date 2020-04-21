# Network_Port_Scanner
A simple Program to Find available Ports on a Target Server.

## INTRODUCTION

- A Network is incomplete without a port. Port and IP plays an important role in network communication in telling user where and to whom to send data.
For Example an IP address can be simplified as the House address of a family and the ports associated to that ip can be viewed as the rooms alloted to different members of that house. hence, it is crucial to check where the parcel needs to be sent and to whom.

- The Project is a small attempt to find the list of all open ports on a machine. 

## HIGHLIGHTS OF THE CODE
The followinf features and working is to be noted from PORT_SCANNER.py
- ```
  import socket
  ```
- is the standard socket library in python used for creating the socket
- time module is imported to keep an eye on the time taken in scanning.
- All  the available ports i.e the 'OPEN' ports are appended to Port_list list.
- Since checking through all ports will create nothing but a mess as most of the ports are reserved for special purpose and won't be open the user has to give a range.
- The available ports have to be in range 0 to 65535
- A standard STREAMING type socket is made i.e TCP form
```
start_time=time.time()
...
.....
stop_time=time.time()
total_time=start_time - stop_time

is used to get the total execution time

```

- Now since a TCP socket is formed we close the connection only if any form of connection is established from that port i.e the port is 'OPEN'
 if the port is not open there will be no connection and we will be stuck with an unreachable port waiting to be connected.
 
 -In order to avoid endless waiting we setup a default timeout condition
 ```
 sock_object.settimeout([seconds])
 
 ```
 is used to make the default time out setting as 1 second
 - if connection is established we say the port is open and append it to Port_list
 
 ### That completes the simple Port Scanner script using python 
