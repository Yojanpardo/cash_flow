from django.contrib import admin
from .models import Registry
from categories.models import Category
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

	list_filter=('user',)
	readonly_fields = ('created','modified')
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == "category":
			kwargs["queryset"] = Category.objects.order_by('name')
		return super(RegistryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)