from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ItemForm
from .models import Item

def home(request):
    items = Item.objects.all()

    search = request.GET.get('search')

    if search:
        items = items.filter(name__icontains=search)

    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()

    return render(request, 'home.html', {
        'form': form,
        'items': items
    })

def hello(request):
    return HttpResponse("Hello World!")
