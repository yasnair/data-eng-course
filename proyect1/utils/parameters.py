URL_BASE        = 'https://s3.amazonaws.com/tripdata/'
FIX_FILE_PATH   = '-citibike-tripdata'

#FILES FOLDERS NAME
FOLDER_ORIGIN_FILES     = 'lake/origin_files/'
FOLDER_RAW_FILES        = 'lake/raw_files/'
FOLDER_DATA_CLEANED     = 'lake/clean_files/'


#DB variables
DB_TABLES_FILENAME          = 'db_tables.sql'
DIM_TABLES_FILENAME         = 'dim_tables.sql'
DIM_MASTER_DATA_FILENAME    = 'dim_master_data.sql'
DB_NAME                     = 'trip' #Db name to create

CONN_DB_DIC = {
    "host"      : "localhost",
   # "database"  : DB_NAME,
    "user"      : "postgres",
    "password"  : "postgres"
}