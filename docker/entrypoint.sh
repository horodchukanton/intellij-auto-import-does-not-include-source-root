#!/usr/bin/env bash
EGGDIR="app.egg-info"
if [ -d "$EGGDIR" ]; then
    rm -rf ${EGGDIR}
fi
pip install -q -e .
"$@"  # execute command passed to script
