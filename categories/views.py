from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .forms import NewCategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category
# Create your views here.

class NewCategoryView(LoginRequiredMixin, CreateView):
	form_class = NewCategoryForm
	template_name = 'categories/new.html'
	success_url = reverse_lazy('registries:home')

class CategoryListView(ListView):
    model = Category
    template_name = "categories/list.html"
    context_object_name = 'categories'

    def get_queryset(self):
    	user = self.request.user
    	return Category.objects.filter(user=user)

class CategoryDetailView(DetailView):
    model = Category
    template_name = "categories/detail.html"