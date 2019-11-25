from django.contrib import admin
from .models import Category, Hotel, Reserve

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass

@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    pass