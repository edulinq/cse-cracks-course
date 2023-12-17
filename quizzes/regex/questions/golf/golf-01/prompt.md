Create a regular expression that matches successfully completes a game a golf with the table below.

Specifics:
 - Match all values in the `Match` column.
 - Do not match any values in the `No Match` column.
 - Write you regex as a raw string using a single or double quotes (not triple quotes).
 - Treat the contents of each table cell as a string (so you do not have the match the quotes).
 - You may assume that any contiguous whitespace is a single space character.
 - You only need to match (or not match) the values in the table, you do not need to extend this pattern to unseen values.


|- Match       | No Match      |
|--------------|---------------|
| `'12:00 AM'` | `'00:00'`     |
| `'05:30 PM'` | `'17:30'`     |
| `'01:45 AM'` | `'01:65 AM'`  |
| `'10:10 PM'` | `'10:10 ZZ'`  |
| `'12:34 PM'` | `'12:34 pm'`  |
| `'11:59 PM'` | `'23:59'`     |
|              | `'123:45 AM'` |
|              | `'12:345 PM'` |
