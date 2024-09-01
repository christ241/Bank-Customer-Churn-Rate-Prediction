import streamlit as st
import eda
import prediction

st.logo('sberbank_logo.jpeg')

page = st.sidebar.selectbox('Pilih Halaman', ('EDA', 'Prediction'))

if page=='EDA':
    eda.run()
else:
    prediction.run()