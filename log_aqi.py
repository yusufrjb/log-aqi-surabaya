import requests
import time
import os
import csv
from datetime import datetime

API_KEY = os.getenv("API_KEY")
CITY = "Surabaya"
STATE = "East Java"
COUNTRY = "Indonesia"

def fetch_aqi():
    url = f"http://api.airvisual.com/v2/city?city={CITY}&state={STATE}&country={COUNTRY}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    try:
        aqi = data['data']['current']['pollution']['aqius']
        time_now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{time_now}] AQI: {aqi}")

        file_exists = os.path.isfile("aqi_log.csv")
        with open("aqi_log.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["timestamp_utc", "aqius"])
            writer.writerow([time_now, aqi])
    except KeyError:
        print("Gagal fetch AQI, respon API tidak sesuai:", data)

# Loop setiap 10 menit selama 30 menit
for _ in range(3):
    fetch_aqi()
    if _ < 2:
        time.sleep(600)  # tunggu 10 menit
