from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=f0837c0529860277fec5df6eb5d8ff7f').read()
        json_data = json.loads(res)
        temp_cel = json_data['main']['temp'] -273
        temp_cel = float("{:.2f}".format(temp_cel))
        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + ', ' + str(json_data['coord']['lat']),
            'temp': str(temp_cel) + ' °' +'C',
            'pressure': str(json_data['main']['pressure']) + '  hPa',
            'humidity': str(json_data['main']['humidity']) + '%',
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})