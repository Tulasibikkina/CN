# Leaky Bucket Algorithm Simulation

def leaky_bucket(bucket_size, output_rate, packet_arrival):
    """
    Simulate leaky bucket congestion control
    :param bucket_size: Maximum capacity of the bucket
    :param output_rate: Number of packets sent per time unit
    :param packet_arrival: List of packets arriving at each time unit
    """
    n = len(packet_arrival)
    bucket = 0  # Current number of packets in bucket
    time_unit = 0

    print("\n--- Leaky Bucket Algorithm Simulation ---\n")
    print("Time\tIncoming\tBucket\tSent\tDropped")

    for i in range(n):
        incoming = packet_arrival[i]
        bucket += incoming

        dropped = 0
        if bucket > bucket_size:
            dropped = bucket - bucket_size
            bucket = bucket_size

        sent = min(bucket, output_rate)
        bucket -= sent

        print(f"{time_unit}\t{incoming}\t\t{bucket + sent}\t{sent}\t{dropped}")
        time_unit += 1

    # Flush remaining packets in bucket
    while bucket > 0:
        sent = min(bucket, output_rate)
        print(f"{time_unit}\t0\t\t{bucket}\t{sent}\t0")
        bucket -= sent
        time_unit += 1

# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    bucket_size = int(input("Enter bucket size: "))
    output_rate = int(input("Enter output rate (packets per time unit): "))
    packet_arrival = list(map(int, input("Enter incoming packets at each time unit (space-separated): ").split()))
    leaky_bucket(bucket_size, output_rate, packet_arrival)
