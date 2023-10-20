<<<<<<< HEAD

from django.db import models

# Create your models here.
class Memo(models.Model):
    summary = models.CharField(max_length=20)
    memo = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
=======

from django.db import models

# Create your models here.
class Memo(models.Model):
    summary = models.CharField(max_length=20)
    memo = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
>>>>>>> 839d8730f0ca103e47c95ab8477c42cb69f4f5e6
    