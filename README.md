# 🌫️ AQI Logger: Surabaya

Proyek ini secara otomatis mengambil dan mencatat data **kualitas udara (AQI)** kota **Surabaya** setiap jam menggunakan API dari [IQAir](https://www.iqair.com/world-air-quality) dan menyimpannya dalam file CSV di repositori ini.

## 🔍 Tujuan

Mendokumentasikan perubahan kualitas udara secara berkala (per jam) untuk:

- Analisis data jangka panjang
- Visualisasi tren polusi udara
- Prediksi atau penelitian terkait kesehatan dan lingkungan

## 📦 Data yang Dicatat

Setiap entri log mencakup:

- `timestamp`: Waktu pengambilan (UTC)
- `aqius`: Indeks kualitas udara berdasarkan standar US
- `main_pollutant`: Polutan utama
- `temp`: Suhu (°C)
- `humidity`: Kelembapan (%)

Contoh isi file `aqi_surabaya.csv`:

```
timestamp,aqius,main_pollutant,temp,humidity
2025-04-11T07:00:00.000Z,57,pm2.5,31,74
```

## ⚙️ Otomatisasi GitHub Actions

Workflow GitHub berjalan otomatis:

- 🕒 **Setiap jam** (`cron: '0 * * * *'`)
- ✅ Dapat juga dijalankan secara manual via GitHub

### Cara Kerja:

1. Menjalankan script `log_aqi.py`
2. Mengambil data AQI dari API IQAir
3. Menyimpan ke `aqi_surabaya.csv`
4. Commit dan push file ke repository

## 🔐 API Key

API berasal dari [IQAir AirVisual API](https://www.iqair.com/air-pollution-data-api).\
Gunakan Free Plan (maks. 10.000 request/bulan).

Tambahkan API key sebagai GitHub Secret:

- Masuk ke **Settings > Secrets and variables > Actions**
- Tambahkan secret dengan nama: `API_KEY`

## 🧪 Manual Run (Opsional)

GitHub Action juga bisa dijalankan secara manual:

- Buka tab **Actions**
- Pilih workflow **"Log AQI Surabaya"**
- Klik tombol **"Run workflow"**

## 📊 Rencana Pengembangan

- Visualisasi data historis
- Prediksi AQI menggunakan model time series
- Perbandingan antar kota (Yogyakarta, Jakarta, dsb)

---

## 👨‍💼 Author

**Nama**: Yusuf\
**Proyek riset**: Prediksi dan pemantauan kualitas udara berbasis data terbuka

---

## 📄 Lisensi

Proyek ini menggunakan lisensi MIT.\
Data berasal dari layanan pihak ketiga (IQAir) — mohon tetap mengikuti [syarat penggunaan API](https://www.iqair.com/terms).

