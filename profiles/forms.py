from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(forms.Form):
	username = forms.CharField(min_length=5,max_length=12,widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control'})
	)
	password = forms.CharField(min_length=8,widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class':'form-control'})
	)
	password_confirmation = forms.CharField(min_length=8,widget=forms.PasswordInput(attrs={'placeholder':'Confirmar contraseña','class':'form-control'})
	)
	first_name = forms.CharField(min_length=2,max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Nombre','class': 'form-control'})
	)
	last_name = forms.CharField(min_length=2,max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Apellido','class': 'form-control'})
    )
	email = forms.CharField(min_length=7,max_length=70,widget=forms.EmailInput(attrs={'placeholder': 'Email','class': 'form-control'})
	)

	def clean_username(self):
		username = self.cleaned_data['username']
		username_taken = User.objects.filter(username=username).exists()
		if username_taken:
			raise forms.ValidationError('El nombre de usuario ya está en uso.')
		return username

	def clean(self):
		data = super().clean()
		password = data['password']
		password_confirmation = data['password_confirmation']
		if password != password_confirmation:
			raise forms.ValidationError('Las contraseñas no coinciden.')
		return data

	def save(self):
		data = self.cleaned_data
		data.pop('password_confirmation')

		user = User.objects.create_user(**data)
		profile = Profile(user=user)
		profile.save()