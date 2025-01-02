import requests
import json
import pyttsx3
engine = pyttsx3.init()
 # Set properties (optional)
engine.setProperty('rate', 100)  # Speed of speech
engine.setProperty('volume', 1)
city=input("Enter the city name:")
url=f"https://api.weatherapi.com/v1/current.json?key=7b6129e10bed4979a26171048241812&q={city}"
r=requests.get(url)
print(r.text)
print(r.status_code)
print(type(r.text))
print("------------------------------------------------------------------------------------")
weather_dict=json.loads(r.text)
w=weather_dict["current"]["temp_c"]
l=weather_dict["current"]["condition"]["text"]
u=weather_dict["current"]["last_updated"]
engine.say(f"The current temperature in {city} is {w} degree celsius and its condition is {l} and is last updated on {u}")

    # Block while processing the commands
engine.runAndWait()