import numpy as np
import scipy.ndimage as ndimage
from enum import Enum
import os
import os.path



pathToImages = "../images/Graffiti_mit_ohne"

class Modus(Enum):
    TEST = "Test"
    TRAINING =  "Training"

def loadTestImages():
    images = []
    testPath = pathToImages
    for dirpath, dirnames, filenames in os.walk(testPath):
        for dir in dirnames:
            if Modus.TRAINING.value in dir:
                images.append(getImages(testPath+"/"+dir))
    return images


def getImages(path):
    images = []
    for _,_, files in os.walk(path):
        for file in files:
            images.append(ndimage.imread(path+"/"+file))
    return images

print(loadTestImages()     )