from django.contrib import admin
from .models import Registry
# Register your models here.

@admin.register(Registry)
class RegistryAdmin(admin.ModelAdmin):
	list_display=('name','description','value')

	fieldsets = (
		('Registry',{
			'fields':(('name','description'),('value','category'),),
		}),
		('Metadata',{
			'fields':(('created','modified'),),
		}),
	)
	readonly_fields = ('created','modified')