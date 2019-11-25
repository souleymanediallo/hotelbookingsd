from django.contrib import admin
from .models import About
from .forms import ContactForm
# Register your models here.

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass
