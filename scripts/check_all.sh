#!/bin/bash

# Run all the checks we would run in CI in a single script.
# We don't call this script in CI so we can see each task broken out.

readonly THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

function main() {
    if [[ $# -ne 0 ]]; then
        echo "USAGE: $0"
        exit 1
    fi

    trap exit SIGINT

    local error_count=0

    "${THIS_DIR}/check_graders.sh"
    ((error_count += $?))

    "${THIS_DIR}/check_local_graders.sh"
    ((error_count += $?))

    "${THIS_DIR}/check_style.sh"
    ((error_count += $?))

    "${THIS_DIR}/check_notebook_output.sh"
    ((error_count += $?))

    "${THIS_DIR}/check_quizzes.sh"
    ((error_count += $?))

    if [[ ${error_count} -gt 0 ]] ; then
        echo "Found ${error_count} issues."
    else
        echo "No issues found."
    fi

    return ${error_count}
}

[[ "${BASH_SOURCE[0]}" == "${0}" ]] && main "$@"
