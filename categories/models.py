from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
	NATURE =(
		('EN','Ingreso'),
		('EG','Egreso'),
	)
	name = models.CharField(max_length=25)
	description = models.TextField(blank=True, null=True)

	nature = models.CharField(max_length=2,choices=NATURE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{}'.format(self.name)

	class Meta:
		verbose_name_plural='Categories'