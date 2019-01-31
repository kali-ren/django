from django.db import models

# Create your models here.

class Jobs(models.Model):
	image 		= models.ImageField(upload_to='images/')
	summary 	= models.CharField(max_length=200)
	description = models.TextField(default='test')

	def __str__(self):
		return self.summary

	class Meta:
		verbose_name_plural = 'jobs'