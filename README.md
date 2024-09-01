# Bank-Customer-Churn-Rate-Prediction

#Cara Pemakaian
1. Clone Git Repository

   git clone https://github.com/christ241/Bank-Customer-Churn-Rate-Prediction.git
   
3. Masuk ke direktori proyek
   
   cd churn-prediction
  
5. Melakukan install requirement yang dibutuhkan
   
   pip install -r requirements.txt

## Overview
Proyek ini bertujuan untuk memprediksi churn rate dari customer di linkungan perbankan menggunakan model machine learning. Disini churn rate yang
dimaksud adalah ketika customer berhenti menggunakan layanan atau produk dari suatu bank. Dengan memprediksi akurasi dari churn ini, bank dapat
mengimplementasikan strategi untuk mempertahankan customer serta mengurangi kerugian di masa depan.

## Data Description
**Penjelasan Kolom:**
1. customer_id: id kustomer bank.
2. credit_score: skor kredit kustomer.
3. country: negara asal kustomer.
4. gender: jenis kelamin kustomer.
5. age: usia kustomer.
6. tenure: sisa waktu berlaku kartu kredit kustomer.
7. balance: saldo dari ksutomer.
8. products_number: jenis produk yang digunakan kustomer di bank tersebut.
9. credit_card: apakah kustomer memiliki kartu kredit atau tidak (1=punya, 0=tidak punya).
10. active_member: apakah kustomer member aktif di bank tersebut (1=aktif, 0=tidak aktif).
11. estimated_salary: gaji per tahun yang diterima kustomer.
12. churn: sebagai target dimana 1 untuk kustomer meninggalkan bank, 0 kustomer loyal terhadap bank.

## Model
1. Random Forest Classifier
2. KNN
3. SVM
4. Decision Tree
5. Adaboost Classifier
6. Gradient Boost Classifier
