from utils import  (
    get_path_file, 
    show_psycopg2_exception, 
    connect,
    execute_sql_file
)
from db_parameters import DIM_TABLES_FILENAME
from psycopg2 import OperationalError

def main():
    message_table       = "Data"
    execute_sql_file(DIM_TABLES_FILENAME,  message_table)    

if __name__ == '__main__':
    main()
