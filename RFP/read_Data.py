import psycopg2
import pandas as pd
import numpy as np
# Update connection string information 

class read_Data:
    def read_dataframe(self,table_name):
        """
        This function is used to read data from Postgresql table using python
        """
        host = "rfpbuilder.postgres.database.azure.com"
        dbname = "rfp_dev_001"
        user = "rfpadmin@rfpbuilder"
        password = "India@india@123"
        sslmode = "require"
        # Construct connection string

        # [!INCLUDE [applies-to-postgresql-flexible-server](../includes/applies-to-postgresql-flexible-server.md)]
        conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
        conn = psycopg2.connect(conn_string) 
        print("Connection established")
        cursor = conn.cursor()

        ### Reading the data from database
#         dataFrame= pd.read_sql("select * from \"RFP_rfpdata\"", conn);
        dataFrame= pd.read_sql("select * from \""+table_name+"\"", conn);
        return dataFrame