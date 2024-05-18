def main(decimal_str):
    num = int(decimal_str)
    print(f"\nInput number: {num}")
    print(f"Binary representation: {bin(num)}, symbol count: {len(bin(num)) - 2}")

    L1 = num & 0xFF  # bits [7:0]
    L2 = (num >> 8) & 0xF  # bits [11:8]
    L3 = (num >> 12) & 0x7  # bits [14:12]
    print(f"L1: {bin(L1)}, L2: {bin(L2)}, L3: {bin(L3)}")

    output_num = (L2 << 20) | (L3 << 17) | (L1 << 9)

    # Convert the output number to a hexadecimal string
    output_hex = f"0x{output_num:06X}"
    print(bin(output_num))

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
    assert main("19153") == "0x153440"
    # Test case 3
    assert main("2444") == "0x1223000"
    # Test case 4
    assert main("20833") == "0x358400"
    print("All test cases pass")


test()
