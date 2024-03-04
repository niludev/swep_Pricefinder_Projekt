from django.shortcuts import render
from django.views.generic import ListView
from .models import Form
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Create your views here.

# def indexView(request):
#     return render(request, 'form.html')


class indexView(ListView):
    model = Form
    template_name = 'form.html'


@method_decorator(csrf_exempt, name='dispatch')  # Disable CSRF token for this view
class submitView(View):
    def post(self, request) -> JsonResponse:
        data = json.loads(request.body)
        # ......
        # price = 120000
        price = 120000
        return JsonResponse({'price': price})