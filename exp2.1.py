# Character Stuffing in Data Link Layer

def character_stuffing(data, flag='F', escape='E'):
    """
    Adds character stuffing to the data.
    flag: frame delimiter
    escape: escape character
    """
    stuffed_data = ''
    for char in data:
        if char == flag or char == escape:
            stuffed_data += escape  # Add escape before flag/escape
        stuffed_data += char
    # Add flags at start and end
    framed_data = flag + stuffed_data + flag
    return framed_data

# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    data_char = input("Enter data for character stuffing: ")
    framed_char_data = character_stuffing(data_char)
    print("Framed Data:", framed_char_data)