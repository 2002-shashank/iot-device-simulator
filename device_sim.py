import json
import time
import ssl
import random
import paho.mqtt.client as mqtt

# ===============================
# CONFIG — CHANGE ONLY THESE 2
# ===============================

IOT_ENDPOINT = "a2rtdeqrvgnovt-ats.iot.us-east-1.amazonaws.com"
DEVICE_ID = "truck001"

ROOT_CA_PATH = "AmazonRootCA1.pem"
CERT_PATH = "device.pem.crt"
PRIVATE_KEY_PATH = "private.pem.key"

# ===============================
# MQTT CALLBACKS
# ===============================

def on_connect(client, userdata, flags, rc):
    print("CONNECTED TO AWS IoT | rc =", rc)

    # listen for shadow delta / commands
    topic = f"devices/{DEVICE_ID}/commands"
    client.subscribe(topic)
    print("SUBSCRIBED TO:", topic)


def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    print("\nDELTA RECEIVED:")
    print(json.dumps(payload, indent=2))

    # device acts on delta
    reported = payload.get("delta", {})

    # publish reported state
    client.publish(
        f"devices/{DEVICE_ID}/reported",
        json.dumps(reported),
        qos=1
    )

    print("REPORTED STATE SENT:", reported)


# ===============================
# MAIN
# ===============================

client = mqtt.Client(client_id=DEVICE_ID)

client.tls_set(
    ca_certs=ROOT_CA_PATH,
    certfile=CERT_PATH,
    keyfile=PRIVATE_KEY_PATH,
)

client.on_connect = on_connect
client.on_message = on_message

print("CONNECTING TO AWS IoT...")
client.connect(IOT_ENDPOINT, 8883)
client.loop_start()

# publish telemetry every 5 seconds
while True:
    telemetry = {
        "deviceId": DEVICE_ID,
        "temperature": random.randint(25, 40),
        "speed": random.randint(40, 80),
        "battery": random.randint(60, 100)
    }

    client.publish(
        f"devices/{DEVICE_ID}/telemetry",
        json.dumps(telemetry),
        qos=1
    )

    print("TELEMETRY SENT:", telemetry)
    time.sleep(5)

