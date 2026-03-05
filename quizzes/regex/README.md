# Regular Expressions Quiz

This is a fully functional quiz about regular expressions.
This quiz is a companion to the [Regular Expressions Assignment](/assignments/regex).

This quiz also serves as a good demonstration of the [Quiz Composer](https://github.com/edulinq/quiz-composer),
as it covers all the primary question types.

Questions for this quiz live in the [questions directory](./questions),
and the quiz itself is represented with the [quiz.json](./quiz.json) file.

A compiled PDF version of the quiz is available as [quiz.pdf](./quiz.pdf).

## Working with the Quiz

There are many things you can do with this quiz using the [Quiz Composer](https://github.com/edulinq/quiz-composer) Python library.
Here we will highlight a few of the commands.
See the repository for more specifics.

These commands all assume that you have the Quiz Composer installed
and are running the commands from this directory.

Compile to HTML:
```sh
python3 -m quizcomp.cli.parse.quiz quiz.json --format html > quiz.html
```

Compile to TeX:
```sh
python3 -m quizcomp.cli.parse.quiz quiz.json --format tex > quiz.tex
```

Create a PDF:
```sh
python3 -m quizcomp.cli.pdf.create quiz.json
```

Upload to Canvas:
```sh
python3 -m quizcomp.cli.canvas.upload quiz.json --course <canvas course id> --token <canvas access token>
```

Upload to GradeScope:
```sh
python3 -m quizcomp.cli.gradescope.upload quiz.json --course <course id> --user <username> --pass <password>
```
