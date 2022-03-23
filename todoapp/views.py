from django.shortcuts import render
from .models import todolist
from datetime import datetime
from django.contrib import messages

# Create your views here.     
def todo(request):
    if request.method == 'POST' and 'add' in request.POST:
        title = 'title' in request.POST and request.POST['title']
        desc = 'desc' in request.POST and request.POST['desc']
        price = 'price' in request.POST and request.POST['price']
        
        add_item = todolist(item_title=title, description=desc, item_price=price, date=datetime.now())
        add_item.save()
        messages.success(request, 'Items added successfully')
        
    elif request.method == 'POST' and 'delete' in request.POST:
        id = 'id' in request.POST and request.POST['id']
        todolist.objects.filter(pk=id).delete()
        messages.success(request, 'Items removed successfully')
        
    elif request.method == 'POST' and 'edit' in request.POST:
        id = 'id' in request.POST and request.POST['id']
        title = 'title' in request.POST and request.POST['title']
        desc = 'desc' in request.POST and request.POST['desc']
        price = 'price' in request.POST and request.POST['price']
        
        edit = todolist.objects.get(pk=id)
        edit.item_title = title
        edit.description = desc
        edit.item_price = price
        edit.save()
        messages.success(request, 'Items updated successfully')
        
    all_items = todolist.objects.all()
    count = todolist.objects.count()
    expand = todolist.objects.values_list('item_price')
    
    return render(request, 'todo.html', context={'all_items': all_items, 'count': count, 'expand': expand})