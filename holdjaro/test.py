import unittest
import holdjaro as h

class TestSum(unittest.TestCase):

    
    def test_forward_step(self):
        x = h.holdjaro()
        x.step("f")
        self.assertEqual(x.coord,[0,1])


if __name__ == '__main__':
    unittest.main()