from django.db import models

# Create your models here.
class Messages(models.Model):
	message = models.CharField(max_length=250)

	def __str__(self):
		return self.message
	
	class Meta:
		verbose_name_plural = 'Messages'