from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from gdstorage.storage import GoogleDriveStorage
gd_storage = GoogleDriveStorage()
import os

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=160)
    date_posted = models.DateTimeField(default=timezone.now)
    audio = models.FileField(null=True, upload_to='musics', storage=gd_storage)
    image = models.ImageField(null=True, upload_to='audio-image', storage=gd_storage)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    duration = models.CharField(max_length=9)
    # f_size = models.TextField(null=True)
    samp_freq = models.DecimalField(null=True,max_digits=5,decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})


    # def save(self,*args, **kwargs):
    #     super().save()

    #     self.f_size = os.path.getsize(self.audio.path) >>10
    #     print(self.f_size)
    #     super(Post, self).save(*args, **kwargs)

    #     audioFile = Sound(self.audio.path)
    #     audioFile.getImage(self.image.path)




