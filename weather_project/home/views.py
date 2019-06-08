from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests

# Create your views here.
def home(request):

	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=271d1234d3f497eed5b1d80a07b3fcd1'
	extra_parameters = {}
	
	if request.method == 'POST':
		form = CityForm(request.POST)
		if form.is_valid():
			city_custom = form.cleaned_data.get('name')
			r 			= requests.get(url.format(city_custom)).json()
			celsius 	= round( ((r['main']['temp']-32)*5)/9, 1)

			extra_parameters = {
			'city': city_custom,
			'temp': celsius,
			'desc': r['weather'][0]['description'], 
			'icon': r['weather'][0]['icon'],
			}

	form = CityForm()

	cities = City.objects.all()
	cities_list = []
	
	for city in cities:
		r 		= requests.get(url.format(city)).json()
		celsius = round( ((r['main']['temp']-32)*5)/9, 1)
		
		city_parameters = {
		'city': city,
		'temp': celsius,
		'desc': r['weather'][0]['description'], 
		'icon': r['weather'][0]['icon'],
	} 
		cities_list.append(city_parameters)
		
	r 		= requests.get(url.format('fortaleza')).json()
	celsius = round( ((r['main']['temp']-32)*5)/9, 1)

	local = {
		'city': 'Fortaleza',
		'temp': celsius,
		'desc': r['weather'][0]['description'],
		'icon': r['weather'][0]['icon'],
	}

	context = {'cities_data': cities_list, 'local': local, 'form': form, 'extra_parameters': extra_parameters}
	return render(request,'home/home.html',context)