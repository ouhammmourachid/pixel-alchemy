from django.urls import path

from .views import *

urlpatterns = [
    path('style', StyleOperationView.as_view()),
]
