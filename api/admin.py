from django.contrib import admin

# Register your models here.
from api.models import Category, Food
admin.site.register(Category)
admin.site.register(Food)
