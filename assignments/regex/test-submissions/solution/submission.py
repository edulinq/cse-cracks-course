# A test solution just needs to expose the portions of the assignment that the grader will use.
# It could be a full iPython notebook, but a simple Python file is also sufficient.

TASK1_REGEX = r'cat'

TASK2_REGEX = r'\d\w\w\w\d\d\d'

TASK3_REGEX = r'code_\w = ".\d\d\d"'

TASK4_REGEX = r'code_[a-z][ \t]=[ \t]"[a-zA-Z0-9]\d\d\d"'

TASK5_REGEX = r'^0x[0-9a-f][0-9a-f]\.[0-9a-f][0-9a-f]$'

TASK6_REGEX = r'^0x[0-9a-f]+\.?[0-9a-f]*$'

TASK8_REGEX = r'code_[a-z]\s*=\s*"([a-zA-Z0-9]\d{3})"'
TASK8_REPLACEMENT = r'code_\1 = "\1"'
