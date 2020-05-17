.PHONY: init
init:
	test -d _venv || \
	python3 -m venv _venv && \
	source _venv/bin/activate && \
	pip install -U pip

.PHONY: reqs
reqs:
	source _venv/bin/activate && \
	pip install -r requirements.txt

.PHONY: test
test:
	py.test --cov-report term-missing --cov-report xml --cov sphinxcontrib --cov-config tox.ini {posargs:tests}
