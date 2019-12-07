import itertools
import threading
from queue import Queue
from typing import List

from util.utils import read_file_lines


def process_program(program: List[int], in_queue: Queue, out_queue: Queue) -> None:
    ip = 0
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
            program[program[ip + 1]] = in_queue.get()
            ip += 2
        elif opcode == 4:
            "Output"
            eax = program[program[ip + 1]] if instruction[2] == 0 else program[ip + 1]
            out_queue.put(eax)
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


def thruster_signal(program: List[int], phase_sequence: List[int]):
    a_b_queue = Queue()
    a_b_queue.put(phase_sequence[1])
    b_c_queue = Queue()
    b_c_queue.put(phase_sequence[2])
    c_d_queue = Queue()
    c_d_queue.put(phase_sequence[3])
    d_e_queue = Queue()
    d_e_queue.put(phase_sequence[4])
    e_a_queue = Queue()
    e_a_queue.put(phase_sequence[0])
    e_a_queue.put(0)

    threads = [threading.Thread(target=process_program, args=[program.copy(), e_a_queue, a_b_queue]),
               threading.Thread(target=process_program, args=[program.copy(), a_b_queue, b_c_queue]),
               threading.Thread(target=process_program, args=[program.copy(), b_c_queue, c_d_queue]),
               threading.Thread(target=process_program, args=[program.copy(), c_d_queue, d_e_queue]),
               threading.Thread(target=process_program, args=[program.copy(), d_e_queue, e_a_queue])]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return e_a_queue.get()


def solve_part_one():
    program = [int(d) for d in read_file_lines("day_07.txt")[0].split(',')]
    phase_sequence = [0, 1, 2, 3, 4]
    max_thruster_signal = 0
    for perm_sequence in itertools.permutations(phase_sequence):
        signal = thruster_signal(program.copy(), list(perm_sequence))
        if signal > max_thruster_signal:
            max_thruster_signal = signal
    return max_thruster_signal


def solve_part_two():
    program = [int(d) for d in read_file_lines("day_07.txt")[0].split(',')]
    phase_sequence = [5, 6, 7, 8, 9]
    max_thruster_signal = 0
    for perm_sequence in itertools.permutations(phase_sequence):
        signal = thruster_signal(program.copy(), list(perm_sequence))
        if signal > max_thruster_signal:
            max_thruster_signal = signal
    return max_thruster_signal
