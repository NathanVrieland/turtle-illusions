import numpy as np
from PIL import Image

class ImageProcessor:

    def __init__(self, image):
        self.image = image
        self.imageArray = np.asarray(self.image)
        self.width = self.imageArray.shape[0]
        self.height = self.imageArray.shape[1]
        self.channels = self.imageArray.shape[2]

    def greyScale(self):
        for i in range(self.width):
            for j in range(self.height):
                average = 0
                for k in range(self.channels):
                    average += self.imageArray[i][j][k]
                average /= self.channels
                for k in range(self.channels):
                    self.imageArray[i][j][k] = average

    def twoTone(self, percent):
        limit = int((percent * 255) / 100)
        for i in range(self.width):
            for j in range(self.height):
                average = 0
                for k in range(self.channels):
                    average += self.imageArray[i][j][k]
                average /= self.channels
                for k in range(self.channels):
                    if average < limit:
                        average = 0
                    else:
                        average = 255
                    self.imageArray[i][j][k] = average

# this does not work in the slightest
    # def changeBrightness(self, percent):
    #     change = int((percent * 255) / 100)
    #     for i in range(self.width):
    #         for j in range(self.height):
    #             for k in range(self.channels):
    #                 self.imageArray[i][j][k] += change


    def setSize(self, width, height, channels = 3):
        newArray = np.ndarray((width, height, channels), dtype=np.uint8)
        for i in range(width):
            for j in range(height):
                for k in range(channels):
                    newArray[i][j][k] = self.imageArray[int((i / width) * self.width)][int((j / height) * self.height)][k]
        self.__setNewArray(newArray)

    def __setNewArray(self, newArray):
        shape = newArray.shape
        self.imageArray = newArray
        self.width = shape[0]
        self.height = shape[1]
        self.channels = shape[2]

    def reset(self):
        self.imageArray = np.asarray(self.image)
        self.__setNewArray(self.imageArray)

    def getArray(self):
        return self.imageArray

    def export(self):
        return Image.fromarray(self.imageArray)

    def saveImage(self, filename):
        saveImage = Image.fromarray(self.imageArray)
        saveImage.save(filename)

if __name__ == '__main__':
    filename = "faith1.jpg"
    image = Image.open(filename)
    processor = ImageProcessor(image)
    processor.greyScale()
    processor.saveImage("outImage.png")