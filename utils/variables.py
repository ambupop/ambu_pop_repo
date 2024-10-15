import os

connection_str = os.getenv("CONNECTION_STR")
sex_list = ["", 'M', 'F', 'Non Binario', 'Altro']
access_list = ["", 'Chiamata', 'Sportello']
know_list = ["", 'Iniziative', 'Volantinaggio', 'Passaparola']
access_problem_list = ['Agende Chiuse', 'Mancata presa in carico', 'Mancato rispetto priorità',
                       'Mediazione/Stranier*', 'Servizi Sociali', 'Servizi Consultoriali',
                       'Altro']
ente_list = ["", 'Regione', 'Municipio', 'Comune', 'Altro']
status_list = ["In corso", "Positivo", "Negativo", "Parziale"]
variables_list = ["data_inserimento", "nome", "cognome", "età", "sesso_genere", "indirizzo",
                  "città", "contatto", "modalità_accesso", "conoscenza_sportello", 
                  "descrizione_problema_accesso", "problema_accesso", "problema_di_accesso_altro", 
                  "prestazione_richiesta", "codice_prestazione", "azioni_intraprese", "ente_coinvolto", 
                  "ente_coinvolto_altro", "struttura_coinvolta", "documentazione", "riscontro", 
                  "note_riscontro", "data_riscontro" ]
