#!/usr/bin/env python3

"""
Do a local practice grading.
The score you recieve here is not an actual score,
but gives you an idea on how prepared you are to submit to the autograder.
"""

import types
import os
import sys

import autograder.assignment
import autograder.question
import autograder.style

class HO0(autograder.assignment.Assignment):
    def __init__(self, **kwargs):
        super().__init__(
            name = 'Practice Grading for Hands-On 0',
            questions = [
                T1A(1, "Task 1.A (my_function)", 1),
                T2A(1, "Task 2.A (test_my_function_value)", 1),
                T2B(1, "Task 2.B (TestMyFunction)", 1),
                autograder.style.Style(kwargs.get('input_dir'), max_points = 0),
            ], **kwargs)

class T1A(autograder.question.Question):
    def score_question(self, submission):
        # We cal call your code using the submission object.
        result = submission.__all__.my_function()

        # Does the function return NotImplemented?
        if (self.check_not_implemented(result)):
            return

        # Does the function return a boolean?
        if (not isinstance(result, bool)):
            self.fail("Function must return a boolean value.")
            return

        # Add your code here.

        self.full_credit()

class T2A(autograder.question.Question):
    def score_question(self, submission):
        try:
            submission.__all__.test_my_function_value(4)
            self.fail("Function did not raise an exception on a bad value (4).")
        except Exception:
            self.full_credit()

class T2B(autograder.question.Question):
    def score_question(self, submission):
        question = submission.__all__.TestMyFunction(100, "Test my_function()")

        def my_bad_function():
            return False

        test_submission = types.SimpleNamespace(my_function = my_bad_function)
        result = question.grade(test_submission)

        if (result.score == 100):
            self.fail("Test class passed a function that returned a bad value (False).")
            return

        self.full_credit()

def main(path):
    assignment = HO0(input_dir = path)
    result = assignment.grade()
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
