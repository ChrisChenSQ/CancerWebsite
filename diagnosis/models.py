from django.db import models

# Create your models here.


class Image(models.Model):
    image_name =models.TextField("Image_name", max_length=50)
    image_path = models.TextField("Image_path")

    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Image'