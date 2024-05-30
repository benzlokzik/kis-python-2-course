def main(decimal_str):
    num = int(decimal_str)

    L1 = num & 0xFF  # bits [7:0]
    L2 = (num >> 8) & 0xF  # bits [11:8]
    L3 = (num >> 12) & 0x7  # bits [14:12]

    output_num = (
        "0b"
        + "0" * (4 - len(bin(L2)[2:]))
        + bin(L2)[2:]
        + "0" * (3 - len(bin(L3)[2:]))
        + bin(L3)[2:]
        + "0" * (8 - len(bin(L1)[2:]))
        + bin(L1)[2:]
        + "0" * 10
    )
    output_num = int(output_num, 2)
    output_hex = f"0x{output_num:06X}".lower()

    return output_hex


# Test cases
print(main("6084"))  # Expected output: '0xE71000'
print(main("19153"))  # Expected output: '0x153440'
print(main("2444"))  # Expected output: '0x1223000'
print(main("20833"))  # Expected output: '0x358400'


def test():
    # Test case 1
    assert main("6084") == "0xE71000"
    # Test case 2
    assert main("19153") == "0x1534400"
    # Test case 3
    assert main("2444") == "0x1223000"
    # Test case 4
    assert main("20833") == "0x358400"
    print("All test cases pass")


test()
