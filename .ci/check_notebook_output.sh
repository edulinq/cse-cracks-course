#!/bin/bash

# Check all .ipynb files for output.

readonly THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
readonly BASE_DIR="${THIS_DIR}/.."

readonly TEMP_PATH='/tmp/csei123/__notebook_output_check__/test.ipynb'

function main() {
    if [[ $# -ne 0 ]]; then
        echo "USAGE: $0"
        exit 1
    fi

    trap exit SIGINT

    local tempDir="$(dirname "${TEMP_PATH}")"
    mkdir -p "${tempDir}"

    local error_count=0
    for path in $(find "${BASE_DIR}" -type f -name '*.ipynb' | sort) ; do
        if [[ "${path}" == *'.ipynb_checkpoints'* ]] ; then
            continue
        fi

        echo "Checking notebook for output: '${path}'."
        jupyter nbconvert --clear-output --output "${TEMP_PATH}" "${path}" > /dev/null 2> /dev/null
        if [[ $? -ne 0 ]] ; then
            echo "Could not remove output from notebook: '${path}'."
            ((error_count++))
            continue
        fi

        diff -q "${path}" "${TEMP_PATH}" > /dev/null
        if [[ $? -ne 0 ]] ; then
            echo "Found notebook with output: '${path}'."
            ((error_count++))
            continue
        fi
    done

    rm -rf "${tempDir}"

    if [[ ${error_count} -gt 0 ]] ; then
        echo "Found ${error_count} notebooks with output."
    else
        echo "Found no notebooks with output."
    fi

    return ${error_count}
}

[[ "${BASH_SOURCE[0]}" == "${0}" ]] && main "$@"
