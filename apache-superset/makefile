VENV_DIR := /home/manfucci/github.com/amanfucci/sistemi-informativi/apache-superset/venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip
SUPERSET := $(VENV_DIR)/bin/superset
SUPERSET_DB := /home/manfucci/.superset
SECRET_KEY := not_a_secret
ADMIN_USER := admin
ADMIN_PASSWORD := admin

.PHONY: all venv install load_examples init create-admin start clean

all: venv install init load_examples create-admin start

venv:
	@test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)

install: venv
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install -r requirements.txt

load_examples: init venv
	@export FLASK_APP=superset; \
	export SUPERSET_SECRET_KEY=$(SECRET_KEY); \
	$(SUPERSET) db upgrade; \
	$(SUPERSET) load_examples; \
	$(SUPERSET) init

init: venv
	@export FLASK_APP=superset; \
	export SUPERSET_SECRET_KEY=$(SECRET_KEY); \
	$(SUPERSET) db upgrade; \
	$(SUPERSET) init

create-admin: init venv
	@export FLASK_APP=superset; \
	export SUPERSET_SECRET_KEY=$(SECRET_KEY); \
	$(SUPERSET) fab create-admin --username $(ADMIN_USER) --firstname admin --lastname admin --email admin@admin.com --password $(ADMIN_PASSWORD)

start: init venv
	@export FLASK_APP=superset; \
	export SUPERSET_SECRET_KEY=$(SECRET_KEY); \
	$(SUPERSET) run -p 8088 --with-threads --reload --debugger

clean:
	rm -rf $(VENV_DIR)
	rm -rf $(SUPERSET_DB)
