from django import forms
from .models import Registry

class NewRegistryForm(forms.ModelForm):
	class Meta:
		model = Registry
		fields = ['name','description','category','value','user']