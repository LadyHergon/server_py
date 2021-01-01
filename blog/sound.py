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
    lineWidth = 8000/len(audio)
    if lineWidth < 0.01:
       lineWidth = 0.01
    plt.plot(time,audio,linewidth=lineWidth)       

    plt.savefig(figure, bbox_inches='tight',format="png")
    plt.close()
    return InMemoryUploadedFile(figure,'ImageField','image','image/jpeg',sys.getsizeof(figure),None)
def Duration(audioFile):
    Duration = lr.get_duration(y=None, sr=22050, S=None, n_fft=2048, hop_length=512, center=True, filename=audioFile)
    return Duration

def Fsize(audioFile):
    Fsize = lr.get_samplerate(audioFile)
    return Fsize

def Ftype(audioFile):
    rate = 44100
    data = np.random.uniform(-1, 1, size=(rate * 10, 2))
    Ftype = sf.write(audioFile, data, lr.get_samplerate(audioFile), subtype='PCM_24')
    return Ftype

def SampFreq(audioFile):
    audio, sfreq = lr.load(audioFile)
    return sfreq
