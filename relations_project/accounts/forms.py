from django import forms
from .models import Player, Team
from django.contrib.auth.forms import User

class UserForm(forms.ModelForm):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=50,  label="Password", widget=forms.TextInput(attrs={'type':'password'}))
	
	class Meta:
		model  = User
		fields = ('username', 'email', 'password')

	def clean_username(self):
		username = self.cleaned_data['username']

		if User.objects.filter(username=username).exists():
			raise forms.ValidationError(('User already exists'), code='Invalid')

		return username


	def clean_email(self):
		email = self.cleaned_data['email']

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError(('Email already taken'), code='Invalid')

		return email

class PlayerForm(forms.ModelForm):
	class Meta:
		model  = Player
		fields = ('company', )


class LoginForm(forms.ModelForm):
	username = forms.CharField(max_length=50,  label="username", widget=forms.TextInput(attrs={'placeholder':'Username or E-mail'}))
	password = forms.CharField(max_length=50,  label="password", widget=forms.TextInput(attrs={'type':'password', 'placeholder':'Password'}))

	class Meta:
		model  = User
		fields = ('username', 'password')


class TeamForm(forms.ModelForm):
	name = forms.CharField(max_length=50, label='name', widget=forms.TextInput(attrs={'placeholder':'name'}))

	class Meta:
		model  = Team
		fields = ('name',)

	def clean_name(self):
		name = self.cleaned_data['name']

		if Team.objects.filter(name=name).exists():
			raise forms.ValidationError('Team name already taken')

		return name