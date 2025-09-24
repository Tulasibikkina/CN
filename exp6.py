# Go-Back-N Sliding Window Protocol Simulation

def send_frames(data, window_size):
    n = len(data)
    base = 0
    next_frame = 0

    print("\n--- Go-Back-N Protocol Simulation ---\n")
    while base < n:
        # Send frames in window
        while next_frame < base + window_size and next_frame < n:
            print(f"Frame {next_frame} sent: {data[next_frame]}")
            next_frame += 1

        # Simulate acknowledgment
        ack = input(f"Enter last correctly received frame number (ACK) for frames {base} to {next_frame-1}: ")
        try:
            ack = int(ack)
        except ValueError:
            print("Invalid input. Assuming no frames received correctly.")
            ack = base - 1

        if ack >= base:
            base = ack + 1
            print(f"Sliding window moves. Next frame to send: {base}\n")
        else:
            print("Error detected. Resending frames from base.\n")
            next_frame = base  # Resend all frames in window

# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    data = input("Enter data to send (as string): ")
    window_size = int(input("Enter window size: "))
    send_frames(data, window_size)