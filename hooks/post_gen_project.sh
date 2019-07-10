#!/bin/bash

set -e

if [ -d {{ cookiecutter.ref_dir }} ]; then
    ln -s {{ cookiecutter.ref_dir }} ref/{{ cookiecutter.ref_name }}
else
    exit 1
fi
