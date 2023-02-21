from django.shortcuts import render

from apps.about.models import ThirdBlock
from apps.project.models import Sett


def about(request):
    setting = Sett.objects.latest('id') 
    third_block = ThirdBlock.objects.all() 
    context = {
        'setting':setting,
        'third_block':third_block, 
    }
    return render(request, 'page/about.html', context)