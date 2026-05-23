#!/usr/bin/env python3
"""
Example 4: Advanced Filtering
Demonstrates packet filtering capabilities
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core.packet_analysis import PacketAnalyzer
from src.core.pcap_handler import PCAPHandler

def main():
    analyzer = PacketAnalyzer()
    handler = PCAPHandler()
    
    # Load a PCAP file
    files = handler.get_pcap_files()
    if not files:
        print("No PCAP files found.")
        return
    
    filename = files[0]
    success, packets = handler.load_packets(filename)
    if not success:
        print(f"Error: {packets}")
        return
    
    analyzer.load_packets(packets)
    
    print(f"Loaded {len(packets)} packets from {filename}\n")
    
    # Example 1: Filter by protocol
    print("=== Filter by Protocol ===")
    tcp_packets = analyzer.filter_packets({'protocol': 'TCP'})
    print(f"TCP packets: {len(tcp_packets)}")
    
    udp_packets = analyzer.filter_packets({'protocol': 'UDP'})
    print(f"UDP packets: {len(udp_packets)}")
    
    icmp_packets = analyzer.filter_packets({'protocol': 'ICMP'})
    print(f"ICMP packets: {len(icmp_packets)}")
    
    # Example 2: Filter by source IP (if data available)
    print("\n=== Filter by Source IP ===")
    if packets:
        from scapy.all import IP
        if IP in packets[0]:
            src_ip = packets[0][IP].src
            same_src = analyzer.filter_packets({'src_ip': src_ip})
            print(f"Packets from {src_ip}: {len(same_src)}")
    
    # Example 3: Filter by port
    print("\n=== Filter by Port ===")
    port_80 = analyzer.filter_packets({'port': 80})
    print(f"Port 80 packets: {len(port_80)}")
    
    port_443 = analyzer.filter_packets({'port': 443})
    print(f"Port 443 packets: {len(port_443)}")
    
    # Example 4: Complex filtering
    print("\n=== Complex Filter ===")
    tcp_port_80 = analyzer.filter_packets({'protocol': 'TCP', 'port': 80})
    print(f"TCP port 80 packets: {len(tcp_port_80)}")

if __name__ == '__main__':
    main()
