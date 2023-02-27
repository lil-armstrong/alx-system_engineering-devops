# 0x04. Loops, conditions and parsing

## Resources

Read or watch:

-   [Loops sample](https://intranet.alxswe.com/rltoken/wT98UJfv_E2tk4yP9PcLLw)
-   [Variable assignment and arithmetic](https://intranet.alxswe.com/rltoken/olvOKX699pq50rkHRE5cSA)
-   [Comparison operators](https://intranet.alxswe.com/rltoken/HxohzllkOWh0t4dy_HptIQ)
-   [File test operators](https://intranet.alxswe.com/rltoken/g8of2ABPEJfCNtPrDQaqVw)
-   [Make your scripts portable](https://intranet.alxswe.com/rltoken/O0Ay21p7tDhfLMsYbtAKug)

man or help:

-   `env`
-   `cut`
-   `for`
-   `while`
-   `until`
-   `if`

**ShellCheck - A shell script static analysis tool**

> `ShellCheck` is a GPLv3 tool that gives warnings and suggestions for bash/sh shell scripts.

`Shellcheck` is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. `Shellcheck` is your friend! **All your Bash scripts must pass `Shellcheck` without any error or you will not get any points on the task**.

`Shellcheck` is available on the school’s computers. If you want to use it on your own computer, here is how to [install it](https://intranet.alxswe.com/rltoken/jbz0_-i3TV3WpKgxhyrtpA).

## Operators

### **Assignment**

All-purpose assignment operator, which works for both arithmetic and string assignments.

```bash
var=27
category=minerals  # No spaces allowed after the "=".
```

**Caution**

Do not confuse the "=" assignment operator with the = test operator.

```bash
#   =  as a test operator

if [ "$string1" = "$string2" ]
then
   command
fi
```

**Arithmetic**

-   Plus (+)

```shell
n=1
let "n=$n + 1"
```

-   Minus (-)
-   Multiplication (\*)
-   Division (/)
-   Exponentiation (\*\*)

    ```bash
    # Bash, version 2.02, introduced the "**" exponentiation operator.

    let "z=5**3"    # 5 * 5 * 5
    echo "z = $z"   # z = 125
    ```

-   Modulo(%)
-   Plus-equal(+=)
-   Minus-equal(-=)
-   Times-equal(\*=)
-   Slash-equal(/=)
-   Mod-equal(%=)

> Bash does not understand floating point arithmetic. It treats numbers containing a decimal point as strings.

```bash
a=1.5

let "b = $a + 1.3"  # Error.
# t2.sh: let: b = 1.5 + 1.3: syntax error in expression
#                            (error token is ".5 + 1.3")

echo "b = $b"       # b=1
```

> Use **bc** in scripts that that need floating point calculations or math library functions

**Bitwise**

-   Bitwise left shift(<<)
-   Left-shift-equal (<<=)
-   Left-shift-equal (<<=)
-   Bitwise right shift (>>)
-   Right-shift-equal (inverse of <<=)
-   Bitwise AND (&)
-   Bitwise AND-equal (&=)
-   Bitwise OR (|)
-   Bitwise OR-equal (|=)
-   Bitwise NOT(~)
-   Bitwise XOR (^)
-   Bitwise XOR-equal(^=)

**Logical**

-   NOT (!)
-   AND (&&)
-   OR (||)

**Miscllaneous**

-   Comma (,)

### Comparison

> There is some blurring between the arithmetic and string comparisons, since Bash variables are not strongly typed.

**Integer comparison**

-   Equal to (-eq)
-   Not equal to (-ne)
-   Greater than (-gt)
-   Greater than or equal to (-ge)
-   Less than (-lt)
-   Less than or equal to (-le)
-   Less than (<)
-   Less than or equal (<=)
-   Greater than (>)
-   Greater than or equal(>=)

**String comparison**

-   Equal to (`=`)

    ```bash
    if [ "$a" = "$b" ]
    ```

    > **Caution:**
    > Note the whitespace framing the =.

    `if [ "$a"="$b" ]` is not equivalent to the above.

-   Equal to (`==`)

    `if [ "$a" == "$b" ]`
    This is a synonym for `=`.
    The `==` comparison operator behaves differently within a double-brackets test than within single brackets.

    ```bash
    [[ $a == z* ]]   # True if $a starts with an "z" (pattern matching).
    [[ $a == "z*" ]] # True if $a is equal to z* (literal matching).

    [ $a == z* ]     # File globbing and word splitting take place.
    [ "$a" == "z*" ] # True if $a is equal to z* (literal matching).
    ```

-   Not equal to (!=):

```bash
if [ "$a" != "$b" ]
```

-   Less than (`<`)

```bash
if [[ "$a" < "$b" ]]
if [ "$a" \< "$b" ]
```

> **Note:** that the `<` needs to be escaped within a `[ ]` construct.

-   Greater than (`>`)

```bash
if [[ "$a" > "$b" ]]
if [ "$a" \> "$b" ]
```

> **Note:** that the `>` needs to be escaped within a `[ ]` construct.

-   is NULL (`-z`): string is null

```bash
 String=''   # Zero-length ("null") string variable.

if [ -z "$String" ]
then
  echo "\$String is null."
else
  echo "\$String is NOT null."
fi     # $String is null.
```

-   is NOT NULL (`-n`) - string is not null

**Compound comparison**

-   Logical and (-a)

    `exp1 -a exp2` returns true if both exp1 and exp2 are true.

-   Logical or (-o)

    `exp1 -o exp2` returns true if either exp1 or exp2 is true.

> These are similar to the Bash comparison operators `&&` and `||`, used within double brackets.

```bash
if [ "$expr1" -a "$expr2" ]
then
  echo "Both expr1 and expr2 are true."
else
  echo "Either expr1 or expr2 is false."
fi
```

But

```bash
[ 1 -eq 1 ] && [ -n "`echo true 1>&2`" ]   # true
[ 1 -eq 2 ] && [ -n "`echo true 1>&2`" ]   # (no output)
# ^^^^^^^ False condition. So far, everything as expected.
# However ...
[ 1 -eq 2 -a -n "`echo true 1>&2`" ]       # true
# ^^^^^^^ False condition. So, why "true" output?

# Is it because both condition clauses within brackets evaluate?
[[ 1 -eq 2 && -n "`echo true 1>&2`" ]]     # (no output)
# No, that's not it.

# Apparently && and || "short-circuit" while -a and -o do not.
```

## Loops

### for loops

```bash
for arg in [list]
do
 command(s)...
done
```

```bash
for arg in "$var1" "$var2" "$var3" ... "$varN"
# In pass 1 of the loop, arg = $var1
# In pass 2 of the loop, arg = $var2
# In pass 3 of the loop, arg = $var3
# ...
# In pass N of the loop, arg = $varN

# Arguments in [list] quoted to prevent possible word splitting.
```

> The argument list may contain wild cards. If do is on same line as for, there needs to be a semicolon after list.

```bash
for arg in [list] ; do
```

> A variable may supply the [list] in a for loop.

```bash
#!/bin/bash
# fileinfo.sh

FILES="/usr/sbin/accept
/usr/sbin/pwck
/usr/sbin/chroot
/usr/bin/fakefile
/sbin/badblocks
/sbin/ypbind"     # List of files you are curious about.
                  # Threw in a dummy file, /usr/bin/fakefile.

echo

for file in $FILES
do

  if [ ! -e "$file" ]       # Check if file exists.
  then
    echo "$file does not exist."; echo
    continue                # On to next.
   fi

  ls -l $file | awk '{ print $8 "         file size: " $5 }'  # Print 2 fields.
  whatis `basename $file`   # File info.
  # Note that the whatis database needs to have been set up for this to work.
  # To do this, as root run /usr/bin/makewhatis.
  echo
done

exit 0
```

> If the [list] in a for loop contains wild cards (\* and ?) used in filename expansion, then globbing takes place.

```bash
#!/bin/bash

filename="*txt"

for file in $filename
do
 echo "Contents of $file"
 echo "---"
 cat "$file"
 echo
done
```

> Omitting the in [list] part of a for loop causes the loop to operate on $@ -- the positional parameters.

```bash
#!/bin/bash

#  Invoke this script both with and without arguments,
#+ and see what happens.

for a
do
 echo -n "$a "
done

#  The 'in list' missing, therefore the loop operates on '$@'
#+ (command-line argument list, including whitespace).

echo

exit 0
```

**Example 11-8. A grep replacement for binary files**

```bash
#!/bin/bash
# bin-grep.sh: Locates matching strings in a binary file.

# A "grep" replacement for binary files.
# Similar effect to "grep -a"

E_BADARGS=65
E_NOFILE=66

if [ $# -ne 2 ]
then
  echo "Usage: `basename $0` search_string filename"
  exit $E_BADARGS
fi

if [ ! -f "$2" ]
then
  echo "File \"$2\" does not exist."
  exit $E_NOFILE
fi


IFS=$'\012'       # Per suggestion of Anton Filippov.
                  # was:  IFS="\n"
for word in $( strings "$2" | grep "$1" )
# The "strings" command lists strings in binary files.
# Output then piped to "grep", which tests for desired string.
do
  echo $word
done

# As S.C. points out, lines 23 - 30 could be replaced with the simpler
#    strings "$2" | grep "$1" | tr -s "$IFS" '[\n*]'


#  Try something like  "./bin-grep.sh mem /bin/ls"
#+ to exercise this script.

exit 0
```

**Example 11-9. Listing all users on the system**

```bash
#!/bin/bash
# userlist.sh

PASSWORD_FILE=/etc/passwd
n=1           # User number

for name in $(awk 'BEGIN{FS=":"}{print $1}' < "$PASSWORD_FILE" )
# Field separator = :    ^^^^^^
# Print first field              ^^^^^^^^
# Get input from password file  /etc/passwd  ^^^^^^^^^^^^^^^^^
do
  echo "USER #$n = $name"
  let "n += 1"
done


# USER #1 = root
# USER #2 = bin
# USER #3 = daemon
# ...
# USER #33 = bozo

exit $?

#  Discussion:
#  ----------
#  How is it that an ordinary user, or a script run by same,
#+ can read /etc/passwd? (Hint: Check the /etc/passwd file permissions.)
#  Is this a security hole? Why or why not?
```

### While loops

```bash
while [ condition ]
do
 command(s)...
done

# One liner
while [ condition ] ; do
```

_Example_

```bash
#!/bin/bash

var0=0
LIMIT=10

while [ "$var0" -lt "$LIMIT" ]
#      ^                    ^
# Spaces, because these are "test-brackets" . . .
do
  echo -n "$var0 "        # -n suppresses newline.
  #             ^           Space, to separate printed out numbers.

  var0=`expr $var0 + 1`   # var0=$(($var0+1))  also works.
                          # var0=$((var0 + 1)) also works.
                          # let "var0 += 1"    also works.
done                      # Various other methods also work.

echo

exit 0
```

_Example_

```bash
#!/bin/bash

echo
                               # Equivalent to:
while [ "$var1" != "end" ]     # while test "$var1" != "end"
do
  echo "Input variable #1 (end to exit) "
  read var1                    # Not 'read $var1' (why?).
  echo "variable #1 = $var1"   # Need quotes because of "#" . . .
  # If input is 'end', echoes it here.
  # Does not test for termination condition until top of loop.
  echo
done

exit 0
```

_Example: C-style syntax in a while loop_

```bash
#!/bin/bash
# wh-loopc.sh: Count to 10 in a "while" loop.

LIMIT=10                 # 10 iterations.
a=1

while [ "$a" -le $LIMIT ]
do
  echo -n "$a "
  let "a+=1"
done                     # No surprises, so far.

echo; echo

# +=================================================================+

# Now, we'll repeat with C-like syntax.

((a = 1))      # a=1
# Double parentheses permit space when setting a variable, as in C.

while (( a <= LIMIT ))   #  Double parentheses,
do                       #+ and no "$" preceding variables.
  echo -n "$a "
  ((a += 1))             # let "a+=1"
  # Yes, indeed.
  # Double parentheses permit incrementing a variable with C-like syntax.
done

echo

# C and Java programmers can feel right at home in Bash.

exit 0
```

### Until loops

This construct tests for a condition at the top of a loop, and keeps looping as long as that condition is false (opposite of while loop).

```bash
until [ condition-is-true ]
do
 command(s)...
done

until [ condition-is-true ] ; do
```

_Example_

```bash
#!/bin/bash

END_CONDITION=end

until [ "$var1" = "$END_CONDITION" ]
# Tests condition here, at top of loop.
do
  echo "Input variable #1 "
  echo "($END_CONDITION to exit)"
  read var1
  echo "variable #1 = $var1"
  echo
done

#                     ---                        #

#  As with "for" and "while" loops,
#+ an "until" loop permits C-like test constructs.

LIMIT=10
var=0

until (( var > LIMIT ))
do  # ^^ ^     ^     ^^   No brackets, no $ prefixing variables.
  echo -n "$var "
  (( var++ ))
done    # 0 1 2 3 4 5 6 7 8 9 10


exit 0
```

## Tasks

### 0. Create a SSH RSA key pair

Read for this task:

-   [Linux and Mac OS users](https://intranet.alxswe.com/rltoken/Cy1plV2eR3VphjPqliXB8A)
-   [Windows users](https://intranet.alxswe.com/rltoken/PXriGT0IKaSXC7L5l0CVag)

man: `ssh-keygen`

You will soon have to manage your own servers concept page hosted on remote data centers. We need to set them up with your RSA public key so that you can access them via SSH.

**Create a RSA key pair.**

Requirements:

-   Share your public key in your answer file `0-RSA_public_key.pub`
-   Fill the SSH public key field of your intranet profile with the public key you just generated
-   Keep the private key to yourself in a secure location, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
-   If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase

SSH and RSA keys will be covered in depth in a later project.

### 1. For Best School loop

Write a Bash script that displays `Best School` 10 times.

Requirement:

-   You must use the for loop (`while` and `until` are forbidden)

### 2. While Best School loop

Write a Bash script that displays `Best School` 10 times.

Requirements:

-   You must use the `while` loop (`for` and `until` are forbidden)

### 3. Until Best School loop

Write a Bash script that displays `Best School` 10 times.

Requirements:

-   You must use the `until` loop (`for` and `while` are forbidden)

### 4. If 9, say Hi!

Write a Bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` and then `Hi on a new line`.

Requirements:

-   You must use the while loop (for and until are forbidden)
-   You must use the if statement

### 5. 4 bad luck, 8 is your chance

Write a Bash script that loops from 1 to 10 and:-

-   displays `bad luck` for the 4th loop iteration
-   displays `good luck` for the 8th loop iteration
-   displays `Best School` for the other iterations

Requirements:

-   You must use the `while` loop (`for` and `until` are forbidden)
-   You must use the `if`, `elif` and `else` statements

### 6. Superstitious numbers

Write a Bash script that displays numbers from 1 to 20 and:

-   displays `4` and then `bad luck from China` for the 4th loop iteration
-   displays `9` and then `bad luck from Japan` for the 9th loop iteration
-   displays `17` and then `bad luck from Italy` for the 17th loop iteration

Requirements:

-   You must use the while loop (for and until are forbidden)
-   You must use the case statement

### 7. Clock

Write a Bash script that displays the time for 12 hours and 59 minutes:

-   display hours from 0 to 12
-   display minutes from 1 to 59

Requirements:

-   You must use the `while` loop (`for` and `until` are forbidden)

Note that in this example, we only display the first 70 lines using the head command.

### 8. For ls

Write a Bash script that displays:

-   The content of the current directory
-   In a list format
-   Where only the part of the name after the first dash is displayed (refer to the example)

Requirements:

-   You must use the for loop (`while` and `until` are forbidden)
-   Do not display hidden files

### 9. To file, or not to file

Write a Bash script that gives you information about the school file.

**Requirements:**

-   You must use if and, else (case is forbidden)
-   Your Bash script should check if the file exists and print:
    -   if the file exists: school file exists
    -   if the file does not exist: school file does not exist
-   If the file exists, print:
-   if the file is empty: school file is empty
-   if the file is not empty: school file is not empty
-   if the file is a regular file: school is a regular file
-   if the file is not a regular file: (nothing)

### 10. FizzBuzz

Write a Bash script that displays numbers from 1 to 100.

Requirements:

-   Displays `FizzBuzz` when the number is a multiple of 3 and 5
-   Displays `Fizz` when the number is multiple of 3
-   Displays `Buzz` when the number is a multiple of 5
-   Otherwise, displays the number
-   In a list format
