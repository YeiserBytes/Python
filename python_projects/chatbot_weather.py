import random
import string
import requests
import json


api_key = '31fc60c8c9d80f817da97029543051ed'

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang=es&appid={api_key}'
    response = requests.get(url)
    weather_data = json.loads(response.text)
    weather = weather_data["weather"][0]["description"]
    temp = weather_data["main"]["temp"]
    temp_celsius = round(temp - 273.15, 2)
    return f'El clima de {city} es {weather} con una temperatura de {temp_celsius} grados Celsius'

def greet_and_introduce():
    messages = [
        "¡Hola! Soy un chatbot que te puede dar información sobre el clima.",
        "¡Bienvenido! ¿En qué puedo ayudarte con el clima?",
        "¡Hola! ¿Qué quieres saber sobre el clima?"
    ]
    print(random.choice(messages))

def chat():
    greet_and_introduce()
    while True:
        user_message = input("Tú: > ").lower()
        if user_message in ['salir', 'chao', 'adios']:
            print('Chatbot: > Hasta pronto!')
            break
        elif 'clima' in user_message:
            words = user_message.split()
            city = words[-1].capitalize()
            response = get_weather(city)
            print(f'Chatbot: > {response}')
        else:
            print('Chatbot: > Lo siento, no entiendo lo que esta preguntando.')

chat()