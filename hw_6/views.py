from django.http import HttpResponse
from django.shortcuts import render
from hw_6.data import product


def getEntityById(request, id):
    productList = product.productList['productList']
    productItem = next((item for item in productList if item['id'] == id), None)

    if productItem is None:
        return HttpResponse("Product with specified id not found :(")

    return render(request, 'displayEntities.html', {'products': [productItem]})


def deleteEntityById(request, id):
    productList = product.productList['productList']
    initialLen = len(productList)

    for item in productList:
        if item['id'] == id:
            productList.remove(item)

    if(initialLen != len(productList)):
        return HttpResponse("Product deleted successfully <a href='http://127.0.0.1:8000/hw_6/entities/'> view product list</a>")
    else:
        return HttpResponse("Product not found :( <a href='http://127.0.0.1:8000/hw_6/entities/'> view product list</a>")


def createEntity(request):
    return HttpResponse('gamer')


def listAllEntities(request):
    return render(request, 'displayEntities.html', {'products': product.productList['productList']})


def testing(request):
    return HttpResponse("Very kind and nice words :)")
