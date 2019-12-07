from unittest import TestCase

from day_05.solution import solve_part_one, process_program_string, solve_part_two


class TestDay05(TestCase):
    def test_solve_part_1(self):
        self.assertEqual(7157989, solve_part_one()[-1])

    def test_examples_part_2(self):
        self.assertEqual(1, process_program_string("3,9,8,9,10,9,4,9,99,-1,8", [8])[0])
        self.assertEqual(0, process_program_string("3,9,8,9,10,9,4,9,99,-1,8", [9])[0])
        self.assertEqual(0, process_program_string("3,9,7,9,10,9,4,9,99,-1,8", [9])[0])
        self.assertEqual(1, process_program_string("3,9,7,9,10,9,4,9,99,-1,8", [7])[0])

        self.assertEqual(1, process_program_string("3,3,1108,-1,8,3,4,3,99", [8])[0])
        self.assertEqual(0, process_program_string("3,3,1108,-1,8,3,4,3,99", [9])[0])
        self.assertEqual(0, process_program_string("3,3,1107,-1,8,3,4,3,99", [9])[0])
        self.assertEqual(1, process_program_string("3,3,1107,-1,8,3,4,3,99", [7])[0])

        self.assertEqual(0, process_program_string("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", [0])[0])
        self.assertEqual(1, process_program_string("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", [1])[0])
        self.assertEqual(1, process_program_string("3,3,1105,-1,9,1101,0,0,12,4,12,99,1", [1])[0])
        self.assertEqual(1, process_program_string("3,3,1105,-1,9,1101,0,0,12,4,12,99,1", [1])[0])

        self.assertEqual(999, process_program_string("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,"
                                                     "0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,"
                                                     "20,4,20,1105,1,46,98,99", [7])[0])
        self.assertEqual(1000,
                         process_program_string("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,"
                                                "0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,"
                                                "20,4,20,1105,1,46,98,99", [8])[0])
        self.assertEqual(1001,
                         process_program_string("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,"
                                                "0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,"
                                                "20,4,20,1105,1,46,98,99", [9])[0])

    def test_solve_part_two(self):
        self.assertEqual(7873292, solve_part_two()[0])
