import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data
all_df = pd.read_csv("https://raw.githubusercontent.com/Anjaszz/analisis-data-ecommerce/refs/heads/master/dashboard/all_data.csv")

# Set title untuk dashboard
st.title("Dashboard Analisis E-Commerce")

# Menampilkan rata-rata nilai transaksi per customer
st.header("Rata-rata Nilai Transaksi per Customer (2017-2018)")
avg_transaction_per_customer = all_df.groupby('customer_unique_id')['payment_value'].mean().reset_index()
avg_transaction_per_customer.rename(columns={'payment_value': 'avg_payment_value'}, inplace=True)

# Visualisasi
fig, ax = plt.subplots()
sns.histplot(avg_transaction_per_customer['avg_payment_value'], kde=True, ax=ax, color='#72BCD4')
ax.set_title('Distribusi Rata-rata Nilai Transaksi per Customer (2017-2018)')
ax.set_xlabel('Rata-rata Nilai Transaksi')
ax.set_ylabel('Frekuensi')
st.pyplot(fig)

# Persentase metode pembayaran
st.header("Persentase Metode Pembayaran")
payment_type_distribution = all_df['payment_type'].value_counts(normalize=True).reset_index()
payment_type_distribution.columns = ['payment_type', 'percentage']
payment_type_distribution['percentage'] = payment_type_distribution['percentage'] * 100

# Visualisasi
fig, ax = plt.subplots()
sns.barplot(x='percentage', y='payment_type', data=payment_type_distribution, palette='Blues_d', ax=ax)
ax.set_title('Persentase Metode Pembayaran yang Paling Banyak Digunakan')
ax.set_xlabel('Persentase')
ax.set_ylabel('Metode Pembayaran')
st.pyplot(fig)

# Rata-rata skor ulasan per kategori produk
st.header("Rata-rata Skor Ulasan per Kategori Produk")
avg_review_by_category = all_df.groupby('product_category_name_english')['review_score'].mean().reset_index().sort_values(by='review_score', ascending=False)

# Visualisasi
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='review_score', y='product_category_name_english', data=avg_review_by_category.head(10), palette='coolwarm', ax=ax)
ax.set_title('Kategori Produk dengan Rata-rata Skor Ulasan Tertinggi')
ax.set_xlabel('Rata-rata Skor Ulasan')
ax.set_ylabel('Kategori Produk')
st.pyplot(fig)

# Kesimpulan
st.header("Kesimpulan")
st.write("""
- Rata-rata nilai transaksi per customer cenderung stabil, menunjukkan bahwa pelanggan berbelanja dengan bijaksana.
- Metode pembayaran yang paling banyak digunakan adalah kartu kredit, diikuti oleh boleto. 
- Kategori produk seperti elektronik dan fashion memiliki rata-rata skor ulasan yang lebih tinggi, menunjukkan kepuasan pelanggan yang tinggi.
""")
