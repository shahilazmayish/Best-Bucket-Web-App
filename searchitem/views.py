from django.shortcuts import render
from .models import Product


def homepage(request):

    return render(request, "homepage.html", {"name": "Best Bucket"})



def searchproduct(request):
    query = str(request.GET['q'])
    product=Product.objects.filter(name__icontains=query)

    return render(request, "result.html", {'product': product})