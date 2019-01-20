from django.urls import path
from . import views

urlpatterns = [
	path('nueva/',views.NewCategoryView.as_view(),name='new'),
	path('',views.CategoryListView.as_view(), name='list'),
	path('<int:pk>/',views.CategoryDetailView.as_view(), name='detail'),
	path('actualizar/<int:pk>/',views.CategoryUpdateView.as_view(), name='update'),
]