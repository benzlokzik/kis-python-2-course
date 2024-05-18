def x0(x, left, mid, right):
    if x[0] == "MUPAD":
        return left
    elif x[0] == "NIM":
        return mid
    elif x[0] == "PAN":
        return right


def x1(x, left, mid, right):
    if x[1] == 1987:
        return left
    elif x[1] == 1974:
        return mid
    elif x[1] == 2003:
        return right


def x2(x, left, mid, right):
    if x[2] == "CMAKE":
        return left
    elif x[2] == "SAS":
        return mid
    elif x[2] == "EC":
        return right


def x3(x, left, mid):
    if x[3] == "RED":
        return left
    elif x[3] == "C++":
        return mid


def x4(x, left, mid, right):
    if x[4] == "INI":
        return left
    elif x[4] == "X10":
        return mid
    elif x[4] == "SCAML":
        return right


def main(x):
    return x2(
        x,
        x0(
            x,
            x3(x, 0, x4(x, 1, 2, 3)),
            x1(x, 4, x4(x, 5, 6, 7), x4(x, 8, 9, 10)),
            11,
        ),
        12,
        13,
    )
