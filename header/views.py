from django.views.generic import TemplateView

# def headerView(request):
#     return render(request, 'home.html')


class HeaderView(TemplateView):
    template_name = 'home.html'