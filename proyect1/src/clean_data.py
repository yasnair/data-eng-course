"""
- PROCESS RAW DATA:
    - Get file to process 
    - Clean data.
    - Load data into DB table 
"""

from operator import index
import os,sys
sys.path.insert(1, f'{os.getcwd()}/proyect1/utils')
import pandas as pd
from io import StringIO
from psycopg2 import OperationalError
from parameters import FIX_FILE_PATH,  FOLDER_RAW_FILES, FOLDER_DATA_CLEANED
from utils_all import (
    get_dir,
    get_date_to_run
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

def create_clean_file(df):
    path            = get_dir(FOLDER_DATA_CLEANED) 
    date_to_run     = get_date_to_run()
    filename        = path + date_to_run + FIX_FILE_PATH + '.csv' #File .csv
    if os.path.exists(filename):
        print('This file was alrady procesed......')
    else:
        print('Creating clean file......')
        df.to_csv(filename, index = False) 
    

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
                        pipe(create_clean_file)
                    )

if __name__ == '__main__':
    main()
