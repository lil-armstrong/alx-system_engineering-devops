# Tasks

## Tools
### Netcat (nc)
Netcat or nc is a networking utility for debugging and investigating the network. It can be used in two modes:

- Server mode:
You can open a port and listen to incoming connections. Example:
```bash
nc -l 2389
```
The above command will open port `2389` and will listen for incoming request or messages

- Client mode:
You can run `nc` as a client as well. For example:
```bash
nc localhost 2389
```
The above command will try to connect to your computer using port 2389. Now, if we write some text at the client side, it reaches the server side.

You can also use `nc` to transfer file. To learn more, visit [here](https://www.thegeekstuff.com/2012/04/nc-command-examples/)


## 0. Change your home IP

Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

-   localhost resolves to 127.0.0.2
-   facebook.com resolves to 8.8.8.8.
-   The checker is running on Docker, so make sure to read this

##  1. Show attached IPs 
Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.
