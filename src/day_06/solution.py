from typing import List, Dict

from util.utils import read_file_lines


def build_map(inputs: List[str]) -> Dict[str, str]:
    orbital_map = {}

    for notation in inputs:
        what, who = notation.split(')')
        orbital_map[who] = what

    return orbital_map


def count_orbits(orbit_map: Dict[str, str]):
    orbit_num = 0

    for who, what in orbit_map.items():
        orbits = what
        while True:
            orbit_num += 1
            if orbits in orbit_map:
                orbits = orbit_map[orbits]
            else:
                break
    return orbit_num


def build_path(orbit_map: Dict[str, str], who: str):
    path = {}
    transfers = 0
    orbits = orbit_map[who]
    while True:
        if orbits in orbit_map:
            transfers += 1
            path[orbits] = transfers
            orbits = orbit_map[orbits]
        else:
            path["COM"] = transfers + 1
            break
    return path


def find_transfers(path_one: Dict[str, int], path_two: Dict[str, int]) -> int:
    for key, value in path_one.items():
        if key in path_two:
            return value - 1 + path_two[key] - 1


def solve_for_input(input_str: str):
    return count_orbits(build_map(input_str.split()))


def solve_two_for_input(input_str: str):
    orbit_map = build_map(input_str.split())
    path_you = build_path(orbit_map, "YOU")
    path_san = build_path(orbit_map, "SAN")
    return find_transfers(path_you, path_san)


def solve_part_one():
    return count_orbits(build_map(read_file_lines("day_06.txt")))


def solve_part_two():
    orbit_map = build_map(read_file_lines("day_06.txt"))
    path_you = build_path(orbit_map, "YOU")
    path_san = build_path(orbit_map, "SAN")
    return find_transfers(path_you, path_san)
