#author : erdiansahlan@student.ub.ac.id

import paho.mqtt.client as mqtt_client

sub.connect("127.0.0.1", port=1883)

def handle_message(client, object, msg)
    print("Topiknya adalah : "+msg.topic+" Message : "+msg.payload.decode('ascii'))

sub.on_message = handle_message

sub.subscribe("/sensor/suhu/1")

sub.loop_forever()