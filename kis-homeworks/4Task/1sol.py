import math


def main(n):
    if n == 0:
        return 0.76
    elif n == 1:
        return 0.21
    else:
        main_fn_minus_2 = main(n - 2)
        main_fn_minus_1 = main(n - 1)
        result = (
            (math.sin(main_fn_minus_2) ** 3 / 14)
            - main_fn_minus_2
            - (main_fn_minus_1**3 - main_fn_minus_1)
        )
    return result
