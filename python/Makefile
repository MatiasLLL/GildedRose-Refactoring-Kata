.PHONY: install test lint typecheck check

install:
	poetry install

test:
	poetry run pytest -v

lint:
	poetry run ruff check . && poetry run ruff format --check .

typecheck:
	poetry run mypy gilded_rose.py

check: lint typecheck test
