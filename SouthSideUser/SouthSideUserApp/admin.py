from django.contrib import admin
from . models import DataModel
from . models import AgentModel
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(DataModel, ImportExportModelAdmin)
admin.site.register(AgentModel)
