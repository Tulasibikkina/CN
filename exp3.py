# Data Link Layer: Checksum Method

def calculate_checksum(data):
    """
    Calculates simple checksum by summing ASCII values of characters
    and returning modulo 256 (8-bit checksum)
    """
    checksum = 0
    for char in data:
        checksum += ord(char)  # Convert char to ASCII
    checksum %= 256  # Keep it 8-bit
    return checksum

def verify_checksum(data, received_checksum):
    """
    Verifies data integrity using checksum
    """
    calculated = calculate_checksum(data)
    if calculated == received_checksum:
        return True
    else:
        return False

# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    # Sender Side
    data = input("Enter data to send: ")
    checksum = calculate_checksum(data)
    print(f"Data Sent: {data}")
    print(f"Checksum Sent: {checksum}")

    # Receiver Side
    received_data = input("\nEnter received data: ")
    received_checksum = int(input("Enter received checksum: "))

    if verify_checksum(received_data, received_checksum):
        print("Checksum Verified. Data is intact.")
    else:
        print("Checksum Mismatch. Data is corrupted.")