# Bank-Customer-Churn-Rate-Prediction

# Langkah Instalasi
1. Clone Git Repository

   git clone https://github.com/christ241/Bank-Customer-Churn-Rate-Prediction.git

3. Navigasi ke direktori proyek

   cd Bank-Customer-Churn-Rate-Prediction
   
5. Install requirements yang berada di folder deployment

   pip install requirements.txt

# Penggunaan
Untuk menggunakan prediksi ini dapat dilakukan dengan cara

streamlit run-app.py

## Overview

Proyek ini bertujuan untuk memprediksi customer churn rate pada sektor perbankan. Dimana churn ini berkaitan dengan customer yang berhenti
menggunakan produk atau layanan dari bank tersebut. Sehingga hal ini dapat membantu bank untuk mempertahankan customer yang sudah ada serta
mengetahui faktor-faktor yang berkontribusi pada churn rate customer, dan memprediksi customer yang berisiko untuk churn.

## Kolom Data yang Digunakan
**Penjelasan Kolom:**
1. **customer_id**: id kustomer bank.
2. **credit_score**: skor kredit kustomer.
3. **country**: negara asal kustomer.
4. **gender**: jenis kelamin kustomer.
5. **age**: usia kustomer.
6. **tenure**: sisa waktu berlaku kartu kredit kustomer.
7. **balance**: saldo dari ksutomer.
8. **products_number**: jenis produk yang digunakan kustomer di bank tersebut.
9. **credit_card**: apakah kustomer memiliki kartu kredit atau tidak (1=punya, 0=tidak punya).
10. **active_member**: apakah kustomer member aktif di bank tersebut (1=aktif, 0=tidak aktif).
11. **estimated_salary**: gaji per tahun yang diterima kustomer.
12. **churn**: sebagai target dimana 1 untuk kustomer meninggalkan bank, 0 kustomer loyal terhadap bank.
