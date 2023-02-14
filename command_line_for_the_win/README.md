## Background

[CMD CHALLENGE](https://intranet.alxswe.com/rltoken/a83_NOBEtXgFr1Yqej0HYA) is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

This project is NOT mandatory at all. It is 100% optional. Doing any part of this project will add a project grade of over 100% to your average. Your score won’t get hurt if you don’t do it, but if your current average is greater than your score on this project, your average might go down. Have fun!

## Tasks

### 0. First n task

Complete the first 9 tasks.

### 1. Reach n completed task

Complete the 9 next tasks, getting to 18 total.

-   List names of all the files in the current directory, one file per line.

```bash
ls | cat
```

-   Print the last 5 lines of "access.log".

```bash
tail -n 5 acess.log
```

-   Create a symbolic link named take-the-command-challenge that points to the file tmp/files/take-the-command-challenge.

```bash
ln -s tmp/files/take-the-command-challenge take-the-command-challenge
```

-   Delete all of the files in this challenge directory including all subdirectories and their contents.

> **Hint:** _There are files and directories that start with a dot ".", "rm -rf \*" won't work here!_

```bash
find . -delete
```

-   There are files in this challenge with different file extensions. Remove all files with the .doc extension recursively in the current working directory.

```bash
find . -name '*.doc' -delete
rm -rf **/*.doc
find . -name "*.doc" -type f -delete
find . -name "*.doc" | xargs rm
```

-- Print all matching lines (without the filename or the file path) in all files under the current directory that start with "access.log" that contain the string "500".

> _Note that there are no files named access.log in the current directory, you will need to search recursively._

```bash
grep -r -h "500"
```

-   Extract all IP addresses from files that start with "access.log" printing one IP address per line.

```bash
grep -ro ^[0-9.]*
```

-   Count the number of files in the current working directory. Print the number of files as a single integer.

```bash
ls -l | wc -l
```

-   Print the contents of access.log sorted.

```bash
cat | sort access.log
```

-   There is a file named access.log in the current working directory. Print all lines in this file that contains the string "GET".

```bash
cat access.log | grep "GET"
```

-   Print all files in the current directory, one per line (not the path, just the filename) that contain the string "500".

```bash
grep -l "500" *
```
- Print the number of lines in access.log that contain the string "GET".
```bash
cat access.log | grep "GET" | wc -l
```

- The file split-me.txt contains a list of numbers separated by a ; character.
Split the numbers on the ; character, one number per line.
```bash
cat split-me.txt |tr ";" "\n"
cat split-me.txt |tr \; "\n"
```

- Print the numbers 1 to 100 separated by spaces.
```bash
echo {1...100}
seq -s " " 1 100
```
