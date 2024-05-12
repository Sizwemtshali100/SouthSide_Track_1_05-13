from . models import QA_Models  #, QAAgent
from django import forms
from django.forms import ModelForm


class QA_Forms(ModelForm):
    class Meta:
        model = QA_Models
        fields = ['Policy_Number',
                  'Date',
                  'Agents',
                  'Case_Number',
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
                  'Comment']     

        widgets = {

        }
        
            