#DB variables
DB_TABLES_FILENAME          = 'db_tables.sql'
DIM_TABLES_FILENAME         = 'dim_tables.sql'
DIM_MASTER_DATA_FILENAME    = 'dim_master_data.sql'
DB_NAME                     = 'trip' #Db name to create
# instantiate a cursor object from the connection
CONN_DB_DIC = {
    "host"      : "localhost",
   # "database"  : DB_NAME,
    "user"      : "postgres",
    "password"  : "postgres"
}