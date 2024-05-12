from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AgentModel(models.Model):
    AgentName = models.CharField(max_length=50)

    def __str__(self):
        return str(self.AgentName)

class DataModel(models.Model):
    JE_Code = models.CharField(max_length=8, null=True)
    Store = models.CharField(max_length=20, default=False, null=False)
    Country = models.CharField(max_length=20, null=True)
    Region = models.CharField(max_length=20, default=False, null=False)
    Salesperson = models.CharField(max_length=20, default=False, null=False)
    Item = models.CharField(max_length=50, null=True)
    List_Price = models.IntegerField(null=True)
    Actual_Price = models.DecimalField(max_digits=10, decimal_places=2, default=False, null=False)

    def __str__(self):
        return str(self.JE_Code)

