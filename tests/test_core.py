import pytest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core.packet_capture import PacketCapture
from src.core.packet_analysis import PacketAnalyzer
from src.core.packet_sender import PacketSender
from src.core.pcap_handler import PCAPHandler


class TestPacketCapture:
    """Tests for packet capture functionality"""
    
    def test_packet_capture_init(self):
        """Test PacketCapture initialization"""
        capture = PacketCapture()
        assert capture.is_capturing == False
        assert capture.packet_count == 0
        assert len(capture.packets) == 0
    
    def test_get_interfaces(self):
        """Test getting network interfaces"""
        capture = PacketCapture()
        interfaces = capture.get_interfaces()
        assert isinstance(interfaces, list)
    
    def test_clear_packets(self):
        """Test clearing captured packets"""
        capture = PacketCapture()
        capture.packet_count = 5
        capture.packets = [1, 2, 3, 4, 5]
        capture.clear_packets()
        assert capture.packet_count == 0
        assert len(capture.packets) == 0


class TestPacketAnalyzer:
    """Tests for packet analysis functionality"""
    
    def test_analyzer_init(self):
        """Test PacketAnalyzer initialization"""
        analyzer = PacketAnalyzer()
        assert len(analyzer.packets) == 0
    
    def test_load_packets(self):
        """Test loading packets"""
        analyzer = PacketAnalyzer()
        test_packets = [1, 2, 3]
        analyzer.load_packets(test_packets)
        assert len(analyzer.packets) == 3
    
    def test_get_statistics_empty(self):
        """Test getting statistics on empty packets"""
        analyzer = PacketAnalyzer()
        stats = analyzer.get_statistics()
        assert stats == {}
    
    def test_filter_packets_empty(self):
        """Test filtering empty packets"""
        analyzer = PacketAnalyzer()
        filtered = analyzer.filter_packets({})
        assert len(filtered) == 0


class TestPacketSender:
    """Tests for packet sending functionality"""
    
    def test_sender_init(self):
        """Test PacketSender initialization"""
        sender = PacketSender()
        assert sender.sent_count == 0
    
    def test_get_sent_count(self):
        """Test getting sent packet count"""
        sender = PacketSender()
        assert sender.get_sent_count() == 0
    
    def test_reset_counter(self):
        """Test resetting packet counter"""
        sender = PacketSender()
        sender.sent_count = 5
        sender.reset_counter()
        assert sender.sent_count == 0


class TestPCAPHandler:
    """Tests for PCAP file handling"""
    
    def test_pcap_handler_init(self):
        """Test PCAPHandler initialization"""
        handler = PCAPHandler()
        assert handler.pcap_dir == "pcap_files"
    
    def test_get_pcap_files(self):
        """Test getting PCAP files list"""
        handler = PCAPHandler()
        files = handler.get_pcap_files()
        assert isinstance(files, list)
    
    def test_delete_nonexistent_pcap(self):
        """Test deleting non-existent PCAP"""
        handler = PCAPHandler()
        result = handler.delete_pcap("nonexistent.pcap")
        assert result == False


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
