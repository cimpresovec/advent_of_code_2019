from typing import List

from util.utils import read_file_lines


def process_program(program: List[int], inputs: List[int]) -> List[int]:
    ip = 0
    inputs_pos = 0
    outputs = []
    while True:
        instruction = [int(d) for d in str(program[ip]).rjust(5, '0')]
        opcode = instruction[3] * 10 + instruction[4]
        if opcode == 99:
            break
        elif opcode == 1:
            "Addition"
            eax = program[program[ip + 1]] if instruction[2] == 0 else program[ip + 1]
            ebx = program[program[ip + 2]] if instruction[1] == 0 else program[ip + 2]
            program[program[ip + 3]] = eax + ebx
            ip += 4
        elif opcode == 2:
            "Multiplication"
            eax = program[program[ip + 1]] if instruction[2] == 0 else program[ip + 1]
            ebx = program[program[ip + 2]] if instruction[1] == 0 else program[ip + 2]
            program[program[ip + 3]] = eax * ebx
            ip += 4
        elif opcode == 3:
            "Input"
            program[program[ip + 1]] = inputs[inputs_pos]
            inputs_pos += 1
            ip += 2
        elif opcode == 4:
            "Output"
            eax = program[program[ip + 1]] if instruction[2] == 0 else program[ip + 1]
            outputs.append(eax)
            ip += 2
        elif opcode == 5:
            "jump-if-true"
            eax = program[program[ip + 1]] if instruction[2] == 0 else program[ip + 1]
            ebx = program[program[ip + 2]] if instruction[1] == 0 else program[ip + 2]
            if eax != 0:
                ip = ebx
            else:
                ip += 3
        elif opcode == 6:
            "jump-if-false"
            eax = program[program[ip + 1]] if instruction[2] == 0 else program[ip + 1]
            ebx = program[program[ip + 2]] if instruction[1] == 0 else program[ip + 2]
            if eax == 0:
                ip = ebx
            else:
                ip += 3
        elif opcode == 7:
            "less than"
            eax = program[program[ip + 1]] if instruction[2] == 0 else program[ip + 1]
            ebx = program[program[ip + 2]] if instruction[1] == 0 else program[ip + 2]
            program[program[ip + 3]] = 1 if eax < ebx else 0
            ip += 4
        elif opcode == 8:
            "equals"
            eax = program[program[ip + 1]] if instruction[2] == 0 else program[ip + 1]
            ebx = program[program[ip + 2]] if instruction[1] == 0 else program[ip + 2]
            program[program[ip + 3]] = 1 if eax == ebx else 0
            ip += 4
    return outputs


def process_program_string(input_str: str, inputs: List[int]) -> List[int]:
    program = [int(n) for n in input_str.split(',')]
    return process_program(program, inputs)


def solve_part_one():
    program = [int(n) for n in read_file_lines("day_05.txt")[0].split(',')]
    return process_program(program, [1])


def solve_part_two():
    program = [int(n) for n in read_file_lines("day_05.txt")[0].split(',')]
    return process_program(program, [5])
