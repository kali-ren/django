from django.db import models

# Create your models here.

class Post(models.Model):
	title 		= models.CharField(max_length = 100)
	date_posted = models.DateTimeField(auto_now_add = True)
	body   		= models.TextField()
	image  		= models.ImageField(upload_to = 'images/')
	to_url 		= models.CharField(max_length = 200, default='test') 

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'posts'