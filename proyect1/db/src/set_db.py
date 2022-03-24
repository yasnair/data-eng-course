"""
- SET DB
    - Create DB if not exists
    - Create  Tables.
    - Fill master data.
"""
from db_parameters import DB_NAME, CONN_DB_DIC, DB_TABLES_FILENAME, DIM_MASTER_DATA_FILENAME
from psycopg2 import OperationalError
from utils import (
    connect, 
    show_psycopg2_exception,
    execute_sql_file

)

def create_db():
    conn_params_dic = CONN_DB_DIC
    conn = connect(conn_params_dic)
    conn.autocommit = True

    if conn!=None:
        
        
        try:
            cursor = conn.cursor()
            # Dropping database irisdb if exists
            print(f'Deleting DB "{DB_NAME} if no exist"..........')
            sql = f'DROP DATABASE IF EXISTS {DB_NAME};'
            cursor.execute(sql)
        
            print(f'Creating DB "{DB_NAME}"..........')
            # Creating a database
            sql = f'CREATE DATABASE {DB_NAME};'
            cursor.execute(sql)
            print(f'{DB_NAME} database is created successfully..................')
        
            # Closing the cursor & connection
            cursor.close()
            conn.close()
            
        except OperationalError as err:

            # pass exception to function
            show_psycopg2_exception(err)
            # set the connection to 'None' in case of error
            conn = None


def main():
    message_table       = "Tables"
    message_master_data = "Master data"
    create_db()
    execute_sql_file(DB_TABLES_FILENAME,  message_table)
    execute_sql_file(DIM_MASTER_DATA_FILENAME, message_master_data)
    

if __name__ == '__main__':
    main()