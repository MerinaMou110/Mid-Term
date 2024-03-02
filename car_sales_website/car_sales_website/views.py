from django.shortcuts import render
from Brand.models import brand
from Car.models import car
def home(request,brand_slug=None):
    data = car.objects.all() 
    if brand_slug is not None: 
        selected_brand = brand.objects.get(slug = brand_slug) 
        data = car.objects.filter(Brand= selected_brand) 
    brands = brand.objects.all() 
    return render(request, 'home.html', {'data' : data, 'brand_list' :brands})