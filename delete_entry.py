import pandas as pd
import streamlit as st # type: ignore
from utils.variables import (connection_str)
from datalake.dbconnector import PostGresConnector

connector = PostGresConnector(
    connection_str=connection_str
    )

with st.form("Tabella anagrafica sportello"):

    anafrafica_table = connector.select_query(query_sql="SELECT * FROM anagrafica_sportello")
    num_id = st.text_input('**SQ_ID Utente**', value="", help="ID dell'utente da modificare")
    
    st.write(f'ID selezionato: {num_id}')
    
    show_button = st.form_submit_button("Mostra Dataset")

if show_button:
    if num_id != "":
        df = anafrafica_table[anafrafica_table['sq_id'] == int(num_id)]
    else:
        df = anafrafica_table
    st.dataframe(data=df)

st.write("**Elimina i dati utente della dashboard**")

id = st.text_input('**SQ_ID Utente**', value="", help="ID dell'utente da eliminare")
st.write(f'ID: {id}')

if st.button("Elimina"):
    sql_query = f"DELETE FROM anagrafica_sportello WHERE sq_id = '{id}'" 
    try:
        connector.run_query(sql_query=sql_query)
    except Exception as e:
        st.error(f"Error {e}")
    st.write(f"Utente con ID {id} eliminato con successo")
    st.rerun()
