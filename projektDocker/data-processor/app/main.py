# data-processor/main.py
import paho.mqtt.client as mqtt
import requests
import json

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)
    # Do something with the payload (process data, etc.)
    print("Received message:", payload)

client = mqtt.Client()
client.connect("mqtt-broker", 1883, 60)
client.subscribe("input_topic")
client.on_message = on_message

client.loop_forever()
