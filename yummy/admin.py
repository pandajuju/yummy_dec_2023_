from django.contrib import admin
from .models import DishCategory
from django.utils.safestring import mark_safe

admin.site.register(DishCategory)

