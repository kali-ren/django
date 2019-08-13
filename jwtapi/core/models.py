from django.db import models

# Create your models here.
class Role(models.Model):
	name = models.CharField(max_length=20)
	role = models.CharField(max_length=20)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Role'