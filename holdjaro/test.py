import unittest
import moonRover as mr


class TestSum(unittest.TestCase):
    
    def test_forward_step(self):
        myMap = mr.map()
        x = mr.moonRover(myMap.shape, myMap)
        x.step("f")
        self.assertEqual(x.coord,[0,1])

    def test_backwards_step(self):
        myMap = mr.map()
        x = mr.moonRover(myMap.shape, myMap)
        x.coord = [4,4]
        x.step("b")
        self.assertEqual(x.coord,[4,3])

    def test_forwards_step_edge(self):
        myMap = mr.map()
        x = mr.moonRover(myMap.shape, myMap)
        x.coord = [0,7]
        x.step("f")
        self.assertEqual(x.coord,[0,0])

    def test_backwards_step_edge(self):
        myMap = mr.map()
        x = mr.moonRover(myMap.shape, myMap)
        x.coord = [0,0]
        x.step("b")
        self.assertEqual(x.coord,[0,7])

    def test_turn_left(self):
        myMap = mr.map()
        x = mr.moonRover(myMap.shape, myMap)
        x.coord = [0,0]
        x.turn("l")
        self.assertEqual(x.coord,[0,0])
        self.assertEqual(x.direction, "W")

    def test_turn_right(self):
        myMap = mr.map()
        x = mr.moonRover(myMap.shape, myMap)
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
        rover = mr.moonRover(myMap.getMapShape(), myMap)
        rover.coord = [0,2]
        rover.turn("l")
        self.assertEqual(rover.getCoordInFront(), [1,2])
        
    def test_in_front_coords_2(self):
        myMap = mr.map()
        rover = mr.moonRover(myMap.getMapShape(), myMap)
        rover.coord = [0,2]
        rover.turn("r")
        self.assertEqual(rover.getCoordInFront(), [7,2])
       
    def test_obstacle_detection(self):
        givenMap = "00010000|00010000|00010000|00010000|00010000|00010000|00010000|00010000|"
        myMap = mr.map(givenMap)
        rover = mr.moonRover(myMap.getMapShape(), myMap)
        rover.coord = [2,2]
        rover.turn("l")
        self.assertEqual(rover.checkObstacle(), True)
        
    def test_obstacle_detection_2(self):
        givenMap = "10000000|01000000|00100000|00010000|00001000|00000100|00000010|00000001|"
        myMap = mr.map(givenMap)
        rover = mr.moonRover(myMap.getMapShape(), myMap)
        rover.coord = [1,0]
        rover.turn("l")
        self.assertEqual(rover.checkObstacle(), False)
        
    def test_self_driving_init(self):
        givenMap = "10000000|01000000|00100000|00010000|00001000|00000100|00000010|00000001|"
        myMap = mr.map(givenMap)
        rover = mr.moonRover(myMap.getMapShape(), myMap)
        sdm = mr.self_driving_module(rover, myMap)
        self.assertEqual(sdm.rover.map.getMapAsString(), mr.map.fromShape(myMap.getMapShape()).getMapAsString())
        self.assertEqual(sdm.map.getMapAsString(), givenMap)
        
    def test_self_driving_movement_1(self):
        myMap = mr.map()
        rover = mr.moonRover(myMap.getMapShape(), myMap)
        sdm = mr.self_driving_module(rover, myMap)
        sdm.drive_full_length()
        self.assertEqual(sdm.rover.coord, [0,7])

    def test_self_driving_movement_2(self):
        myMap = mr.map()
        rover = mr.moonRover(myMap.getMapShape(), myMap)
        sdm = mr.self_driving_module(rover, myMap)
        sdm.drive_full_length_circle()
        self.assertEqual(sdm.rover.coord, [1,0])
    
    def test_self_driving_movement_3(self):
        givenMap = "00000000|01000000|00000000|00010000|00000000|00000100|00000000|00000001|"
        myMap = mr.map(givenMap)
        rover = mr.moonRover(myMap.getMapShape(), myMap)
        sdm = mr.self_driving_module(rover, myMap)
        sdm.drive_full_length_circle()
        self.assertEqual(sdm.rover.coord, [1,7])
        
    def test_self_driving_movement_4(self):
        givenMap = "00000000|01000000|00000000|00010000|00000000|00000100|00000000|00000001|"
        outputMap ="55000000|51000000|55000000|55000000|55000000|55000000|55000000|55000000|"
        myMap = mr.map(givenMap)
        rover = mr.moonRover(myMap.getMapShape(), myMap)
        sdm = mr.self_driving_module(rover, myMap)
        sdm.drive_full_length_circle()
        self.assertEqual(sdm.rover.map.getMapAsString(), outputMap)
        self.assertEqual(sdm.rover.coord, [1,7])
        
    def test_full_self_driving_movement_1(self):
        givenMap = "00000000|01000000|00000000|00010000|00000000|00000100|00000000|00000001|"
        outputMap ="55555555|51555555|55555555|55515555|55555555|55555155|55555555|55555551|"
        myMap = mr.map(givenMap)
        rover = mr.moonRover(myMap.getMapShape(), myMap)
        sdm = mr.self_driving_module(rover, myMap)
        sdm.drive_full_map()
        self.assertEqual(sdm.rover.map.getMapAsString(), outputMap)
        
    def test_full_self_driving_movement_2(self):
        givenMap = "00000010|00010000|01000000|00000100|00010000|00000010|00100000|00000010|00010000|01000000|00000001|00001000|00100000|10000000|00010000|00000100|00000001|01000000|00001000|10000000|"
        outputMap ="55555515|55515555|51555555|55555155|55515555|55555515|55155555|55555515|55515555|51555555|55555551|55551555|55155555|15555555|55515555|55555155|55555551|51555555|55551555|15555555|"
        myMap = mr.map(givenMap)
        rover = mr.moonRover(myMap.getMapShape(), myMap)
        sdm = mr.self_driving_module(rover, myMap)
        sdm.drive_full_map()
        self.assertEqual(sdm.rover.map.getMapAsString(), outputMap)
        
if __name__ == '__main__':
    unittest.main()