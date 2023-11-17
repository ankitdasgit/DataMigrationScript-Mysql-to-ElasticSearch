from elasticsearch import Elasticsearch
import mysql.connector

# attach your MySQL Configurations
MYSQL_HOST = 'localhost'
MYSQL_USER = ''
MYSQL_PASSWORD = ''
MYSQL_DB = ''
MYSQL_TABLE = ''

# Elasticsearch Configurations
ES_HOST = 'localhost:9200'
ES_INDEX = ''

# Connect to MySQL
try:
    mysql_conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        passwd=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {MYSQL_TABLE}") 

# Connect to Elasticsearch
    es = Elasticsearch([ES_HOST])

# Migrate data from MySQL to Elasticsearch
    for row in cursor:
        es.index(index=ES_INDEX, body=row)

    print("Data migration from MySQL to Elasticsearch completed.")

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")

finally:
    if 'mysql_conn' in locals() and mysql_conn.is_connected():
        cursor.close()
        mysql_conn.close()