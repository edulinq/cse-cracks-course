# Quizzes

This directory contains quizzes (Canvas and paper) for CSE Cracks course.
These quizzes serve the dual purposes of being real educating tools,
and being samples for using the [Quiz Generator](https://github.com/eriq-augustine/quizgen).

These quizzes are created in a neutral Markdown-like format that can be converted to
Canvas quizzes, raw HTML quizzes (using form submission), and Gradescope-compatible Tex/PDF quizzes.
Keeping quizzes in a textual format like this has the advantage of working well with source control
and allowing "write-once" quizzes that do not need to be re-written for different formats.
Additionally, the quiz generator tool can be run during CI to verify that all quizzes parse and generate properly.

## Commands

Below are some useful commands for working with these quizzes with the quiz generator.
The full reference for all these commands live at the [quiz generator repo](https://github.com/eriq-augustine/quizgen).

### Uploading a Quiz to Canvas

To upload a quiz to Canvas, the `quizgen.cli.upload-quiz` module can be used.
The basic usage is as follows:
```
python3 -m quizgen.cli.upload-quiz regex/quiz.json --course <canvas course id> --token <canvas access token>
```

If an existing quiz with the same name is found, then nothing will be uploaded unless the `--force` flag is given..

### Parsing a Specific Quiz

To parse an entire specific quiz, you can use the `quizgen.cli.parse-quiz` module.
This is useful if you want to check if a quiz properly parses.
The basic usage is as follows:
```
python3 -m quizgen.cli.parse-quiz regex/quiz.json
```

This command will output the fully parsed quiz in for format controlled by the `--format` option,
and will exit with a non-zero status if the parse failed.
Parsing a quiz is particularly useful in CI to ensure that all course quizzes are properly maintained.

### Parsing a Specific Question

To parse a specific quiz question, you can use the `quizgen.cli.parse-question` module.
This is useful if you want to check if a question properly parses.
The basic usage is as follows:
```
python3 -m quizgen.cli.parse-question regex/questions/basic-01/question.json
```

This command will output the fully parsed question in the JSON format,
and will exit with a non-zero status if the parse failed.

### Parsing a Specific File

To parse a specific file, you can use the `quizgen.cli.parse-file` module.
This is useful if you want to check if/how a specific document parses.
The basic usage is as follows:
```
python3 -m quizgen.cli.parse-file regex/questions/golf/golf-01/prompt.md
```

This command will output the fully parsed file in for format controlled by the `--format` option,
and will exit with a non-zero status if the parse failed.
This can be used to parse prompt markdown files.
