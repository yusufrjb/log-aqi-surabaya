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

import requests
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

def insert_to_supabase(row):
    url = f"{SUPABASE_URL}/rest/v1/air_quality"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "timestamp": row["timestamp"],
        "aqius": row["aqius"],
        "main_pollutant": row["main_pollutant"],
        "temp": row["temp"],
        "humidity": row["humidity"]
    }
    r = requests.post(url, headers=headers, json=payload)
    print(r.status_code, r.text)

