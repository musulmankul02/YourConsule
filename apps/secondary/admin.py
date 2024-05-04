from django.contrib import admin
from apps.secondary import models as secondary
# Register your models here.
class NewsFilterAdmin(admin.ModelAdmin):
    list_filter = ('descriptions', 'descriptions2')
    search_fields = ('descriptions', 'descriptions2')

class HistoryFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

class TeamFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', 'work')
    search_fields = ('title', 'work')

class legalinformationFilterAdmin(admin.ModelAdmin):
    list_filter = ('descriptions', 'descriptions2')
    search_fields = ('descriptions', 'descriptions2')

admin.site.register(secondary.Legalinformation, legalinformationFilterAdmin)
admin.site.register(secondary.News, NewsFilterAdmin)
admin.site.register(secondary.History, HistoryFilterAdmin)
admin.site.register(secondary.Year)
admin.site.register(secondary.Team, TeamFilterAdmin)
