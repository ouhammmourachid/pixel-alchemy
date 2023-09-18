from django.urls import path

from .views import *

urlpatterns = [
    # this pattern for style transfer
    path('style', StyleOperationView.as_view()),
    path('enhance', EnhanceQualityOperationView.as_view()),
]
