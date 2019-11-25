from django.contrib import admin
from .models import Agents
# Register your models here.
@admin.register(Agents)
class AgentAdmin(admin.ModelAdmin):
    pass

