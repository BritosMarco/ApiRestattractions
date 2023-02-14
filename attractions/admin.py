from django.contrib import admin
from .models import Attractions


class AttractionsAdmin(admin.ModelAdmin):
    list_display = ['name', 'opening_hours', 'minimun_age']
    # opção de pesquisar campos
    search_fields = ['name']


admin.site.register(Attractions, AttractionsAdmin)
