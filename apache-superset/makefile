include .env
export
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip
SUPERSET := $(VENV_DIR)/bin/superset
ADMIN_USER := admin
ADMIN_PASSWORD := admin

.PHONY: all venv install init setup load_backup load_examples store_backup start clean_venv clean_all

all: venv install init setup start

venv:
	@test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)

install: venv
	$(PIP) install --upgrade pip setuptools wheel; \
	$(PIP) install -r requirements.txt

init: venv
	$(SUPERSET) db upgrade; \
	$(SUPERSET) init

setup: init venv
	$(SUPERSET) fab create-admin --username $(ADMIN_USER) --firstname admin --lastname admin --email admin@admin.com --password $(ADMIN_PASSWORD)

load_examples: venv init
	$(SUPERSET) load_examples;

load_backup: venv init
	$(SUPERSET) fab create-admin --username $(ADMIN_USER) --firstname admin --lastname admin --email admin@admin.com --password $(ADMIN_PASSWORD)
	$(SUPERSET) import-dashboards --dashboard-file $(SUPERSET_BACKUP);

store_backup: venv init
	$(SUPERSET) export-dashboards --dashboard-file $(SUPERSET_BACKUP);

start: init venv
	$(SUPERSET) run -p $(SUPERSET_PORT) --with-threads --reload --debugger

clean_venv:
	rm -rf $(VENV_DIR)

clean_all:
	rm -rf $(VENV_DIR)
	rm -rf $(SUPERSET_HOME)