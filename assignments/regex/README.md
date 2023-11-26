# Assignment: Regular Expressions

This is an assignment to get students familir with [regular expressions](https://en.wikipedia.org/wiki/Regular_expression),
also known as "regex" or "regexp".

## Jupyter Lab

This specific assignment will use an iPython notebook.
Notebooks are not required for using Python or the autograder,
but can be useful for some assignment setups.



In this course most your assignments will be distributed in the form of iPython notebooks,
and we encourage you to work with them through [Jupyter Lab](https://jupyter.org/).
iPython notebooks, "notebooks" for short, let you write Python code in an interactive environment that
can display visual elements like images and graphs.

Unfortunately, notebooks are not intended to be edited directly like most source code files.
So, we will be using Jupyter Lab to work with our notebooks.
When we run Jupyter Lab, it will open a session in a web browser that allows us to edit and view our notebooks.

For a tutorial on iPython notebooks with Jupyter Lab, see:
 - [Text Tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
 - [Video Tutorial](https://www.youtube.com/watch?v=HW29067qVWk)

## Grader

Graders are classes that extend [autograder.assignment.Assignment](https://github.com/eriq-augustine/autograder-py/blob/main/autograder/assignment.py).

Take in a submission and grade.

Most simply, can behave like a unit test.
But good graders are deeper.
Partial credit.
Good Feedback.

### Local

optional, but recommended
(especially for courses that limit the number of submissions)

### Remote

Running locally

## Submitting Your Assignment

Config



**Edit config.json**

Open up `config.json` and put your information in there:
    - `course` -- The current course you are enrolled in (already set).
    - `assignment` -- The current assignment you are working on (already set).
    - `server` -- The autograding server to submit assignment to (already set).
    - `user` -- Your username (email) for the autograder.
    - `pass` -- The password that was emailed to you in the beginning of this course.
                    If you didn't get the password, forgot it, etc; talk to a TA.

For example, Sammy Slug would have a `config.json` for HO0 that looks like:
```json
{
    "course": "CSE40",
    "assignment": "HO0",
    "server": "http://lighthouse.soe.ucsc.edu",
    "user": "sslug@ucsc.edu",
    "pass": "1234567890"
}
```

```sh
python3 -m autograder.cli.submission.submit assignment.ipynb
```

## Writing New Test Cases
