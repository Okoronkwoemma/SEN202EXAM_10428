from django.contrib import admin
from .models import Manager, Intern, Address

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'department', 'has_company_card')

@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mentor', 'internship_end')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('manager', 'intern', 'street', 'city', 'state', 'zip_code')
