import unittest
import holdjaro as h

class TestSum(unittest.TestCase):

    
    def test_step(self):
        x = h.holdjaro()
        x.coord = (0,0)
        x.step("f")
        self.assertEqual(x.coord,(0,1))


if __name__ == '__main__':
    unittest.main()