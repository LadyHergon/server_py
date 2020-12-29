from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()

from .sound import Sound
import uuid

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    audio = models.FileField(null=True, upload_to='./musics')
    image = models.ImageField(default='./audio-image/' + str(uuid.uuid4()) + ".png" ,
                            null=True, upload_to='./audio-image', storage=gd_storage)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

    def save(self,*args, **kwargs):
        super().save()

        audioFile = Sound(self.audio.path)
        audioFile.getImage(self.image.path)




