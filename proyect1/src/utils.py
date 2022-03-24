

import pandas as pd
import sys, os
from decouple import config
from datetime import datetime
from zipfile import ZipFile
import psycopg2
from psycopg2 import OperationalError
  

def get_dir(dirName):
    # Create target directory & all intermediate directories if don't exists
    actual_dir= os.getcwd()
    new_path = os.path.join(actual_dir, dirName)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        print("Directory " , new_path,  " Created ")

    return dirName

def get_path_file(filename):
    for root, dirs, files in os.walk(os.getcwd()):
        for name in files:
            if name == filename:
                return os.path.abspath(os.path.join(root, name))

def get_date_to_run():
    try:
        date_to_run = sys.argv[1]
    except IndexError:   
        now = datetime.now() # current date and time
        date_to_run = now.strftime("%Y") + now.strftime("%m")
    return date_to_run

def unzip_file(dir_originfiles, dir_processedfiles,date_to_run):
    filename = f'{date_to_run}-citibike-tripdata.zip'
    filepath = os.path.join(dir_originfiles , filename)
    try:

        with ZipFile(filepath, 'r') as zipObj:
            # Extract all the contents of zip file in different directory
            zipObj.extractall(dir_processedfiles)
        return 'OK', filepath

    except:
        return 'ERROR', ''

def file_exist(path: str, pattern: str): 
    files = list(filter(lambda x: pattern in x, os.listdir(path)))
    if files:
        return True
    else:
         return False

def connect(conn_params_dic):
    conn = None
    try:
        print('Connecting to the PostgreSQL...........')
        conn = psycopg2.connect(**conn_params_dic)
        print("Connection successfully..................")
        
    except OperationalError as err:
        # passing exception to function
        show_psycopg2_exception(err)        
        # set the connection to 'None' in case of error
        conn = None
    return conn

# Define a function that handles and parses psycopg2 exceptions
def show_psycopg2_exception(err):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()    
    # get the line number when exception occured
    line_n = traceback.tb_lineno    
    # print the connect() error
    print ("\npsycopg2 ERROR:", err, "on line number:", line_n)
    print ("psycopg2 traceback:", traceback, "-- type:", err_type) 
    # psycopg2 extensions.Diagnostics object attribute
    print ("\nextensions.Diagnostics:", err.diag)    
    # print the pgcode and pgerror exceptions
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")  
            
