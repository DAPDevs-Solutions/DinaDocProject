from modeltranslation.translator import register, TranslationOptions
from .models import Menu, ContactUs, Category, ServiceBlock


@register(Menu)
class MenuTranslationsOptions(TranslationOptions):
    fields = ('title', 'url')


@register(ContactUs)
class ContactUsTranslationsOptions(TranslationOptions):
    fields = ('name', 'email', 'message')


@register(Category)
class CategoryTranslationsOptions(TranslationOptions):
    fields = ('category',)


@register(ServiceBlock)
class ServiceBlockTranslationsOptions(TranslationOptions):
    fields = ('category', 'service')

