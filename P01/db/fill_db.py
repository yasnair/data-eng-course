
from http.client import OK
import utils, os

dir_originfiles       = utils.get_dir('lake/origin_files/')
dir_processedfiles    = utils.get_dir('lake/processed_files/')

 #get date to fill
date_to_run = utils.get_date_to_run()
result, filepath = utils.unzip_file(dir_originfiles, dir_processedfiles, date_to_run)
if result == OK:
    # instantiate a cursor object from the connection
    conn, cursor = utils.get_db_connect()
    # check if the connection was valid
    if cursor != None:
        print ("\nconnection successful:", conn, "\n")
        try:
            cursor = conn.cursor()
            #cursor.execute('TRUNCATE TABLE rawdata;')
            #conn.commit()
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
