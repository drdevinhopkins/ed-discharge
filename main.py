import streamlit as st

params = st.experimental_get_query_params()

st.title('ED Discharge Assistant')

if params:
    # st.sidebar.write(params)
    st.sidebar.write(params['name'][0])
    st.sidebar.write(params['ramq'][0])
