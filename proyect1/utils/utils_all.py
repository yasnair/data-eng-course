

import pandas as pd
import sys, os
from decouple import config
from datetime import datetime
from zipfile import ZipFile
import psycopg2
from psycopg2 import OperationalError
  
# Create target directory & all intermediate directories if don't exists
def get_dir(dirName:str):
    actual_dir= os.getcwd()
    new_path = os.path.join(actual_dir, dirName)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        print("Directory " , new_path,  " Created ")

    return dirName

#Given a filename returns the filepath
def get_path_file(filename:str):
    for root, dirs, files in os.walk(os.getcwd()):
        for name in files:
            if name == filename:
                return os.path.abspath(os.path.join(root, name))

#Get the date to execute the process. 
def get_date_to_run():
    try:
        date_to_run = sys.argv[1]
    except IndexError:   
        now = datetime.now() # current date and time
        date_to_run = now.strftime("%Y") + now.strftime("%m")
    return date_to_run

#check if a file exists
def file_exist(path: str, pattern: str): 
    files = list(filter(lambda x: pattern in x, os.listdir(path)))
    if files:
        return True
    else:
         return False
'''
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
            
'''