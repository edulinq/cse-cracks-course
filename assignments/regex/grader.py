#!/usr/bin/env python3

import re
import sys

import autograder.assignment
import autograder.cmd.gradeassignment
import autograder.question
import autograder.style

class Regex(autograder.assignment.Assignment):
    def __init__(self, **kwargs):
        super().__init__(name = "Regex Tutorial", questions = [
            T1(10, "Task 1: My First Match"),
            T2(10, "Task 2: License Plates"),
            T3(10, "Task 3: Mysterious Code"),
            T4(10, "Task 4: Mysterious Code - Better"),
            T5(10, "Task 5: Finding Bad Data"),
            T6(10, "Task 6: Finding Bad Data - Better"),
            # T7(10, "Task 7: Finding Bad Data - Best"),
            T8(10, "Task 8: Mysterious Code - Best"),
            # You can automatically add a question that checks the assignment's Python style.
            autograder.style.Style(kwargs.get('input_dir'), max_points = 0),
        ], **kwargs)

class T1(autograder.question.Question):
    def score_question(self, submission):
        # The student's code has already been imported inside the "submission" object.
        # This automatic importing can be disabled at the assignment level.
        # Imported objects can either be referenced by packages/modules,
        # or using the '__all__' namespace, which flattens out all imported objects.
        regex = submission.__all__.TASK1_REGEX

        # It is usually a good idea to test the type of the student's result
        # before testing the value.
        # This allows for more clear feedback.
        if ((not isinstance(regex, str)) or (regex == "")):
            self.fail("Your regex should be a non-empty string.")

        # You can assigned points in a positive fashion or as deductions,
        # depending on what works best for your assignment.
        # This question will start at full credit, and assign deductions.
        # Note that this pattern may allow students to get points for no real implementation
        # (e.g., an empty string will get points for this question).
        self.full_credit()

        # Set up some test cases.
        # We will assign one point to each test case.
        # Writing feedback is one of the most difficult parts of writing a grader.
        # Feedback needs to be specific enough to be useful,
        # but general enough to not give away the answer.
        # [(string, is_match?, feedback), ...]
        test_cases = [
            # Matching test cases.
            ("cat", True, "the target sequence by itself"),
            ("cat___", True, "the target sequence with text after"),
            ("___cat", True, "the target sequence with text before"),
            ("___cat___", True, "the target sequence surrounded by text"),
            ("catcatcat", True, "the target sequence repeated"),

            # Non-matching test cases.
            ("dog", False, "a non-target sequence by itself"),
        ]

        _run_regex_test_cases(self, regex, test_cases)

        # Ensure that the assigned score is in [0, max_poionts].
        # You can skip this for questions that can have negative or bonus points.
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
            ("1ABC123", True, "a normal plate with all uppercase"),
            ("1abc123", True, "a normal plate with all lowercase"),
            ("1aBc123", True, "a normal plate with mixed case"),
            ("1234567", True, "all numbers"),

            # Non-matching test cases.
            ("abcdefg", False, "all letters"),
            ("", False, "empty"),
            ("1ABC12", False, "too short"),
            ("zABC123", False, "bad starting character"),
            ("1ABC12z", False, "bad ending character"),
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
            ('code_z = "z987"', True, "variable ending with a letter, code starting with a letter"),
            ('code_Z = "Z987"', True, "uppercase in variable and code"),
            ('code_1 = "0987"', True, "variable ending with a digit, code starting with a digit"),
            ('code__ = "0987"', True, "variable ending with an underscore"),
            ('code_a = "_123"', True, "code starting with an underscore"),

            # Non-matching test cases.
            ('a = "a123"', False, "variable does not start with standard prefix"),
            ('code_a = "123"', False, "code does not start with prefix"),
            ('code_a = "a1"', False, "code too short"),
            ('code_ = "a134"', False, "variable too short"),
            ('code_a = "abcd"', False, "code only letters"),
            ('code_a\t=\t"a123"', False, "non-space characters used"),
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
            ('code_z = "z987"', True, "variable ending with a letter, code starting with a letter"),
            ('code_z = "Z987"', True, "code starting with an uppercase letter"),
            ('code_a\t=\t"a123"', True, "non-space characters used"),
            ('code_a =\t"a123"', True, "one space and one tab"),
            ('code_a\t= "a123"', True, "one tab and one space"),
            ('code_a = "0987"', True, "code starting with a digit"),

            # Non-matching test cases.
            ('code_a = "_123"', False, "code starting with an underscore"),
            ('code_Z = "Z987"', False, "uppercase in variable and code"),
            ('code__ = "0987"', False, "variable ending with an underscore"),
            ('code_1 = "0987"', False, "variable ending with a digit"),
            ('a = "a123"', False, "variable does not start with standard prefix"),
            ('code_a = "123"', False, "code does not start with prefix"),
            ('code_a = "a1"', False, "code too short"),
            ('code_ = "a134"', False, "variable too short"),
            ('code_a = "abcd"', False, "code only letters"),
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
            ('0x12.34', True, 'only numeric'),
            ('0xfe.dc', True, 'only alpha'),
            ('0x10.00', True, 'smallest possible value'),
            ('0xff.ff', True, 'largest possible value'),

            # Non-matching test cases.
            ('xff.ff', False, 'bad hex prefix'),
            ('0000xff.ff', False, 'junk at the beginning'),
            ('0xff.fffff', False, 'junk at the end'),
            ('0xff.f', False, 'too few places after the point'),
            ('0xff', False, 'not float'),
            ('0xffff', False, 'no point'),
            ('0x12.AB', False, 'uppercase'),
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
            ('0x12.34', True, 'only numeric'),
            ('0xfe.dc', True, 'only alpha'),
            ('0x0', True, 'fewest numeric digits'),
            ('0xf', True, 'fewest alpha digits'),
            ('0x123456789.abcdef', True, 'long number'),
            ('0x0001.0000000', True, 'lots of zeros'),
            ('0x12.', True, 'trailing point'),

            # Non-matching test cases.
            ('xff.ff', False, 'bad hex prefix'),
            ('zzz0xff.ff', False, 'junk at the beginning'),
            ('0xff.ffzzz', False, 'junk at the end'),
            ('0x12.AB', False, 'uppercase'),
            ('0x12.34.', False, 'extra point'),
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
            ('code_z = "z987"', 'code_z987 = "z987"', "code starting with a lowercase letter"),
            ('code_z = "Z987"', 'code_Z987 = "Z987"', "code starting with an uppercase letter"),
            ('code_a\t=\t"a123"', 'code_a123 = "a123"', "non-space characters used"),
            ('code_a =\t"a123"', 'code_a123 = "a123"', "one space and one tab"),
            ('code_a\t= "a123"', 'code_a123 = "a123"', "one tab and one space"),
            ('code_a = "0987"', 'code_0987 = "0987"', "code starting with a digit"),
        ]

        for (target, expected, feedback) in test_cases:
            actual = re.sub(regex, replacement, target)

            if (actual != expected):
                message = "Missed test case: '%s'." % (feedback)
                self.add_message(message, add_score = -1)

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

def main():
    return autograder.cmd.gradeassignment.main()

if (__name__ == '__main__'):
    sys.exit(main())
