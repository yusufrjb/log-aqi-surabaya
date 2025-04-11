import requests
import csv
import os
from datetime import datetime

API_KEY = os.getenv("API_KEY")  # <- dari Secrets GitHub
CITY = "Surabaya"
STATE = "East Java"
COUNTRY = "Indonesia"
FILENAME = "aqi_surabaya.csv"

def get_aqi():
    url = f"http://api.airvisual.com/v2/city?city={CITY}&state={STATE}&country={COUNTRY}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if data.get("status") == "success":
        pollution = data['data']['current']['pollution']
        weather = data['data']['current']['weather']
        return {
            "timestamp": pollution['ts'],
            "aqius": pollution['aqius'],
            "main_pollutant": pollution['mainus'],
            "temp": weather['tp'],
            "humidity": weather['hu']
        }
    else:
        print("Gagal ambil data:", data)
        return None

def save_to_csv(data):
    file_exists = os.path.isfile(FILENAME)
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

# Eksekusi 1x (untuk dipanggil setiap jam oleh GitHub Actions)
print(f"[{datetime.now()}] Mengambil data AQI Surabaya...")
aqi_data = get_aqi()
if aqi_data:
    save_to_csv(aqi_data)
    print("Data berhasil disimpan.")
else:
    print("Gagal simpan data.")
