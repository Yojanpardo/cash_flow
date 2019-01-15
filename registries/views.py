from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from .forms import NewRegistryForm
from .models import Registry
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from datetime import datetime
from categories.models import Category
# Create your views here.

class HomeView(LoginRequiredMixin,TemplateView):
	template_name = 'registries/home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user = self.request.user
		egresses = Registry.objects.filter(category__nature='EG',user=user)
		entries = Registry.objects.filter(category__nature='EN',user=user)
		total_egresses = 0
		total_entries = 0
		for egress in egresses:
			total_egresses += egress.value
		for entry in entries:
			total_entries += entry.value
		balance = total_entries - total_egresses
		context['balance'] = balance
		return context

class NewRegistryView(LoginRequiredMixin,CreateView):
	form_class = NewRegistryForm
	template_name = 'registries/new.html'
	success_url = reverse_lazy('registries:home')
	extra_context = {'date':datetime.now().strftime('%Y-%m-%d')}
	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    user = self.request.user
	    context['categories'] = Category.objects.filter(user=user).order_by('name')
	    return context

class ListRegistriesView(LoginRequiredMixin,ListView):
	template_name = 'registries/list.html'
	model = Registry
	paginated_by = 30
	context_object_name = 'registries'
	query_set = User.objects.all()
	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    user = self.request.user
	    context['registries'] = Registry.objects.filter(user=user).order_by('-date')
	    return context