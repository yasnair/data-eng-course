URL_BASE        = 'https://s3.amazonaws.com/tripdata/'
FIX_FILE_PATH   = '-citibike-tripdata'

#FILES FOLDERS NAME
FOLDER_ORIGIN_FILES     = 'lake/origin_files/'
FOLDER_RAW_FILES        = 'lake/raw_files/'

DB_NAME                     = 'trip' #Db name to create
# instantiate a cursor object from the connection
conn_params_dic = {
    "host"      : "localhost",
    "database"  : DB_NAME,
    "user"      : "postgres",
    "password"  : "postgres"
}