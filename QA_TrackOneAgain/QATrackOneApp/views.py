from django.shortcuts import render, redirect
from . models import QA_Models
from django.contrib.auth.models import User
from . forms import QA_Forms
from django.contrib.auth.decorators import login_required
from . decorators import allowed_user
import csv
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='LoginUser')
@allowed_user(allowed_roles=['Manager','Agent'])
def Home(request):
    TheData = QA_Models.objects.all()
    return render(request, 'Home.html',
                  {'TheData':TheData})  

@login_required(login_url='LoginUser')
@allowed_user(allowed_roles=['Manager','Agent'])     
def MainPage(request):  
    TheForm = QA_Forms(request.POST)
    TheData = QA_Models.objects.all()
    if request.method == "POST":
        if TheForm.is_valid():
            TheSubmit = TheForm.save(commit=True)
            TheSubmit.Agents = request.user
            TheSubmit.save()
            return redirect('Home')
    else:
        TheForm = QA_Forms()
    return render(request, 'MainPage.html', {'TheForm':TheForm})

@login_required(login_url='LoginUser')
@allowed_user(allowed_roles=['Manager','Agent'])
def DataInformation(request, id):
    TheDataInformation = QA_Models.objects.get(pk=id)
    return render(request, 'DataInformation.html',
                  {'TheDataInformation':TheDataInformation})
    
@login_required(login_url='LoginUser')
@allowed_user(allowed_roles=['Manager'])   
def Dashboard(request): # This is the page for the bars and charts.
    QAAgentsCount = User.objects.all() #Pull all users 
    
    AgentSubmission = {} # Important list creation
    for users in QAAgentsCount:
        Count = QA_Models.objects.filter(Agents=users).count() # Counting the number of users
        AgentSubmission[users.username] = Count #linking the count to the users
        
    labels = list(AgentSubmission.keys()) # list of all users
    data = list(AgentSubmission.values())  # lists of all data to the users  

    return render(request, 'Dashboard.html',
                  {'labels':labels, 'data':data}) 

@login_required(login_url='LoginUser')
@allowed_user(allowed_roles=['Manager'])
def Summary(request):
    QAAgentsCount = User.objects.all()
    AgentSubmission = {}
    for users in QAAgentsCount:
        Count = QA_Models.objects.filter(Agents=users).count()
        AgentSubmission[users.username] = Count
    #First Compliance outcomes    
    QAOutcomesProduct = QA_Models.objects.filter(KPA_1='Product').count()
    QAOutcomesPass = QA_Models.objects.filter(KPA_1='Pass').count()
    QAOutcomesCompliance = QA_Models.objects.filter(KPA_1='Compliance').count()
    QAOutcomesDC = QA_Models.objects.filter(KPA_1='Data Capturing').count()
    QAOutcomesTCF = QA_Models.objects.filter(KPA_1='TCF').count()
    #HIV tests
    QAHIVYES = QA_Models.objects.filter(HIV_Required='YES').count()
    QAHIVNO = QA_Models.objects.filter(HIV_Required='NO').count()
    return render(request, 'Summary.html',
                  {'QAHIVYES':QAHIVYES,
                   'QAHIVNO':QAHIVNO,
                   'QAOutcomesProduct':QAOutcomesProduct,
                   'QAOutcomesPass':QAOutcomesPass,
                   'QAOutcomesCompliance':QAOutcomesCompliance,
                   'QAOutcomesDC':QAOutcomesDC,
                   'QAOutcomesTCF':QAOutcomesTCF})
    
@login_required(login_url='LoginUser')
@allowed_user(allowed_roles=['Manager','Agent'])       
def Download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['content-disposition'] = 'attachment; filename=Outcome_QA.csv'

    writer = csv.writer(response)
    Downloading_all = QA_Models.objects.all()
    writer.writerow(['Date',
                     'Agents',
                     'Policy_Number',
                     'Case_Number',
                    'SalesAgent',
                    'AVS_Check',
                    'Caller_ID',
                    'Call_duration',
                    'Start_date',
                    'Premium',
                    'Debit_date',
                    'Cover_amount',
                    'QA_Correct',
                    'KPA_1',
                    'KPA_2',
                    'KPA_3',
                    'HIV_Required',
                    'Comment',
                    ])
    for download in Downloading_all:
        writer.writerow([download.Date,
                    download.Agents,
                    download.Policy_Number,
                    download.Case_Number,
                    download.SalesAgent,
                    download.AVS_Check,
                    download.Caller_ID,                   
                    download.Call_duration,
                    download.Start_date,
                    download.Premium,
                    download.Debit_date,
                    download.Cover_amount,
                    download.QA_Correct,
                    download.KPA_1,
                    download.KPA_2,
                    download.KPA_3,
                    download.HIV_Required,
                    download.Comment,

                    ])
    return response 
    