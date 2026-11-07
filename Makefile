.PHONY: install run lint format formatcheck typecheck test fullcheck fulltest precommit

PYTHON ?= python

install:
	$(PYTHON) -m pip install -e ".[dev]"

run:
	$(PYTHON) -m unittest discover -s tests -v

lint:
	$(PYTHON) -m ruff check .

format:
	$(PYTHON) -m ruff format .

formatcheck:
	$(PYTHON) -m ruff format --check .

typecheck:
	$(PYTHON) -m pyright

test:
	$(PYTHON) -m unittest discover -s tests -v

fullcheck: lint formatcheck typecheck

fulltest: fullcheck test

precommit:
	$(PYTHON) -m pre_commit install --hook-type pre-commit --hook-type pre-push
