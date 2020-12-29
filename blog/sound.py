import numpy as np
import matplotlib.pyplot as plt
import librosa as lr
import os

class Sound():

    def __init__(self, path):
        self.path = path

    def getImage(self,imgPath):
        audio, sfreq = lr.load(self.path)   #Read the audiofile
        time = np.arange(0,len(audio))/sfreq    #create the time line

        fig, ax = plt.subplots()
        ax.plot(time, audio)    # Plot audio over time
        #ax.set(xlabel='Time(s)', ylabel='Amplitude')
        plt.savefig(imgPath, bbox_inches='tight')

        return imgPath

    # def __del__(self):
        # os.remove(self.path)    #delete the file after processing
    