from scapy.all import sniff, IP, TCP, UDP, ICMP


def analyze_packet(packet):
    if IP in packet:
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"
        else:
            protocol = "Other"

        print("-" * 60)
        print(f"Source IP      : {source_ip}")
        print(f"Destination IP : {destination_ip}")
        print(f"Protocol       : {protocol}")
        print(f"Packet Length  : {len(packet)} bytes")


print("CodeAlpha Basic Network Sniffer")
print("Capturing packets... Press CTRL+C to stop.")
print()

sniff(prn=analyze_packet, store=False)