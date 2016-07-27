import sys
import Adafruit_DHT
import json
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
    #client.publish("pi3/temperature")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()

while True:
	humidity, temperature = Adafruit_DHT.read_retry(11,4)
	data = {}
	data['Temperature'] = temperature
	data['Humidity'] = humidity
	#print 'Temp: {0:0.1f} C Humidity: {1:0.1f}%'.format(temperature, humidity)
	client.publish("paho/temperature", json.dumps(data))
client.loop_forever()
