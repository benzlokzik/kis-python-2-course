def f(x: float, z: float, y: float) -> float:
    return (
        (y - z**3 / 88) ** 2
        + (x - y**2 / 28) ** 6
        - (
            (31 * x**4 + 77 * ((z**3 + y**2 + 70 * y) ** 7))
            / (((11 * x**2) ** 6) + ((y**3 + z**2) ** 3))
        )
    )


def main(x, z, y):
    return f(x, z, y)
