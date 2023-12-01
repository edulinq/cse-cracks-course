#!/usr/bin/env python3

"""
Do a local practice grading.
The score you receive here is not an actual score,
but gives you an idea on how prepared you are to submit to the autograder.

This local grader will test the same test cases seen in the assignment text,
but can be extended with more test cases.
"""

import os
import re
import sys

import autograder.assignment
import autograder.question
import autograder.style

class Regex(autograder.assignment.Assignment):
    def __init__(self, **kwargs):
        super().__init__(
            name = 'Practice Grading for Regex Tutorial',
            questions = [
                T1(1, "Task 1: My First Match"),
                T2(1, "Task 2: License Plates"),
                T3(1, "Task 3: Mysterious Code"),
                T4(1, "Task 4: Mysterious Code - Better"),
                T5(1, "Task 5: Finding Bad Data"),
                T6(1, "Task 6: Finding Bad Data - Better"),
                T7(1, "Task 7: Finding Bad Data - Best"),
                T8(1, "Task 8: Mysterious Code - Best"),
                autograder.style.Style(kwargs.get('input_dir'), max_points = 0),
            ], **kwargs)

class T1(autograder.question.Question):
    def score_question(self, submission):
        regex = submission.__all__.TASK1_REGEX

        if ((not isinstance(regex, str)) or (regex == "")):
            self.fail("Your regex should be a non-empty string.")

        self.full_credit()

        # Use the test cases that are already in the assignment text.
        # [(string, is_match?, feedback), ...]
        test_cases = [
            # Matching test cases.
            ("cat", True, "cat"),
            ("cats", True, "cats"),
            ("some cat", True, "some cat"),
            ("categories", True, "categories"),

            # Non-matching test cases.
            ("dog", False, "dog"),
            ("cta", False, "cta"),
        ]

        _run_regex_test_cases(self, regex, test_cases)

        self.cap_score()

class T2(autograder.question.Question):
    def score_question(self, submission):
        regex = submission.__all__.TASK2_REGEX

        if ((not isinstance(regex, str)) or (regex == "")):
            self.fail("Your regex should be a non-empty string.")

        self.full_credit()

        # [(string, is_match?, feedback), ...]
        test_cases = [
            # Matching test cases.
            ('1ABC123', True, '1ABC123'),
            ('0xyz987', True, '0xyz987'),
            ('1234567', True, '1234567'),

            # Non-matching test cases.
            ('123', False, '123'),
            ('abcdefg', False, 'abcdefg'),
        ]

        _run_regex_test_cases(self, regex, test_cases)

        self.cap_score()

class T3(autograder.question.Question):
    def score_question(self, submission):
        regex = submission.__all__.TASK3_REGEX

        if ((not isinstance(regex, str)) or (regex == "")):
            self.fail("Your regex should be a non-empty string.")

        self.full_credit()

        # [(string, is_match?, feedback), ...]
        test_cases = [
            # Matching test cases.
            ('code_a = "a123"', True, 'code_a = "a123"'),
            ('code__ = "!098"', True, 'code__ = "!098"'),
            ('code_b = "1098"', True, 'code_b = "1098"'),

            # Non-matching test cases.
            ('a = "a123"', False, 'a = "a123"'),
            ('code__ = "098"', False, 'code__ = "098"'),
            ('code_ = "1098"', False, 'code_ = "1098"'),
        ]

        _run_regex_test_cases(self, regex, test_cases)

        self.cap_score()

class T4(autograder.question.Question):
    def score_question(self, submission):
        regex = submission.__all__.TASK4_REGEX

        if ((not isinstance(regex, str)) or (regex == "")):
            self.fail("Your regex should be a non-empty string.")

        self.full_credit()

        # [(string, is_match?, feedback), ...]
        test_cases = [
            # Matching test cases.
            ('code_a = "a123"', True, 'code_a = "a123"'),
            ('code_b = "1098"', True, 'code_b = "1098"'),
            ('code_c\t=\t"z395"', True, 'code_c\t=\t"z395"'),

            # Non-matching test cases.
            ('a = "a123"', False, 'a = "a123"'),
            ('code__ = "098"', False, 'code__ = "098"'),
            ('code_ = "1098"', False, 'code_ = "1098"'),
            ('code_33 = "Z456"', False, 'code_33 = "Z456"'),
            ('code__ = "!098"', False, 'code__ = "!098"'),
            ('code_3 = "Z456"', False, 'code_3 = "Z456"'),
        ]

        _run_regex_test_cases(self, regex, test_cases)

        self.cap_score()

class T5(autograder.question.Question):
    def score_question(self, submission):
        regex = submission.__all__.TASK5_REGEX

        if ((not isinstance(regex, str)) or (regex == "")):
            self.fail("Your regex should be a non-empty string.")

        self.full_credit()

        # [(string, is_match?, feedback), ...]
        test_cases = [
            # Matching test cases.
            ('0x12.34', True, '0x12.34'),
            ('0xfe.dc', True, '0xfe.dc'),

            # Non-matching test cases.
            ('12.34', False, '12.34'),
            ('fedc', False, 'fedc'),
            ('other 0x12.34 junk', False, 'other 0x12.34 junk'),
        ]

        _run_regex_test_cases(self, regex, test_cases)

        self.cap_score()

