import unittest

from day_03.solution import dist_to_closest_intersection, solve_part_1, lowest_steps_to_intersection, solve_part_2


class TestDay03(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(dist_to_closest_intersection("R75,D30,R83,U83,L12,D49,R71,U7,L72",
                         "U62,R66,U55,R34,D71,R55,D58,R83"), 159)
        self.assertEqual(dist_to_closest_intersection("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                                                      "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"), 135)

    def test_examples_two(self):
        self.assertEqual(lowest_steps_to_intersection("R75,D30,R83,U83,L12,D49,R71,U7,L72",
                         "U62,R66,U55,R34,D71,R55,D58,R83"), 610)
        self.assertEqual(lowest_steps_to_intersection("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                                                      "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"), 410)

    def test_solution_part_1(self):
        self.assertEqual(solve_part_1(), 768)

    def test_solution_part_2(self):
        self.assertEqual(solve_part_2(), 8684)


if __name__ == '__main__':
    unittest.main()
