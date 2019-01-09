from django.db import models

# Create your models here.

class Registry(modesl.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
	value = models.BigIntegerField()
	nature = models.ForeignKey('natures.Nature', on_delete=models.CASCADE)
	