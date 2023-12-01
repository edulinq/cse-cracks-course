#!/bin/bash

readonly THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
readonly BASE_DIR="${THIS_DIR}/.."

# Just run the local tests on all the submissions to make sure nothing crashes.
function check_local_grader() {
    local assignment_dir="${1}"

    local error_count=0
    local local_grader_path="${assignment_dir}/local_grader.py"
    local submissions_dir="${assignment_dir}/test-submissions"

    for submission_path in "${submissions_dir}"/*/*.py ; do
        if [[ ! -f "${submission_path}" ]] ; then
            continue
        fi

        echo "Testing local submission: ${submission_path}"

        "${local_grader_path}" "${submission_path}" > /dev/null
        local result=$?

        if [[ $result -ne 0 ]] ; then
            ((error_count += $result))
            echo "ERROR: Failed to run local grader (${local_grader_path}) on submission (${submission_path})."
        fi
    done

    return ${error_count}
}

function check_assignments() {
    local error_count=0

    for assignment_dir in "${BASE_DIR}/assignments/"* ; do
        echo "Checking local grader for assignment: '${assignment_dir}'."
        check_local_grader "${assignment_dir}"
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
        echo "Found ${error_count} local grader issues."
    else
        echo "No local grader issues found."
    fi

    return ${error_count}
}

[[ "${BASH_SOURCE[0]}" == "${0}" ]] && main "$@"
