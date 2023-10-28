import unittest
import moonRover as mr


class TestSum(unittest.TestCase):
    
    def test_forward_step(self):
        myMap = mr.map()
        x = mr.moonRover(myMap.shape)
        x.step("f")
        self.assertEqual(x.coord,[0,1])

    def test_backwards_step(self):
        myMap = mr.map()
        x = mr.moonRover(myMap.shape)
        x.coord = [4,4]
        x.step("b")
        self.assertEqual(x.coord,[4,3])

    def test_forwards_step_edge(self):
        myMap = mr.map()
        x = mr.moonRover(myMap.shape)
        x.coord = [0,7]
        x.step("f")
        self.assertEqual(x.coord,[0,0])

    def test_backwards_step_edge(self):
        myMap = mr.map()
        x = mr.moonRover(myMap.shape)
        x.coord = [0,0]
        x.step("b")
        self.assertEqual(x.coord,[0,7])

    def test_turn_left(self):
        myMap = mr.map()
        x = mr.moonRover(myMap.shape)
        x.coord = [0,0]
        x.turn("l")
        self.assertEqual(x.coord,[0,0])
        self.assertEqual(x.direction, "W")

    def test_turn_right(self):
        myMap = mr.map()
        x = mr.moonRover(myMap.shape)
        x.coord = [0,0]
        x.turn("r")
        self.assertEqual(x.coord,[0,0])
        self.assertEqual(x.direction, "E")
    
    def test_init_given_8x8_map(self):
       givenMap = "00010000|00010000|00010000|00010000|00010000|00010000|00010000|00010000|"
       myMap = mr.map(givenMap)
       self.assertEqual(myMap.getMapAsString(), givenMap)
       
    def test_init_given_10x9_map(self):
       givenMap = "000100001|000100001|000100001|000100001|000100001|000100001|000100001|000100001|000100001|000100001|"
       myMap = mr.map(givenMap)
       self.assertEqual(myMap.getMapAsString(), givenMap)
       self.assertEqual(myMap.getMapShape(), (10,9))
       
    def test_in_front_coords(self):
        myMap = mr.map()
        rover = mr.moonRover(myMap.getMapShape())
        rover.coord = [0,2]
        rover.turn("r")
        self.assertEqual(rover.getCoordInFront(), [0,3])
        
    def test_in_front_coords_2(self):
        myMap = mr.map()
        rover = mr.moonRover(myMap.getMapShape())
        rover.coord = [0,2]
        rover.turn("r")
        rover.turn("r")
        self.assertEqual(rover.getCoordInFront(), [7,2])
       
    def test_obstacle_detection(self):
        givenMap = "00010000|00010000|00010000|00010000|00010000|00010000|00010000|00010000|"
        myMap = mr.map(givenMap)
        rover = mr.moonRover(myMap.getMapShape())
        rover.coord = [0,2]
        rover.turn("r")
        self.assertEqual(rover.checkObstacle(myMap), True)
        
    def test_obstacle_detection_2(self):
        givenMap = "10000000|01000000|00100000|00010000|00001000|00000100|00000010|00000001|"
        myMap = mr.map(givenMap)
        rover = mr.moonRover(myMap.getMapShape())
        rover.coord = [1,0]
        rover.turn("l")
        self.assertEqual(rover.checkObstacle(myMap), False)
        
    def test_self_driving_init(self):
        givenMap = "10000000|01000000|00100000|00010000|00001000|00000100|00000010|00000001|"
        myMap = mr.map(givenMap)
        rover = mr.moonRover(myMap.getMapShape())
        sdm = mr.self_driving_module(rover, myMap)
        self.assertEqual(sdm.rover.map.getMapAsString(), mr.map.fromShape(myMap.getMapShape()).getMapAsString())
        self.assertEqual(sdm.map.getMapAsString(), givenMap)
        
        
if __name__ == '__main__':
    unittest.main()