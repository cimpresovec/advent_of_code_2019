import unittest

from src.day_01 import solution


class TestDay01(unittest.TestCase):
    def test_solve_part_1(self):
        self.assertEqual(solution.solve_part_1(), 3254441)

    def test_solve_part_2(self):
        self.assertEqual(solution.solve_part_2(), 4878818)


if __name__ == '__main__':
    unittest.main()
