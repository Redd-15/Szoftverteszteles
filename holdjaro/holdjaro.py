import numpy as np


MAP = "00000000|00000000|00000000|00000000|00000000|00000000|00000000|00000000|"

class holdjaro():

    def __init__(self):
        self.coord = (0, 0)
        self.direction = "N"
        self.map = np.zeros((8, 8))

    def step(self, dir):
        return


class map():

    def __init__(self):
        self.map = np.zeros((8, 8))
        x = 0
        y = 0
        for i in MAP:
            if i == "0":
                self.map[x, y] = i
                x = x+1
            if i == "|":
                y = y+1
                x = 0

        

x = map()
print (x.map)