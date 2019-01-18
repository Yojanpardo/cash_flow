#Django
from django.urls import path
#Views
from . import views

urlpatterns=[
	path('',views.HomeView.as_view(),name='home'),
	path('registros/nuevo/',views.NewRegistryView.as_view(),name='new'),
	path('registros/',views.ListRegistriesView.as_view(), name='registries'),
	path('registros/busqueda', views.RegistriesSearchView.as_view(), name='search'),
	path('registros/<int:year>/<int:month>/<int:day>',views.DayReport.as_view(), name='day_report'),
]