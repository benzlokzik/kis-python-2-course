# Умножение на 15. Используйте 3 сложения и 2 вычитания.


def mul(x: int) -> int:
    a = x + x  # 2
    b = a + a  # 4
    c = b + b  # 8
    d = c - (x - c)  # 15

    return d


print(mul(10))
