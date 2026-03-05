# 날씨 정보를 요청해서 CSV로 저장하는 코드
import requests
import csv
import os
from datetime import datetime

MY_API_KEY = os.getenv("WEATHER_API_KEY")
city_name = "Seoul"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={MY_API_KEY}"
url += "&units=metric"

# 정보 요청
response = requests.get(url)
result = response.json()

# 날씨 정보
main = result["weather"][0]["main"]
temp = result["main"]["temp"]
humidity = result["main"]["humidity"]

# 시간 정보
current_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")

# weather.csv를 만들자
# 최초  생성 시 -> 헤더도 추가
# 파일이 존재하면 -> 덮어쓰기

csv_exist = os.path.exists("weather.csv")
header = ["current_time", "temp", "humidity", "main"]

with open("weather.csv", "a", newline="") as file:
    writer = csv.writer(file)

    if not csv_exist:
        writer.writerow(header)
    
    writer.writerow([current_time, temp, humidity, main])

print("날씨 저장 완료")
