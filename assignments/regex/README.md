# Assignment: Regular Expressions

This is an assignment to get students familiar with [regular expressions](https://en.wikipedia.org/wiki/Regular_expression),
also known as "regex" or "regexp".

## Jupyter Lab

This specific assignment will use an iPython notebook.
Notebooks are not required for using Python or the autograder,
but can be useful for some assignment setups.

## Grader

Graders are classes that extend [autograder.assignment.Assignment](https://github.com/eriq-augustine/autograder-py/blob/main/autograder/assignment.py).
Their task is to look at a student's submission, assign a score, and give feedback to the student.
The default grader for Python should be called [grader.py](grader.py).
More complex or custom grading is possible in the autograder system,
custom graders just need to produce a JSON file (result.json) that describes the outcome of grading.

The most simple version of a grader is essentially a unit test,
where different cases are tested and it raises an exception on the first failure (or assertion error).
However, good graders will usually a little deeper and incorporate the following aspects:
 - Test all test cases, even if earlier ones fail.
 - Test empty cases.
 - Check types.
 - Assign partial credit relative to the amount of effort.
 - Give feedback for each test case that is specific enough to help the student,
   but general enough to not give away the solution.
   Ideally, a student should be able to make their own test case from the feedback.

Coming up with good feedback is typically the hardest part of writing graders.

The grader can be run locally using:
```sh
./grader.py -s test-submissions/solution
```

Note that the grader accepts vanilla Python files and iPython notebooks.

### Local

An optional component of an assignment is a local grader.
Local graders are a grader that will be given to the students and contain simple test cases.

Local graders serve a few main purposes:
 - Let the students run basic tests without sending a submission to the autograder.
   - This can be especially useful if your grader checks style.
 - Gives the students a place to write their own test cases without needing to write any surrounding infrastructure.
 - Give a place to check types before being sent to the autograder (which can avoid confusing errors).
 - Lets the students see the actual infrastructure (and output) that they will be graded with.

In this assignment, the local grader is in [local_grader.py](local_grader.py).

The local grader can be run using:
```sh
./grader.py test-submissions/solution
```

## Submitting Your Assignment

Before submitting an assignment to the autograder,
you need to ensure that the proper configuration is in place,
e.g., server, course, assignment, etc.
All configuration options can be set directly on the command line,
but it is usually easier to have most/all of the options pre-set in a config file.
The [autograder documentation](https://github.com/eriq-augustine/autograder-py/blob/main/README.md#configuration)
goes into detail on how to set options.
It is recommended that you distribute a basic configuration with each assignment that students can just copy and override with their own information.
In this assignment, that is [config.json](config.json).

With the config in place, you can submit an assignment with:
```sh
python3 -m autograder.run.submit assignment.ipynb
```

To check your most resent submission, you can use:
```sh
python3 -m autograder.run.peek
```

Or to check all your past submission, you can use:
```sh
python3 -m autograder.run.history
```

## Test Submissions

Testing graders is strongly encouraged.

One way to test graders is by using [test-submissions](test-submissions).
A test submission is a directory that contains all the code a student would submit (in whatever expected directory structure)
and a `test-submssion.json` file that defines the expected grading result.

You can test an assignment against all your test submissions using the `autograder.cli.testing.test-submissions` tool:
```sh
python3 -m autograder.cli.testing.test-submissions -a assignment.json -s test-submissions
```

Testing your graders is a great thing to put in continuous integration for your course.

To create a new `test-submission.json` file, you can just use the grader with the `-t` / `--test-submission-path` argument:
```sh
./grader.py -s test-submissions/solution -t test-submissions/solution
```

This will create [test-submissions/solution/test-submission.json](test-submissions/solution/test-submission.json).

For any test case where the output cannot be string compared
(like if it uses random numbers, times, or absolute paths (*such as the style checker*)),
you can set `ignore_message` to true.
You can see this in action in the [bad-style test submission](test-submissions/bad-style/test-submission.json).
