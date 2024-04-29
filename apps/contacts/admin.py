from django.contrib import admin
from apps.contacts import models as contacts
# Register your models here.

class ContactsFilterAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')
    list_filter = ('first_name','last_name')
    search_fields = ('first_name','last_name')

admin.site.register(contacts.Contacts, ContactsFilterAdmin)