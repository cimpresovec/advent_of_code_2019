import math
from typing import List, Optional

from util.utils import read_file_lines


class WireInstruction:
    def __init__(self, direction: str, amount: int):
        self.direction = direction
        self.amount = amount


def find_intersections(wire_one: List[WireInstruction], wire_two: List[WireInstruction]) -> List[List[int]]:
    wire_one_path = {}
    position = [0, 0]
    steps = 0
    for instruction in wire_one:
        for n in range(0, instruction.amount):
            if instruction.direction == "L":
                position[0] -= 1
            elif instruction.direction == "R":
                position[0] += 1
            elif instruction.direction == "U":
                position[1] += 1
            elif instruction.direction == "D":
                position[1] -= 1
            steps += 1
            if tuple(position) not in wire_one_path:
                wire_one_path[tuple(position)] = steps
    intersections = []
    position = [0, 0]
    steps = 0
    for instruction in wire_two:
        for n in range(0, instruction.amount):
            if instruction.direction == "L":
                position[0] -= 1
            elif instruction.direction == "R":
                position[0] += 1
            elif instruction.direction == "U":
                position[1] += 1
            elif instruction.direction == "D":
                position[1] -= 1
            steps += 1
            if tuple(position) in wire_one_path:
                cross = position.copy()
                cross.append(wire_one_path[tuple(position)] + steps)
                intersections.append(cross)
    return intersections


def dist_to_closest_intersection(wire_one: str, wire_two: str) -> Optional[float]:
    wire_one = parse_wire_instructions(wire_one)
    wire_two = parse_wire_instructions(wire_two)
    intersections = find_intersections(wire_one, wire_two)
    closest_distance = None
    for intersection in intersections:
        dist = manhattan_distance([0, 0], intersection)
        if not closest_distance:
            closest_distance = dist
        elif dist < closest_distance:
            closest_distance = dist
    return closest_distance


def lowest_steps_to_intersection(wire_one: str, wire_two: str) -> int:
    wire_one = parse_wire_instructions(wire_one)
    wire_two = parse_wire_instructions(wire_two)
    intersections = find_intersections(wire_one, wire_two)
    return min(intersections, key=lambda t: t[2])[2]


def manhattan_distance(p1: List[int], p2: List[int]):
    return math.fabs(p1[0] - p2[0]) + math.fabs(p1[1] - p2[1])


def solve_part_1():
    lines = read_file_lines("day_03.txt")
    return dist_to_closest_intersection(lines[0], lines[1])


def solve_part_2():
    lines = read_file_lines("day_03.txt")
    return lowest_steps_to_intersection(lines[0], lines[1])


def parse_wire_instructions(wire: str) -> List[WireInstruction]:
    instructions = []
    for instruction in wire.split(','):
        instructions.append(WireInstruction(instruction[0], int(instruction[1:])))
    return instructions
