#!/usr/bin/env bash

set -e

SCRIPT_DIR_NAME="$( cd "$( dirname "$0" )" && pwd )"

if [ $# != 1 ]; then
    echo "usage: $(basename "$0") <release-branch>" >&2
    exit 1
fi

RELEASE_BRANCH=${1:-}

pushd "$SCRIPT_DIR_NAME"

sed -i "" -e \
    "s|?branch=master|?branch=$RELEASE_BRANCH|g" \
    "README.md"

build_readme_dot_rst.sh
build_python_package.sh

popd

exit 0
