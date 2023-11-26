from elasticsearch import Elasticsearch
import mysql.connector


#indices create by using this command
# client.indices.create(index="employee_index")  


# attach your MySQL Configuratiions here
Mysql_Host = 'your database host name'
Mysql_User = 'Database user name'
Mysql_Password = 'Database password'
Mysql_DB = 'Database Name'
Mysql_Table = 'mysql Table name'

# elasticsearch Configurations
ES_HOST = 'ElasticSearch Host Name'
ES_INDEX= 'Elastic search index name'
ELASTIC_PASSWORD = "ElasticSearch password"
ELASTIC_USERNAME="elasticSearch username"


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