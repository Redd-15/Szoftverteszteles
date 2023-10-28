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

    def getCoordInFront(self):
        localCoord = self.coord
        
        if self.direction == "N":
            localCoord[0] +=1
        elif self.direction == "S":
            localCoord[0] -=1
        elif self.direction == "E":
            localCoord[1] +=1
        elif self.direction == "W":
            localCoord[1] -=1
        
        return localCoord

class map():

    def __init__(self, inputMap="00000000|00000000|00000000|00000000|00000000|00000000|00000000|00000000|"):

        countLines = inputMap.count('|')
        countRows = round((len(inputMap)-countLines)/countLines)
        
        self.shape = (countLines,countRows)
        self.map = np.zeros(self.shape)
        
        x = 0
        y = 0
        
        print(inputMap)
        for i in inputMap:
            if i == "|":
                x = x+1
                y = 0
            else:
                self.map[x, y] = i
                y = y+1
            
                
    def getMap(self):
        return self.map
    
    def getMapShape(self):
        return self.shape
    
    def getMapAsString(self):
        output = ""
        
        for i in range(self.map.shape[0]):
            for x in range(self.map.shape[1]):
                output += str(round(self.map[i,x]))
            output += "|"
        
        return output
            
if __name__ == '__main__':
    
    myMap = map("00010000|00010000|00010000|00010000|00010000|00010000|00010000|00010000|")
    myMoonRover = moonRover(myMap.shape)
    print(myMap.getMapAsString())