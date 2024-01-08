from django.views.generic import TemplateView
from .models import Menu


menu = Menu.objects.all()


class MainPage(TemplateView):
    template_name = 'main_page/main_page.html'
    context_object_name = 'menu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context
