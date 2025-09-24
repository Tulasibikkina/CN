# Bit Stuffing in Data Link Layer

def bit_stuffing(data):
    """
    Adds bit stuffing: inserts a 0 after 5 consecutive 1s.
    """
    count = 0
    stuffed_data = ''
    for bit in data:
        stuffed_data += bit
        if bit == '1':
            count += 1
            if count == 5:
                stuffed_data += '0'  # Insert 0 after 5 consecutive 1s
                count = 0
        else:
            count = 0
    return stuffed_data

# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    data_bit = input("Enter binary data for bit stuffing (e.g., 1101111110111): ")
    stuffed_bit_data = bit_stuffing(data_bit)
    print("Bit Stuffed Data:", stuffed_bit_data)
