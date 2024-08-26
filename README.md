
#  Dover - Automated Information Gathering & Vulnerability Assessment Tool

##  Overview

Dover is a tool designed to automate the critical first steps of penetration testing: **Information Gathering** and **Vulnerability Assessment**. As systems become increasingly complex and interconnected, the risk of vulnerabilities grows. Dover simplifies the process of identifying these vulnerabilities, helping you secure your network efficiently and effectively.

Say goodbye to the tedious, manual steps of penetration testing and say hello to streamlined, automated security analysis!

##  Key Features

- **Network Confirmation**: Automatically confirms the host network.
- **Host Discovery**: Identifies all live devices on the same network.
- **Comprehensive Port Scanning**: Scans for all open ports, revealing service details, versions, and the operating system.
- **Vulnerability Identification**: Flags commonly exploited ports and highlights potential security risks with severity warnings.
- **Automated PDF Reporting**: Generates a detailed, timestamped report for easy analysis.

##  Getting Started

### Prerequisites

- **Operating System**: Linux (Tested on Kali Linux and Ubuntu)
- **Python**: Version 2.7
- **Dependencies**:
  - [Arp-Scan](https://github.com/royhills/arp-scan)
  - [Nmap](https://nmap.org/)
  - Python Libraries: `termcolor`, `fpdf`

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/dover.git
   cd dover
   ```

2. **Install Dependencies**:
   ```bash
   sudo apt-get install arp-scan nmap
   pip install termcolor fpdf
   ```

3. **Run Dover**:
   ```bash
   sudo python2 dover.py
   ```

##  How It Works

1. **Network Confirmation**: Dover confirms the network using `ifconfig`, converting your IP address to CIDR notation.
2. **Host Discovery**: Utilizes `arp-scan` to find all live devices on the network.
3. **Port Scanning**: Performs a thorough scan with `nmap` to identify open ports, services, and operating systems.
4. **Intense Scan**: An additional nmap scan that performs a detailed assessment of the open ports
5. **Vulnerability Identification**: Checks for commonly exploited ports, categorizing them by severity (Critical, Medium, Low).
6. **Report Generation**: Compiles all findings into a clean, organized PDF report.

##  Example Output

Here's a sneak peek at what your PDF report will look like:

![Dover Report](https://yourimageurl.com/dover_report_example.png)

## Conclusion

The Dover tool streamlines the early stages of penetration testing by automating critical information-gathering and vulnerability identification processes. This ensures that potential security risks are identified efficiently, allowing administrators to focus on mitigating them.

