from django.urls import path
from . import views

urlpatterns = [
	path('nueva/',views.NewCategoryView.as_view(),name='new'),
	path('todas/',views.CategoryListView.as_view(), name='list'),
	path('<int:pk>/',views.CategoryDetailView.as_view(), name='detail'),
	path('<int:pk>/',views.CategoryUpdateView.as_view(), name='update'),
]