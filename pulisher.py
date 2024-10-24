import paho.mqtt.client as mqtt
import time

# Define MQTT broker details
broker = "192.168.206.246"  # Local broker
port = 1883           # Standard MQTT port
topic = "timed/data"  # Topic to publish data

# Callback when connected to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))

# Create MQTT client and connect to broker
client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker, port, 60)

# Start the client loop
client.loop_start()

try:
    while True:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        client.publish(topic, timestamp)
        print(f"Published: {timestamp} to topic: {topic}")
        time.sleep(1)  # Send data every second
except KeyboardInterrupt:
    print("Exiting...")
finally:
    client.loop_stop()
    client.disconnect()
