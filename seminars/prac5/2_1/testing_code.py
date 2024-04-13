def distance(x1, y1, x2, y2):
    """
    Считает Евклидово расстояние между двумя точками.

    Args:
        x1 (float): x-координата первой точки.
        y1 (float): y-координата первой точки.
        x2 (float): x-координата второй точки.
        y2 (float): y-координата второй точки.

    Returns:
        float: Евклидово расстояние между двумя точками.

    Examples:
    >>> distance(0, 0, 0, 0)
    0.0
    >>> distance(0, 0, 1, 0)
    1.0
    >>> distance(0, 0, 0, 1)
    1.0
    >>> distance(0, 0, 1, 1)
    1.0
    >>> distance(-1, -1, 1, 1)
    2.8284271247461903
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def triangle_type(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    if a == b == c:
        return "равнобедренный"
    elif a == b or a == c or b == c:
        return "равносторонний"
    elif a != b != c:
        return "разносторонний"


def triangle_type_correct(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)

    if max((a, b, c)) >= sum((a, b, c)) - max((a, b, c)):
        return "не существует"
    if a == b == c:
        return "равносторонний"
    elif a == b or a == c or b == c:
        return "равнобедренный"
    else:
        return "разносторонний"
