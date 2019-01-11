from django.urls import path
from . import views
urlpatterns = [
	path('new/',views.NewCategory.as_view,name='new'),
]