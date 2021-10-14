.DEFAULT_GOAL := all
isort = isort foran tests
black = black -S -l 120 --target-version py39 foran tests

.PHONY: install
install:
	pip install -U pip wheel
	pip install -r tests/requirements.txt
	pip install -U .

.PHONY: install-all
install-all: install
	pip install -r tests/requirements-dev.txt

.PHONY: isort
format:
	$(isort)
	$(black)

.PHONY: lint
lint:
	python setup.py check -ms
	flake8 foran/ tests/
	$(isort) --check-only --df
	$(black) --check --diff

.PHONY: mypy
mypy:
	mypy foran

.PHONY: test
test:
	pytest --cov=foran --log-format="%(levelname)s %(message)s"

.PHONY: testcov
testcov: test
	@echo "building coverage html"
	@coverage html

.PHONY: all
all: lint mypy testcov

.PHONY: fixtures
fixtures:
	mkdir -p tests/fixtures/non_remote && cd tests/fixtures/non_remote && git init && git branch -m default && touch emptiness && git add emptiness && git commit -m "Void"

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf .cache
	rm -rf htmlcov
	rm -rf *.egg-info
	rm -f .coverage
	rm -f .coverage.*
	rm -rf build
	rm -rf tests/fixtures/non_remote
	rm -f foran-eller-bagved.*
	python setup.py clean
