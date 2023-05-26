import requests
import mysql.connector
from datetime import datetime

api_key = "41f6ce1045f8d19e3939db4bc4a0ccbd"
cities = ['Toronto', 'África do Sul', 'Punta Cana', 'California', 'Pyongyang', 'Kiev', 'Atenas', 'Seul', 'Camberra', 'Pequim', 'Moscou', 'Chernobyl','Switzerland', 'Papua-Nova Guiné', 'Juneau', 'Nova Delhi', 'Manhattan', 'Roma', 'Cairo', 'Jaco']
data_atual = datetime.now().date()
data_formatada = data_atual.strftime("%d/%m/%Y")
agora = datetime.now()
hora_formatada = agora.strftime("%H:%M:%S")

dados = {
    'user' : 'kenji',
    'password' : '5677',
    'host' : 'localhost',
    'database' : 'banquinho'
}

conexao = mysql.connector.connect(**dados)
cursor = conexao.cursor()

for city in cities:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    country = data["sys"]["country"]
    weather_kelvin = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    speed = data["wind"]["speed"]
    clouds = data["clouds"]["all"]
    descript = data ["weather"][0]["description"]
    celsius = round(weather_kelvin - 273.15, 2)  # Arredondando para 2 casas decimais

    consulta = "INSERT INTO mesa (Cidade, Temperatura, Descricao, Speed, Clouds, Humidity, Data_atual, Hora_atual) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (city, celsius, descript, speed, clouds, humidity, data_formatada, hora_formatada)
    cursor.execute(consulta, valores)

conexao.commit()
cursor.close()
conexao.close()
