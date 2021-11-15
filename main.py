from PIL import Image
from image_processor import ImageProcessor
from linedrawer import LineDrawer
import turtle

WIDTH = HEIGHT = 1000
ROWS, RESOLUTION, DENSITY = 50, 70, 0.7
filename = "faith1.jpg"

if __name__ == '__main__':
    image = Image.open(filename)
    processor = ImageProcessor(image)

    # Processing image
    processor.setSize(WIDTH, HEIGHT)
    processor.greyScale()
    # done

    root = turtle.Screen()
    root.setup(WIDTH, HEIGHT)
    pen = turtle.Turtle()
    pen.speed(0)
    drawer = LineDrawer(imageArray=processor.getArray(), width=WIDTH, height=HEIGHT, screen=root, turtle=pen)
    drawer.draw(ROWS, RESOLUTION, DENSITY)

    processor.saveImage("outImage.png")

