from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField, URLField
from django.db.models.fields.files import ImageField


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = ImageField(verbose_name="Imagen",upload_to="portafolio/images/")
    link = models.URLField(null=True, blank=True, verbose_name="Dirección web")
    type = models.CharField(max_length=100, default="web", verbose_name="Tipo")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title
# Create your models here.......

def get_embed_url(self):
        """Convierte una URL de YouTube en su formato de inserción"""
        if "youtube.com" in self.link or "youtu.be" in self.link:
            video_id = self.link.split("v=")[-1] if "v=" in self.link else self.link.split("/")[-1]
            return f"https://www.youtube.com/embed/{video_id}"
        return self.link