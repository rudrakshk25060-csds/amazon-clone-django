from django.shortcuts import render

# Create your views here.
def product_show(request):
    return render(request, 'product.html')

def showId(request):
    return render(request, 'showid.html')
