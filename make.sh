#!/bin/bash
virtualenv --distribute --no-site-packages venv
source venv/bin/activate
pip install -r beltbadgers_com/etc/requirements.txt