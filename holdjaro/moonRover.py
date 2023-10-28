import numpy as np

class self_driving_module():
    def __init__(self, rover, map):
        self.rover = rover
        self.map = map
        
    def drive_full_length(self):
        for i in range(self.rover.map.getMapShape()[1]-1):
            self.rover.step("f")
        

class moonRover():

    def __init__(self, mapSize):
        self.coord = [0, 0]
        self.direction = "N"
        self.map = map.fromShape(mapSize)

    def step(self, dir):
        if dir == "f":
            self.coord[1] = self.coord[1] + 1
            if self.coord[1] == self.map.getMapShape()[1]:
                self.coord[1] = 0
        elif dir == "b":
            self.coord[1] = self.coord[1] - 1
            if self.coord[1] == -1:
                self.coord[1] = self.map.getMapShape()[1] - 1

    def turn(self, dir):
        dirs = ["N","E","S","W"]
        dirID = 0
        
        for i in range(4):
            if self.direction == dirs[i]:
                dirID = i
                break
        
        if dir == "l":
            dirID -= 1
        elif dir == "r":
            dirID += 1
        
        if dirID == -1:
            dirID = 3
        elif dirID == 4:
            dirID = 0
            
        self.direction = dirs[dirID]
        
    
    def checkObstacle(self, map):
        if map.getMapInCoord(self.getCoordInFront()) == 1:
            return True
        else:
            return False

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
        
        if localCoord[0] == -1:
            localCoord[0] = self.map.getMapShape()[0]-1
        elif localCoord[1] == -1:
            localCoord[1] = self.map.getMapShape()[1]-1
        elif localCoord[0] == self.map.getMapShape()[0]:
            localCoord[0] = 0
        elif localCoord[1] == self.map.getMapShape()[1]:
            localCoord[1] = 0
                        
        return localCoord

class map():

    def __init__(self, inputMap="00000000|00000000|00000000|00000000|00000000|00000000|00000000|00000000|"):

        countLines = inputMap.count('|')
        countRows = round((len(inputMap)-countLines)/countLines)
        
        self.shape = (countLines,countRows)
        self.map = np.zeros(self.shape)
        
        x = 0
        y = 0
        
        for i in inputMap:
            if i == "|":
                x = x+1
                y = 0
            else:
                self.map[x, y] = i
                y = y+1
        
    @classmethod    
    def fromShape(cls, inputshape):            
        mapstring = ""
        for i in range(inputshape[0]):
            for x in range(inputshape[1]):
                mapstring += "0"
            mapstring += "|"
            
        return map(mapstring)
            
                
    def getMap(self):
        return self.map
    
    def getMapInCoord(self, coord):
        return self.map[coord[0], coord[1]]
    
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