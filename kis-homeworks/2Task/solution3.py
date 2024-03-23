def main(x: float) -> float:
    result1: float = x**3 if x < 88 else 0
    result2: float = (12 * x**3) ** 6 if x < 132 else 0
    result3: float = 45 * (x**2 - 77 * x**3) ** 6 if x < 209 else 0
    result4: float = 13 * x**7 if x < 283 else 0
    result5: float = 67 * (73 * x**3 + 65) ** 7 if x >= 283 else 0

    return (
        result1
        if x < 88
        else (
            result2
            if x < 132
            else result3 if x < 209 else result4 if x < 283 else result5
        )
    )
