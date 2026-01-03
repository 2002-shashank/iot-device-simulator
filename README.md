# AWS IoT Device Simulator (MQTT + TLS)

A simple **Python-based AWS IoT device simulator** that connects securely to **AWS IoT Core** using **X.509 certificates**, publishes telemetry data, and listens for cloud-to-device commands.

This project demonstrates a **real-world IoT device lifecycle** including telemetry, device shadow updates, and command handling — suitable for **internships, resumes, and demos**.

---

## Features

- Secure MQTT connection to **AWS IoT Core** using TLS
- Publishes simulated telemetry data
- Subscribes to device command topic
- Works with AWS IoT Device Shadow (desired → delta)
- Lightweight and easy to run locally

---

## Project Structure

```text
iot-device-simulator/
├── device_sim.py          # Main device simulator
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore rules
├── AmazonRootCA1.pem      # Root CA (not committed)
├── device.pem.crt         # Device certificate (not committed)
├── private.pem.key        # Private key (not committed)
└── venv/                  # Python virtual environment

