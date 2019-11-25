from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path('about/', views.about, name="about"),
    path('contact', views.send_mail, name="send_mail"),
    path('message/', views.sucess_message, name="message"),
]