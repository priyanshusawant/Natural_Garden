from django.shortcuts import render
from django.http import HttpResponse
from plants.models import Item

# Create your views here.

def index(request):
    itemlist = Item.objects.all()

    context = {
        'itemlist':itemlist
    }

    return render(request, 'plants/index.html', context)

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)

    context = {
        'item':item
    }

    return render(request, 'plants/detail.html', context)
