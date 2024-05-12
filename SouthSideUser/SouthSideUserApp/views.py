from django.shortcuts import render
from collections import Counter
from . models import DataModel

# Create your views here.
def Home(request):
    TheDataView = DataModel.objects.all()
   #AegntCount = TheDataView.()
    return render(request, 'Home.html',
    {'egypt_count':egypt_count})

def Learning(request):
    TheDataView_EMEA = DataModel.objects.filter(Region="EMEA")
    TheDataView_LATAM = DataModel.objects.filter(Region="LATAM")
    TheDataView_APAC = DataModel.objects.filter(Region="APAC")
    TheDataView_NA = DataModel.objects.filter(Region="NA")
    
    egypt_count_EMEA_1 = TheDataView_EMEA.count()
    egypt_count_LATAM_1 = TheDataView_LATAM.count()
    egypt_count_NA_1 = TheDataView_APAC.count()
    egypt_count_APAC_1 = TheDataView_NA.count()
    return render(request, 'Learning.html',
    {'egypt_count_EMEA_1':egypt_count_EMEA_1,
     'egypt_count_LATAM_1':egypt_count_LATAM_1,
     'egypt_count_NA_1':egypt_count_NA_1,
     'egypt_count_APAC_1':egypt_count_APAC_1,
     })

def Dashboard_agent(request):

    ThePriceListData = []
    TheActualPrice = []
    TheCountriesLabel = []

    InData = DataModel.objects.all()[:10]
    for information in InData:
        TheCountriesLabel.append(information.Country)
        ThePriceListData.append(information.List_Price)
        #TheSalesAgent.append(information.Salesperson)
        TheActualPrice.append(information.Actual_Price)
    return render(request, 'Dashboard_agent.html',
    {
    'TheCountriesLabel':TheCountriesLabel,
    'ThePriceListData':ThePriceListData,
    #'TheSalesAgent':TheSalesAgent,
    'TheActualPrice':TheActualPrice,
    })

def Dashboard(request):
    #The View of the Country to Pricing
    ThePriceListData = []
    TheActualPrice = []
    TheCountriesLabel = []
    TheSalesAgent = []

    InData = DataModel.objects.all()[:10]
    for information in InData:
        TheCountriesLabel.append(information.Country)
        ThePriceListData.append(information.List_Price)
        TheSalesAgent.append(information.Salesperson)
        TheActualPrice.append(information.Actual_Price)
    return render(request, 'Dashboard.html',
    {'TheCountriesLabel':TheCountriesLabel,
    'ThePriceListData':ThePriceListData,
    'TheSalesAgent':TheSalesAgent,
    'TheActualPrice':TheActualPrice,
    })