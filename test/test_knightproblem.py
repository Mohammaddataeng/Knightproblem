import unittest
import src
from src.com.demo import knightproblem


class KnightTestCase(unittest.TestCase):
    def test_stepToReachTarget(self):
        N = 8
        knightpos = [4, 4]
        targetpos = [7, 7]
        path = knightproblem.stepToReachTarget(knightpos, targetpos, N)

        self.assertEqual(['D4', 'F5', 'G7'], path)  # add assertion here


if __name__ == '__main__':
    unittest.main()