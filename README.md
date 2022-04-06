# data-eng-course
Data set: https://ride.citibikenyc.com/system-data.

Ingest: Wget/zipfile

Warehouse: Postgresql

Pipeline: Pandas

Dashboard: Falcon

Orchestration: Make file

## Prerequisites:
Install Postgresql 
https://www.postgresql.org/download/

## How to run
Open a terminal inside data-eng-course folder and run:
1) Run default initial date '201306'
```bash
 make default
```
2) Run custom date in AAAAMM format:
```bash
 make DATE=AAAAMM
```
## Dashboard
Open Falcon, connect with your DB and copy the query from:

https://github.com/yasnair/data-eng-course/blob/68ebe68598116b42a0088c626fe4fa6a849eaa45/proyect1/db/sql/querys.sql

