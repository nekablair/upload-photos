from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='django_uploads/files/covers') 