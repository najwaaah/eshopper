from django.contrib import admin
from .models import Client,contact,Carosuel

admin.site.register(Client)
# admin.site.register(contact)

@admin.register(contact)
class contactadmin(admin.ModelAdmin):
    list_display=('name','email','subject')


@admin.register(Carosuel)
class Carosueladmin(admin.ModelAdmin):
    list_display=('sub_content','main_content')