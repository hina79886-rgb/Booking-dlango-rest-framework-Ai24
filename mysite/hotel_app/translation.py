from .models import Services,City,Country
from modeltranslation.translator import TranslationOptions,register


@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('service_name',)

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)










