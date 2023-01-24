import urllib.request
import json
from googletrans import Translator, constants
from pprint import pprint

weatherValues = {
    'clouds' : '\u2601',
    'rain' : '\u26C8',
    'thunderstorm' : '\u26A1',
    'clear' : '\u2600'
}
weatherActualValue = ''

def get_weather():
    translator = Translator()
    weatherActualValue = ''
    url = "http://api.openweathermap.org/data/2.5/weather?q=Panama&APPID=29949e307139f813796fb514c8e3cda3"
    response = urllib.request.urlopen(url)
    parseResponse = json.loads(response.read())

    temperature = parseResponse['main']['temp'] - 273.15
    weather = parseResponse['weather'][0]['description']
    for v in weather.split():
        if v in weatherValues:
            weatherActualValue = v
    weather = translator.translate(weather, dest="es")
    return temperature, weather.text + ' ' + weatherValues[weatherActualValue]