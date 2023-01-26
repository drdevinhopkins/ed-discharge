import streamlit as st

params = st.experimental_get_query_params()

st.title('ED Discharge Assistant')

if params:
    # st.sidebar.write(params)
    st.sidebar.write(params['unumber'][0])
    st.sidebar.write(params['name'][0])
    st.sidebar.write(params['ramq'][0])
    st.sidebar.write(params['dob'][0])
    st.sidebar.write(params['phone'][0])
    st.sidebar.write(params['postalcode'][0])
