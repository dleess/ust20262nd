#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 msa_lab.py --self-test
python3 msa_lab.py "$@"
