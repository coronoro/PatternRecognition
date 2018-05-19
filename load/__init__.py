import numpy as np
import scipy.ndimage as ndimage
from enum import Enum
import os
import os.path


pathToImages = "C:/Users/Tim Streicher/Desktop/Mustererkennung"

class Modus(Enum):
    TEST = ""
    TRAINING = "/Graffiti_mit_ohne"

def loadTestImages():
    images = []
    testPath = pathToImages + Modus.TRAINING.value
    for dirpath, dirnames, filenames in os.walk(testPath):
        for dir in dirnames:
            if "Training" in dir:
                images.append(getImages(testPath+"/"+dir))
    return images


def getImages(path):
    images = []
    for _,_, files in os.walk(path):
        for file in files:
            images.append(ndimage.imread(path+"/"+file))
    return images

print(loadTestImages()     )