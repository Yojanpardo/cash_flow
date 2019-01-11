from django.contrib import admin
from .models import Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display=('name','description',)

	fieldsets = (
		('Category',{
			'fields':(('name','description'),('nature'),),
		}),
		('Metadata',{
			'fields':(('created','modified'),),
		}),
	)
	readonly_fields = ('created','modified')