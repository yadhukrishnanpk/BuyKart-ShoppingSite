from django.shortcuts import render,get_object_or_404
from item.models import Item
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    item =Item.objects.filter(created_by=request.user)
    instockcount = item.filter(is_sold=False).count()
    notinstockcount = item.filter(is_sold=True).count()
    out_of_stock_items = Item.objects.filter(created_by=request.user, is_sold=True)
    in_stock_items = Item.objects.filter(created_by=request.user, is_sold=False)
    context={
        'item': item,
        'stock': instockcount,
        'outofstock': notinstockcount,
        'out_of_stock_items': out_of_stock_items,
        'in_stock_items': in_stock_items
        
    }
    return render(request, 'dashboard/dashboard.html', context)

def contact(request):
    return render(request, 'dashboard/contact.html')
from django.shortcuts import render

def about_view(request):
    return render(request, 'dashboard/about.html')

def privacy_policy(request):
    return render(request, 'dashboard/privacy_policy.html')
def termsandcondition(request):
    return render(request, 'dashboard/terms&condition.html')

