#!/usr/bin/env bash

set -eu

# TODO: place real preparations for your parser here

python3.8 -m venv venv
. venv/bin/activate

pip install -r requirements.txt
