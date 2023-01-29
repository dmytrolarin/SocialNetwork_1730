from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)