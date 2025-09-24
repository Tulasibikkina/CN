# Hamming Code Generation for Error Detection and Correction

def calculate_parity_bits(data):
    """
    Insert parity bits at positions 1,2,4,8,... 
    in the data list (1-indexed)
    """
    n = len(data)
    r = 0
    # Find number of parity bits needed
    while (2**r) < (n + r + 1):
        r += 1

    # Initialize Hamming code with parity bits (0 for now)
    hamming = []
    j = 0  # data bit index
    for i in range(1, n + r + 1):
        if i & (i-1) == 0:  # position is power of 2 -> parity bit
            hamming.append(0)
        else:
            hamming.append(int(data[j]))
            j += 1

    # Calculate parity bits
    for i in range(r):
        parity_pos = 2**i
        parity = 0
        for j in range(1, n + r + 1):
            if j & parity_pos != 0:
                parity ^= hamming[j-1]  # XOR all bits covered by this parity
        hamming[parity_pos-1] = parity

    return hamming

def detect_error(hamming):
    """
    Detect single-bit error position
    """
    n = len(hamming)
    r = 0
    while (2**r) < n + 1:
        r += 1

    error_pos = 0
    for i in range(r):
        parity_pos = 2**i
        parity = 0
        for j in range(1, n + 1):
            if j & parity_pos != 0:
                parity ^= hamming[j-1]
        if parity != 0:
            error_pos += parity_pos
    return error_pos

# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    data = input("Enter binary data (e.g., 1011): ")
    hamming_code = calculate_parity_bits(data)
    print("Hamming Code Generated:", ''.join(map(str, hamming_code)))

    # Optional: Simulate error
    choice = input("Do you want to simulate error? (y/n): ").lower()
    if choice == 'y':
        error_bit = int(input("Enter bit position to flip (1-indexed): "))
        hamming_code[error_bit-1] ^= 1
        print("Hamming Code with error:", ''.join(map(str, hamming_code)))

    # Detect and correct error
    error_pos = detect_error(hamming_code)
    if error_pos == 0:
        print("No error detected ✅")
    else:
        print(f"Error detected at position: {error_pos}")
        # Correct error
        hamming_code[error_pos-1] ^= 1
        print("Corrected Hamming Code:", ''.join(map(str, hamming_code)))