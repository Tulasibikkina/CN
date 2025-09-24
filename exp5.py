# CRC Implementation in Python

def xor(a, b):
    """Perform XOR between two binary strings"""
    result = []
    for i in range(1, len(b)):
        result.append('0' if a[i] == b[i] else '1')
    return ''.join(result)

def crc_remainder(data, poly, poly_len):
    """Compute CRC remainder"""
    # Append zeros to data equal to polynomial length - 1
    data = data + '0'*(poly_len-1)
    temp = data[:poly_len]

    while len(temp) <= len(data):
        if temp[0] == '1':
            temp = xor(poly, temp) + (data[poly_len] if poly_len + len(temp)-1 < len(data) else '')
        else:
            temp = xor('0'*poly_len, temp) + (data[poly_len] if poly_len + len(temp)-1 < len(data) else '')
        temp = temp[1:]  # Remove leftmost bit
        if len(temp) < poly_len:
            break
    return temp.zfill(poly_len-1)

def char_to_binary(data):
    """Convert string to binary representation"""
    return ''.join(format(ord(c), '08b') for c in data)

# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    data = input("Enter data (characters): ")
    bin_data = char_to_binary(data)
    print(f"Binary data: {bin_data}")

    # CRC Polynomials in binary (excluding MSB 1)
    crc_polys = {
        "CRC-12": "1100000001111",       # x^12 + x^11 + x^3 + x^2 + x + 1
        "CRC-16": "11000000000000101",   # x^16 + x^15 + x^2 + 1
        "CRC-CCITT": "10001000000100001" # x^16 + x^12 + x^5 + 1
    }

    for name, poly in crc_polys.items():
        poly_len = len(poly)
        remainder = crc_remainder(bin_data, poly, poly_len)
        print(f"{name} CRC Remainder: {remainder}")