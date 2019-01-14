from django.urls import path
from . import views

urlpatterns = [
	path('nuevo/',views.NewCategoryView.as_view(),name='new'),
]