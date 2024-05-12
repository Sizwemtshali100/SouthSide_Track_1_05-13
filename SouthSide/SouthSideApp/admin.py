from django.contrib import admin
from . models import CollectionModel
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(CollectionModel, ImportExportModelAdmin)
