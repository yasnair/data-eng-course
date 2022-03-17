
from distutils.log import ERROR
from http.client import OK
from psycopg2 import connect, sql
import sys, os
from decouple import config
from datetime import date
from zipfile import ZipFile


def get_db_connect():
    # instantiate a cursor object from the connection
    try:

        # declare a new PostgreSQL connection object
        conn = connect (
            dbname = "trip",
            user = "postgres",
            host = "localhost",
            password = "postgres"
        )
        
        # attempt to create a cursor object
        cursor = conn.cursor()

    except Exception as err:
        # set the cursor to None if exception
        cursor = None
        print ("\npsycopg2 error:", err)

    return conn, cursor

def get_dir(dirName):
    # Create target directory & all intermediate directories if don't exists
    actual_dir= os.getcwd()
    new_path = os.path.join(actual_dir, dirName)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        print("Directory " , new_path,  " Created ")

    return dirName

def get_date_to_run():
    try:
        date_to_run = sys.argv[1]
    except IndexError:   
        date_to_run = date.today().year + date.today().month
    return date_to_run

def unzip_file(dir_originfiles, dir_processedfiles,date_to_run):
    filename = f'{date_to_run}-citibike-tripdata.zip'
    filepath = os.path.join(dir_originfiles , filename)
    try:

        with ZipFile(filepath, 'r') as zipObj:
            # Extract all the contents of zip file in different directory
            zipObj.extractall(dir_processedfiles)
        return OK, filepath

    except:
        return ERROR, ''
