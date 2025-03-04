import requests
import json

URL = "https://rickandmortyapi.com/api/character/?name=Rick Sanchez"

def get_character():
    try:
        response = requests.get(URL)
        data = response.json()

        if "error" in data:
            print("Персонаж не найден")
            return
        
        character = data["results"][0]  # Берем первого найденного персонажа

        # Выводим 5-7 ключевых полей
        print(f"Имя: {character['name']}")
        print(f"Статус: {character['status']}")
        print(f"Вид: {character['species']}")
        print(f"Пол: {character['gender']}")
        print(f"Местоположение: {character['location']['name']}")
        print(f"Эпизоды: {len(character['episode'])}")

    except Exception as e:
        print(f"Ошибка запроса: {e}")

if __name__ == "__main__":
    get_character()
