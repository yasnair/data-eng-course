import psycopg2

#establishing the connection
conn = psycopg2.connect(
    dbname = "postgres",
    user = "postgres",
    host = "localhost",
    password = "postgres")
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
sql = '''CREATE database trip''';

#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection
conn.close()