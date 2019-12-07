def is_valid(number: int) -> bool:
    digits = [int(d) for d in str(number)]
    if len(digits) != 6:
        return False
    pair = False
    for i in range(1, len(digits)):
        if digits[i] < digits[i-1]:
            return False
        if digits[i] == digits[i-1]:
            pair = True
    return pair


def is_valid_extra(number: int) -> bool:
    digits = [int(d) for d in str(number)]
    if len(digits) != 6:
        return False
    pair = False
    i = 1
    while i < len(digits):
        if digits[i] < digits[i - 1]:
            return False
        count = 0
        # Damn son this ugly
        while digits[i] == digits[i - 1]:
            count += 1
            if i + 1 == len(digits):
                if count == 1:
                    pair = True
                break
            elif digits[i+1] != digits[i]:
                if count == 1:
                    pair = True
                break
            i += 1
        i += 1
    return pair


def solve_part_one() -> int:
    count = 0
    for number in range(156218, 652527 + 1):
        if is_valid(number):
            count += 1
    return count


def solve_part_two() -> int:
    count = 0
    for number in range(156218, 652527 + 1):
        if is_valid_extra(number):
            count += 1
    return count
