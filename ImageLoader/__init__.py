import numpy as np
import scipy.ndimage as ndimage
import scipy.misc as misc
from enum import Enum
import os
import os.path

limit = 700

pathToImages = "../images/Graffiti_mit_ohne"

class Modus(Enum):
    TEST = "Test"
    TRAINING =  "Training"

def loadTrainingImages():
    return loadImage(Modus.TRAINING)


def loadImage(modus:Modus):
    allImages = []
    allDetect = []
    testPath = pathToImages
    for dirpath, dirnames, filenames in os.walk(testPath):
        for dir in dirnames:
            if modus.value in dir:
                images, detect = getImages(testPath,dir)
                allImages.extend(images)
                allDetect.extend(detect)
    return np.array(allImages), np.array(allDetect)

def loadTestImages():
    return loadImage(Modus.TEST)

def getImages(path, dir):
    images = []
    detect = []
    temp = 0
    for dirpath ,_, files in os.walk(path+ "/" + dir):
        for file in files:
            if temp < limit:
                image = ndimage.imread(path + "/" + dir + "/" + file)
                image = misc.imresize(image,(100, 75))
                images.append(image)

                if "ohne" in dir:
                    detect.append(False)
                else:
                    detect.append(True)
                temp+=1
            else:
                break
    return images, detect
