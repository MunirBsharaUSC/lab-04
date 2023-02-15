import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

# global variable
messagefrompong=1
"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    client.subscribe("bshara/pong")
    client.message_callback_add("bshara/pong", on_message_from_pong)

# publish with ping
def on_message_from_pong(client, userdata, message):
    messagefrompong=0
    print("Custom callback - Pong Message: " + message.payload.decode())
    client.publish("bshara/ping", int(message.payload.decode())+1)
    print("Publishing ping")
    time.sleep(1)


if __name__ == '__main__':
    #get IP address
    ip_address=socket.gethostbyname(socket.gethostname())
    """your code here"""
    #create a client object
    client = mqtt.Client()
    
    client.on_message
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    
    # connecting to host
    client.connect(host="172.20.10.3", port=1883, keepalive=60)

    client.publish("bshara/ping", 1)
    print("Publishing ping")
    client.loop_forever()
