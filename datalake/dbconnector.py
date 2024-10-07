import psycopg2
import enum
import pandas as pd
import os
from sqlalchemy import create_engine
from datetime import datetime as dt
import logging

class PostGresConnector():

    def __init__(self, connection_str: str) -> None:
        self._conn_str =  connection_str
        self.connect()

    # Initialize Connection and Cursor
    def connect(self):
        try:
            self._conn = psycopg2.connect(self._conn_str)
        except Exception as e:
            logging.error(f"Error during Postgres connection: {e}")
            raise e
    
    # Run a query
    def run_query(self, sql_query: str) -> None:
        """
        Run a generic query

        :param sql_query: SQL query to execute
        """
        try:
            cursor = self._conn.cursor()
            cursor.execute(sql_query)
            self._conn.commit()
            logging.info(f"Query executed: {sql_query}")
        except Exception as e:
            logging.error(f"Error in run_query: {e}")
        finally:
            cursor.close() if cursor else None

    # Select query
    def select_query(self, query_sql: str) -> pd.DataFrame:
        """
        Execute a select query and return the result as a pandas dataframe

        :param query_sql: SQL query to execute
        :return: pandas dataframe with the result of the query
        """

        cursor = None
        try:
            logging.debug(f"Select query: {query_sql[0:100]}")
            cursor = self._conn.cursor()
            cursor.execute(query_sql)
            output = {
                'columns': [column[0] for column in cursor.description],
                'rows': list(cursor.fetchall())
            }
            logging.info(f"Select query output: {output}")
            # init table dataframe
            table_df = pd.DataFrame.from_records(output['rows'], columns=output['columns'])
            return table_df
        except Exception as e:
            logging.error(f"Error in select_query: {e}")
        finally:
            cursor.close() if cursor else None
    
    