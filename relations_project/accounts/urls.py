from django.urls import path
from . import views

app_name    = 'accounts'
urlpatterns = [
	path('', views.home, name='home'),
	path('signup/',		views.signup,    name='signup'),
	path('login/',  	views.login,     name='login'),
	path('logout/', 	views.logout,    name='logout'),
	#path('teams/',  views.teams,  name='teams'),
	path('virgo/',  	views.virgo,      name='virgo'),
	path('createteam/', views.createteam, name='createteam'),
	path('jointeam/',   views.jointeam,   name='jointeam')

]