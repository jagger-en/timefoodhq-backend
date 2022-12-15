#!/bin/bash

set -eu

echo "Linting ./src"
pylint --rcfile ./.pylintrc  ./src/**/*.py

echo "Linting ./tests"
pylint --rcfile ./.pylintrc  ./tests/**/*.py
