from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=48fb6313e9de67844f0be2cdce4e1f5e').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(round(json_data['main']['temp'] -273.15, 2)) + ' C',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']) + '%',
        }   
    else:
        city = ''
        data = {}
    return render(request, "index.html",{'city': city, 'data':data})
