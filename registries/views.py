from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DayArchiveView
from django.urls import reverse_lazy
from .forms import NewRegistryForm
from .models import Registry
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from datetime import datetime
from categories.models import Category
from django.http import Http404
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

class RegistriesSearchView(ListView):
    model = Registry
    template_name = "registries/search.html"
    paginated_by = 30
    context_object_name = 'registries'

    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	user = self.request.user
    	date = self.request.GET['date']
    	year = date[0:4]
    	month = date[5:7]
    	day = date[8:10]
    	context['registries'] = Registry.objects.filter(user=user,date=date).order_by('category')
    	context['date'] = {'date':date,'year':year,'month':month,'day':day}
    	return context

class DayReport(LoginRequiredMixin, DayArchiveView):
	"""DayReport renders a template with a day detail """
	queryset = Registry.objects.all()
	date_field = "date"
	allow_future = True
	template_name = 'registries/day_report.html'
	context_object_name = 'registries'
	month_format = '%m'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user = self.request.user
		month = self.get_month
		date = '{}-{}-{}'.format(self.get_year(),self.get_month(),self.get_day())
		context['registries'] = Registry.objects.filter(date=date, user=user).order_by('category',)
		if not context['registries']:
			raise Http404('No se encontraron registros de este dia')
		return context