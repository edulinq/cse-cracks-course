Implement a function with the folowing signature and description:

```
import re

def compute(text):
    """
    Compute the result of the binary expression represented in the |text| variable.
    The possible operators are: "+", "-", "*", and "/".
    Operands may be any real number.
    The the operation is division, the RHS (denominator) will not be zero.
    """

    return NotImplemented
```

Create a regular expression that matches successfully completes a game a golf with the table below.

Specifics:
 - Your function must use regular expressions.
 - You may not use `eval()` or any other Python ast functionality.
 - You may only import modules from the Python standard library.
 - You should return a float that is the result of the binary operation represented by `text`.
 - The operator will be one of:  $ \{+, -, *, /\} $.
 - Operands may be any real number.
