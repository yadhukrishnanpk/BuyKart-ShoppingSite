from django.shortcuts import render
from item.models import Item,Category

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    Categories = Category.objects.all()
    context={
        'categories': Categories,
        'items' : items
    }
    return render(request, 'core/index.html', context)

def contact(request):
    return render(request, 'core/contact.html')

