from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from .forms import NewRegistryForm
from .models import Registry
# Create your views here.

class HomeView(TemplateView):
	template_name = 'registries/home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		egresses = Registry.objects.filter(category__nature='EG')
		entries = Registry.objects.filter(category__nature='EN')
		total_egresses = 0
		total_entries = 0
		for egress in egresses:
			total_egresses += egress.value
		for entry in entries:
			total_entries += entry.value
		balance = total_entries - total_egresses
		context['balance'] = balance
		return context

class NewRegistryView(CreateView):
	form_class = NewRegistryForm
	template_name = 'registries/new.html'
	success_url = reverse_lazy('registries:home')

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['user'] = self.request.user
	    return context

class ListRegistriesView(ListView):
	template_name = 'registries/list.html'
	model = Registry
	ordering = 'name'
	paginated_by = 30
	context_object_name = 'registries'