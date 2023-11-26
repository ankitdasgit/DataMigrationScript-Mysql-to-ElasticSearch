from elasticsearch import Elasticsearch
import mysql.connector

# attach your MySQL Configuratiions here
Mysql_Host = 'localhost'
Mysql_User = 'root'
Mysql_Password = 'ankit1234'
Mysql_DB = 'dmsdemo'
# Mysql_Table = 'mysql Table name'

# Elasticsearch Configurations
ES_HOST = 'https://localhost:9200'
ES_INDEX_PREFIX = 'dms_index'  
ELASTIC_PASSWORD = "UH4G4=S1oxr=26CyrQk_"
ELASTIC_USERNAME="elastic"

try:
    # Connect to MySQL
    mysql_conn = mysql.connector.connect(
        host=Mysql_Host,
        user=Mysql_User,
        passwd=Mysql_Password,
        database=Mysql_DB
    )
    mysql_cursor = mysql_conn.cursor()

    # Connect to Elasticsearch
    es=Elasticsearch([ES_HOST],
                 verify_certs=False,
                 basic_auth=(ELASTIC_USERNAME,ELASTIC_PASSWORD)
                 )
    
    # es.indices.create(index="dms_index")
    ES_INDEX_PREFIX= 'dms_index'  
    
    # Fetch list of tables in the database
    mysql_cursor.execute("SHOW TABLES")
    tables = mysql_cursor.fetchall()
    print(tables)

    for table in tables:
        table_name = table[0]
        print(f"Table name: {table_name}")

        # Fetch data from the table
        mysql_cursor.execute(f"SELECT * FROM {table_name}")
        table_data = mysql_cursor.fetchall()
        print(f"Data fetched from {table_name}: {table_data}")

        # Define the Elasticsearch index name for each table
        es_index_name = f"{ES_INDEX_PREFIX}_{table_name.lower()}"
        print(f"Elasticsearch Index name: {es_index_name}")

        # Index data into Elasticsearch
        for row in table_data:
            # Prepare data to be indexed as a dictionary
            document = {
                'table': table_name,
                'data': str(row)  # Assuming `row` is a tuple or a list
            }

            # Index the document
            es.index(index=es_index_name, body=document)
            print(f"Data indexed in {es_index_name}: {document}")   

    print("Data migration completed.")

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")

finally:
    if mysql_conn and mysql_conn.is_connected():
        mysql_cursor.close()
        mysql_conn.close()
