This Python script for how to migrate data from a MySQL database to Elasticsearch and visualize it using Kibana.


## Prerequisites
1. install elasticsearch and kibana and configure in your machine(save your elasticsearch username and password)

Before running the script, ensure you have the following installed:

- elasticsearch library (`pip install elasticsearch`)
- mysql-connector-python library (`pip install mysql-connector-python`)


## how to run script 
1. Install Required Librarie
2. Set Up kibana and Elasticsearch Configurations
3. Ensure Elasticsearch is Running
4. run using "python wholeDatabaseMigration.py" command


## Visualizing Data in Kibana

1. Open Kibana in your web browser.

2. use username and password of elasticSearch, and

2. Create an index pattern in Kibana:(you can also create index in script)

- Go to Management -> Index Patterns.
- Enter the name of your Elasticsearch index (specified in the script).
- Go to Management and search index management
- Enter the name of your Elasticsearch index (specified in the script).
  


## references
1. https://episyche.com/blog/how-to-configure-elasticsearch-and-kibana-setup (setup in ec2 instance)

