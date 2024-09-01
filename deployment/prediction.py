import streamlit as st
import pandas as pd
import pickle

with open('best_models_gb.pkl', 'rb') as file_4:
    gbmodel = pickle.load(file_4)

def run():
    st.title('**Prediction Bank Customer**')

    st.write('**Context**')
    st.write('Pada bagian ini, kita akan melakukan deployment pengujian'
              'dimana kita akan melakukan input yang kemudian model akan memprediksi apakah customer tersebut churn atau tidak.')

    with st.form('form_credit_card'):
        products_number = st.selectbox('Input Product Number', (1, 2, 3, 4), help='Input produk yang Anda gunakan')
        gender = st.selectbox('Input Gender', ("Male", "Female"), help='Jenis kelamin Anda')
        balance = st.slider('Input Balance', min_value=0, max_value=170000, value=85000, help='Slide jumlah balance Anda')
        active_member = st.selectbox('Active Member', (1, 0), help='Apakah Anda member aktif atau tidak')
        country = st.selectbox('Input Country', ("France", "Spain", "Germany"), help='Masukkan negara asal Anda')
        age = st.slider('Input Age', min_value=20, max_value=95, value=35, help='Slide umur Anda')

        # Submit button
        submitted = st.form_submit_button('Predict')

    data_bank_customer = {
        "products_number": products_number,
        "gender": gender,
        "balance": balance,
        "active_member": active_member,
        "country": country,
        "age": age
    }     

    data_bank_customer = pd.DataFrame([data_bank_customer])

    if submitted:

        st.write(data_bank_customer)

        y_pred_inf = gbmodel.predict(data_bank_customer)
        if y_pred_inf == 0:
            st.write('### Hasil: 0 - Selamat customer ini kemungkinan besar tidak churn terhadap bank.')
        else:
            st.write('### Hasil: 1 - Sayang customer ini termasuk ke dalam churn terhadap bank.')

if __name__ == "__main__":
    run()
