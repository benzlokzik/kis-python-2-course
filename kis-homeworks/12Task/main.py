from struct import unpack_from, calcsize


class Types:
    char = "c"
    int8 = "b"
    uint8 = "B"
    int16 = "h"
    uint16 = "H"
    int32 = "i"
    uint32 = "I"
    int64 = "q"
    uint64 = "Q"
    float = "f"
    double = "d"


class BinaryReader:
    def __init__(self, data, offset, order=">"):
        self.data = data
        self.offset = offset
        self.order = order

    def jump(self, offset):
        return BinaryReader(self.data, offset, self.order)

    def read(self, pattern):
        data = unpack_from(self.order + pattern, self.data, self.offset)
        self.offset += calcsize(pattern)
        return data[0]


def read_e(reader: BinaryReader):
    e1 = reader.read(Types.int8)
    e2_size = reader.read(Types.uint32)
    e2_ptr = reader.read(Types.uint32)
    e2_reader = reader.jump(e2_ptr)
    e2 = [e2_reader.read(Types.int16) for _ in range(e2_size)]
    e3 = reader.read(Types.uint16)
    e4 = reader.read(Types.uint64)
    e5_size = reader.read(Types.uint16)
    e5_ptr = reader.read(Types.uint32)
    e5_reader = reader.jump(e5_ptr)
    e5 = [e5_reader.read(Types.int8) for _ in range(e5_size)]
    e6 = reader.read(Types.double)
    e7 = reader.read(Types.float)
    return dict(E1=e1, E2=e2, E3=e3, E4=e4, E5=e5, E6=e6, E7=e7)


def read_d(reader: BinaryReader):
    d1 = reader.read(Types.int16)
    d2 = reader.read(Types.int8)
    return dict(D1=d1, D2=d2)


def read_c(reader: BinaryReader):
    c1 = reader.read(Types.uint16)
    c2 = ""
    c2_size = reader.read(Types.uint16)
    c2_ptr = reader.read(Types.uint16)
    c2_reader = reader.jump(c2_ptr)
    for _ in range(c2_size):
        c2 += c2_reader.read(Types.char).decode("utf-8")
    c3 = reader.read(Types.uint32)

    return dict(C1=c1, C2=c2, C3=c3)


def read_b(reader: BinaryReader):
    b1_ptr = reader.read(Types.uint32)
    b1_reader = reader.jump(b1_ptr)
    b1 = read_c(b1_reader)
    b2 = reader.read(Types.int16)
    b3 = [read_d(reader) for _ in range(2)]
    b4_ptr = reader.read(Types.uint16)
    b4_reader = reader.jump(b4_ptr)
    b4 = read_e(b4_reader)
    b5 = reader.read(Types.double)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5)


def read_a(reader: BinaryReader):
    a1_ptr = reader.read(Types.uint32)
    a1_reader = reader.jump(a1_ptr)
    a1 = read_b(a1_reader)
    a2_size = reader.read(Types.uint32)
    a2_ptr = reader.read(Types.uint16)
    a2_reader = reader.jump(a2_ptr)
    a2 = [a2_reader.read(Types.uint32) for _ in range(a2_size)]

    return dict(A1=a1, A2=a2)


def main(bts):
    reader = BinaryReader(bts, 4, "<")
    return read_a(reader)
