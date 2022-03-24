
# import the error handling libraries for psycopg2
from psycopg2 import OperationalError,connect
from db_parameters import DB_NAME, CONN_DB_DIC
import psycopg2
import sys, os

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

def get_path_file(filename):
    for root, dirs, files in os.walk(os.getcwd()):
        for name in files:
            if name == filename:
                return os.path.abspath(os.path.join(root, name))

def execute_sql_file(sql_file: str, message: str):
    conn_params_dic = CONN_DB_DIC
    conn_params_dic['database'] = DB_NAME
    conn = connect(conn_params_dic)
    conn.autocommit = True

    if conn!=None:
        try:
            print(f'Creating {message} from {sql_file} file ..................')
            dir_path = os.path.dirname(os.path.realpath(__file__))
            file_path = get_path_file(sql_file)
            cursor = conn.cursor()

            #Execute query
            sqlfile = open(file_path, 'r')
            cursor.execute(sqlfile.read())
            conn.commit()

            print(f'{message}  created successfully..................')
            # close the cursor object to avoid memory leaks
            cursor.close()

            # close the connection object
            conn.close()
            
        except OperationalError as err:
            # pass exception to function
            show_psycopg2_exception(err)
            # set the connection to 'None' in case of error
            conn = None
