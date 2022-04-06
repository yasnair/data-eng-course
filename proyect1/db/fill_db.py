import sys, os
sys.path.insert(1, f'{os.getcwd()}/proyect1/utils')
from parameters import DIM_TABLES_FILENAME, FOLDER_DATA_CLEANED, FIX_FILE_PATH, CONN_DB_DIC, DB_NAME
from psycopg2 import OperationalError
import pandas as pd
from io import StringIO
from utils_db import (
    connect, 
    show_psycopg2_exception,
    execute_sql_file

)
from utils_all import (
    get_dir,
    get_date_to_run,
    get_path_file
)

def load_raw_data():
    path            = get_dir(FOLDER_DATA_CLEANED)
    date_to_run     = get_date_to_run()
    filename        = os.getcwd() + '/' + path + date_to_run + FIX_FILE_PATH + '.csv' #File .csv

    if os.path.exists(filename):
        try:
            #Read file to process
            df = pd.read_csv(filename, index_col=False)
            df.head()
            print(len(df))
            
            conn_params_dic = CONN_DB_DIC
            conn_params_dic['database'] = DB_NAME
            conn = connect(conn_params_dic)
            conn.autocommit = True
            if conn!=None:
                # save dataframe to an in memory buffer
                buffer = StringIO()
                df.to_csv(buffer, header=False, index = False)
                buffer.seek(0)
                try:

                    cursor = conn.cursor()
                    cursor.execute('TRUNCATE TABLE rawdata;')
                    conn.commit()
                    print('Cleaning rawdata TABLE..........')
                    cursor.copy_from(buffer, 'rawdata', sep=",")

                    conn.commit()
                    print("Raw data loaded successfully..................")
                    # close the cursor object to avoid memory leaks
                    cursor.close()

                    # close the connection object
                    conn.close()
                    
                except OperationalError as err:
                    # pass exception to function
                    show_psycopg2_exception(err)
                    # set the connection to 'None' in case of error
                    conn = None
            
            
        except OperationalError as err:
            print(f'Error processing file {filename}')
            # pass exception to function
            show_psycopg2_exception(err)
            # set the connection to 'None' in case of error
            conn = None
    

def main():
    message_table       = "Data"
    load_raw_data()
    execute_sql_file(DIM_TABLES_FILENAME,  message_table)    

if __name__ == '__main__':
    main()
