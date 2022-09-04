from django.db import models

class Video(models.Model):
    """ Видео
    """
    file = models.FileField(upload_to='media/videos/', verbose_name="Видео")
    caver = models.ImageField(upload_to='media/cavers/', verbose_name="Обложка")
    text = models.CharField(max_length=200,verbose_name="Описание")

    def __str__(self):
        return self.file.name


class Screenshots(models.Model):
    """ Скриншоты к видео
    """
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    screenshot = models.FileField(upload_to='media/screenshots/', verbose_name="Скриншот")

