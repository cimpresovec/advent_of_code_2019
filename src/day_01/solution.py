import math

from util.utils import read_file_numbers


def calculate_fuel(mass):
    return math.floor(mass / 3) - 2


def calculate_fuel_fuel(fuel):
    fuel_sum = 0
    while fuel > 0:
        fuel = calculate_fuel(fuel)
        if fuel > 0:
            fuel_sum += fuel
    return fuel_sum


def solve_part_1():
    fuel_sum = 0
    for mass in read_file_numbers("day_01.txt"):
        fuel_sum += calculate_fuel(mass)
    return fuel_sum


def solve_part_2():
    fuel_sum = 0
    for mass in read_file_numbers("day_01.txt"):
        fuel_sum += calculate_fuel(mass)
        fuel_sum += calculate_fuel_fuel(calculate_fuel(mass))
    return fuel_sum
