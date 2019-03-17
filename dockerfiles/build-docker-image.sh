#!/usr/bin/env bash

set -e

SCRIPT_DIR_NAME="$( cd "$( dirname "$0" )" && pwd )"

if [ $# != 2 ]; then
    echo "usage: $(basename "$0") <dist-tar-gz> <image-name>" >&2
    exit 1
fi

DIST_TAR_GZ=${1:-}
IMAGE_NAME=${2:-}

CONTEXT_DIR=$(mktemp -d 2> /dev/null || mktemp -d -t DAS)

cp "$DIST_TAR_GZ" "$CONTEXT_DIR/dev_env_testing.tar.gz"
docker build -t "$IMAGE_NAME" --file "$SCRIPT_DIR_NAME/Dockerfile" "$CONTEXT_DIR"

rm -rf "$CONTEXT_DIR"

exit 0
