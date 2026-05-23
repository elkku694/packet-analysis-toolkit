#!/usr/bin/env python3
"""
Packet Analysis Toolkit - Main Entry Point
Educational tool for packet capture, analysis, and manipulation
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from PyQt6.QtWidgets import QApplication
from src.gui.main_window import MainWindow
from src.utils.logger import get_logger

logger = get_logger(__name__)

def main():
    """Main entry point"""
    logger.info("Starting Packet Analysis Toolkit")
    
    app = QApplication(sys.argv)
    
    # Set application name and version
    app.setApplicationName("Packet Analysis Toolkit")
    app.setApplicationVersion("1.0.0")
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    logger.info("Main window displayed")
    
    # Run application
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
