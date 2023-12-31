#!/bin/bash

# Parse and render all the quizzes.

readonly THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
readonly BASE_DIR="${THIS_DIR}/.."
readonly QUIZ_DIR="${BASE_DIR}/quizzes"

readonly TEMP_DIR='/tmp/csei123/__quizgen_check__'

readonly FORMATS='json tex'

function main() {
    if [[ $# -ne 0 ]]; then
        echo "USAGE: $0"
        exit 1
    fi

    trap exit SIGINT

    mkdir -p "${TEMP_DIR}"

    local error_count=0
    for path in $(find "${QUIZ_DIR}" -type f -name 'quiz.json' | sort) ; do
        for format in ${FORMATS} ; do
            echo "Rendering '${path}' to '${format}'."
            local out_path="${TEMP_DIR}/$(basename $(dirname "${path}")).${format}"

            python3 -m quizgen.cli.parse-quiz "${path}" --flatten-groups --format "${format}" > "${out_path}"
            if [[ $? -ne 0 ]] ; then
                echo "ERROR: Failed to render '${path}' with format '${format}'."
                ((error_count++))
            fi
        done
    done

    rm -rf "${TEMP_DIR}"

    if [[ ${error_count} -gt 0 ]] ; then
        echo "Found ${error_count} errors with quiz rendering."
    else
        echo "Found no quiz rendering issues."
    fi

    return ${error_count}
}

[[ "${BASH_SOURCE[0]}" == "${0}" ]] && main "$@"
