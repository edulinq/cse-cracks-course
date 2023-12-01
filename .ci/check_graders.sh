#!/bin/bash

readonly THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
readonly BASE_DIR="${THIS_DIR}/.."

function check_grader() {
    local assignment_dir="${1}"

    local assignment_path="${assignment_dir}/assignment.json"
    local submissions_dir="${assignment_dir}/test-submissions"

    python -m autograder.cli.testing.test-submissions -a "${assignment_path}" -s "${submissions_dir}"
    local error_count=$?

    if [[ ${error_count} -gt 0 ]] ; then
        echo "ERROR: Grader test failed for assignment: '${assignment_dir}'."
    fi

    return ${error_count}
}

function check_assignments() {
    local error_count=0

    for assignment_dir in "${BASE_DIR}/assignments/"* ; do
        echo "Checking grader for assignment: '${assignment_dir}'."
        check_grader "${assignment_dir}"
        ((error_count += $?))
    done

    return ${error_count}
}

function main() {
    if [[ $# -ne 0 ]]; then
        echo "USAGE: $0"
        exit 1
    fi

    trap exit SIGINT

    local error_count=0

    check_assignments
    error_count=$?

    if [[ ${error_count} -gt 0 ]] ; then
        echo "Found ${error_count} grader issues."
    else
        echo "No grader issues found."
    fi

    return ${error_count}
}

[[ "${BASH_SOURCE[0]}" == "${0}" ]] && main "$@"
