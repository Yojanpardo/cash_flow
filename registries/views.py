from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import NewRegistryForm

# Create your views here.

class HomeView(TemplateView):
	template_name = 'registries/home.html'
	extra_context = {'pene':'vagina'}

class NewRegistryView(CreateView):
	form_class = NewRegistryForm
	template_name = 'registries/new.html'
	success_url = reverse_lazy('registries:home')

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['user'] = self.request.user
	    return context