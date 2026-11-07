# Lab 1 — Code quality tools and CI

The code is adapted from [karpathy/micrograd](https://github.com/karpathy/micrograd/blob/master/micrograd/engine.py), copyright (c) 2020 Andrej Karpathy, MIT license. See `LICENSE`.

## Purpose

Add automated code quality tools to an existing Python module: Ruff linter and formatter, Pyright type checking, Makefile shortcuts, Git hooks and GitHub Actions.

## Setup

Requirements: Python 3.11+, pip, Git and GNU Make.

```bash
python -m pip install -e ".[dev]"
make fulltest
make precommit
```

On Windows, GNU Make must be installed separately (for example via MSYS2 or Git Bash with make available). The equivalent checks can always be run directly:

```bash
python -m ruff check .
python -m ruff format --check .
python -m pyright
python -m unittest discover -s tests -v
```

To format: `make format`. To install hooks: `make precommit`. Hooks check Ruff before commit; Ruff, Pyright, and tests before push.

## GitHub Actions (bonus)

`.github/workflows/quality.yml` runs lint, formatting, type checking, and unit tests on PRs and pushes to `main`. **To prove the bonus works, publish the project, open a PR, and provide a screenshot of the successful Actions run.** A workflow file alone is not proof of a successful run.

## Original project

Original project URL: https://github.com/karpathy/micrograd

Original file: https://github.com/karpathy/micrograd/blob/master/micrograd/engine.py

Changes: introduced explicit Python typing, Ruff-compatible formatting, Pyright configuration, tests, Makefile, Git hooks and CI. Keep the original link in the Pull Request description when submitting.
