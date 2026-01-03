# AWS IoT Device Simulator (Python)

A simple Python-based simulator that mimics an IoT device connecting to **AWS IoT Core** using **MQTT over TLS (X.509 certificates)**.

This project was built to demonstrate:
- Secure device-to-cloud connectivity
- Telemetry publishing
- Cloud-to-device command handling

---

## Features
- Connects to AWS IoT Core using TLS certificates
- Publishes simulated telemetry data (temperature, speed, battery)
- Subscribes to command topic:
iot-device-simulator/
├── device_sim.py # Main simulator script
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
└── README.md
