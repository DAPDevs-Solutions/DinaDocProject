from django.contrib import admin
from menu_pages.models import Menu, ContactUs, Category, ServiceBlock
# from modeltranslation.admin import TranslationAdmin


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']
    list_filter = ['title']
    ordering = ('title', )


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    list_filter = ['email']
    ordering = ('email', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']
    list_filter = ['category']
    ordering = ('category', )


@admin.register(ServiceBlock)
class ServiceBlockAdmin(admin.ModelAdmin):
    list_display = ['category', 'service']
    list_filter = ['category', 'service']
    ordering = ('category', 'service')