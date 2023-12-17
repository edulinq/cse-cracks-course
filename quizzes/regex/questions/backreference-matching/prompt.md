Suppose that we are trying to write a script extract name information from text and put it into a CSV (comma\-separated value) file.
The order of the columns in our CSV file are: first name, last name, and title.
As part of our script, we have a regular expression that looks for people that have their name's written as "last, first".

```
import re

def create_csv_line(text_line):
    regex = r'^\s*((Dr).?)?\s*([^,]+)\s*,\s*(.+)\s*$'
    replacement = MY_REPLACEMENT_STRING

    return re.sub(regex, replacement, text_line)
```

Fill in the blanks in `MY_REPLACEMENT_STRING` to make the above code work correctly.

`MY_REPLACEMENT_STRING = r'`[[BLANK1]]`,`[[BLANK2]]`,`[[BLANK3]]`'`
