from django.urls import path
from . import views

urlpatterns = [
	path('new/',views.NewCategoryView.as_view(),name='new'),
]