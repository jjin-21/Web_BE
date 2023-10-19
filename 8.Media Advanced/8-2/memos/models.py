
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

# Create your models here.
class Memo(models.Model):
    summary = models.CharField(max_length=20)
    memo = models.TextField()
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFit(200, 200)],
        format='JPEG',
        options={'quality': 90}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    