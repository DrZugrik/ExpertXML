from django.contrib import admin
from mysite.models import UserProfile, XMLSchema, AI_Models

admin.site.register(XMLSchema)
admin.site.register(AI_Models)
admin.site.register(UserProfile)  # Регистрация UserProfile в админке

