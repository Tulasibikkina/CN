# Selective Repeat Sliding Window Protocol Simulation

def selective_repeat(data, window_size):
    n = len(data)
    base = 0
    next_frame = 0
    received = [False] * n  # Track received frames

    print("\n--- Selective Repeat Protocol Simulation ---\n")

    while not all(received):
        # Send frames within window
        while next_frame < n and next_frame < base + window_size:
            if not received[next_frame]:
                print(f"Frame {next_frame} sent: {data[next_frame]}")
            next_frame += 1

        # Simulate acknowledgment for each frame
        print("\nEnter received frame numbers separated by space (simulate ACKs, leave blank if none): ")
        ack_input = input()
        ack_frames = []
        if ack_input.strip():
            ack_frames = [int(x) for x in ack_input.strip().split()]
        
        # Update received frames
        for ack in ack_frames:
            if 0 <= ack < n:
                received[ack] = True

        # Slide window to next unacknowledged frame
        while base < n and received[base]:
            base += 1
        print(f"Window slides. Next base frame: {base}\n")
        next_frame = base

# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    data = input("Enter data to send (as string): ")
    window_size = int(input("Enter window size: "))
    selective_repeat(data, window_size)
