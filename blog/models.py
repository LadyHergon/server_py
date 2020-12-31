from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()

<<<<<<< HEAD
<<<<<<< HEAD
from .sound import Sound
import uuid

=======
>>>>>>> 5905079 (Moved logic to view)
=======
>>>>>>> c31c90e11e1db9a4bb82a880b2d1b152839d4c13
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    audio = models.FileField(null=True, upload_to='musics')
<<<<<<< HEAD
<<<<<<< HEAD
    image = models.ImageField(default='audio-image/' + str(uuid.uuid4()) + ".png" ,
                            null=True, upload_to='audio-image', storage=gd_storage)
=======
    image = models.ImageField(default="abc.png",null=True, upload_to='audio-image', storage=gd_storage)
>>>>>>> 5905079 (Moved logic to view)
=======
    image = models.ImageField(default="abc.png",null=True, upload_to='audio-image', storage=gd_storage)
>>>>>>> c31c90e11e1db9a4bb82a880b2d1b152839d4c13
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
<<<<<<< HEAD
<<<<<<< HEAD

    def save(self,*args, **kwargs):
        super().save()

        audioFile = Sound(self.audio.path)
        audioFile.getImage(self.image.path)
=======
        
>>>>>>> 5905079 (Moved logic to view)
=======
        
>>>>>>> c31c90e11e1db9a4bb82a880b2d1b152839d4c13




