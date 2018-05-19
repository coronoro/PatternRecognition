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
    allImages = []
    allDetect = []
    testPath = pathToImages
    for dirpath, dirnames, filenames in os.walk(testPath):
        for dir in dirnames:
            if Modus.TRAINING.value in dir:
                images, detect = getImages(testPath+"/"+dir)
                allImages.append(images)
                allDetect.append(detect)
    return allImages, allDetect


def getImages(path):
    images = []
    detect = []
    for dirpath ,_, files in os.walk(path):
        for file in files:
            images.append(ndimage.imread(path + "/" + file))
            if "ohne" in dirpath:
                detect.append(False)
            else:
                detect.append(True)
    return images, detect
