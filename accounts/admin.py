from django.contrib import admin

from .models import Tokens, User

admin.site.register(User)
admin.site.register(Tokens)
