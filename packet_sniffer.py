from scapy.all import IP, TCP, UDP, ICMP, Raw

def analyze_packet(pkt):
    print("=" * 40)
    if pkt.haslayer(IP):
        print(f"Source IP: {pkt[IP].src}")
        print(f"Destination IP: {pkt[IP].dst}")
        print(f"Protocol: {pkt[IP].proto}")

    if pkt.haslayer(TCP):
        print(f"Type: TCP")
        print(f"Source Port: {pkt[TCP].sport}")
        print(f"Destination Port: {pkt[TCP].dport}")
        print(f"Flags: {pkt[TCP].flags}")
    elif pkt.haslayer(UDP):
        print(f"Type: UDP")
        print(f"Source Port: {pkt[UDP].sport}")
        print(f"Destination Port: {pkt[UDP].dport}")
    elif pkt.haslayer(ICMP):
        print(f"Type: ICMP")

    if pkt.haslayer(Raw):
        print(f"Payload: {pkt[Raw].load}")
    print("=" * 40)

sample_packets = [
    IP(src="192.168.1.10", dst="192.168.1.1") / TCP(sport=443, dport=54321, flags="SA") / Raw(load="Hello Server"),
    IP(src="10.0.0.5", dst="8.8.8.8") / UDP(sport=53, dport=12345) / Raw(load="DNS Query"),
    IP(src="192.168.1.20", dst="192.168.1.1") / ICMP(),
]

print("Analyzing sample network packets...\n")
for packet in sample_packets:
    analyze_packet(packet)
