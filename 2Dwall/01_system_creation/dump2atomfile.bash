#!/usr/bin/env bash

set -euo pipefail

dump="${1}"

sed -n '4p;10,$p' "${dump}"

