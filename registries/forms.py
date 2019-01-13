from django import forms
from .models import Registry
from categories.models import Category

class NewRegistryForm(forms.ModelForm):
	class Meta:
		model = Registry
		fields = ['name','description','category','date','value','user']