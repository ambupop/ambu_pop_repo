import streamlit as st
import pandas as pd
from datalake.dbconnector import PostGresConnector
from utils.variables import connection_str

st.write("**Dati Accessi Sportello**")
connector = PostGresConnector(connection_str=connection_str)
anafrafica_table = connector.select_query(query_sql="SELECT * FROM anagrafica_sportello")

st.dataframe(data=anafrafica_table)

st.download_button(
    label="Download",
    data=anafrafica_table.to_csv(index=False),
    file_name='anagrafica_sportello.csv',
    mime='text/csv'
)
