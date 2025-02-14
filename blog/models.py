from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog/images', null=True, blank=True)
    date=models.DateTimeField(datetime.datetime.today)
    
    def __str__(self):
        return self.title