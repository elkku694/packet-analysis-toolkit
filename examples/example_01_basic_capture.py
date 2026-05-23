#!/usr/bin/env python3
"""
Example 1: Basic Packet Capture
Demonstrates how to capture packets from a network interface
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core.packet_capture import PacketCapture
from src.core.pcap_handler import PCAPHandler
import time

def callback(packet_info):
    """Callback for each captured packet"""
    print(f"[{packet_info['number']}] {packet_info['src']} -> {packet_info['dst']} "
          f"({packet_info['protocol']}) - {packet_info['size']} bytes")

def main():
    # Create packet capture instance
    capture = PacketCapture(callback=callback)
    
    # Get available interfaces
    interfaces = capture.get_interfaces()
    print(f"Available interfaces: {interfaces}")
    
    if not interfaces:
        print("No interfaces found. Make sure Npcap is installed.")
        return
    
    # Use first interface
    interface = interfaces[0]
    print(f"\nCapturing on {interface}...")
    print("Press Ctrl+C to stop\n")
    
    # Start capture for 10 seconds
    capture.start_capture(interface, packet_filter="", packet_count=0)
    
    try:
        time.sleep(10)
    except KeyboardInterrupt:
        pass
    
    # Stop capture
    count = capture.stop_capture()
    print(f"\nCaptured {count} packets")
    
    # Save to PCAP
    if capture.packets:
        pcap_handler = PCAPHandler()
        success, path = pcap_handler.save_packets(capture.packets, "example_capture.pcap")
        if success:
            print(f"Saved to: {path}")

if __name__ == '__main__':
    main()
