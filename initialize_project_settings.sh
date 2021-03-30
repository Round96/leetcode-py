#!/bin/sh

pip3 install --upgrade -r requirements.list

echo "#/bin/sh\nmake" > .git/hooks/pre-commit