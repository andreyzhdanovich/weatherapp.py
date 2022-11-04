import requests
from django.shortcuts import render

def index(request):
    appid = '46f810bd4ba3d2a88562c9738b438c9e'
    url = 'https://api.openweathermap.org/data/2.5/weather?g={}&units=metric&appid=' + appid

    city = 'london'
    res = requests.get(url.format(city))

    return render(request, 'weather/index.html')
