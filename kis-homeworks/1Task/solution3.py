import math


def f(x: float, z: float, y: float) -> float:
    a = [
        math.pow((y - math.pow(z, 3) / 88), 2),
        math.pow((x - math.pow(y, 2) / 28), 6),
        31 * math.pow(x, 4)
        + 77 * math.pow((math.pow(z, 3) + math.pow(y, 2) + 70 * y), 7),
        math.pow(11 * math.pow(x, 2), 6)
        + math.pow((math.pow(y, 3) + math.pow(z, 2)), 3),
    ]
    return a[0] + a[1] - (a[2] / a[3])


def main(x, z, y):
    return f(x, z, y)
