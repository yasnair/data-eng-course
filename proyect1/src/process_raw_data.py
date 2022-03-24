"""
- PROCESS RAW DATA:
    - Get file to process 
    - Clean data.
    - Load data into DB table 
"""

import os
import pandas as pd
from io import StringIO
from psycopg2 import OperationalError
from parameters import FIX_FILE_PATH, conn_params_dic, FOLDER_RAW_FILES
from utils import (
    get_dir,
    get_date_to_run,
    show_psycopg2_exception,
    connect
)



def copy_df(df):
   return df.copy()

#Delete rows with null values
def drop_missing(df):
    df.dropna(subset=['tripduration','starttime','stoptime','start station id','end station id', 'bikeid'], inplace=True)
    return df

#remove rows without sense 
def remove_outliers_dates(df, column_date_start, column_date_end):
    print('Removing outliers dates......')
    df[column_date_start] = pd.to_datetime(df[column_date_start],format='%Y/%m/%d %H:%M:%S')
    df[column_date_end] = pd.to_datetime(df[column_date_end],format='%Y/%m/%d %H:%M:%S')
    #get index of rows where starttime > stoptime
    index_del = df[df[column_date_start] > df[column_date_end]].index
    # drop these given row
    # indexes from dataFrame
    df.drop(index_del, inplace = True)
    return df

def convert_int_values(df, column_names):
    print('Converting INT values......')
    for column_name in column_names:
        df[column_name] = df[column_name].fillna(0)
        df[column_name]= df[column_name].astype(int)
    return df


def load_raw_data_bd(df, conn_params_dic):
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
    
def main():
    path            = get_dir(FOLDER_RAW_FILES)
    date_to_run     = get_date_to_run()
    filename        = path + date_to_run + FIX_FILE_PATH + '.csv' #File .csv

    if os.path.exists(filename):
        try:
            #Read file to process
            df = pd.read_csv(filename)
            df.head()

            #Pipelines
            
        except:
            print(f'Error processing file {filename}')

        df_cleaned = ( df.
                        pipe(copy_df).
                        pipe(drop_missing).
                        pipe(remove_outliers_dates, 'starttime', 'stoptime').
                        pipe(convert_int_values, ['start station id', 'end station id', 'birth year']).
                        pipe(load_raw_data_bd, conn_params_dic)
                    )

if __name__ == '__main__':
    main()
'''
variables = get_common_var()
date_to_run = variables['date_to_run']
filename = date_to_run + FIX_FILE_PATH + '.csv'
filepath = get_path_file(filename)


col_names=['tripduration','starttime','stoptime','start_station_id','end_station_id', 'bikeid', 'gender']
df = pd.read_csv(filepath)
df.head()

df_cleaned = ( df.
                pipe(copy_df).
                pipe(drop_missing).
                pipe(remove_outliers_dates, 'starttime', 'stoptime').
                pipe(convert_int_values, ['start station id', 'end station id', 'birth year']).
                pipe(load_raw_data_bd, conn_params_dic)
            )
'''

