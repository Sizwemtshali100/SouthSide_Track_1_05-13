from django.shortcuts import render, redirect
from . models import QA_Models
from django.contrib.auth.models import User
from . form import QA_Forms
from . decorations import allowed_user
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
@allowed_user(allowed_roles=['Manager','Agent'])
def Home(request):
    TheData = QA_Models.objects.all()
    return render(request, 'Home.html',
                  {'TheData':TheData})   
@login_required
@allowed_user(allowed_roles=['Manager','Agent'])
def MainPage(request):  
    TheForm = QA_Forms(request.POST)
    if request.method == 'POST':
        if TheForm.is_valid():
            TheSubmit = TheForm.save(commit=True)
            TheSubmit.Agents = request.user
            TheSubmit.save()
            return redirect(request, 'Home')  
    else:
        TheForm = QA_Forms()
    return render(request, 'MainPage.html', {'TheForm':TheForm})


@allowed_user(allowed_roles=['Manager','Agent'])
def DataInformation(request, id):
    TheDataInformation = QA_Models.objects.get(pk=id)
    return render(request, 'DataInformation.html',
                  {'TheDataInformation':TheDataInformation})
    
@allowed_user(allowed_roles=['Manager'])
def Dashboard(request): 
    QAOutcomesProduct = QA_Models.objects.filter(KPA_1='Product').count()
    QAOutcomesPass = QA_Models.objects.filter(KPA_1='Pass').count()
    QAOutcomesCompliance = QA_Models.objects.filter(KPA_1='Compliance').count()
    QAOutcomesDC = QA_Models.objects.filter(KPA_1='Data Capturing').count()
    QAOutcomesTCF = QA_Models.objects.filter(KPA_1='TCF').count()
    return render(request, 'Dashboard.html',
                  {'QAOutcomesProduct':QAOutcomesProduct,
                   'QAOutcomesPass':QAOutcomesPass,
                   'QAOutcomesCompliance':QAOutcomesCompliance,
                   'QAOutcomesDC':QAOutcomesDC,
                   'QAOutcomesTCF':QAOutcomesTCF}) 

@allowed_user(allowed_roles=['Manager'])
def Summary(request): 
    QAOutcomesProduct = QA_Models.objects.filter(KPA_1='Product').count()
    QAOutcomesPass = QA_Models.objects.filter(KPA_1='Pass').count()
    QAOutcomesCompliance = QA_Models.objects.filter(KPA_1='Compliance').count()
    QAOutcomesDC = QA_Models.objects.filter(KPA_1='Data Capturing').count()
    QAOutcomesTCF = QA_Models.objects.filter(KPA_1='TCF').count()
    return render(request, 'Summary.html',
                  {'QAOutcomesProduct':QAOutcomesProduct,
                   'QAOutcomesPass':QAOutcomesPass,
                   'QAOutcomesCompliance':QAOutcomesCompliance,
                   'QAOutcomesDC':QAOutcomesDC,
                   'QAOutcomesTCF':QAOutcomesTCF})
       
    
    
