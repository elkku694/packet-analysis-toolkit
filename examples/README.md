# Examples - Educational Packet Analysis

This directory contains educational examples demonstrating the Packet Analysis Toolkit features.

## Examples

### 1. Basic Packet Capture (`example_01_basic_capture.py`)

Demonstrates live packet capture from a network interface.

```bash
python examples/example_01_basic_capture.py
```

**What it does:**
- Lists all available network interfaces
- Captures packets for 10 seconds
- Saves captured packets to PCAP file

**Output:**
```
Available interfaces: ['Ethernet', 'Wi-Fi', 'Loopback']
Capturing on Ethernet...
[1] 192.168.1.100 -> 8.8.8.8 (TCP:443) - 1514 bytes
[2] 8.8.8.8 -> 192.168.1.100 (TCP:443) - 1460 bytes
...
Captured 150 packets
Saved to: pcap_files/example_capture.pcap
```

### 2. Packet Analysis (`example_02_analysis.py`)

Demonstrates how to load and analyze PCAP files.

```bash
python examples/example_02_analysis.py
```

**What it does:**
- Lists available PCAP files
- Loads the first PCAP file
- Generates statistics
- Shows top IPs and ports
- Demonstrates filtering

**Output:**
```
=== STATISTICS ===
Total packets: 150
Total bytes: 245.32 MB

Protocol breakdown:
  TCP: 120
  UDP: 25
  ICMP: 5

=== TOP IPS ===
Top Source IPs:
  192.168.1.100: 85 packets
  192.168.1.101: 40 packets
  8.8.8.8: 25 packets
```

### 3. Sending Packets (`example_03_sending.py`)

Demonstrates packet crafting and sending (requires admin).

```bash
python examples/example_03_sending.py
```

**What it does:**
- Shows how to send ICMP pings
- Shows how to send TCP packets
- Shows how to send UDP packets
- Displays packet counter

**Note:** Requires administrator privileges and Npcap installed.

### 4. Advanced Filtering (`example_04_filtering.py`)

Demonstrates advanced packet filtering.

```bash
python examples/example_04_filtering.py
```

**What it does:**
- Filters packets by protocol
- Filters packets by source IP
- Filters packets by port
- Demonstrates complex filtering

**Output:**
```
=== Filter by Protocol ===
TCP packets: 120
UDP packets: 25
ICMP packets: 5

=== Filter by Port ===
Port 80 packets: 45
Port 443 packets: 55
```

## Running Examples

### Prerequisites

```bash
# Install dependencies
pip install -r ../requirements.txt
```

### For Capture and Send Examples

Run as Administrator:

```bash
# Windows
runas /user:Administrator "python examples/example_01_basic_capture.py"

# Or open Command Prompt as Administrator and run:
python examples/example_01_basic_capture.py
```

### For Analysis Examples

No special privileges needed:

```bash
python examples/example_02_analysis.py
```

## Learning Outcomes

After running these examples, you'll understand:

1. ✅ How to capture network packets
2. ✅ How to work with PCAP files
3. ✅ How to analyze packet data
4. ✅ How to filter packets by various criteria
5. ✅ How to craft and send custom packets
6. ✅ Network protocol fundamentals
7. ✅ How to use Scapy for packet manipulation

## Troubleshooting

### "No module named 'scapy'"
```bash
pip install scapy
```

### "No interfaces found"
- Ensure Npcap is installed: https://npcap.com
- Run as Administrator
- Check Windows Firewall

### "Permission Denied"
- Run Command Prompt as Administrator
- Run Python script with admin privileges

### "No PCAP files found"
- First run `example_01_basic_capture.py` to generate a PCAP file
- Or provide your own PCAP file in `pcap_files/` directory

## Next Steps

1. Modify examples to fit your learning goals
2. Try different packet filters
3. Analyze your own network traffic
4. Create custom packet crafting scripts
5. Explore the Scapy documentation

## References

- **Scapy Documentation:** http://www.secdev.org/projects/scapy/doc/
- **PCAP Format:** https://en.wikipedia.org/wiki/Pcap
- **Network Protocols:** https://en.wikipedia.org/wiki/Internet_protocol_suite
- **BPF Syntax:** https://www.tcpdump.org/papers/sniffing-faq.html

---

**Educational Use Only** - Use these examples responsibly on networks you own or have permission to test.
