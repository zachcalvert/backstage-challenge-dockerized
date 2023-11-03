from django.apps import AppConfig
from django.core.cache import cache


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    if not cache.get('difference'):
        cache.set('differences', {})
        cache.set('pythagorean_triplets', {})
