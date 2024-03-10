from django.urls import path

from price_prediction.views import PredictView
from .views import indexView, submitView

urlpatterns = [
    path('', indexView.as_view(), name='form'),
    path('submit', submitView.as_view()),
    path('predict/', PredictView.as_view(), name='predict'),
]