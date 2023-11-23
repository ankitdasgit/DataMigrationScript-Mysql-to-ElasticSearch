from elasticsearch import Elasticsearch
import mysql.connector

ELASTIC_PASSWORD = ""
ELASTIC_USERNAME=""


# attach your MySQL Configuratiions here
Mysql_Host = ''
Mysql_User = ''
Mysql_Password = ''
Mysql_DB = ''
Mysql_Table = ''

# elasticsearch Configurations
ES_HOST = ''
ES_INDEX= ''


# Connect to MySQL
try:
    mysql_conn = mysql.connector.connect(
        host=Mysql_Host,
        user=Mysql_User,
        passwd=Mysql_Password,
        database=Mysql_DB
    )
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {Mysql_Table}") 

# Connect to Elasticsearch
    es=Elasticsearch([ES_HOST],
                 verify_certs=False,
                 basic_auth=(ELASTIC_USERNAME,ELASTIC_PASSWORD)
                 )

# Migrate data from MySql to elasticsearch
    for row in cursor:
        es.index(index=ES_INDEX, body=row)
    print("Data migration completed.")

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")

finally:
    if 'mysql_conn' in locals() and mysql_conn.is_connected():
        cursor.close()
        mysql_conn.close()