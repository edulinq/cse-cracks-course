#!/usr/bin/env python3

import types
import sys

import autograder.assignment
import autograder.cmd.gradeassignment
import autograder.question
import autograder.style

class HO0(autograder.assignment.Assignment):
    def __init__(self, **kwargs):
        super().__init__(questions = [
            T1A(40, "Task 1.A (my_function)"),
            autograder.style.Style(kwargs.get('input_dir'), max_points = 0),
        ], **kwargs)

class T1A(autograder.question.Question):
    def score_question(self, submission):
        my_function = submission.__all__.my_function

        result = my_function()
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, bool)):
            self.fail("Function must return a boolean value.")
            return

        if (not result):
            self.fail("Function must return True.")
            return

        self.full_credit()

def main():
    return autograder.cmd.gradeassignment.main()

if (__name__ == '__main__'):
    sys.exit(main())
