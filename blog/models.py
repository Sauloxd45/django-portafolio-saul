from django.db import models
import datetime
from django.db import models
from embed_video.fields import EmbedVideoField
from urllib.parse import urlparse, parse_qs


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    url = models.URLField(blank=True ,null=True)  # Para almacenar el enlace de YouTube
    # video = EmbedVideoField()  # same like models.URLField()
    archivo = models.FileField(upload_to='blog/pdfs', blank=True ,null=True)  # Guarda los archivos en la carpeta "blog/pdfs/"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog/images', null=True, blank=True)
    date=models.DateTimeField(default=datetime.datetime.now)
    
    def __str__(self):
        return self.title
    
    # def get_embed_url(self):
    #     """Convierte una URL de YouTube en su formato de inserción"""
    #     if "youtube.com" in self.url or "youtu.be" in self.url:
    #         video_id = self.url.split("v=")[-1] if "v=" in self.url else self.url.split("/")[-1]
    #         return f"https://www.youtube.com/embed/{video_id}"
    #     return self.url
    
    
    def get_embed_url(self):
        """Convierte una URL de YouTube en su formato de inserción, extrayendo solo el ID del video."""
        if not self.url:
            return ""

        parsed_url = urlparse(self.url)
        
        # Para URLs tipo "https://www.youtube.com/watch?v=VIDEO_ID"
        if "youtube.com" in parsed_url.netloc:
            query_params = parse_qs(parsed_url.query)
            video_id = query_params.get("v")
            if video_id:
                return f"https://www.youtube.com/embed/{video_id[0]}"
        
        # Para URLs tipo "https://youtu.be/VIDEO_ID"
        elif "youtu.be" in parsed_url.netloc:
            video_id = parsed_url.path.lstrip("/")
            return f"https://www.youtube.com/embed/{video_id}"

        # Si no es una URL válida de YouTube, devolver la original
        return self.url