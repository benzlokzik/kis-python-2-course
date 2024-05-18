class DecisionMaker:
    def __init__(self, x):
        self.x = x

    def x0(self, left, mid, right):
        return {"MUPAD": left, "NIM": mid, "PAN": right}.get(self.x[0], None)

    def x1(self, left, mid, right):
        return {1987: left, 1974: mid, 2003: right}.get(self.x[1], None)

    def x2(self, left, mid, right):
        return {"CMAKE": left, "SAS": mid, "EC": right}.get(self.x[2], None)

    def x3(self, left, mid):
        return {"RED": left, "C++": mid}.get(self.x[3], None)

    def x4(self, left, mid, right):
        return {"INI": left, "X10": mid, "SCAML": right}.get(self.x[4], None)

    def main(self):
        return self.x2(
            self.x0(
                self.x3(0, self.x4(1, 2, 3)),
                self.x1(4, self.x4(5, 6, 7), self.x4(8, 9, 10)),
                11,
            ),
            12,
            13,
        )


def main(x):
    return DecisionMaker(x).main()
