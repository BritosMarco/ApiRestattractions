from django.contrib import admin

from .models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ['address1', 'city', 'country']
    # opção de pesquisar campos
    search_fields = ['country']


admin.site.register(Address, AddressAdmin )  # Register your models here.
