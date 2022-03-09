import email
from math import prod
import re
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.template import context
from Home.models import Combos, Featured, Orders, Pizzas, Beverages
from datetime import datetime


# Create your views here.
def index(request):
    allcombos = Combos.objects.all()
    allfeatured = Featured.objects.all()
    # print(allcombos)
    context = {
        'combos':allcombos,
        'featured':allfeatured[:4]
    }
    return render(request, 'index.html', context=context)

def bookmeal(request):
    largepizzas = Pizzas.objects.filter(size='Large')
    mediumpizza = Pizzas.objects.filter(size='Medium')
    allbeverages = Beverages.objects.all()
    print(largepizzas)
    print(mediumpizza)
    context = {
        'large':largepizzas,
        'medium':mediumpizza,
        'bever':allbeverages,
    }
    return render(request, 'bookmeal.html', context)

def combos(request):
    return render(request, 'combos.html')

def tracking(request):
    return render(request, 'tracking.html')

def checkout(request, cfpb, id):
    if cfpb == 1:
        product = Combos.objects.filter(id = int(id))
        product = product[0]
        context = {
            'product_name':product.name,
            'price':product.price,
            'size':'Not Specified',
            'type':cfpb,
            'id':id
        }
    elif cfpb == 2:
        product = Featured.objects.filter(id=int(id))
        product = product[0]
        context = {
            'product_name':product.name,
            'price':product.price,
            'size':'Not Specified',
            'type':cfpb,
            'id':id
        }
    elif cfpb == 3:
        product = Pizzas.objects.filter(id=int(id))
        product = product[0]
        context = {
            'product_name':product.name,
            'price':product.price,
            'size':product.size,
            'type':cfpb,
            'id':id
        }
    elif cfpb == 4:
        product = Beverages.objects.filter(id=int(id))
        product = product[0]
        context = {
            'product_name':product.name,
            'price':product.price,
            'size':product.quantity,
            'type':cfpb,
            'id':id
        }
    else:
        return HttpResponse('Invalid Criterias')
    return render(request, 'checkout.html',context)

def booked(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        description = request.POST.get('description')
        price = request.POST.get('price')
        status = 1
        date_time= datetime.now()
        prdtype = request.POST.get('product_type')
        prdid = request.POST.get('product_id')

        order = Orders(name=name,
                        email=email,
                        phone=phone, 
                        desr=description,
                        address=address, 
                        totalamount=price,
                        datetime=date_time, 
                        status=status, 
                        productType = prdtype,
                        productId= prdid)
        order.save()
        ordernum = Orders.objects.all()
        last = len(ordernum)-1
        context = {
            'order':ordernum[last]
        }
        return render(request, 'success.html', context=context)

def tracked(request):
    if request.method == 'POST':
        orderid = request.POST.get('orderid')
        order = Orders.objects.filter(orderid=orderid)
        order = order[0]
        if order.status == 1:
            status = 'Booked'
        elif order.status == 2:
            status ='In the Kitchen'
        elif order.status == 3:
            status = 'On the way'
        elif order.status == 4:
            status =  'Delivered! Enjoy your food'
        else:
            status = 'LOSSTTTTTT! Sorry for the inconvenience'
        context = {
            'order':order,
            'status':status
        }
        return render(request, 'tracked.html', context=context)
    
