from django.urls import path
from . import views

app_name = "hotel"

urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search, name="search"),
    path('list/', views.hotel_list, name="hotel-list"),
    path('list/<int:hotel_id>/', views.hotel_detail, name="hotel-detail"),
]
