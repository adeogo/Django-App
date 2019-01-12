from django.db import models

class Store(models.Model):
	name = models.CharField(max_length=40)
	email = models.CharField(max_length=50)

	def __str__(self):
		return self.name