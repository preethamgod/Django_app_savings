
from bq_login import Bqlogin
from TD_login import Tdlogin
import pandas as pd


def update_bq():
    query_bq = """select dataset_id, table_id,row_count from customers10.__TABLES__;"""
    query_job = Bqlogin.client.query(query_bq)  # Make an API request.
    print("The query data:") 
    for row in query_job:
        # Row values can be accessed by field name or index.
        print("dataset={}, table={}, count=".format(row["dataset_id"], row["table_id"]),row["row_count"])


def update_td():
    query_td = """select DatabaseName,
        TableName,
        RowCount
        from 
        (SELECT  DatabaseName,
            TableName,
            RowCount,
            row_number() over(partition by TableName order by LastCollectTimeStamp desc) as rw
             FROM    DBC.TableStatsV ) temp 
             where rw=1"""

        #Reading query to df
    df_td = pd.read_sql(query_td, Tdlogin.connect)
    # do something with df,e.g.
    print(df_td.head())  # to see the first 5 rows
def compare_table():
    pass

if __name__ == "__main__":
    update_bq()
    update_td()
    compare_table()
