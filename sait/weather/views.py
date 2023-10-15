from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from django.http import HttpResponseRedirect
def index(request):

    city = City.objects.all()
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a4ca2af1a4971c53823e814daafdb547'

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm

    all_cities = []
    for cit in city:
        try:
            res = requests.get(url.format(cit.name)).json()
            city_info = {
                'city':cit.name,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon']
                }
            if City.objects.filter(name=cit.name).exists():
                all_cities.append(city_info)
        except:
            pass


    context = {'info':all_cities, 'form':form}

    return render(request, 'weather.html',context)




def Delete(request,city):
    delete = City.objects.get(name=city)
    delete.delete()
    return HttpResponseRedirect('/')