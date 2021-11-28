from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones1 = list(Phone.objects.values())
    sorting = request.GET.get('sort')
    print(sorting)
    if sorting == 'name':
        phones = sorted(phones1, key=lambda d: d['name'])
    elif sorting == 'min_price':
        phones = sorted(phones1, key=lambda d: d['price'])
    elif sorting == 'max_price':
        phones = sorted(phones1, key=lambda d: d['price'], reverse=True)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    print(phone)
    context = {'phone': phone}
    return render(request, template, context)
