import turtle
import numpy as np

class LineDrawer:

    def __init__(self, imageArray, width, height, screen, turtle):
        self.array = imageArray
        self.width = width
        self.height = height
        self.screen = screen
        self.turtle = turtle

    def draw(self, rows, resolution, density = 0.75):
        DIMENSIONS = self.array.shape
        Y_SPACING = DIMENSIONS[0] // rows
        X_SPACING = DIMENSIONS[1] // resolution
        for i in range(self.height // 2, -self.height // 2, -Y_SPACING): # each row
            self.turtle.up()
            self.turtle.setpos( -self.width // 2, i)
            self.turtle.down()
            for j in range(self.width // X_SPACING): # each forward movement
                pos = self.getArrayPos()
                alpha = 0
                num = 0
                for k in range(X_SPACING):
                    for l in range(-Y_SPACING // 2, Y_SPACING // 2):
                        try:
                            alpha += self.array[int(pos[0]) + k][int(pos[1]) + l][0]
                            num += 1
                        except IndexError:
                            pass
                if num == 0:
                    num += 1
                self.turtle.width(Y_SPACING * density - (((alpha / num) / 255) * Y_SPACING * density))
                self.turtle.fd(X_SPACING)



        self.turtle.getscreen()._root.mainloop()

    def getArrayPos(self):
        turtlePos = self.turtle.pos()
        return np.abs(turtlePos[1] - self.width // 2), np.abs(turtlePos[0] + self.width // 2)


if __name__ == '__main__':
    pass