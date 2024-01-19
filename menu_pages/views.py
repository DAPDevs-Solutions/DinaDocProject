from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.utils.translation import activate
from django.urls import reverse_lazy, reverse
from .models import Menu, ContactUs, Category
from .forms import FeedbackForm
from DinaDocProject import settings


menu = Menu.objects.all()


class MainPage(TemplateView):
    template_name = 'menu_page/main_page.html'
    context_object_name = 'menu',

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu

        return context


class ServicesPage(TemplateView):
    template_name = 'services_page/services_page.html'
    context_object_name = 'menu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu

        categories = Category.objects.all()

        services_dict = {}
        for category in categories:
            services = category.serviceblock_set.values_list('service', flat=True)
            services_dict[category.category] = list(services)

        context['services_dict'] = services_dict
        return context


class PricePage(TemplateView):
    template_name = 'price_page/price_page.html'
    context_object_name = 'menu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


class ContactPage(CreateView):
    model = ContactUs
    form_class = FeedbackForm
    template_name = 'contact_page/contact_page.html'
    context_object_name = 'menu'
    success_url = reverse_lazy('contact_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['feedback_form'] = self.form_class()
        return context
