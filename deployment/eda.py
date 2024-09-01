import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so
import plotly.express as px
from PIL import Image

def run():

    #Membuat judul
    st.title('Bank Customer Churn')

    image = Image.open('Churn-Prediction-scaled.jpeg')
    st.image(image, caption='Customer Churn')

    st.write('**Context**')

    st.write('Selamat datang di aplikasi Bank Customer Churn Prediction, saat ini bank ingin melakukan prediksi klasifikasi berdasarkan'
             'input data yang diberikan kepada model untuk mengetahui strategi bisnis marketing seperti apa yang harus dilakukan'
             'oleh bank tersebut sehingga dapat menarik perhatian kustomer lebih banyak lagi')

    st.markdown('------')

    #Sub judul untuk Exploratory Data Analysis
    st.subheader('Exploratory Data Analysis Customer Churn')

    #Memanggil dataset
    data_bank_customer = pd.read_csv('Bank_Customer_Churn_Prediction.csv')
    data_bank_customer

    st.write("#### Rata-rata Credit Score Berdasarkan Negara")
    #Melakukan groupby berdasarkan negara terhadap credit_score
    credit_country = data_bank_customer.groupby(['country'])['credit_score'].mean().sort_values(ascending=False).reset_index()
    #Membuat visualisasi rata-rata credit score berdasarkan negara
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create the bar plot
    sns.barplot(x="country", y="credit_score", data=credit_country, ax=ax, color='green')

    # Add text annotations on the bars
    for index, row in credit_country.iterrows():
        ax.text(row.name, row.credit_score, round(row.credit_score, 2), color='black', ha="center")

    # Set title and labels
    ax.set_title("Rata-rata Credit Score Berdasarkan Negara")
    ax.set_xlabel("Country")
    ax.set_ylabel("Average Credit Score")

    st.write('Dari sini, kita mendapatkan bahwa Germany dan Spain memiliki rata-rata credit score dari setiap customer yang cukup tinggi dan hampir sama'
             ' yaitu 651. Sementara France berada di belakang dengan selisih sedikit yaitu 649.')
    
    st.write ('Hal ini menunjukkan bahwa customer credit card dari masing-masing negara sehat'
             'dan juga rutin melakukan pembayaran dan juga pembelian dengan menggunakan credit card.')

    # Display the plot in Streamlit
    st.pyplot(fig)
    st.write("#### Jumlah Active Member menurut Negara")
    #Melakukan groupby berdasarkan negara terhadap active_member
    member_country = data_bank_customer.groupby(['country'])['active_member'].value_counts().reset_index()
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(member_country, x="country", y="count", hue="active_member")
    # Menambahkan label ke bar
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge', fontsize=12)

    plt.title('Jumlah Active Member menurut Negara')
    st.pyplot(fig, ax)

    st.write('Berdasarkan visualisasi data di atas kita mendapatkan bahwa, mayoritas jumlah customer baik dari aktif dan tidak berasal dari negara France (Prancis)'
             ', diikuti oleh Jerman (Germany), dan terakhir Spain (Spanyol). Dengan jumlah customer terpusat pada Prancis, maka bisa diasumsikan'
             'bahwa pusat bank atau setidaknya bank tersebut berada di wilayah Prancis.')
    
    st.write('Sementara berdasarkan jenis active member, dimana jumlah customer dari bank tersebut secara jumlah mayoritas bukan customer atau anggota '
             'aktif di bank tersebut daripada member yang aktif. Disini bank perlu meningkatkan marketing atau menarik dengan promo dan lain-lain sehingga'
             'dapat menarik minat customer untuk menjadi member aktif di bank tersebut.')

    st.write("#### Rata-rata Salary berdasarkan Negara")
    #Melakukan groupby berdasarkan negara terhadap estimated salary
    salary_country = data_bank_customer.groupby(['country'])['estimated_salary'].mean().sort_values().reset_index()
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(salary_country, x="country", y="estimated_salary")
    # Menambahkan label ke bar
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge', fontsize=12)

    plt.title('Rata-rata Salary berdasarkan Negara')
    st.pyplot(fig, ax)

    st.write('Berdasarkan data di atas, kita mendapatkan bahwa Germany (Jerman) memiliki rata-rata salary paling tinggi di antara negara lainnya. Walaupun selisih antara negara Spain (Spanyol) dan France (Prancis) tidak terlalu jauh.')

    st.write('Disini salary bisa mempengaruhi tingkat churn dari bank. Dimana salary dapat mempengaruhi balance dari seorang customer, dengan semakin tinggi balance dari customer maka kemungkinan customer untuk meninggalkan bank akan semakin kecil.')


    st.write("#### Rata-rata Income yang diterima berdasarkan Gender di setiap Negara")
    #Melakukan groupby berdasarkan negara dan gender terhadap estimated salary
    gender_income_country = data_bank_customer.groupby(['country','gender'])['estimated_salary'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(gender_income_country, x="country", y="estimated_salary", hue="gender")
    # Menambahkan label ke bar
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge', fontsize=12)

    plt.title('Rata-rata Income yang diterima berdasarkan Gender di setiap Negara')
    st.pyplot(fig, ax)

    st.write('Berdasarkan grafik di atas, kita mendapatkan bahwa rata-rata salary yang diterima oleh wanita cukup bersaing dengan customer pria dimana jarak selisih salary yang diterima tidak jauh dengan selisih paling jauh adalah $3000.')

    st.write('Selain itu, hal ini menguatkan asumsi bahwa salary meningkatkan balance dan meningkatkan kemungkinan churn atau kembali ke bank tersebut daripada kebalikannya.')

if __name__ == "__main__":
    run()