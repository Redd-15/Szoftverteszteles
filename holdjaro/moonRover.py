import numpy as np

class self_driving_module():
    def __init__(self, rover, map):
        self.rover = rover
        self.map = map
        
    def drive_full_length(self):
        for i in range(self.rover.map.getMapShape()[1]-1):
            self.rover.step("f")
        
    def drive_full_length_circle(self):
        for i in range(self.rover.map.getMapShape()[1]-1):
            self.rover.step("f")
        self.rover.turn("l")
        self.rover.step("f")
        self.rover.turn("l")
        for i in range(self.rover.map.getMapShape()[1]-1):
            self.rover.step("f")
            
    def drive_full_map(self):
        while self.rover.map.getMapAsString().count("0") > 0:
            for i in range(self.rover.map.getMapShape()[1]-1):
                self.rover.step("f")
            self.rover.turnAround()
            print(self.rover.map.map)

class moonRover():

    def __init__(self, mapSize, RealMap:map):
        self.coord = [0, 0]
        self.direction = "N"
        self.map = map.fromShape(mapSize)
        self.RealMap = RealMap

    def step(self, dir):
                
        add = 0
        if dir == "f":
            add = 1
            if self.checkObstacle():
                self.obstacleAvoidance()
                return
            
        elif dir == "b":
            add = -1
        
        if self.direction == "N":
            self.coord[1] = self.coord[1] + add
        elif self.direction == "S":
            self.coord[1] = self.coord[1] - add
        elif self.direction == "W":
            self.coord[0] = self.coord[0] + add
        elif self.direction == "E":
            self.coord[0] = self.coord[0] - add
        
        
        if self.coord[1] < 0:
            self.coord[1] = self.map.getMapShape()[1] - 1
        elif self.coord[1] == self.map.getMapShape()[1]:
            self.coord[1] = 0
        elif self.coord[0] < 0:
            self.coord[0] = self.map.getMapShape()[0] - 1
        elif self.coord[0] == self.map.getMapShape()[0]:
            self.coord[0] = 0

    def turnAround(self):
        if self.direction == "N":
            self.turn("l")
            self.step("f")
            self.turn("l")
        elif self.direction == "S":
            self.turn("r")
            self.step("f")
            self.turn("r")
        
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
        
    def checkObstacle(self):
        
        if round(self.RealMap.getMapInCoord(self.getCoordInFront())) == 1:
            self.map.modify(self.getCoordInFront(), 1)
            return True
        else:
            self.map.modify(self.getCoordInFront(), 5)
            return False

    def obstacleAvoidance(self):
        self.turn("l")
        self.step("f")
        self.turn("r")
        self.step("f")
        self.step("f")
        self.turn("r")
        self.step("f")
        self.turn("l")

    def getCoordInFront(self):
        localCoord = [self.coord[0], self.coord[1]]
        
        if self.direction == "N":
            localCoord[1] += 1
            
        elif self.direction == "S":
            localCoord[1] -= 1
        
        elif self.direction == "W":
            localCoord[0] += 1    
        
        elif self.direction == "E":
            localCoord[0] -= 1
            
        
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
            
    def modify(self, coords, item):
        self.map[coords[1], coords[0]] = item
                
    def getMap(self):
        return self.map
    
    def getMapInCoord(self, coord):
        return self.map[coord[1], coord[0]]
    
    def getMapShape(self):
        return self.shape
    
    def getMapAsString(self):
        output = ""
        
        for y in range(self.map.shape[0]):
            for x in range(self.map.shape[1]):
                output += str(round(self.map[y,x]))
            output += "|"
        
        return output
            
if __name__ == '__main__':
    
    myMap = map("00010000|00010000|00010000|00010000|00010000|00010000|00010000|00010000|")
    myMoonRover = moonRover(myMap.shape, myMap)
    print(myMap.getMapAsString())
    
    givenMap = "00010000|00010000|00010000|00010000|00010000|00010000|00010000|00010000|"
    myMap = map(givenMap)
    rover = moonRover(myMap.getMapShape(), myMap)
    rover.coord = [2,2]
    rover.turn("l")
    #rover.turn("r")
    print(rover.direction)
    print(rover.getCoordInFront())