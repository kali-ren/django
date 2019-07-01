from django.shortcuts import render
from .forms import UserForm, PlayerForm, LoginForm, TeamForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Player, Team
import hashlib
from datetime import datetime


def has_team(request):
	player = Player.objects.get(user=request.user).team
	
	if player is None:
		return False
	return True

# Create your views here.
def home(request):
	return render(request, 'accounts/home.html')


def signup(request):#user form valida se ja tem um caboco registrado!!
	if request.user.is_authenticated:
		return HttpResponseRedirect('/accounts/')	

	if request.method == 'POST':
		user_form   = UserForm(request.POST)
		player_form = PlayerForm(request.POST)
		
		if user_form.is_valid() and player_form.is_valid():
			#user 		= user_form.save()
			username 	= user_form.cleaned_data.get('username')
			password	= user_form.cleaned_data.get('password')
			email 		= user_form.cleaned_data.get('email')
			
			user        = User.objects.create_user(username=username, password=password, email=email)
			player   	= player_form.save(commit=False)
			player.user = user
			
			player.save()
		
			return HttpResponseRedirect(reverse('accounts:login'))
		
		else:
			error = {
				'user_form':   user_form,
				'player_form': player_form,
			}
		
			return render(request, 'accounts/signup.html', error)

	user_form   = UserForm()
	player_form = PlayerForm()
	
	context = {
		'user_form': user_form,
		'player_form': player_form
	}

	return render(request, 'accounts/signup.html', context)

def login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/accounts/')

	form = LoginForm()
	
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		try:
			user = authenticate(username=User.objects.get(email=username), password=password)			
		except:
			user = authenticate(username=username, password=password)
		
		if user is not None:
			auth_login(request, user)
			has_team = Player.objects.get(user=user).team
			#print('nao tem time ') if Player.objects.get(user=user).team is None else print('tem time')
			if has_team is None:
				return HttpResponseRedirect(reverse('accounts:virgo'))
			
			return HttpResponseRedirect(reverse('accounts:home'))

		return render(request, 'accounts/login.html', {'form': form, 'erro': 'Please enter a correct username and password. Note that both fields may be case-sensitive.'})

	return render(request, 'accounts/login.html', {'form': form})

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect(reverse('accounts:home'))


@login_required(login_url="accounts/login/")
def virgo(request):
	if has_team(request) == True:
		return HttpResponseRedirect('/accounts')
	
	return render(request,'accounts/virgo.html')


@login_required(login_url="accounts/login/")
def createteam(request):# view para poder playar
	if has_team(request) == True:
		return HttpResponseRedirect('/accounts/')
	
	if request.method == 'POST':
		team_form = TeamForm(request.POST)

		if team_form.is_valid():
			now 		= datetime.now()
			name    	= team_form.cleaned_data.get('name')
			captain 	= request.user.username
			hash_team 	= hashlib.md5( (name+str(now.second)).encode('utf-8') ).hexdigest()

			new_team    = Team(name=name, captain=captain, hash_team=hash_team, points=0)
			new_team.save()
			
			player      = Player.objects.get(user=request.user)
			player.team = new_team
			player.save()
			
			#return render(request, 'accounts/home.html', hello)
			return HttpResponseRedirect(reverse('accounts:home'))
		
		else:
			return render(request, 'accounts/createteam.html', {'team_form': team_form})

	team_form = TeamForm()		
	return render(request, 'accounts/createteam.html', {'team_form': team_form})


@login_required(login_url="accounts/login/")
def jointeam(request):
	
	if has_team(request) == True:
		return HttpResponseRedirect('/accounts/')
	
	if request.method == 'POST':
		hash_field = request.POST['hash']
	
		if len(hash_field) != 32:
			return render(request, 'accounts/jointeam.html', {'erro':'Invalid Hash'})

		team_exists = Team.objects.filter(hash_team=hash_field).exists()
		if team_exists:
			team 	    = Team.objects.get(hash_team=hash_field)
			player      = Player.objects.get(user=request.user)
			player.team = team
			
			player.save()
			team.save()

			return HttpResponseRedirect(reverse('accounts:home'))

		else:
			error = {
				'erro': 'team not exists'
			}
			return render(request, 'accounts/jointeam.html', error)#mudar isso ctza

	return render(request, 'accounts/jointeam.html')