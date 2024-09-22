# E-Commerce Data Analysis Dashboard 📊
Proyek ini bertujuan untuk menganalisis data e-commerce menggunakan dataset publik. Dashboard ini memungkinkan pengguna untuk melihat analisis pendapatan, metode pembayaran, dan kepuasan pelanggan berdasarkan skor ulasan.
## Features
- Visualisasi pendapatan per bulan
- Persentase metode pembayaran
- Rata-rata skor ulasan berdasarkan kategori produk

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```
## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard.py
```