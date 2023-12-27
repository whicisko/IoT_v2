# mqtt-client/main.py
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print("Received message:", msg.payload)

client = mqtt.Client()
client.connect("mqtt-broker", 1883, 60)
client.subscribe("output_topic")
client.on_message = on_message

client.loop_forever()
