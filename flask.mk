# VERSION=1.0.0

VE ?= ./ve
MANAGE ?= ./manage.py
SYS_PYTHON ?= python3
PY_SENTINAL ?= $(VE)/sentinal
WHEEL_VERSION ?= 0.33.4
PIPENV_VERSION ?= 2018.11.26
MAX_COMPLEXITY ?= 10
INTERFACE ?= localhost
RUNSERVER_PORT ?= 8000
PY_DIRS ?= $(APP)

# Travis has issues here. See:
# https://github.com/travis-ci/travis-ci/issues/9524
ifeq ($(TRAVIS),true)
	BANDIT ?= bandit
	FLAKE8 ?= flake8
	PIPENV ?= pipenv
else
	BANDIT ?= $(VE)/bin/bandit
	FLAKE8 ?= $(VE)/bin/flake8
	PIPENV ?= $(VE)/bin/pipenv
endif

$(PY_SENTINAL):
	rm -rf $(VE)
	$(SYS_PYTHON) -m venv $(VE)
	$(PIPENV) install pipenv==$(PIPENV_VERSION)
	$(PIPENV) install --upgrade setuptools
	$(PIPENV) install wheel==$(WHEEL_VERSION)
	$(PIPENV) install --no-deps --requirement $(REQUIREMENTS) --no-binary cryptography
	touch $@

flake8: $(PY_SENTINAL)
	$(FLAKE8) $(PY_DIRS) --max-complexity=$(MAX_COMPLEXITY) --exclude=*/migrations/*.py --extend-ignore=$(FLAKE8_IGNORE)

runserver: $(PY_SENTINAL)
	env FLASK_APP=hello.py flask run -h $(INTERFACE) -p $(RUNSERVER_PORT)

clean:
	rm -rf $(VE)
	find . -name '*.pyc' -exec rm {} \;

.PHONY: flake8 runserver clean
