import streamlit as st
from utils.variables import connection_str
from utils.utils import set_bg_hack
from datalake.dbconnector import PostGresConnector
from datalake.queries import select_user_table

def main():
    st.set_page_config(
        page_title='Sportello Sanitario Villa Tiburtina',
          layout='wide' if st.session_state.get('layout_mode', False) else 'centered'
    )
    st.title("Sportello Sanitario")
    # set_bg_hack('/Users/a465265/VT/frontend_VT/images/villa_tiburtina.png')

    # Add user_state
    if 'user_state' not in st.session_state:
        st.session_state.user_state = {
            'username': '',
            'logged_in': False,
            'user_role': ''
        }
    
    if not st.session_state.user_state['logged_in']:
        st.write("Effettua l'accesso")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        submit = st.button("Accedi")
        connector = PostGresConnector(connection_str=connection_str)
        user_table = connector.select_query(query_sql=select_user_table)
        if submit:
            if username not in user_table['username'].tolist():
                st.error("Username o Password Non Validi")
            elif password != user_table[user_table['username'] == username]['password'].values[0]:
                st.error("Username o Password Non Validi")
            elif password == user_table[user_table['username'] == username]['password'].values[0]:
                st.session_state.user_state['logged_in'] = True
                st.session_state.user_state['user_role'] = user_table[user_table['username'] == username]['role'].values[0]
                st.session_state.user_state['username'] = username
                st.success("Logged in")
                st.rerun()
            else:
                st.error("Username o Password Non Validi")

    if st.session_state.user_state['logged_in']:
        # Anagrafica pages
        new_entry_page = st.Page("insert_entry.py", title="Inserisci accesso sportello",
                              icon=":material/add:")
        modify_entry_page = st.Page("modify_entry.py", title="Modifica dati sportello",
                                icon=":material/search:")
        delete_entry_page = st.Page("delete_entry.py", title="Elimina accesso sportello",
                                icon=":material/delete:")
        download_entry_page = st.Page("download_entry.py", title="Download dati sportello",
                                icon=":material/download:")
        # Users pages
        new_user_page = st.Page("insert_user.py", title="Aggiungi users",
                                icon=":material/person:")
        delete_user_page = st.Page("delete_user.py", title="Elimina users",
                                icon=":material/delete:")

        if st.session_state.user_state['user_role'] == 'admin':
            pg = st.navigation({"Accessi Sportello": [new_entry_page, modify_entry_page, 
                                                      delete_entry_page, download_entry_page],
                                "Gestisci Dashboard": [new_user_page, delete_user_page]})
        else:
            pg = st.navigation({"Accessi Sportello": [new_entry_page, modify_entry_page,
                                                      download_entry_page]})
        pg.run()

if __name__ == "__main__":
    main()