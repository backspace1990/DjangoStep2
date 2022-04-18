from django.apps import AppConfig

# Uygulama ile ilgili ayarlarin 
# bulundugu yer.

class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'
