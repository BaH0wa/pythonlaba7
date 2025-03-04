import requests

API_KEY = "cd62a9fc9f00e18ef7951a3504866ce6"

city_name = "Chelyabinsk"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=ru"
response = requests.get(url)
if response.status_code == 200:

    data = response.json() 
    city = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    weather_desc = data["weather"][0]["description"]
    

    print(f"Город: {city}, {country}")
    print(f"Температура: {temperature}°C (ощущается как {feels_like}°C)")
    print(f"Влажность: {humidity}%")
    print(f"Давление: {pressure} hPa")
    print(f"Погода: {weather_desc.capitalize()}")

else:
    print("Возникла ошибка! Введеные данные не являются коректными!!")