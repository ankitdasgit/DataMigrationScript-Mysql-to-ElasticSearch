import mysql.connector
from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = "UH4G4=S1oxr=26CyrQk_"
ELASTIC_USERNAME="elastic"
Mysql_Table="employee"
ES_INDEX="employee_index"

es = Elasticsearch(
    "ES_HOST",
    verify_certs=False,
    basic_auth=(ELASTIC_USERNAME,ELASTIC_PASSWORD)
)

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="ankit1234",
#     database="dmsdemo"
#     )

# print(mydb.database)

# cursor = mydb.cursor(dictionary=True)
# cursor.execute(f"SELECT * FROM {Mysql_Table}")


# for row in cursor:
#     es.index(index=ES_INDEX, body=row)


# mydb.commit()

print("All good")