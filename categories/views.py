from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import NewCategoryForm

# Create your views here.

class NewCategoryView(CreateView):
	form_class = NewCategoryForm
	template_name = 'categories/new.html'
	success_url = reverse_lazy('registries:home')