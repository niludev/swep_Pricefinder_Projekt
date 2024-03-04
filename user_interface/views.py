from django.shortcuts import render
from django.views.generic import ListView
from .models import Form
from django.views import View
from django.http import JsonResponse

# Create your views here.

# def indexView(request):
#     return render(request, 'form.html')


class indexView(ListView):
    model = Form
    template_name = 'form.html'


class submitView(View):
    def post(self, request) -> None:
        return JsonResponse({'ok': True})