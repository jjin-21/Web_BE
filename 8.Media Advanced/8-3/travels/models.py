from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class Travel(models.Model):
    location = models.CharField(max_length=10)
    plan = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/')
    image_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFit(100, 100)],
                                    format='JPEG',
                                    options={'quality': 90})
    start_date = models.DateField()
    end_date = models.DateField()
