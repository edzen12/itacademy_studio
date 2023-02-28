from django.shortcuts import render
from apps.project.models import Sett
from apps.service.models import Service, Prices

def service_page_view(request):
    setting = Sett.objects.latest('id') 
    service = Service.objects.all() 
    prices = Prices.objects.all() 
    name_page = 'Услуги'
    context = {
        'setting':setting,
        'service_all':service, 
        'prices':prices, 
        'name_page':name_page, 
        
    }
    return render(request, 'page/service.html', context)
