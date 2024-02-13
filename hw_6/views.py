from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from hw_6.data import product


def mainPage(request):
    return render(request, 'mainPage.html')

def displayImage(request):
    return render(request, )

def getEntityById(request, id):
    productList = product.productList['productList']
    productItem = next((item for item in productList if item['id'] == id), None)

    if productItem is None:     #yes these paths are hardcoded but whatever they're just a quick quality of life change
        return HttpResponse("Product with specified id not found :( <a href='http://127.0.0.1:8000/hw_6/entities/'> view product list</a>")

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


@csrf_exempt
def createEntity(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        price = request.POST.get('price').replace(',', '.')
        category = request.POST.get('category')
        description = request.POST.get('description')
        availability = request.POST.get('availability') == 'True'
        productId = request.POST.get('id')

        try:
            price = float(price)
        except ValueError:
            return HttpResponse("Invalid price format :( <a href='http://127.0.0.1:8000/hw_6/entities/'> view product list</a>")

        newProduct = {
            'name': name,
            'price': price,
            'category': category,
            'description': description,
            'availability': availability,
            'id': productId
        }

        product.productList['productList'].append(newProduct)

        return render(request, 'displayEntities.html', {'products': [newProduct]})
    else:
        return HttpResponse("Something went wrong :( <a href='http://127.0.0.1:8000/hw_6/entities/'> view product list</a>")


def listAllEntities(request):
    return render(request, 'displayEntities.html', {'products': product.productList['productList']})


def testing(request):
    return HttpResponse("Very kind and nice words :)")
