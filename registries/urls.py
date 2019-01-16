#Django
from django.urls import path
#Views
from . import views

urlpatterns=[
	path('',views.HomeView.as_view(),name='home'),
	path('nuevo/',views.NewRegistryView.as_view(),name='new'),
	path('registros/',views.ListRegistriesView.as_view(), name='registries'),
	path('<int:year>/<int:month>/<int:day>',views.DayReport.as_view(), name='day_report'),
]