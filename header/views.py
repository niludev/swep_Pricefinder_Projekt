from django.views.generic import ListView
from .models import Header

# def headerView(request):
#     return render(request, 'home.html')


class HeaderView(ListView):
    model = Header
    template_name = 'home.html'