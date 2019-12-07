import os


def file_path(file_name):
    return os.path.join(os.path.dirname(__file__), "../inputs/", file_name)


def read_file_numbers(file_name):
    numbers = []
    file = open(file_path(file_name), "r")
    for line in file:
        numbers.append(int(line))
    file.close()
    return numbers


def read_file_lines(file_name):
    file = open(file_path(file_name), "r")
    lines = file.read().splitlines()
    file.close()
    return lines
