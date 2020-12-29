from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

# from django.core.files.storage import default_storage as storage

permission =  GoogleDriveFilePermission(
   GoogleDrivePermissionRole.OWNER,
   GoogleDrivePermissionType.USER,
   "tanwai@django-skel.iam.gserviceaccount.com"
)
gd_storage = GoogleDriveStorage(permissions=(permission, ))

import numpy as np
import matplotlib.pyplot as plt
import librosa as lr
import os
import uuid

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    audio = models.FileField(null=True, upload_to='./musics')
    image = models.ImageField(default='audio-image/' + str(uuid.uuid4()) + ".png" ,
                            null=True, upload_to='audio-image', storage=gd_storage)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

    def save(self,*args, **kwargs):
        super().save()

        # audioFile = Sound(self.audio.name)
        audio, sfreq = lr.load(self.audio.path)   #Read the audiofile
        time = np.arange(0,len(audio))/sfreq    #create the time line
        fig, ax = plt.subplots()
        ax.plot(time, audio)    # Plot audio over time
        #ax.set(xlabel='Time(s)', ylabel='Amplitude')
        # fh = storage.open(self.image.name, "w")
        plt.savefig(self.image.path, bbox_inches='tight')       
        # audioFile.getImage(self.image.name)




