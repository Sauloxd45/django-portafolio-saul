from django.contrib import admin
from .models import Project

# Register your models here.
admin.site.register(Project)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url')