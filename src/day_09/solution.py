import threading
from queue import Queue
from typing import List

from util.utils import read_file_lines


def get_parameter(num, ip, base, program, instruction):
    if instruction[3 - num] == 0:
        return program[program[ip + num]]
    elif instruction[3 - num] == 1:
        return program[ip + num]
    else:
        return program[base + program[ip + num]]


def process_program(program: List[int], in_queue: Queue, out_queue: Queue) -> None:
    ip = 0
    relative_base = 0
    while True:
        instruction = [int(d) for d in str(program[ip]).rjust(5, '0')]
        opcode = instruction[3] * 10 + instruction[4]
        if opcode == 99:
            break
        elif opcode == 1:
            "Addition"
            eax = get_parameter(1, ip, relative_base, program, instruction)
            ebx = get_parameter(2, ip, relative_base, program, instruction)
            # eax = program[program[ip + 1]] if instruction[2] == 0 else program[ip + 1]
            # ebx = program[program[ip + 2]] if instruction[1] == 0 else program[ip + 2]
            program[program[ip + 3] if instruction[0] == 0 else relative_base + program[ip + 3]] = eax + ebx
            ip += 4
        elif opcode == 2:
            "Multiplication"
            eax = get_parameter(1, ip, relative_base, program, instruction)
            ebx = get_parameter(2, ip, relative_base, program, instruction)
            # eax = program[program[ip + 1]] if instruction[2] == 0 else program[ip + 1]
            # ebx = program[program[ip + 2]] if instruction[1] == 0 else program[ip + 2]
            program[program[ip + 3] if instruction[0] == 0 else relative_base + program[ip + 3]] = eax * ebx
            ip += 4
        elif opcode == 3:
            "Input"
            if instruction[2] == 0:
                program[program[ip + 1]] = in_queue.get()
            else:
                program[relative_base + program[ip + 1]] = in_queue.get()
            ip += 2
        elif opcode == 4:
            "Output"
            eax = get_parameter(1, ip, relative_base, program, instruction)
            # eax = program[program[ip + 1]] if instruction[2] == 0 else program[ip + 1]
            out_queue.put(eax)
            ip += 2
        elif opcode == 5:
            "jump-if-true"
            eax = get_parameter(1, ip, relative_base, program, instruction)
            ebx = get_parameter(2, ip, relative_base, program, instruction)
            # eax = program[program[ip + 1]] if instruction[2] == 0 else program[ip + 1]
            # ebx = program[program[ip + 2]] if instruction[1] == 0 else program[ip + 2]
            if eax != 0:
                ip = ebx
            else:
                ip += 3
        elif opcode == 6:
            "jump-if-false"
            eax = get_parameter(1, ip, relative_base, program, instruction)
            ebx = get_parameter(2, ip, relative_base, program, instruction)
            # eax = program[program[ip + 1]] if instruction[2] == 0 else program[ip + 1]
            # ebx = program[program[ip + 2]] if instruction[1] == 0 else program[ip + 2]
            if eax == 0:
                ip = ebx
            else:
                ip += 3
        elif opcode == 7:
            "less than"
            eax = get_parameter(1, ip, relative_base, program, instruction)
            ebx = get_parameter(2, ip, relative_base, program, instruction)
            # eax = program[program[ip + 1]] if instruction[2] == 0 else program[ip + 1]
            # ebx = program[program[ip + 2]] if instruction[1] == 0 else program[ip + 2]
            program[program[ip + 3] if instruction[0] == 0 else relative_base + program[ip + 3]] = 1 if eax < ebx else 0
            ip += 4
        elif opcode == 8:
            "equals"
            eax = get_parameter(1, ip, relative_base, program, instruction)
            ebx = get_parameter(2, ip, relative_base, program, instruction)
            # eax = program[program[ip + 1]] if instruction[2] == 0 else program[ip + 1]
            # ebx = program[program[ip + 2]] if instruction[1] == 0 else program[ip + 2]
            program[program[ip + 3] if instruction[0] == 0 else relative_base + program[ip + 3]] = 1 if eax == ebx else 0
            ip += 4
        elif opcode == 9:
            "adjust relative base"
            eax = get_parameter(1, ip, relative_base, program, instruction)
            # eax = program[program[ip + 1]] if instruction[2] == 0 else program[ip + 1]
            relative_base += eax
            ip += 2


def get_output(program: List[int], input_val):
    for x in range(100000):
        program.append(0)
    in_queue = Queue()
    out_queue = Queue()
    in_queue.put(input_val)

    threads = [threading.Thread(target=process_program, args=[program.copy(), in_queue, out_queue])]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    out = []
    while not out_queue.empty():
        out.append(out_queue.get())
    return out


def solve_part_one():
    program = [int(d) for d in read_file_lines("day_09.txt")[0].split(',')]
    return get_output(program, 1)


def solve_part_two():
    program = [int(d) for d in read_file_lines("day_09.txt")[0].split(',')]
    return get_output(program, 2)
