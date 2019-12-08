from textwrap import wrap
from typing import List

from util.utils import read_file_lines


class WireImage:
    def __init__(self, data: List[int], width: int, height: int):
        self.data = data
        self.width = width
        self.height = height
        self.num_layers = int(len(data) / (width * height))

    def get_layer(self, n: int) -> List[int]:
        return self.data[n * (self.width * self.height):(n * (self.width * self.height)) + self.width * self.height]

    def decode_image(self) -> List[int]:
        decoded = []
        for n in range(self.width * self.height):
            for layer_n in range(self.num_layers):
                if self.get_layer(layer_n)[n] == 0:
                    decoded.append(0)
                    break
                elif self.get_layer(layer_n)[n] == 1:
                    decoded.append(1)
                    break
        return decoded

    def print_image(self):
        img = self.decode_image()
        for line in wrap("".join("X" if d == 1 else " " for d in img), self.width):
            print(line)


def solve_part_one():
    data = [int(d) for d in read_file_lines("day_08.txt")[0]]
    image = WireImage(data, 25, 6)
    best_ones = 0
    best_twos = 0
    min_zeroes = 25 * 6
    for layer_n in range(image.num_layers):
        layer = image.get_layer(layer_n)
        zeroes = 0
        ones = 0
        twos = 0
        for d in layer:
            if d == 0:
                zeroes += 1
            elif d == 1:
                ones += 1
            elif d == 2:
                twos += 1
        if zeroes < min_zeroes:
            min_zeroes = zeroes
            best_ones = ones
            best_twos = twos
    return best_ones * best_twos


def solve_part_two():
    data = [int(d) for d in read_file_lines("day_08.txt")[0]]
    image = WireImage(data, 25, 6)
    image.print_image()
    return image.decode_image()
