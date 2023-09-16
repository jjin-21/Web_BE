from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.TextField(max_length=50)
    genre = models.TextField(max_length=10)

    def __str__(self):
        show = str(self.id) + '번글 - ' + str(self.title) + ' : (' + str(self.genre) + ')'
        return show