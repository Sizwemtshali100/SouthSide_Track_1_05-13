from django.contrib import admin
from . models import QA_Models
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(QA_Models, ImportExportModelAdmin)
