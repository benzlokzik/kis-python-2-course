def main(x: float, z: float, y: float) -> float:
    return (
        pow((y - pow(z, 3) / 88), 2)
        + pow((x - pow(y, 2) / 28), 6)
        - (31 * pow(x, 4) + 77 * pow((pow(z, 3) + pow(y, 2) + 70 * y), 7))
        / (pow((11 * pow(x, 2)), 6) + pow((pow(y, 3) + pow(z, 2)), 3))
    )
