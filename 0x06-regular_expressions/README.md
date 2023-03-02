# Regular Expressions

## Resources

-   [Basics](https://intranet.alxswe.com/rltoken/6VeaVMaugIxcFAwA27TBdQ)
-   [Advanced](https://intranet.alxswe.com/rltoken/rntjh3-3S86zt0Qy28L10w)
-   [Interactive Exxamples](https://intranet.alxswe.com/rltoken/XsQ6rzS1uy-E6bnswUqIKg)

## Modifiers

Modifiers are used to modify search criteria:

| Modifier | Description                                                                          |
| -------- | ------------------------------------------------------------------------------------ |
| g        | Perform a global match (find all matches rather than stopping after the first match) |
| i        | Perform case-insensitive matching                                                    |
| m        | Perform multiline matching                                                           |

## Brackets

Brackets are used to find range of characters

| Expressions | Description                                                |
| ----------- | ---------------------------------------------------------- |
| [abc]       | Find any character between the brackets                    |
| [^abc]      | Find any character NOT between the brackets                |
| [0-9]       | Find any character that is a digit within the range of 0-9 |
| (x\|y)      | Find any of the alternatives specified                     |

## Meta-characters

These are characters with a soecified meaning

| Meta-character | Description                                                                                 |
| -------------- | ------------------------------------------------------------------------------------------- |
| .              | Find a single character, except newline or line terminator                                  |
| \w             | Find a word character                                                                       |
| \W             | Find a non-word character                                                                   |
| \d             | Find a digit                                                                                |
| \D             | Find a non-digit character                                                                  |
| \s             | Find a whitespace character                                                                 |
| \S             | Find a non-whitespace character                                                             |
| \b             | Find a match at the beginning/end of a word, beginning like this: \bHI, end like this: HI\b |
| \B             | Find a match, but not at the beginning/end of a word                                        |
| \0             | Find a NULL character                                                                       |
| \n             | Find a new line character                                                                   |
| \f             | Find a form feed character                                                                  |
| \r             | Find a carriage return character                                                            |
| \t             | Find a tab character                                                                        |
| \v             | Find a vertical tab character                                                               |
| \xxx           | Find the character specified by an octal number xxx                                         |

\xdd
| \xdd | Find the character specified by a hexadecimal number dd
\udddd
| \uddd | Find the Unicode character specified by a hexadecimal number dddd

## Quantifiers

| Quantifiers | Description                                                    |
| ----------- | -------------------------------------------------------------- |
| n+          | Matches any string that contains at least one n                |
| n\*         | Matches any string that contains zero or more occurrences of n |
| n?          | Matches any string that contains zero or one occurrences of n  |
| n{X}        | Matches any string that contains a sequence of X n's           |
| n{X,Y}      | Matches any string that contains a sequence of X to Y n's      |
| n{X,}       | Matches any string that contains a sequence of at least X n's  |
| n$          | Matches any string with n at the end of it                     |
| ^n          | Matches any string with n at the beginning of it               |
| ?=n         | Matches any string that is followed by a specific string n     |
| ?!n         | Matches any string that is not followed by a specific string n |

# Tasks

## 0. Simply matching School

Requirements:

-   The regular expression must match School
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

## 1. Repetition Token #0

<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230302%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230302T080349Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3f545a760080e886c07a3908d85aa70cd15671029309f6eafb9c82a8886a1c2a" alt="Repetition token sample"/>

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

## 2. Repetition Token #1

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

## 3. Repetition Token #2

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

## 4. Repetition Token #3

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
-   Your regex should not contain square brackets

## 5. Not quite HBTN yet

Requirements:

-   The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

## 6. Call me maybe

This task is brought to you by a professional advisor [Neha Jain](https://intranet.alxswe.com/rltoken/GqwvXAvTXR_JXqyTvZ4AzQ), Senior Software Engineer at LinkedIn.

Requirement:

-   The regular expression must match a 10 digit phone number

## 7. OMG WHY ARE YOU SHOUTING?

Requirement:

-   The regular expression must be only matching: capital letters
