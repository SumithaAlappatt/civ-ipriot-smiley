from smiley import Smiley

class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=Smiley.RED)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [42, 43, 44, 45] # straight 

        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):

        eyes = [9, 18, 21, 14]

        color = self.BLANK if wide_open else self.RED
        for pixel in eyes:
            self.pixels[pixel] = color

