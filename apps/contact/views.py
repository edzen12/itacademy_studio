from django.shortcuts import render
from apps.project.models import Sett

# Create your views here.
def contact(request):
    setting = Sett.objects.latest('id')  
    name_page = 'Контакты'
    context = {
        'setting':setting,   
        'name_page':name_page
    }
    return render(request, 'page/contact.html', context)