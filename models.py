from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from pathlib import Path
import os
from django_cleanup import cleanup  # django-cleanup 사용

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed_image = models.ImageField(upload_to='todo_images/', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='todo_images/thumbnails/', null=True, blank=True, default='path/to/default_thumbnail.jpg')

    def save(self, *args, **kwargs):
        # 이미지가 있다면 썸네일을 생성
        if self.completed_image:
            # Pillow 라이브러리로 이미지 열기
            img = Image.open(self.completed_image)
            
            # 썸네일 만들기
            thumbnail_name = f"{Path(self.completed_image.name).stem}_thumbnail.jpg"
            thumbnail_path = os.path.join('todo_images/thumbnails/', thumbnail_name)

            # 썸네일 크기 설정 (예: 100x100)
            img.thumbnail((100, 100))

            # 메모리 상에 저장
            thumb_io = BytesIO()
            img.save(thumb_io, 'JPEG')
            thumb_io.seek(0)

            # 이미지 저장
            self.thumbnail = InMemoryUploadedFile(thumb_io, 'ImageField', thumbnail_name, 'image/jpeg', thumb_io.tell(), None)

        super().save(*args, **kwargs)  # 부모 클래스의 save 호출

    def __str__(self):
        return self.title

