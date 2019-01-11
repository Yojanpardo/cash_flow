from django.db import models

# Create your models here.

class Category(models.Model):
	NATURE =(
		('EN','Ingreso'),
		('EG','Egreso'),
	)
	name = models.CharField(max_length=25)
	description = models.TextField(blank=True, null=True)

	nature = models.CharField(max_length=2,choices=NATURE)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural='Categories'