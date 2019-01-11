from django.db import models

# Create your models here.

class Registry(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
	value = models.BigIntegerField()

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural='Registries'