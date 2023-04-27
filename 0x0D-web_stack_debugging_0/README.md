# Task
After connecting to the container and fixing whatever needed to be fixed (here is your mission), you can see that curling port 80 return a page that contains Hello Holberton. Paste the command(s) you used to fix the issue in your answer file.

Test and verify your assumptions

The idea is to ask a set of questions until you find the issue. For example, if you installed a web server and it isn’t serving a page when browsing the IP, here are some questions you can ask yourself to start debugging:

    Is the web server started? - You can check using the service manager, also double check by checking process list.
    On what port should it listen? - Check your web server configuration
    Is it actually listening on this port? - netstat -lpdn - run as root or sudo so that you can see the process for each listening port
    It is listening on the correct server IP? - netstat is also your friend here
    Is there a firewall enabled?
    Have you looked at logs? - usually in /var/log and tail -f is your friend
    Can I connect to the HTTP port from the location I am browsing from? - curl is your friend

There is a good chance that at this point you will already have found part of the issue.
Get a quick overview of the machine state

Youtube video First 5 Commands When I Connect on a Linux Server

When you connect to a server/machine/computer/container you want to understand what’s happened recently and what’s happening now, and you can do this with 5 commands in a minute or less:

`w`

    shows server uptime which is the time during which the server has been continuously running
    shows which users are connected to the server
    load average will give you a good sense of the server health - (read more about load here and here)

`history`

    shows which commands were previously run by the user you are currently connected to
    you can learn a lot about what type of work was previously performed on the machine, and what could have gone wrong with it
    where you might want to start your debugging work

`top`

    shows what is currently running on this server
    order results by CPU, memory utilization and catch the ones that are resource intensive

`df`

    shows disk utilization

`netstat`

    what port and IP your server is listening on
    what processes are using sockets
    try netstat -lpn on a Ubuntu machine
