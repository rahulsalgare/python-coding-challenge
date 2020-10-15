from django.shortcuts import render
import requests


def home(request):
    response = requests.get('http://127.0.0.1:8000/api/customer?format=json')
    data = response.json()
    response = requests.get('http://127.0.0.1:8000/api/cart/?format=json')
    orders = response.json()
    return render(request, 'front/dashboard.html', {"data": data, "orders": orders})

def products(request):
    response = requests.get('http://127.0.0.1:8000/api/product')
    data = response.json()
    return render(request, 'front/products.html',{"products": data})

def customerdetail(request, pk):
    response = requests.get("http://127.0.0.1:8000/api/customer/" + pk)
    data = response.json()
    response = requests.get("http://127.0.0.1:8000/api/customer/" + pk + "/cart")
    cart = response.json()
    return render(request, 'front/customerdetail.html', {"data": data, "cart": cart})

def createcustomer(request):
    return render(request, 'front/createcustomer.html')

def orderdelete(request,ck,ok):
    print(ck, ok)
    return render(request, 'front/orderdelete.html', {'customer': ck,'order':ok})
