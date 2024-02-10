def fast_mul(x: int, y: int) -> int:
    result: int = y
    even = 0
    while x > 1:
        if x % 2 == 1:
            even += result
        result *= 2
        x //= 2

    return result + even


# print(fast_mul(2, 10))


def fast_pov(y: int, x: int) -> int:
    result: int = y
    even = 0
    while x > 1:
        if y % 2 == 1:
            even += result
        result *= 2
        x -= 1

    return result + even


print(fast_pov(2, 10))
