from flask import Flask ,render_template
#from pprint import pprint
import os
#import requests 
#r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=1fa58a5f84a8045a3e8405953748d0c0')
#pprint(r.json())

#import json
#import pyowm		methods=['GET']

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


#owm = pyowm.OWM('1fa58a5f84a8045a3e8405953748d0c0')
#observation =owm.weather_at_place('')
#w = observation.get_weather()

#def Get()

#	print('The current temperature is ' + str(w.get_temperature()) +'and the wind blows at ' + str(w.get_wind()))

if __name__=='__main__':
	port=int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port) 
