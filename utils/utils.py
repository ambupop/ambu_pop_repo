import streamlit as st
import base64
import logging

def check_mandatory_fields_new_entry(x: dict) -> bool:
    """
    Check if all the mandatory fields are filled

    :param x: dictionary containing the user input
    :return: True if all mandatory fields are filled, False otherwise    
    """
    mandatory_fields = ['nome', 'cognome', 'età', 'indirizzo', 'contatto', 'problema_accesso',
                        'prestazione_richiesta', 'descrizione_problema_accesso']

    for field in mandatory_fields:
        if (x[field] == '') or (x[field] is None):
            return False
        
    return True

def check_consistency_altro_fields(x: dict) -> bool:
    """
    Check if the 'Altro' fields are filled consistently
    
    :param x: dictionary containing the user input
    :return: True if the 'Altro' fields are filled consistently, False otherwise
    """

    if (x['problema_accesso'] == 'Altro') and (x['problema_di_accesso_altro'] == ""):
        return False
    if (x['ente_coinvolto'] == 'Altro') and (x['ente_coinvolto_altro'] == ""):
        return False

    return True

def generate_insert_statement_anagrafica_sportello(new_entry: dict) -> str:
    """
    Generate the insert statement for the anagrafica_sportello table

    :param new_entry: dictionary containing the user input
    :return: the insert statement
    """

    variables = [k for k in new_entry.keys() if new_entry[k] is not None]
    values = [f"'{new_entry[k]}'" for k in new_entry.keys() if new_entry[k] is not None]

    sql_query = f"""
        INSERT INTO anagrafica_sportello
        ({', '.join(variables)})
        VALUES ({', '.join(values)});
        """
    logging.error(f"Insert query: {sql_query}")
    return sql_query

def replace_apostrophe(text: str):
    return text.replace("'", "*")

def set_bg_hack(main_bg):
    """
    Unpack an image from root folder and set as bg

    :return: the background
    """

    # set bg name
    main_bg_ext = 'png'

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{
        base64.b64encode(open(main_bg, "rb").read()).decode()
        });
            background-size: 80vw 100vh;
            background-position: center;  
            background-repeat: no-repeat         }}
         </style>
         """,
        unsafe_allow_html=True
    )
