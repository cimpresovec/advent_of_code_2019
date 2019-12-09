import unittest

from day_09.solution import get_output, solve_part_one, solve_part_two


class TestDay09(unittest.TestCase):
    def test_thruster_signal(self):
        program = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
        program = [int(n) for n in program.split(',')]
        self.assertEqual([109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99], get_output(program, 1))

        program = "1102,34915192,34915192,7,4,7,99,0"
        program = [int(n) for n in program.split(',')]
        self.assertEqual([1219070632396864], get_output(program, 1))

        program = "104,1125899906842624,99"
        program = [int(n) for n in program.split(',')]
        self.assertEqual([1125899906842624], get_output(program, 1))

    def test_solve_part_one(self):
        self.assertEqual([2457252183], solve_part_one())

    def test_solve_part_two(self):
        self.assertEqual([70634], solve_part_two())


if __name__ == '__main__':
    unittest.main()
