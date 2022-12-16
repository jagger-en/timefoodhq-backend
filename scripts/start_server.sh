#!/bin/bash

set -eu

ROOT_DIR=$(dirname $(dirname "$0"))
PYTHONPATH=${ROOT_DIR}/src ${ROOT_DIR}/src/backend/server.py
