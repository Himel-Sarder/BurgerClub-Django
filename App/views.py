from django.shortcuts import render

def home(request):
    return render(request, 'home.html') 

from django.shortcuts import render
from .models import MenuItem

def menu(request):
    menu_items = MenuItem.objects.all()  # Fetch all menu items from the database
    return render(request, 'menu.html', {'menu_items': menu_items})
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')