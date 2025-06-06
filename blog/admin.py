from django.contrib import admin
from .models import Post
from django.contrib import admin
from embed_video.admin import AdminVideoMixin


# Register your models here.
admin.site.register(Post)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url')

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'archivo')
    
    
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

