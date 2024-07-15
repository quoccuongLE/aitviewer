#!/bin/bash
VENV_DIR=${1:-".venv/aitviewer"}
if [ -f lock.conda.yaml ]; then
    conda env create -f lock.conda.yaml --prefix $VENV_DIR
else
    conda env create -f conda.yaml --prefix $VENV_DIR
    # $VENV_DIR/bin/python -m pip install -e ../star/
fi
