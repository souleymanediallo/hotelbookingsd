from django.shortcuts import render
from .models import Agents

# Create your views here.
def agents(request):
    list_agents = Agents.objects.all()
    context = {'agents': list_agents}
    return render(request, "agents/list_agents.html", context)