import math


def main(m, a, b):
    return sum(
        73 * k - 13 * (62 * i**2 - i**3) ** 5 - 33 * math.exp(4) * c
        for c in range(1, b + 1)
        for k in range(1, a + 1)
        for i in range(1, m + 1)
    )
