from django.urls import path
from .views import indexView, submitView

urlpatterns = [
    path('', indexView.as_view(), name='form'),
    path('submit', submitView.as_view())
]