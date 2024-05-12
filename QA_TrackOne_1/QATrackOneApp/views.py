from django.shortcuts import render, redirect
from . models import QA_Models
from django.contrib.auth.models import User
from . forms import QA_Forms
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Home(request):        
    TheForm = QA_Forms(request.POST)
    data = QA_Models.objects.all()
    if request.method == "POST":
        if TheForm.is_valid():
            TheSubmit = TheForm.save(commit=True)
            TheSubmit.Agents = request.user
            TheSubmit.save()
            data = QA_Models.objects.all()
    else:
        TheForm = QA_Forms()
    return render(request, 'Home.html',
                  {'TheForm':TheForm,
                   'data':data})

