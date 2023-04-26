import requests
import json
x = requests.get('https://home.openweathermap.org/api_keys')

print(x.json())
print(x.status_code)
print(x.headers)

title = "mze"
temperatura = "30c"
url = f'https://home.openweathermap.org/api_keys?={title}&{temperatura}'
print(json.loads(x.text))

import sqlite3

conn = sqlite3.connect("weather")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE  weather
(id INTEGER PRIMARY KEY AUTOINCREMENT,
weather(autoincrement),
title VARCHAR(),
temperature VARCHAR(),
""")

