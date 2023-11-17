This Python script for how to migrate data from a MySQL database table to Elasticsearch and visualize it using Kibana.

## Prerequisites
1. install elasticsearch and kibana and configure in your machine


Before running the script, ensure you have the following installed:

- elasticsearch library (`pip install elasticsearch`)
- mysql-connector-python library (`pip install mysql-connector-python`)




## how to run script 
1. Install Required Librarie
2. Set Up MySQL and Elasticsearch Configurations
3. Ensure MySQL and Elasticsearch are Running
4. run using "python MysqltoES.py" command


## Visualizing Data in Kibana

1. Open Kibana in your web browser.

2. use username and password of elasticSearch, and

2. Create an index pattern in Kibana:
- Go to Management -> Index Patterns.
- Enter the name of your Elasticsearch index (specified in the Python script).

3. Go to Discover and select the newly created index pattern to explore your data.


## references
1. https://episyche.com/blog/how-to-configure-elasticsearch-and-kibana-setup
