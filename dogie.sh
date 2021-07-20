#!/bin/bash

if [ -d "doge_venv" ]; then
    if [ $OSTYPE = msys ]; then
        . ./doge_venv/Scripts/activate
        python dogie.py
    else
        . ./doge_venv/bin/activate
        python dogie.py
    fi
else
    echo "*** setting up virtual env ***"
    python3 -m venv doge_venv
    if [ $OSTYPE = msys ]; then
        . ./doge_venv/Scripts/activate
        pip install -r requirements.txt
        python dogie.py
    else
        . ./doge_venv/bin/activate
        pip install -r requirements.txt
        python dogie.py
    fi
fi

deactivate