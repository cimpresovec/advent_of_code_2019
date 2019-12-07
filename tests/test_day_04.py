from unittest import TestCase

from day_04.solution import is_valid, solve_part_one, solve_part_two


class TestDay04(TestCase):
    def test_is_valid(self):
        self.assertTrue(is_valid(111111))
        self.assertFalse(is_valid(223450))
        self.assertFalse(is_valid(123789))

    def test_solve(self):
        self.assertEqual(1694, solve_part_one())

    def test_solve_two(self):
        self.assertEqual(1148, solve_part_two())