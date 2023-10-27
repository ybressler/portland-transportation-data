# Because some folks 'round here use a different SHELL:
export SHELL=/bin/bash

# the most important line in any shell script (exit on uncaught errors)
SHELL := $(SHELL) -e

## Since we do not actually compile anything, the builtin rules just clutter debugging
MAKEFLAGS += --no-builtin-variables
MAKEFLAGS += --no-builtin-rules

pip_version=22.2.2
poetry_version=1.3.2

default:: help

.PHONY : help
# Magic help adapted: from https://gitlab.com/depressiveRobot/make-help/blob/master/help.mk (MIT License)
help:
	@printf "Available targets:\n\n"
	@awk -F: '/^[a-zA-Z\-_0-9%\\ ]+:/ { \
			helpMessage = match(lastLine, /^## (.*)/); \
			if (helpMessage) { \
					helpCommand = $$1; \
					helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
					printf "  \x1b[32;01m%-35s\x1b[0m %s\n", helpCommand, helpMessage; \
			} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST) | sort -u
	@printf "\n"


# ---------------

homebrew-installed: /usr/local/bin/brew;

/usr/local/bin/brew:
	@/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Confirm essential tools are installed, install them if not
essential-tools: homebrew-installed
	@which pre-commit || (brew install pre-commit && pre-commit install)

# Install requisite python tools
py-libs:
	pip install pip==$(pip_version)
	pip install poetry==$(poetry_version)

.PHONY: setup

## Install all python library dependencies
setup:
	poetry install
