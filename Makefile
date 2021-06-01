PYTHON_VERSION = 3.7


.PHONY: all
all: lint test

.PHONY: install
install: install_tools.sh
	sh install_tools.sh

.PHONY: lint-quiet
lint-quiet:
	find . -type f -not -path "./venv/*" -name "*.py" | tr "\n" " " | xargs autopep8 -ia

.PHONY: lint
lint:
	find . -type f -not -path "./venv/*" -name "*.py" | tr "\n" " " | xargs autopep8 -ia --exit-code

.PHONY: test
test:
	pytest tests -o log_cli=true -o log_cli_level="INFO"
