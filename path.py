from pprint import pprint
import requests 
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=1fa58a5f84a8045a3e8405953748d0c0')
pprint(r.json())

import pyowm

owm = pyowm.OWM('1fa58a5f84a8045a3e8405953748d0c0')
user = str(input('Enter your location and country'))
 
user_input.observation =owm.weather_at_place('')


w = observation.get_weather()



print('The current temperature is ' + str(w.get_temperature()) +'and the wind blows at ' + str(w.get_wind()))


