from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _

from django.views.static import serve as mediaserve


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # main page
#     path('', include('menu_pages.urls')),
#
#     path('i18n/', include('django.conf.urls.i18n')),
# ]

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),

    path('', include('menu_pages.urls')),

    path('i18n/', include('django.conf.urls.i18n')),
    prefix_default_language=True,

)
