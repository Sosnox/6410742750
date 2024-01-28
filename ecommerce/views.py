from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''

    return HttpResponse('Welcome to 6410742750 Inthat Sriphao views!')

def item_view(request, item_id):
    context_data = {
        "item_id": item_id
        }
    return render(request, 'index.html', context=context_data)

def Home_Page(request):
    return render(request, 'Home.html')

def Contact_Page(request):
    return render(request, 'Contact.html')

def Category_Page(request):
    return render(request, 'Category.html')

def Checkout_Page(request):
    return render(request, 'Checkout.html')

def Product_Page(request):
    return render(request, 'Product.html')
