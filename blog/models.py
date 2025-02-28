from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    url = models.URLField(blank=True , null= True)  # Para almacenar el enlace de YouTube
    archivo = models.FileField(upload_to='blog/pdfs', blank=True ,null=True)  # Guarda los archivos en la carpeta "blog/pdfs/"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog/images', null=True, blank=True)
    date=models.DateTimeField(datetime.datetime.today)
    
    def __str__(self):
        return self.title
    
    def get_embed_url(self):
        """Convierte una URL de YouTube en su formato de inserción"""
        if "youtube.com" in self.url or "youtu.be" in self.url:
            video_id = self.url.split("v=")[-1] if "v=" in self.url else self.url.split("/")[-1]
            return f"https://www.youtube.com/embed/{video_id}"
        return self.url