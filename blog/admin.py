from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url')

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'archivo')