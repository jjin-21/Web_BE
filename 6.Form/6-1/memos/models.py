from django.db import models

# Create your models here.
class Memo(models.Model):
    memo = models.TextField()
    summary = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)