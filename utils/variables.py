import os

connection_str = os.getenv("CONNECTION_STR")
sex_list = ["", 'M', 'F', 'Altro']
access_list = ["", 'Chiamata', 'Sportello']
know_list = ["", 'Iniziative', 'Volantinaggio', 'Passaparola']
access_problem_list = ['Agende Chiuse', 'Mancata presa in carico', 'Mancato rispetto priorità',
                       'Mediazione/Stranier*', 'Servizi Sociali', 'Servizi Consultoriali',
                       'Altro']
ente_list = ["", 'ASL', 'Municipio', 'Comune', 'Altro']
status_list = ["In corso", "Positivo", "Negativo"]
variables_list = ["data_inserimento", "nome", "cognome", "età", "sesso", "genere", "indirizzo",
                  "città", "contatto", "modalità_accesso", "conoscenza_sportello", 
                  "descrizione_problema_accesso", "problema_accesso", "problema_di_accesso_altro", 
                  "azioni_intraprese", "ente_coinvolto", "ente_coinvolto_altro", "struttura_coinvolta", 
                  "documentazione", "riscontro", "note_riscontro", "data_riscontro" ]


# with st.form("Elimina Utente Dashboard"):
# 
#    st.write("**Modifica i dati dell'utente della dashboard**")    
#    id = st.text_input('**ID (Obbligatorio)**', value="", help="ID dell'utente da modificare")
#    st.write(f'ID: {id}')
#    button_delete = st.form_submit_button("Elimina Utente Dashboard")

#if button_delete:
#    sql_query = f"DELETE FROM anagrafica_sportello WHERE sq_id = {id}" 
#    connector.run_query(sql_query=sql_query)
#   st.write(f"Utente con ID {id} eliminato con successo")
#
