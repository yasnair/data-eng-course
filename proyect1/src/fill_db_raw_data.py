
import utils, os


variables = utils.get_common_var()
date_to_run = variables['date_to_run']
filepath = utils.get_path_file(f'{date_to_run}-citibike-tripdata.csv')

# instantiate a cursor object from the connection
conn, cursor = utils.get_db_connect()
# check if the connection was valid
if cursor != None:
    print (f'connection successful: {conn}')
    try:
        cursor = conn.cursor()
        cursor.execute('TRUNCATE TABLE rawdata;')
        conn.commit()
        with open(filepath, 'rb') as f:
            next(f) # Skip the header row.
            cursor.copy_from(f, 'rawdata', sep=',')

        conn.commit()
        # close the cursor object to avoid memory leaks
        cursor.close()

        # close the connection object
        conn.close()
    except Exception as err:
            print ("cursor.execute() ERROR:", err)

            # rollback the statement
            conn.rollback()


