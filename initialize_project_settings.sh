#!/bin/sh

pip install -r requirements.list

echo "#/bin/sh\nmake" > .git/hooks/pre-commit