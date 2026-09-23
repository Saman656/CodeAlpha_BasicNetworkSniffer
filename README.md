# CodeAlpha_BasicNetworkSniffer
# CodeAlpha Basic Network Sniffer

## Project Overview

This project is a basic network sniffer developed in Python using the Scapy library.

The program captures network packets on an authorized local network and displays useful information about the captured traffic.

## Features

- Captures network packets
- Displays source IP address
- Displays destination IP address
- Identifies basic protocols such as TCP, UDP and ICMP
- Displays packet length
- Provides basic network traffic analysis

## Technologies Used

- Python
- Scapy

## How to Run

1. Install Python.
2. Install Scapy:

```bash
python -m pip install scapy
Run the program:
python sniffer.py
Press CTRL+C to stop packet capturing.
Sample Output
------------------------------------------------------------
Source IP      : 192.168.1.3
Destination IP : 40.99.70.178
Protocol       : TCP
Packet Length  : 55 bytes
------------------------------------------------------------
Learning Objectives
Understand basic network packet structure
Learn how network traffic flows
Identify common network protocols
Practice packet capturing using Python and Scapy
Ethical Use

This project should only be used on networks and devices where the user has permission to capture and analyze traffic.

Internship

Developed as part of the CodeAlpha Cyber Security Internship.
