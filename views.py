from django.shortcuts import render, get_object_or_404
from .models import Phone

def catalog(request):
    order_by = request.GET.get('order_by', 'name')
    phones = Phone.objects.all().order_by(order_by)
    return render(request, 'catalog.html', {'phones': phones})

def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'phone_detail.html', {'phone': phone})