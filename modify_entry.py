import pandas as pd
import streamlit as st # type: ignore
from utils.variables import (connection_str)
from datalake.dbconnector import PostGresConnector
from utils.variables import (variables_list, sex_list, access_list, know_list, access_problem_list, 
                             ente_list, status_list)

connector = PostGresConnector(
    connection_str=connection_str
    )


def get_values_selectbox():
    if st.session_state.variable == 'sesso_genere':
        value = st.selectbox('**Sesso**', options=sex_list)
    elif st.session_state.variable == 'modalità_accesso':
        value = st.selectbox('**Modalità di accesso**', options=access_list)
    elif st.session_state.variable == 'conoscenza_sportello':
        value = st.selectbox('**Conoscenza Sportello**', options=know_list)
    elif st.session_state.variable == 'problema_accesso':
        value = st.selectbox('**Problema di accesso**', options=access_problem_list)
    elif st.session_state.variable == 'ente_coinvolto':
        value = st.selectbox('**Ente Coinvolto**', options=ente_list)
    elif st.session_state.variable == 'riscontro':
        value = st.selectbox('**Riscontro**', options=status_list)
    elif st.session_state.variable == 'data_inserimento':
        value = st.date_input("**Data Inserimento**", value=pd.Timestamp.now().date(),
                              max_value=pd.Timestamp.now().date())
    elif st.session_state.variable == 'data_riscontro':
        value = st.date_input("**Data Riscontro**", value=pd.Timestamp.now().date(),
                              max_value=pd.Timestamp.now().date())
    elif st.session_state.variable == 'età':
        value = st.number_input("**Età (Obbligatorio)**", min_value=0, max_value=150,
                                value="min")
    else:
        value = st.text_input(f'**{st.session_state.variable}**', value="")
    return value

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

st.write("**Modifica i dati dell'utente della dashboard**")

id = st.text_input('**SQ_ID Utente**', value="", help="ID dell'utente da modificare")
st.write(f'ID: {id}')

variable = st.selectbox('**Seleziona la variabile da modificare**', 
                        options=variables_list, help="Variabile da modificare")
st.write(f'Variabile: {variable}')

st.session_state.variable = variable

value = get_values_selectbox()
st.write(f'Valore: {value}')

if st.button("Modifica"):
    st.write(f'Valore: {value}')
    sql_query = f"UPDATE anagrafica_sportello SET {variable} = '{value}' WHERE sq_id = '{id}'" 
    connector.run_query(sql_query=sql_query)
    st.write(f"Utente con ID {id} modificato con successo")
    st.rerun()

