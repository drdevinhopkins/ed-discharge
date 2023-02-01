import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(page_title=None, page_icon=None, layout="wide",
                   initial_sidebar_state="auto", menu_items=None)
params = st.experimental_get_query_params()

st.sidebar.title('ED Discharge Assistant')

unumber, name, ramq, dob, phone, postalcode = '', '', '', '', '', ''

if params:
    # st.sidebar.write(params)
    if 'unumber' in params:
        unumber = params['unumber'][0]
    if 'name' in params:
        name = params['name'][0]
    if 'ramq' in params:
        ramq = params['ramq'][0]
    if 'dob' in params:
        dob = params['dob'][0]
    if 'phone' in params:
        phone = params['phone'][0]
    if 'postalcode' in params:
        postalcode = params['postalcode'][0]


unumber = st.sidebar.text_input('U-number', unumber)
name = st.sidebar.text_input('Name', name)
ramq = st.sidebar.text_input('RAMQ', ramq)
dob = st.sidebar.text_input('DOB', dob)
phone = st.sidebar.text_input('Phone #', phone)
postalcode = st.sidebar.text_input('Postal Code', postalcode)

ciusss = ''
csss = ''


def get_ciusss(postalcode):
    prefix = postalcode[:3]
    if prefix in ['H3X', 'H4A', 'H4B', 'H4V', 'H4W', 'H4X']:
        csss = "Cavendish"
        ciusss = "CIUSSS du Centre-Ouest"
    elif prefix in ['H2V', 'H3A', 'H3G', 'H3H', 'H3N', 'H3P', 'H3R', 'H3S', 'H3T', 'H3V', 'H3W', 'H3Y', 'H3Z', 'H4P']:
        csss = 'De La Montagne'
        ciusss = "CIUSSS du Centre-Ouest"
    elif prefix in ['H8N', 'H8P', 'H8R', 'H8S', 'H8T', 'H9P', 'H9S']:
        csss = "Dorval-Lachine-Lasalle"
        ciusss = "CIUSSS de l'Ouest"
    elif prefix in ['H8Y', 'H8Z', 'H9A', 'H9B', 'H9C', 'H9E', 'H9G', 'H9H', 'H9J', 'H9K', 'H9R', 'H9X', 'H9W']:
        csss = "Ouest de l'Île"
        ciusss = "CIUSSS de l'Ouest"
    elif prefix in ['H1G', 'H1H', 'H2B', 'H2C', 'H2M', 'H2N', 'H3L']:
        csss = "Ahuntsic & Montreal"
        ciusss = "CIUSSS du Nord"
    elif prefix in ['H4N', 'H4T', 'H3M', 'H4J', 'H4K', 'H4L', 'H4M', 'H4R', 'H4S']:
        csss = "Bordeaux, Cartierville, St-Laurent"
        ciusss = "CIUSSS du Nord"
    elif prefix in ['H2E', 'H2G', 'H2P', 'H2R', 'H2S']:
        csss = "Coeur de l'Île"
        ciusss = "CIUSSS du Nord"
    elif prefix in ['H2H', 'H2J', 'H2K', 'H2L', 'H2T', 'H2W', 'H2X', 'H2Y', 'H2Z']:
        csss = "Jeanne Mance"
        ciusss = "CIUSSS du Centre-Sud"
    elif prefix in ['H3C', 'H3E', 'H3J', 'H3K', 'H4B', 'H4C', 'H4E', 'H4G', 'H4H']:
        csss = "Sud-Ouest Verdun"
        ciusss = "CIUSSS du Centre-Sud"
    elif prefix in ['H1P', 'H1R', 'H1S', 'H1Z', 'H2A']:
        csss = "St-Leonard & St-Michel"
        ciusss = "CIUSSS de l'Est"
    elif prefix in ['H1A', 'H1B', 'H1C', 'H1D', 'H1E', 'H1K', 'H1L']:
        csss = "Pointe de l'Île"
        ciusss = "CIUSSS de l'Est"
    else:
        csss = "Not Montreal"
        ciusss = "Not Montreal"
    return csss, ciusss


csss, ciusss = get_ciusss(postalcode)

st.write(csss, ciusss)
