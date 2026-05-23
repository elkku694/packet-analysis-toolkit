# Installation Guide - Packet Analysis Toolkit

## Prerequisites

- **Windows 11**
- **Python 3.11 or higher**
- **Administrator access** (for packet capture)

## Step-by-Step Installation

### 1. Install Npcap (Required for Windows packet capture)

1. Download Npcap from: https://npcap.com/download.html
2. Run the installer as Administrator
3. Follow the installation wizard
4. **Important:** Check "Install Npcap in WinPcap API-compatible Mode" during installation
5. Restart your computer after installation

### 2. Clone the Repository

```bash
git clone https://github.com/elkku694/packet-analysis-toolkit.git
cd packet-analysis-toolkit
```

### 3. Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

If you encounter issues with Scapy on Windows, you may need to install it separately:

```bash
pip install scapy[complete]
```

### 5. Run the Application

```bash
python src/main.py
```

Or use the entry point (after setup.py install):

```bash
packet-toolkit
```

## Troubleshooting

### "No module named 'scapy'"
```bash
pip install scapy --upgrade
```

### "Permission Denied" errors
- Run Command Prompt or PowerShell as Administrator
- Or run the Python script with Administrator privileges

### Packet capture not working
1. Verify Npcap is installed correctly
2. Run the application as Administrator
3. Check Windows Firewall settings

### "ImportError: No module named 'PyQt6'"
```bash
pip install PyQt6 --upgrade
```

## Development Setup

For development, install additional tools:

```bash
pip install pytest pytest-cov flake8
```

Run tests:
```bash
pytest
```

## First Run Checklist

- [ ] Npcap installed and running
- [ ] Python 3.11+ installed
- [ ] Virtual environment activated
- [ ] All dependencies installed
- [ ] Application running as Administrator
- [ ] Application starts without errors

## System Requirements

| Component | Requirement |
|-----------|------------|
| OS | Windows 11 |
| Python | 3.11+ |
| RAM | 2GB minimum, 4GB+ recommended |
| Disk Space | 500MB for full installation |
| Network | Administrator access to network interfaces |

## Support

For issues or questions:
1. Check the README.md for usage instructions
2. Review the logs in `logs/` directory
3. Ensure Npcap is properly installed
4. Run as Administrator

## Uninstall

To remove the toolkit:

1. Delete the repository folder
2. Remove virtual environment (if created):
   ```bash
   rmdir /s venv
   ```
3. Uninstall Npcap via Windows Control Panel if desired

---

**Educational Use Only** - Use responsibly and only on networks you own or have explicit permission to test.
