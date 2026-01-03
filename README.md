# AWS IoT Device Simulator (Python)

A simple Python-based simulator that mimics an IoT device connecting to **AWS IoT Core** using **MQTT over TLS (X.509 certificates)**.

This project demonstrates core IoT concepts used in real-world systems.

---

## Features
- Secure device-to-cloud connectivity using TLS certificates
- Publishes simulated telemetry data:
  - Temperature
  - Speed
  - Battery level
- Subscribes to cloud-to-device command topic

---

## Project Structure
iot-device-simulator/
├── device_sim.py # Main simulator script
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
└── README.md

yaml
Copy code

> TLS certificates are intentionally excluded from the repository.

---

## Setup & Run

### 1. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
