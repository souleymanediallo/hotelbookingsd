from django.shortcuts import render, redirect
from .models import About
from .forms import ContactForm
from django.core.mail import BadHeaderError
from django.core.mail import send_mail as sm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def about(request):
    about = About.objects.last()
    context = {'about': about}
    return render(request, "pages/about.html", context)

def send_mail(request):
    if request.method == 'POST':
        form_contact = ContactForm(request.POST)
        if form_contact.is_valid():
            subject = form_contact.cleaned_data['subject']
            email = form_contact.cleaned_data['email']
            message = form_contact.cleaned_data['message']

            try:
                sm(subject, email, message, ['apjuin19@gmail.com'])
            except BadHeaderError:
                return HttpResponse('ivalid header')

            return redirect('pages:message')
    else:
        form_contact = ContactForm()

    context = {'form_contact': form_contact}
    return render(request, "pages/contact.html", context)

def sucess_message(request):
    return render(request, "pages/s_message.html")

