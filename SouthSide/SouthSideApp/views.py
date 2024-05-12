from django.shortcuts import render
from . models import CollectionModel

# Create your views here.
def Home(request):
    CollectionView = CollectionModel.objects.all()
    return render(request, 'Home.html',
    {'CollectionView':CollectionView})
