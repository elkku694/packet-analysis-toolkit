# Development Documentation

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│         GUI Layer (PyQt6)                                   │
│  ┌──────────────┬──────────────┬──────────────────────────┐ │
│  │ Capture      │ Analysis     │  Send Packets            │ │
│  │   Tab        │   Tab        │      Tab                 │ │
│  └──────────────┴──────────────┴──────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────────────────────────┐
│      Core Processing Layer                                  │
│  ┌──────────────┬──────────────┬──────────────────────────┐ │
│  │ Capture      │ Analysis     │  Sender                  │ │
│  │ Manager      │ Engine       │  Engine                  │ │
│  └──────────────┴──────────────┴──────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────────────────────────┐
│      Packet Processing Layer (Scapy)                        │
│         PCAP Handler & File I/O                             │
└─────────────────────────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────────────────────────┐
│    System Layer (Windows Network Driver)                    │
│            Npcap / WinPcap                                  │
└─────────────────────────────────────────────────────────────┘
```

## Module Structure

### src/core/

#### packet_capture.py
- **Class: PacketCapture**
  - `get_interfaces()`: Get list of network interfaces
  - `start_capture()`: Begin packet sniffing
  - `stop_capture()`: Stop packet capture
  - `clear_packets()`: Remove captured packets from memory
  - `get_captured_packets()`: Retrieve all captured packets

**Key Features:**
- Multi-threaded capture (non-blocking)
- Real-time callback system
- BPF filter support
- Packet limit configuration

#### packet_analysis.py
- **Class: PacketAnalyzer**
  - `load_packets()`: Load packets for analysis
  - `get_packet_details()`: Extract detailed packet information
  - `get_statistics()`: Generate aggregate statistics
  - `filter_packets()`: Filter based on criteria
  - `get_top_ips()`: Identify top talkers
  - `get_top_ports()`: Find most used ports

**Key Features:**
- Protocol dissection (IP, TCP, UDP, ICMP)
- Multi-criteria filtering
- Statistical analysis
- IP and port analysis

#### packet_sender.py
- **Class: PacketSender**
  - `send_tcp_packet()`: Craft and send TCP packets
  - `send_udp_packet()`: Craft and send UDP packets
  - `send_icmp_packet()`: Send ICMP ping requests
  - `send_custom_packet()`: Send Scapy packet objects
  - `send_packet_async()`: Asynchronous packet sending

**Key Features:**
- Custom packet crafting
- TCP flag options
- Custom payload support
- Async sending

#### pcap_handler.py
- **Class: PCAPHandler**
  - `save_packets()`: Export packets to PCAP file
  - `load_packets()`: Import packets from PCAP file
  - `get_pcap_files()`: List available PCAP files
  - `delete_pcap()`: Remove PCAP file
  - `get_pcap_info()`: Get PCAP file information

**Key Features:**
- PCAP file I/O
- File management
- Metadata extraction
- Error handling

### src/gui/

#### main_window.py
- **Class: MainWindow** (QMainWindow)
- Manages application window and tabs
- Menu bar with File/Help
- Status bar for user feedback

#### capture_tab.py
- **Class: CaptureTab** (QWidget)
- Live packet capture interface
- Interface selection
- BPF filter input
- Real-time packet display
- PCAP export functionality

#### analysis_tab.py
- **Class: AnalysisTab** (QWidget)
- PCAP file loading and analysis
- Protocol filtering
- IP and port analysis
- Statistics generation
- Results display

#### send_tab.py
- **Class: SendTab** (QWidget)
- Packet crafting interface
- TCP/UDP/ICMP options
- Port configuration
- Custom payload input
- Send log and statistics

#### styles.py
- Application-wide styling (CSS-like)
- Color scheme definition
- Font configuration

## Data Flow

### Packet Capture Flow
```
User clicks "Start"
    ↓
CaptureTab.start_capture()
    ↓
PacketCapture.start_capture()
    ↓
Create capture thread
    ↓
Sniff packets (Scapy)
    ↓
For each packet:
  ├→ Extract metadata
  ├→ Call callback
  ├→ Update UI
  └→ Store in memory
    ↓
User clicks "Stop"
    ↓
PacketCapture.stop_capture()
    ↓
Thread joins
    ↓
Optional: Save to PCAP
```

### Packet Analysis Flow
```
User selects PCAP file
    ↓
AnalysisTab.load_pcap()
    ↓
PCAPHandler.load_packets()
    ↓
Scapy rdpcap() reads file
    ↓
PacketAnalyzer.load_packets()
    ↓
User applies filters/analysis
    ↓
PacketAnalyzer methods process packets
    ↓
Results displayed in UI
```

### Packet Sending Flow
```
User inputs packet details
    ↓
User clicks "Send"
    ↓
SendTab.send_packet()
    ↓
Validate inputs
    ↓
PacketSender.send_*_packet()
    ↓
Scapy creates packet object
    ↓
Scapy sends via Npcap
    ↓
Log entry added
    ↓
UI updated with status
```

## Extending the Toolkit

### Adding a New Analyzer Feature

```python
# In packet_analysis.py
class PacketAnalyzer:
    def your_new_feature(self, criteria):
        """Your feature description"""
        results = []
        for packet in self.packets:
            # Your analysis logic
            if packet_matches(criteria):
                results.append(packet)
        return results
```

### Adding a New Tab

```python
# Create new_tab.py in src/gui/
from PyQt6.QtWidgets import QWidget, QVBoxLayout

class NewTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        # Add your widgets
        self.setLayout(layout)

# In main_window.py
from src.gui.new_tab import NewTab

# In __init__:
self.new_tab = NewTab()
self.tabs.addTab(self.new_tab, "New Tab")
```

## Dependencies

- **scapy**: Packet crafting and analysis
- **PyQt6**: User interface framework
- **npcap**: Windows packet capture driver

## Error Handling

All modules include comprehensive logging:

```python
from src.utils.logger import get_logger

logger = get_logger(__name__)

try:
    # Your code
except Exception as e:
    logger.error(f"Error occurred: {e}")
```

Logs are saved to `logs/` directory with timestamps.

## Performance Considerations

1. **Memory**: Large PCAP files loaded entirely into memory
   - Solution: Implement streaming for large files

2. **UI Responsiveness**: Long operations block UI thread
   - Solution: Use QThreadPool for heavy processing

3. **Packet Display**: Tables slow with 10k+ rows
   - Solution: Implement pagination or virtual scrolling

## Testing

Run tests with pytest:

```bash
pytest tests/ -v
pytest tests/ --cov=src  # With coverage
```

## Debugging

Enable debug logging:

```python
# In logger.py
logging.basicConfig(level=logging.DEBUG)  # Change to DEBUG
```

Check logs in `logs/` directory.

## Security Considerations

⚠️ **This is an educational tool. Important warnings:**

1. Only run on networks you own or have permission to test
2. Don't intercept traffic without authorization
3. Don't send unsolicited packets
4. Respect privacy and local laws
5. Use for learning only

---

**For Developers**: Refer to Scapy docs and PyQt6 documentation for detailed API information.
