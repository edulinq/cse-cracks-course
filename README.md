# CSE Cracks -- A Course for Filling in the Missing Cracks in CSE Curriculums

The CSE Cracks course tries to fill some of the gaps in tooling and knowledge present in most CSE curriculums.
This course is inspired by (and in no way a replacement for) [MIT's Missing Semester](https://missing.csail.mit.edu/).

Additionally, this repository serves as an example for courses that use the [autograder](https://github.com/eriq-augustine/autograder-server) system.

## Autograder Courses

Autograder courses are defined by a [course.json](course.json) file.
This file has some configuration information
and tells the autograder that the directory containing it is an autograder course directory.
The autograder will then recursively search the course directory for any `assignment.json` files.

Here are some links that you will find useful when learning about the autograder:
 - [Autograder Server](https://github.com/eriq-augustine/autograder-server)
 - [Autograder Python Interface](https://github.com/eriq-augustine/autograder-server)

### Sample Assignments

This sample course contains a sample assignment in the [assignments](assignments) directory.
