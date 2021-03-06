from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Registry(models.Model):
	name = models.CharField(max_length=30, blank=True, null=True)
	description = models.TextField(blank=True)
	category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
	value = models.BigIntegerField()

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField(default=True)
	
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural='Registries'