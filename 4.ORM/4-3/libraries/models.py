from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=10)
    pubdate = models.DateField()
    price = models.IntegerField()
    adult = models.BooleanField()

    def __str__(self):
        return self.title