CD = $(shell pwd)
DATE = 201306
# define the name of the virtual environment directory
VENV := .venv

# default target, when make executed without arguments
default: fill_db clean

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate
	  echo "....Creating virtual enviroment...."
	  

ingest: venv
	 	python3 ${CD}/proyect1/src/donwload_zip.py $(DATE)
		python3 ${CD}/proyect1/src/unzip.py $(DATE)
		echo "....Ingesting Data...."
		

pipeline: ingest
		  python3 ${CD}/proyect1/src/clean_data.py $(DATE)
		  echo "....Cleaning Data...."
		  

fill_db: pipeline
		 python3 ${CD}/proyect1/db/fill_db.py $(DATE)
		 echo "....Filling DB...."


clean:
	rm -rf ${CD}/lake/
	

.PHONY: default venv run clean
