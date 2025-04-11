import requests
import csv
from datetime import datetime

API_KEY = "54a048fc-5295-4849-b28c-b5260e5641e9"  # Ganti dengan API key kamu
CITY = "Surabaya"
STATE = "East Java"
COUNTRY = "Indonesia"
FILENAME = "aqi_log.csv"

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
    try:
        with open(FILENAME, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)
    except Exception as e:
        print("Gagal simpan:", e)

if __name__ == "__main__":
    aqi_data = get_aqi()
    if aqi_data:
        save_to_csv(aqi_data)
        print("Data tersimpan:", aqi_data)
