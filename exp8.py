# Stop-and-Wait Protocol Simulation

def stop_and_wait(data):
    n = len(data)
    current_frame = 0

    print("\n--- Stop-and-Wait Protocol Simulation ---\n")

    while current_frame < n:
        # Send the current frame
        print(f"Sending Frame {current_frame}: {data[current_frame]}")

        # Simulate acknowledgment
        ack = input(f"Enter ACK for Frame {current_frame} (y/n for received or lost): ").lower()

        if ack == 'y':
            print(f"ACK received for Frame {current_frame}. Moving to next frame.\n")
            current_frame += 1  # Move to next frame
        else:
            print(f"ACK not received. Resending Frame {current_frame}.\n")
            # Resend same frame

# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    data = input("Enter data to send (as string): ")
    stop_and_wait(data)
