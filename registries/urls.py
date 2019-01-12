#Django
from django.urls import path
#Views
from . import views

urlpatterns=[
	path('',views.HomeView.as_view(),name='home'),
	path('new',views.NewRegistryView.as_view(),name='new'),
]