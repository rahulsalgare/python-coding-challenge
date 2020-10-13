from django.shortcuts import render
import requests
import json
from types import SimpleNamespace

# Create your views here.
def home(request):
    response = requests.get('http://127.0.0.1:8000/api/customer?format=json')
    data = response.json()
    response = requests.get('http://127.0.0.1:8000/api/cart/?format=json')
    orders = response.json()
    return render(request, 'front/dashboard.html', {"data":data, "orders":orders})

def products(request):
    return render(request, 'front/products.html')

def customerdetail(request,pk):
    response = requests.get("http://127.0.0.1:8000/api/customer/"+ pk)
    data = response.json()
    print(data)
    return render(request, 'front/customerdetail.html',{"data":data})

def createcustomer(request):
    return render(request, 'front/createcustomer.html')

def orderdelete(request, pk):
    return render(request, 'front/orderdelete.html',{'pk':pk})