class T6(autograder.question.Question):
    def score_question(self, submission):
        regex = submission.__all__.TASK6_REGEX

        if ((not isinstance(regex, str)) or (regex == "")):
            self.fail("Your regex should be a non-empty string.")

        self.full_credit()

        # [(string, is_match?, feedback), ...]
        test_cases = [
            # Matching test cases.
            ('0x12.34', True, '0x12.34'),
            ('0xfe.dc', True, '0xfe.dc'),
            ('0x123456789.abcdef', True, '0x123456789.abcdef'),
            ('0xf', True, '0xf'),
            ('0x0001.0', True, '0x0001.0'),
            ('0x12.', True, '0x12.'),

            # Non-matching test cases.
            ('12.34', False, '12.34'),
            ('fedc', False, 'fedc'),
            ('other 0x12.34 junk', False, 'other 0x12.34 junk'),
            ('0x12.34.', False, '0x12.34.'),
        ]

        _run_regex_test_cases(self, regex, test_cases)

        self.cap_score()

class T7(autograder.question.Question):
    def score_question(self, submission):
        regex = submission.__all__.TASK7_REGEX

        if ((not isinstance(regex, str)) or (regex == "")):
            self.fail("Your regex should be a non-empty string.")

        self.full_credit()

        # [(string, is_match?, feedback), ...]
        test_cases = [
            # Matching test cases.
            ('0x12.34', True, '0x12.34'),
            ('0xfe.dc', True, '0xfe.dc'),
            ('0x123456789.abcdef', True, '0x123456789.abcdef'),
            ('0xf', True, '0xf'),
            ('0x0001.0', True, '0x0001.0'),
            ('0', True, '0'),
            ('1', True, '1'),
            ('2.3', True, '2.3'),
            ('-45.67', True, '-45.67'),

            # Non-matching test cases.
            ('a.12', False, 'a.12'),
            ('+3', False, '+3'),
            ('fedc', False, 'fedc'),
            ('other 0x12.34 junk', False, 'other 0x12.34 junk'),
            ('0x12.', False, '0x12.'),
            ('0x12.34.', False, '0x12.34.'),
        ]

        _run_regex_test_cases(self, regex, test_cases)

        self.cap_score()

class T8(autograder.question.Question):
    def score_question(self, submission):
        regex = submission.__all__.TASK8_REGEX
        replacement = submission.__all__.TASK8_REPLACEMENT

        if ((not isinstance(regex, str)) or (regex == "")):
            self.fail("Your regex should be a non-empty string.")

        if ((not isinstance(replacement, str)) or (replacement == "")):
            self.fail("Your replacement should be a non-empty string.")

        self.full_credit()

        # [(target, expected, feedback), ...]
        test_cases = [
            ('code_a = "a123"', 'code_a123 = "a123"', 'code_a = "a123"'),
            ('code_b     =     "1098"', 'code_1098 = "1098"', 'code_b     =     "1098"'),
            ('code_c\t=\t"z395"', 'code_z395 = "z395"', 'code_c\t=\t"z395"'),
        ]

        for (target, expected, feedback) in test_cases:
            actual = re.sub(regex, replacement, target)

            if (actual != expected):
                message = "Missed test case: '%s'." % (feedback)
                self.add_message(message, add_score = -3)

        self.cap_score()

# A helper function for running regex test cases.
# Test cases should be formatted as: [(string, is_match?, feedback), ...].
def _run_regex_test_cases(question, regex, test_cases):
    for (string, is_match, feedback) in test_cases:
        match = re.search(regex, string)

        if (is_match and (match is not None)):
            continue

        if ((not is_match) and (match is None)):
            continue

        # This case was failed, give the student feedback (and a one point deduction).
        if (is_match):
            message = "Did not match test case when you should have: '%s'." % (feedback)
        else:
            message = "Matched test case when you should not have: '%s'." % (feedback)

        question.add_message(message, add_score = -1)

def main(path):
    assignment = Regex(input_dir = path)
    result = assignment.grade()

    print("***")
    print("This is NOT an actual grade, submit to the autograder for an actual grade.")
    print("***\n")

    print(result.report())

def _load_args(args):
    exe = args.pop(0)
    if (len(args) != 1 or ({'h', 'help'} & {arg.lower().strip().replace('-', '') for arg in args})):
        print("USAGE: python3 %s <submission path (.py or .ipynb)>" % (exe), file = sys.stderr)
        sys.exit(1)

    path = os.path.abspath(args.pop(0))

    return path

if (__name__ == '__main__'):
    main(_load_args(list(sys.argv)))
