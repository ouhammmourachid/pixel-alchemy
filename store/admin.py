from django.contrib import admin

from .models import *

admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Like)
admin.site.register(Tag)
