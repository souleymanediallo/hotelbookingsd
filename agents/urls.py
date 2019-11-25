from django.urls import path
from . import views

app_name = "agents"

urlpatterns = [
    path('agents/', views.agents, name="agent-list")
]