import requests

api_key="7c7a3a4fc97bdebc0cb5a539200a8201"


user_city = input("Enter City: ")
# print(user_city)

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_city}&units=imperial&APPID={api_key}")

# print(weather_data.status)


# print(weather_data.json())

weather = weather_data.json()['weather'][0]['main']
print(weather)