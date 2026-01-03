# AWS IoT Device Simulator (Python)

A simple Python-based simulator that mimics an IoT device connecting to AWS IoT Core using MQTT over TLS (X.509 certificates).

This project demonstrates:
- Secure device-to-cloud connectivity
- Telemetry publishing
- Cloud-to-device command handling

## Features
- Connects to AWS IoT Core using TLS certificates
- Publishes simulated telemetry data (temperature, speed, battery)
- Subscribes to command topic: `devices/<deviceId>/commands`

## Project Structure
iot-device-simulator/

├── device_sim.py # Main simulator script

├── requirements.txt # Python dependencies

├── .gitignore # Git ignore rules

└── README.md # Project documentation


## How It Works
- The simulator authenticates to AWS IoT Core using X.509 certificates
- Periodically publishes telemetry data over MQTT
- Listens for cloud-to-device commands on a subscribed topic
- Prints received commands to the terminal

## Security Notes
- TLS certificates and private keys are excluded from version control
- `.gitignore` prevents accidental credential leaks

## Use Case
This project can be used as a reference for:
- AWS IoT Core MQTT connectivity
- Secure IoT device simulation
