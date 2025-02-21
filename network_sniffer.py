from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        protocol = packet["IP"].proto
        print(f"Source: {src_ip} → Destination: {dst_ip} | Protocol: {protocol}")

print("Starting network sniffer...")
sniff(iface="eth0", filter="ip", prn=packet_callback, store=False)
