import requests

API_KEY = "cd62a9fc9f00e18ef7951a3504866ce6" 
CITY = "Челябинск"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ru"

def get_weather():
    try:
        response = requests.get(URL)
        data = response.json()

        if response.status_code == 200:
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]

            print(f"Погода в {CITY}: {weather.capitalize()}")
            print(f"Температура: {temp}°C")
            print(f"Влажность: {humidity}%")
            print(f"Давление: {pressure} мм рт. ст.")
        else:
            print(f"Ошибка: {data['message']}")
    except Exception as e:
        print(f"Ошибка запроса: {e}")

if __name__ == "__main__":
    get_weather()
 