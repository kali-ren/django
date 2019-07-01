from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Team(models.Model):
	name    	= models.CharField(max_length=50)
	captain 	= models.CharField(max_length=50)
	#limite  	= models.IntegerField(default=5)
	hash_team 	= models.CharField(max_length=40)
	points 		= models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Player(models.Model):
	user  			= models.OneToOneField(User, on_delete=models.CASCADE)
	team 			= models.ForeignKey(Team, null=True, on_delete=models.SET_NULL) 
	company 		= models.CharField(max_length=100)
	
	def __str__(self):
		return self.user.username

