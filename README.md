cat > README.md << 'EOF'

A simple Python MQTT/TLS simulator that:
- Connects to AWS IoT Core using X.509 certs
- Publishes telemetry
- Subscribes to command topic: devices/<deviceId>/commands

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
