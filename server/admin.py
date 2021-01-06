from django.contrib import admin
from .models import *
# Register your models here.

class EnAdminL(admin.StackedInline):
    model = Configuration
    extra = 2

class EnAdmin(admin.ModelAdmin):
    inlines = [EnAdminL]

admin.site.register(Engines, EnAdmin)