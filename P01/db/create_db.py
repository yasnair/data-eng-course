
from utils import get_db_connect
import sys, os


# instantiate a cursor object from the connection
conn, cursor = get_db_connect()

# check if the connection was valid
if cursor != None:
    print ("\nconnection successful:", conn, "\n")
    # get the sql filname from args
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if len(sys.argv) <= 1:
        file_path = os.path.join(dir_path , 'tables.sql')
    else:
        file_path = os.path.join(dir_path , sys.argv[1])

    try:
        sqlfile = open(file_path, 'r')
        cursor.execute(sqlfile.read())
         # commit transactions to PostgreSQL
        conn.commit()

        # close the cursor object to avoid memory leaks
        cursor.close()

        # close the connection object
        conn.close()
    except Exception as err:
            print ("cursor.execute() ERROR:", err)

            # rollback the statement
            conn.rollback()
