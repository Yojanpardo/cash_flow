from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from .forms import NewCategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category
from django.http import Http404
# Create your views here.

class NewCategoryView(LoginRequiredMixin, CreateView):
	form_class = NewCategoryForm
	template_name = 'categories/new.html'
	success_url = reverse_lazy('registries:home')

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "categories/list.html"
    context_object_name = 'categories'

    def get_queryset(self):
    	user = self.request.user
    	return Category.objects.filter(user=user)

class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = "categories/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        pk = self.kwargs.get(self.pk_url_kwarg)
        category = Category.objects.get(pk=pk)
        context['category']=category
        if category.user != user:
            raise Http404('Categoria no encontrada.')
        return context

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = "categories/update.html"
    fields = ['name','description','nature','user']

    def get_success_url(self):
        category = Category.objects.get(pk=self.kwargs.get(self.pk_url_kwarg))
        return reverse_lazy('categories:detail', kwargs={'pk':category.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        pk = self.kwargs.get(self.pk_url_kwarg)
        category = Category.objects.get(pk=pk)
        context['category']=category
        if category.user != user:
            raise Http404('Categoria no encontrada.')
        return context