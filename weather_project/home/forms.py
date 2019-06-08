from django.forms import ModelForm, TextInput, CharField
from .models import City

class CityForm(ModelForm):
	#name = CharField(max_length=25)
	class Meta:
		model   = City
		fields  = ['name']
		widgets = {'name': TextInput(attrs={'class':'input', 'placeholder':'City Name'})}