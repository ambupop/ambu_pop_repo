import streamlit as st
from datalake.dbconnector import PostGresConnector
from datalake.queries import select_user_table_no_password
from utils.variables import connection_str

connector = PostGresConnector(connection_str=connection_str)
user_table = connector.select_query(query_sql=select_user_table_no_password)

st.write("**Lista Utenti Dashboard**")
st.dataframe(data=user_table)

username = st.text_input('**Username da eliminare**', value="", help="Scrivi lo username da eliminare")
st.write(f'Username: {username}')

if st.button("Elimina Utente Dashboard"):
    sql_query = f"DELETE FROM user_table WHERE username = '{username}'" 
    try:
        connector.run_query(sql_query=sql_query)
    except Exception as e:
        st.error(f"Error saving: {e}")
    st.write(f"Utente con Username {username} eliminato con successo")
