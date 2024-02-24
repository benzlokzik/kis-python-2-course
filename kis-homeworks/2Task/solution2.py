def main(x: float) -> float:
    if x < 88:
        return x**3
    if 88 <= x < 132:
        return (12 * x**3) ** 6
    if 132 <= x < 209:
        return 45 * (x**2 - 77 * x**3) ** 6
    if 209 <= x < 283:
        return 13 * x**7
    if x >= 283:
        return 67 * (73 * x**3 + 65) ** 7
