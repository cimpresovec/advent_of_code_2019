from unittest import TestCase

from day_06.solution import solve_for_input, solve_part_one, solve_two_for_input, solve_part_two


class TestDay06(TestCase):
    def test_solve_for_input(self):
        self.assertEqual(42, solve_for_input("""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""))

    def test_solve_tw_for_input(self):
        self.assertEqual(4, solve_two_for_input("""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""))

    def test_solve_part_one(self):
        self.assertEqual(162439, solve_part_one())

    def test_solve_part_two(self):
        self.assertEqual(367, solve_part_two())
