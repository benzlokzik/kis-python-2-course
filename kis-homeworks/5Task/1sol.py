import math


def main(x, z, y):
    n = len(x)
    result = 0

    for i in range(1, n + 1):
        y_index = n - math.floor((i - 1) / 4)
        x_index = math.floor((i - 1) / 2)
        z_index = n - i

        if (
            y_index < 1
            or y_index > n
            or x_index < 0
            or x_index >= n
            or z_index < 0
            or z_index >= n
        ):
            raise IndexError("Calculated index is out of bounds")

        y_val = y[y_index - 1]
        x_val = x[x_index]
        z_val = z[z_index]

        term = (44 * y_val**2 + x_val + 71 * z_val**3) ** 5
        result += term

    return result


main([-0.08, 0.21], [-0.82, -0.19], [-0.68, 1.0])
