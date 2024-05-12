.PHONY: install
install:
	python3 -m venv venv && source venv/bin/activate && python -m pip install . && python -m pip install ".[test,lint]"

.PHONY: lint
lint:
	flake8 src

.PHONY: test
test:
	tox

.PHONY: build
build:
	python3 -m pip install --upgrade build
	python3 -m build

.PHONY: upload
upload: build test lint
	python3 -m pip install --upgrade twine
	python3 -m twine upload --repository testpypi dist/*
