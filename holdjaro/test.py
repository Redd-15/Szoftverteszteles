import unittest
import moonRover


class TestSum(unittest.TestCase):
    
    def test_forward_step(self):
        myMap = moonRover.map()
        x = moonRover.moonRover(myMap.shape)
        x.step("f")
        self.assertEqual(x.coord,[0,1])

    def test_backwards_step(self):
        myMap = moonRover.map()
        x = moonRover.moonRover(myMap.shape)
        x.coord = [4,4]
        x.step("b")
        self.assertEqual(x.coord,[4,3])

    def test_forwards_step_edge(self):
        myMap = moonRover.map()
        x = moonRover.moonRover(myMap.shape)
        x.coord = [0,7]
        x.step("f")
        self.assertEqual(x.coord,[0,0])

    def test_backwards_step_edge(self):
        myMap = moonRover.map()
        x = moonRover.moonRover(myMap.shape)
        x.coord = [0,0]
        x.step("b")
        self.assertEqual(x.coord,[0,7])

    def test_turn_left(self):
        myMap = moonRover.map()
        x = moonRover.moonRover(myMap.shape)
        x.coord = [0,0]
        x.turn("l")
        self.assertEqual(x.coord,[0,0])
        self.assertEqual(x.direction, "W")

    def test_turn_right(self):
        myMap = moonRover.map()
        x = moonRover.moonRover(myMap.shape)
        x.coord = [0,0]
        x.turn("r")
        self.assertEqual(x.coord,[0,0])
        self.assertEqual(x.direction, "E")
    
    def test_init_given_8x8_map(self):
       givenMap = "00010000|00010000|00010000|00010000|00010000|00010000|00010000|00010000|"
       myMap = moonRover.map(givenMap)
       self.assertEqual(myMap.getMapAsString(), givenMap)
       
    def test_init_given_10x9_map(self):
       givenMap = "000100001|000100001|000100001|000100001|000100001|000100001|000100001|000100001|000100001|000100001|"
       myMap = moonRover.map(givenMap)
       self.assertEqual(myMap.getMapAsString(), givenMap)
       self.assertEqual(myMap.getMapShape(), (10,9))
       
    def test_in_front_coords(self):
        myMap = moonRover.map()
        rover = moonRover.moonRover(myMap.getMapShape())
        rover.coord = [0,2]
        rover.turn("r")
        self.assertEqual(rover.getCoordInFront(), [0,3])
        
if __name__ == '__main__':
    unittest.main()