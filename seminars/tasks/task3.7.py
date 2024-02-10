def mul_bits(x, y, bits) -> int:
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


# Представим умножение x на y в следующем виде (S это сдвиг на n/2 разрядов).

# (x1*S + x0) * (y1*S + y0) = x1 * y1 * S^2 + (x0 * y1 + x1 * y0) * S + x0 * y0

def mul16(x, y):
    x1: int
    x0: int
    y1: int
    y0: int

    x1, x0 = x >> 8, x & 0xff
    y1, y0 = y >> 8, y & 0xff
    p0: int = mul_bits(x1, y1, 8)
    p1: int = mul_bits(x1, y0, 8) + mul_bits(y1, x0, 8)
    p2: int = mul_bits(x0, y0, 8)

    return p0 << 16 + p1 << 8 + p2
