import unittest

from src.day_02.solution import process_program, solve_part_1, solve_part_2


class TestDay02(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(process_program([1, 0, 0, 0, 99]), [2, 0, 0, 0, 99])
        self.assertEqual(process_program([2, 3, 0, 3, 99]), [2, 3, 0, 6, 99])
        self.assertEqual(process_program([2, 4, 4, 5, 99, 0]), [2, 4, 4, 5, 99, 9801])
        self.assertEqual(process_program([1, 1, 1, 4, 99, 5, 6, 0, 99]), [30, 1, 1, 4, 2, 5, 6, 0, 99])

    def test_solution_part_1(self):
        self.assertEqual(solve_part_1()[0], 6327510)

    def test_solution_part_2(self):
        self.assertEqual(solve_part_2(), 4112)


if __name__ == '__main__':
    unittest.main()
