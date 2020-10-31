from django.apps import AppConfig 


class SeoConfig(AppConfig):
    name = 'sw_shop.seo'
    verbose_name = 'SEO'

default_app_config = 'sw_shop.seo.SeoConfig'


