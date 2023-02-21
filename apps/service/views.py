from django.shortcuts import render
from apps.project.models import Sett
from apps.service.models import Service, Prices

def service_page_view(request):
    setting = Sett.objects.latest('id') 
    service = Service.objects.all() 
    prices = Prices.objects.all() 
    
    context = {
        'setting':setting,
        'service_all':service, 
        'prices':prices, 
    }
    return render(request, 'page/service.html', context)
