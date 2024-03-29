# 0x16. API advanced

> To check if your module has been documented use 

```bash
python3 -c 'print(__import__("<my_module>").__doc__)'
```

> Your code should use the `PEP 8` style

Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.

## 0. How many subs?

Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

**Requirements:**

    Prototype: def number_of_subscribers(subreddit)
    If not a valid subreddit, return 0.
    NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

# 1. Top ten

Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

**Requirements:**

    Prototype: `def top_ten(subreddit)`
    If not a valid subreddit, print None.
    NOTE: Invalid sub-reddits may return a redirect to search results. Ensure that you are not following redirects.

# 3. Count it!

Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).

**Requirements:**

- Prototype: `def count_words(subreddit, word_list)`

- Note: You may change the prototype, but it must be able to be called with just a subreddit supplied and a list of keywords. AKA you can add a counter or anything else, but the function must work without supplying a starting value in the main.

- If `word_list` contains the same word (case-insensitive), the final count should be the sum of each duplicate (example below with java)

```bash
bob@dylan $ cat 100-main.py 
#!/usr/bin/python3
"""
100-main
"""
import sys

if __name__ == '__main__':
    count_words = __import__('100-count').count_words
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
bob@dylan $             
bob@dylan $ python3 100-main.py programming 'react python java javascript scala no_results_for_this_one'
java: 27
javascript: 20
python: 17
react: 17
scala: 4
bob@dylan $ python3 100-main.py programming 'JavA java'
java: 54
bob@dylan $ python3 100-main.py not_a_valid_subreddit 'python java javascript scala no_results_for_this_one'
bob@dylan $ python3 100-main.py not_a_valid_subreddit 'python java'
```

- Results should be printed in descending order, by the count, and if the count is the same for separate keywords, they should then be sorted alphabetically (ascending, from A to Z). Words with no matches should be skipped and not printed. Words must be printed in lowercase.
- Results are based on the number of times a keyword appears, not titles it appears in. java java java counts as 3 separate occurrences of java.
- To make life easier, `java.` or `java!` or `java_` should not count as java
- If no posts match or the subreddit is invalid, print nothing.
- NOTE: Invalid sub-reddits may return a redirect to search results. Ensure that you are NOT following redirects.

Your code will NOT pass if you are using a loop and not recursively calling the function! This can be done with a loop but the point is to use a recursive function. :)

Disclaimer: number presented in this example cannot be accurate now - Reddit is hot articles are always changing.


**TIP**:
You can use available python library linters that comply with PEP 8. One of such available linter is the `autopep8` package. Enter the following command ot install the linter:

```bash
pip install autopep8 virtualenv
source env/bin/activate
```

Using `autopep8` to fix file:

```bash
autopep8 --in-place --aggressive --aggressive <file_path>
```