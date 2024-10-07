import streamlit as st
import pandas as pd
from datalake.dbconnector import PostGresConnector
from datalake.queries import select_user_table
from utils.variables import connection_str

with st.form("Aggiungi Utente Dashboard"):
    st.write("**Inserisci i dati dell'utente della dashboard**")
    # USERNAME
    username = st.text_input('**Username**', value="", 
                         help="Username dell'utente")
    st.write(f'Username: {username}')
    # PASSWORD
    password = st.text_input("**Password**", value="",
                            help="Password dell'utente")
    st.write(f'Password: {password}')
    # RUOLO
    role = st.selectbox("**Ruolo**", options=['admin', 'user'], 
                       help="Ruolo dell'utente")
    st.write(f'Ruolo: {role}')

    button_check = st.form_submit_button("Controlla Utente Dashboard")
    button_save = st.form_submit_button("Salva Utente Dashboard")

    connector = PostGresConnector(connection_str=connection_str)
    user_table = connector.select_query(query_sql=select_user_table)

    new_entry= {
        'username': username,
        'password': password,
        'role': role
    }

if button_check:
    if username in user_table['username'].tolist():
        st.error("Utente già presente nel sistema")
        st.error("Utente già presente")
    
    st.write("Il nuovo utente avrà i seguenti dati:")
    st.dataframe(pd.DataFrame(new_entry, index=[0]))

if button_save:
    sql_query = f"""
    INSERT INTO users_login (username, password, role)
    VALUES ('{username}', '{password}', '{role}')
    """
    connector.run_query(sql_query)
    st.success("Utente Dashboard aggiunto correttamente")


