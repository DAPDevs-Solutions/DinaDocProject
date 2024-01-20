from modeltranslation.translator import register, translator, TranslationOptions
from .models import Menu, ContactUs, Category, ServiceBlock


@register(Menu)
class MenuTranslationsOptions(TranslationOptions):
    fields = ('title', )


# translator.register(Menu, MenuTranslationsOptions)

# @register(ContactUs)
# class ContactUsTranslationsOptions(TranslationOptions):
#     fields = ('name', 'email', 'message')


# translator.register(ContactUs, ContactUsTranslationsOptions)


@register(Category)
class CategoryTranslationsOptions(TranslationOptions):
    fields = ('category',)


# translator.register(Category, CategoryTranslationsOptions)


@register(ServiceBlock)
class ServiceBlockTranslationsOptions(TranslationOptions):
    fields = ('category', 'service')


# translator.register(ServiceBlock, ServiceBlockTranslationsOptions)