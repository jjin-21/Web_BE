from PIL import Image
from io import BytesIO
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(upload_to='article_thumbnails/', blank=True, null=True)  # 썸네일 필드 추가
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.image:
            image = Image.open(self.image)
            if image.width > 100 or image.height > 100:
                output = BytesIO()
                image.thumbnail((100, 100))
                image.save(output, format='JPEG', quality=90)
                output.seek(0)
                self.image = InMemoryUploadedFile(output, 'ImageField', f"{self.image.name.split('.')[0]}_thumbnail.jpg", 'image/jpeg', sys.getsizeof(output), None)
        super(Article, self).save(*args, **kwargs)