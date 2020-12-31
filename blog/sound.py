import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.core.files.images import ImageFile
import numpy as np
from io import BytesIO
import librosa as lr
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

def Sound(audioFile):
    audio, sfreq = lr.load(audioFile)
    time = np.arange(0,len(audio))/sfreq
    figure = BytesIO()
    figure.seek(0)
    plt.plot(time,audio,linewidth=0.05)       

    plt.savefig(figure, bbox_inches='tight',format="png")
    plt.close()
    return InMemoryUploadedFile(figure,'ImageField','image','image/jpeg',sys.getsizeof(figure),None)
