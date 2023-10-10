# 0x17. Web stack debugging #3

<span>DevOps</span>
<span>SysAdmin</span>
<span>Scripting</span>
<span>Debugging</span>

## 0. Strace is your friend

Using `strace`, find out why `Apache` is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

**Hint:**

- `strace` can attach to a current running process
- You can use `tmux` to run strace in one window and `curl` in another one

**Requirements:**

- Your `0-strace_is_your_friend.pp` file must contain Puppet code
- You can use whatever Puppet resource type you want for you fix

**Solution** 

Using strace to trace the error, I found out the reason for the `500` error. With the fllowing command, I attached `strace` to the Apache process and was able to trace the errors

```bash
strace -Cr -p 144 -o /apache_strace.log
```
The above command instructs the `strace` program to 
- `-C` - Count time , calls and errors for each syscall and report summary, printing regular output
- `-r` - Print relative timestamp
- `p` - Attach to the process PID of the `www-data` running apache
- `-o` - Output the trace log to the file: `/apache_strace.log`  

From the error trace log, I found out that the `var/www/html` folder was missing the index or entry file. The following file formats are expected by Apache to load the webpage 
 - `index.html` file.
 - `index.cgi` file.
 - `index.pl` file.

By adding the missing entry file, which in this case is `index.html`, the Apache no longer returned a `500` error code