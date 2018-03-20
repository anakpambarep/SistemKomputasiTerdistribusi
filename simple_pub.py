#author : erdiansahlan@student.ub.ac.id

import paho.mqtt.client as mqtt_client

pub = mqtt_client.Client()

pub.connect("127.0.0.1", port = 1883)

pub.publish("/sensor/suhu/1", "30")
pub.publish("/sensor/suhu/2", "30")
pub.publish("/sensor/humidity/1", "80%")
pub.publish("/sensor/humidity/2", "90%")

