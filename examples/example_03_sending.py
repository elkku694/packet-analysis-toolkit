#!/usr/bin/env python3
"""
Example 3: Sending Packets
Demonstrates how to craft and send custom packets
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core.packet_sender import PacketSender

def main():
    sender = PacketSender()
    
    print("=== Packet Sender Examples ===")
    print("Note: Requires admin privileges\n")
    
    # Example 1: Send ICMP Ping
    print("1. Sending ICMP Ping to 8.8.8.8...")
    # Uncomment to actually send:
    # sender.send_icmp_packet("127.0.0.1", "8.8.8.8")
    print("   (Skipped - would require admin and network access)")
    
    # Example 2: Send TCP SYN
    print("\n2. Sending TCP SYN packet...")
    print("   Target: 192.168.1.1:80")
    # Uncomment to actually send:
    # sender.send_tcp_packet("127.0.0.1", "192.168.1.1", 12345, 80, flags="S")
    print("   (Skipped - would require admin and network access)")
    
    # Example 3: Send UDP
    print("\n3. Sending UDP packet...")
    print("   Target: 8.8.8.8:53 (DNS)")
    # Uncomment to actually send:
    # sender.send_udp_packet("127.0.0.1", "8.8.8.8", 12345, 53, data="DNS Query")
    print("   (Skipped - would require admin and network access)")
    
    print(f"\nTotal packets sent: {sender.get_sent_count()}")
    print("\nTo actually send packets:")
    print("1. Run this script as Administrator")
    print("2. Uncomment the sender.send_*() calls")
    print("3. Ensure Npcap is installed")
    print("4. Make sure you have network access to targets")

if __name__ == '__main__':
    main()
