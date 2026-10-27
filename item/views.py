from django.shortcuts import render,get_object_or_404,redirect
from .models import Item,Category
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import NewitemForm,EdititemForm,CategoryForm
from  django.db.models import Q


def items(request):
    query = request.GET.get('query','')
    category_id =request.GET.get('category',0)
    items = Item.objects.all()
    categories = Category.objects.all()
    if category_id:
        items = items.filter(category_id=category_id)
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    context ={
        'items' : items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    }
    return render(request, 'item/items.html',context)

def detail(request, pk):
    item = get_object_or_404(Item,pk=pk)
    related_items =Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    
    context={
        'item':item,
        'related_items':related_items
    }
    return render(request,'item/detail.html',context)

@login_required
def newItem(request):
    if request.method == 'POST':
        form = NewitemForm(request.POST,request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('detail', pk=item.id)
    else:
        form = NewitemForm()
    context={
        'form': form,
        'title': 'New Item'
    }
    return render(request, 'item/form.html', context)

@login_required
def editItem(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by=request.user)
    if request.method == 'POST':
        form = EdititemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
           form.save()
           return redirect('detail', pk=item.id)
    else:
        form = EdititemForm(instance=item)
    context={
        'form': form,
        'title': 'Edit Item'
    }
    return render(request, 'item/editform.html', context)

@login_required
def delete(request, pk):
    item = get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()
    return redirect('dashboard')


@staff_member_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_categories')
    else:
        form = CategoryForm()
    context={
        'form': form,
        'title': 'Add Category',
    }
    return render(request, 'item/add_category.html', context)


@staff_member_required
def manage_categories(request):
    categories = Category.objects.all()
    context={
        'categories': categories,
        'title': 'Manage Categories'
    }
    return render(request, 'item/manage_categories.html', context)

@staff_member_required
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('manage_categories')
    else:
        form = CategoryForm(instance=category)
    context= {
        'form': form,
        'title': 'Edit Category',
    }
    return render(request, 'item/add_category.html',context)

@staff_member_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('manage_categories')