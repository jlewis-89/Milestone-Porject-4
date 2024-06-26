from django.contrib import admin

# Register your models here.
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Choice)
