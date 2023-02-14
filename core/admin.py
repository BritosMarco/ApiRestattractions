from django.contrib import admin
from .models import PontoTuristico


class CoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'approved']
    # opção de pesquisar campos
    search_fields = ['name']


admin.site.register(PontoTuristico, CoreAdmin)  # Register your models here.
