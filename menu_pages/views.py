from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Menu, ContactUs
from .forms import FeedbackForm


menu = Menu.objects.all()


class MainPage(TemplateView):
    template_name = 'menu_page/main_page.html'
    context_object_name = 'menu',

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

    # @staticmethod
    # def get_feedback_form(request):
    #     if request.method == 'POST':
    #         feedback_form = FeedbackForm(request.POST)
    #         if feedback_form.is_valid():
    #             feedback_form.save()
    #             return redirect('contact_page')
    #     else:
    #         feedback_form = FeedbackForm()
    #
    #     context = {'feedback_form': feedback_form}
    #     return render(request, 'contact_page/contact_page.html', context)



