from django.shortcuts import render
from apps.project.models import * 
from apps.service.models import Service


def homepage(request):
    setting = Sett.objects.latest('id') 
    service = Service.objects.all()
    plan = Plan.objects.latest('id') 
    categoryPortfolio = CategoryPortfolio.objects.all()
    portfolio = Portfolio.objects.all() 
    reviews = Reviews.objects.all() 
    sliders = Slider.objects.all() 
    
    context = {
        'setting':setting,
        'service':service,
        'plan':plan,
        'categoryPortfolio':categoryPortfolio,
        'portfolio':portfolio,
        'reviews':reviews,  
        'sliders':sliders,  
    }
    return render(request, 'index.html', context)


def projects(request):
    setting = Sett.objects.latest('id')  
    categoryPortfolio = CategoryPortfolio.objects.all()
    portfolio = Portfolio.objects.all()  
    name_page = 'Проекты'
    context = {
        'setting':setting, 
        'categoryPortfolio':categoryPortfolio,
        'portfolio':portfolio,  
        'name_page':name_page
    }
    return render(request, 'page/projects.html', context)


