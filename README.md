# CSE Cracks -- A Course for Filling in the Missing Cracks in CSE Curriculums

The CSE Cracks course tries to fill some of the gaps in tooling and knowledge present in most CSE curriculums.
This course is inspired by (and in no way a replacement for) [MIT's Missing Semester](https://missing.csail.mit.edu/).

Additionally, this repository serves as an example for courses that use the [autograder](https://github.com/edulinq/autograder-server) system.

## Autograder Courses

Autograder courses are defined by a [course.json](course.json) file.
This file has some configuration information
and tells the autograder that the directory containing it is an autograder course directory.
The autograder will then recursively search the course directory for any `assignment.json` files.

Here are some links that you will find useful when learning about the autograder:
 - [Autograder Server](https://github.com/edulinq/autograder-server)
 - [Autograder Python Interface](https://github.com/edulinq/autograder-py)

### Assignments

This course contains fully produced assignments that can be used for teaching in the [assignments](assignments) directory.
All assignments fall under the [licence used in this repo](LICENSE), and may be used freely.

### Sample Assignments

In addition to the real assignments, this repo also contains sample assignments that exist only as examples of autograder usage.
These assignments live in the [sample-assignments](sample-assignments) directory.
