import paho.mqtt.client as mqtt
import os
import time

def on_connect(client,userdata,flags,rc):
      if rc==0:
         print("connected ok")
      else:
         print("Bad connection = ",rc)
def on_disconnect(client,userdata,flags,rc=0):
         print("Disconnect result code"+str(rc))
def on_message(client,userdata,msg):
      topic=msg.topic
      m_decode=str(msg.payload.decode("utf-8"))
      print("message recieved",m_decode)
broker = "test.mosquitto.org"
port = 1883
client = mqtt.Client("python2")
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
print("connecting to broker")
client.connect(broker)
client.loop_start()
client.subscribe("hacklab/sensor2")
while 1:
    time.sleep(6)
    print "Sending data"
    client.publish("hacklab/sensor1","my first mqtt message-1")
client.loop_stop()
client.disconnect()
