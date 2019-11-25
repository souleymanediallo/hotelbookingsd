from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Hotel, Category
from .forms import ReserveForm
from agents.models import Agents
from .models import type
from django.contrib import messages
# Create your views here.

def search(request):
    queryset_hotel = Hotel.objects.order_by('-created')

    #keywords
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            queryset_hotel = queryset_hotel.filter(location__icontains=location)

    if 'type_choice' in request.GET:
        type_choice = request.GET['type_choice']
        if type:
            queryset_hotel = queryset_hotel.filter(location__icontains=type_choice)



    context = {'type': type, 'hotels': queryset_hotel}
    return render(request, "hotel/search.html", context)

def home(request):
    hotels = Hotel.objects.all()[:3]
    agents = Agents.objects.all()[:3]
    context = {'hotels': hotels, 'agents': agents, 'type': type}
    return render(request, "hotel/index.html", context)

def hotel_list(request):
    hotels = Hotel.objects.all()

    paginator = Paginator(hotels, 3)  # Show 25 contacts per page
    page = request.GET.get('page')
    hotels = paginator.get_page(page)

    context = {'hotels': hotels, 'type': type}
    return render(request, "hotel/hotel_list.html", context)

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)

    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
            messages.success(request, f'Send message with sucess')
            return redirect('hotel:home')
    else:
        reserve_form = ReserveForm()

    context = {'hotel': hotel, 'reserve_form': reserve_form}
    return render(request, "hotel/hotel_detail.html", context)