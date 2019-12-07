from util.utils import read_file_lines


def process_program(program):
    ip = 0
    while True:
        if program[ip] == 99:
            break
        instruction = program[ip:ip+4]
        if instruction[0] == 1:
            "Addition"
            program[instruction[3]] = program[instruction[1]] + program[instruction[2]]
        elif instruction[0] == 2:
            "Multiplication"
            program[instruction[3]] = program[instruction[1]] * program[instruction[2]]
        ip += 4
    return program


def solve_part_1():
    program = [int(n) for n in read_file_lines("day_02.txt")[0].split(',')]
    program[1] = 12
    program[2] = 2
    return process_program(program)


def solve_part_2():
    program = [int(n) for n in read_file_lines("day_02.txt")[0].split(',')]

    for noun in range(0, 100):
        for verb in range(0, 100):
            program[1] = noun
            program[2] = verb
            if process_program(program.copy())[0] == 19690720:
                return 100 * noun + verb
