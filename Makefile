CD = $(shell pwd)
DATE = 201306
# define the name of the virtual environment directory
VENV := .venv

# default target, when make executed without arguments
default: venv ingest pipeline fill_db

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

ingest: venv
	 	python3 ${CD}/proyect1/src/donwload_zip.py $(DATE)
		python3 ${CD}/proyect1/src/unzip.py $(DATE)


pipeline: venv
		python3 ${CD}/proyect1/src/process_raw_data.py $(DATE)

fill_db: venv
		 python3 ${CD}/proyect1/db/src/fill_db.py

.PHONY: default venv run clean
