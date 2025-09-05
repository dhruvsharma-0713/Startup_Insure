from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def home_page_view(request):
    return render(request, 'pages/home.html')

def about_page_view(request):
    return render(request, 'pages/about.html')

def services_page_view(request):
    return render(request, 'pages/services.html')

def contact_page_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                f'New Inquiry from {name}',
                message,
                email,
                ['dhruvii.startup.insure@gmail.com'],
            )
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})