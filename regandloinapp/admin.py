from django.contrib import admin
from .models import Reg


# Register your models here.
class Regadmin(admin.ModelAdmin):
    list_display = ['Firstname', 'Lastname', 'username', 'Email', 'Password', 'mobileno']


admin.site.register(Reg, Regadmin)