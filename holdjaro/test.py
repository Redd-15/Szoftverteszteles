import unittest
import holdjaro as h

class TestSum(unittest.TestCase):

    
    def test_forward_step(self):
        myMap = h.map()
        x = h.moonRover(myMap.shape)
        x.step("f")
        self.assertEqual(x.coord,[0,1])

    def test_backwards_step(self):
        myMap = h.map()
        x = h.moonRover(myMap.shape)
        x.coord = [4,4]
        x.step("b")
        self.assertEqual(x.coord,[4,3])

if __name__ == '__main__':
    unittest.main()