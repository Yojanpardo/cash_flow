from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.views.generic import FormView
from .forms import SignupForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class SignupView(FormView):
	template_name = 'profiles/signup.html'
	form_class = SignupForm
	success_url = reverse_lazy('profiles:login')
	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

class LoginView(auth_views.LoginView):
	template_name = 'profiles/login.html'
	redirect_authenticated_user = True

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout View."""
