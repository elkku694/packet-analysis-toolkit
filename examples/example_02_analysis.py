#!/usr/bin/env python3
"""
Example 2: Packet Analysis
Demonstrates how to load and analyze PCAP files
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core.packet_analysis import PacketAnalyzer
from src.core.pcap_handler import PCAPHandler

def main():
    # Create analyzer and handler
    analyzer = PacketAnalyzer()
    handler = PCAPHandler()
    
    # List available PCAP files
    files = handler.get_pcap_files()
    print(f"Available PCAP files: {files}\n")
    
    if not files:
        print("No PCAP files found. Run example_01_basic_capture.py first.")
        return
    
    # Load first file
    filename = files[0]
    print(f"Loading {filename}...")
    success, packets = handler.load_packets(filename)
    
    if not success:
        print(f"Error loading file: {packets}")
        return
    
    analyzer.load_packets(packets)
    
    # Generate statistics
    print("\n=== STATISTICS ===")
    stats = analyzer.get_statistics()
    print(f"Total packets: {stats['total_packets']}")
    print(f"Total bytes: {stats['total_bytes'] / (1024*1024):.2f} MB")
    print(f"\nProtocol breakdown:")
    for protocol, count in sorted(stats['protocols'].items(), key=lambda x: x[1], reverse=True):
        print(f"  {protocol}: {count}")
    
    # Top IPs
    print("\n=== TOP IPS ===")
    top_ips = analyzer.get_top_ips(limit=5)
    print("Top Source IPs:")
    for ip, count in top_ips['top_src_ips']:
        print(f"  {ip}: {count} packets")
    
    print("\nTop Destination IPs:")
    for ip, count in top_ips['top_dst_ips']:
        print(f"  {ip}: {count} packets")
    
    # Top Ports
    print("\n=== TOP PORTS ===")
    top_ports = analyzer.get_top_ports(limit=5)
    for port, count in top_ports:
        print(f"  Port {port}: {count} packets")
    
    # Filter example
    print("\n=== FILTERED RESULTS ===")
    criteria = {'protocol': 'TCP'}
    filtered = analyzer.filter_packets(criteria)
    print(f"TCP packets: {len(filtered)}")

if __name__ == '__main__':
    main()
