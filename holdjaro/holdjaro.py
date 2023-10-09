import numpy as np


class moonRover():

    def __init__(self, mapSize):
        self.coord = [0, 0]
        self.direction = "N"
        self.mapShape = mapSize
        self.map = np.zeros(self.mapShape)

    def step(self, dir):
        if dir == "f":
            self.coord[1] = self.coord[1] + 1
            if self.coord[1] == self.mapShape[1]:
                self.coord[1] = 0
        elif dir == "b":
            self.coord[1] = self.coord[1] - 1
            if self.coord[1] == -1:
                self.coord[1] = self.mapShape[1] - 1

    def turn(self, dir):
        if dir == "l":
            self.direction = "W"
        elif dir == "r":
            self.direction = "E"


class map():

    def __init__(self):

        MAP = "00000000|00000000|00000000|00000000|00000000|00000000|00000000|00000000|"
        MAPSHAPE = (8,8)

        self.shape = MAPSHAPE
        self.map = np.zeros(self.shape)
        
        x = 0
        y = 0
        for i in MAP:
            if i == "0":
                self.map[x, y] = i
                x = x+1
            if i == "|":
                y = y+1
                x = 0

        

myMap = map()
myMoonRover = moonRover(myMap.shape)