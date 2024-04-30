from django.contrib import admin
from apps.base import models
from django.contrib.auth.models import User, Group
# Register your models here.
class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', 'phone', 'email')
    search_fields = ('title', 'phone', 'email')

class ReviewFilterAdmin(admin.ModelAdmin):
    list_filter = ('title',  'message')
    search_fields = ('title', 'message')

class SlideFilterAdmin(admin.ModelAdmin):
    list_filter = ('image', )
    search_fields = ('image', )

class NumbersFilterAdmin(admin.ModelAdmin):
    list_filter = ('client', 'team', 'experience', 'critical', 'review' )
    search_fields = ('client', 'team', 'experience', 'critical', 'review' )

class InjuryFilterAdmin(admin.ModelAdmin):
    list_filter = ('image', )
    search_fields = ('image', )

class SubjectFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

class LegalinsightsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', 'descriptions', 'image')
    search_fields = ('title', 'descriptions', 'image')

admin.site.register(models.Injury, InjuryFilterAdmin)
admin.site.register(models.Subject, SubjectFilterAdmin)
admin.site.register(models.Legalinsights, LegalinsightsFilterAdmin)
admin.site.register(models.Numbers, NumbersFilterAdmin)
admin.site.register(models.Settings, SettingsFilterAdmin)
admin.site.register(models.Service)
admin.site.register(models.Review, ReviewFilterAdmin)
admin.site.register(models.Slide, SlideFilterAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
