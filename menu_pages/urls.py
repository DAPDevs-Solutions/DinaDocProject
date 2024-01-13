from django.urls import path
from .views import MainPage, ContactPage, ServicesPage

urlpatterns = [
    # main page
    path('', MainPage.as_view(), name='menu_page'),

    # contact page
    path('contacts/', ContactPage.as_view(), name='contact_page'),

    # services page
    path('services/', ServicesPage.as_view(), name='services_page')
]
