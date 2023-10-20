from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=30)
    synopsis = models.TextField()
    image = models.ImageField(upload_to='movie_images/', blank=True, null=True)  # 원본 이미지 필드
    thumbnail = models.ImageField(upload_to='movie_thumbnails/', blank=True, null=True)  # 썸네일 필드

    def save(self, *args, **kwargs):
        if self.image:
            image = Image.open(self.image)
            # 이미지 크기가 200x200 이상인 경우 크기를 조절
            if image.width > 200 or image.height > 200:
                output = BytesIO()
                image.thumbnail((200, 200))
                image.save(output, format='JPEG', quality=90)
                output.seek(0)
                self.thumbnail = InMemoryUploadedFile(output, 'ImageField', f"{self.image.name.split('.')[0]}_thumbnail.jpg", 'image/jpeg', sys.getsizeof(output), None)
        super(Movie, self).save(*args, **kwargs)
