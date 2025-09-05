from django.urls import path
from .views import home_page_view, about_page_view, services_page_view, contact_page_view

urlpatterns = [
    path('', home_page_view, name='home'),
    path('about/', about_page_view, name='about'),
    path('services/', services_page_view, name='services'),
    path('contact/', contact_page_view, name='contact'),
]