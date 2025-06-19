import ssl
import time
import logging
import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(level=logging.DEBUG)

MQTT_HOST = os.getenv("MQTT_HOST", "cloud-mqtt.movitherm.com")
MQTT_PORT = int(os.getenv("MQTT_PORT", "8883"))
MQTT_USER = os.getenv("MQTT_USER")
MQTT_PASS = os.getenv("MQTT_PASS")
MQTT_TOPIC = os.getenv("MQTT_TOPIC")

# Check if required environment variables are set
if not MQTT_USER:
    raise ValueError("MQTT_USER environment variable is required")
if not MQTT_PASS:
    raise ValueError("MQTT_PASS environment variable is required")
if not MQTT_TOPIC:
    raise ValueError("MQTT_TOPIC environment variable is required")

def on_connect(client, userdata, flags, rc):
    print(f"[CONNECT] rc={rc}")
    if rc == 0:
        print("Connected successfully.")
    else:
        print(f"Connect failed. Result code: {rc}")

def on_log(client, userdata, level, buf):
    print(f"[LOG] {buf}")

def on_disconnect(client, userdata, rc):
    print(f"[DISCONNECT] rc={rc}")


context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_verify_locations("mqtt_cert.pem")
context.check_hostname = True
context.verify_mode = ssl.CERT_REQUIRED
context.set_ciphers('ECDHE+AESGCM')

client = mqtt.Client()
client.enable_logger()
client.username_pw_set(MQTT_USER, MQTT_PASS)
client.tls_set_context(context)
client.tls_insecure_set(False)

client.on_connect = on_connect
client.on_log = on_log
client.on_disconnect = on_disconnect

client.connect_async(MQTT_HOST, MQTT_PORT, keepalive=60)
client.loop_start()

time.sleep(15)
client.loop_stop()
