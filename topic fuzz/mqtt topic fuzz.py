import paho.mqtt.client as mqtt
import time
import csv
import datetime
import pyradamsa

rad = pyradamsa.Radamsa()
message = "hi"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    
client = mqtt.Client()
client.username_pw_set(username="username",password="password")
client.on_connect = on_connect
client.connect("192.168.0.16", 1883, 60)

cases = []
with open("topics-to-mutate.txt") as f:
    lines = f.readlines()
    for ele in lines:
        cases.append(ele.rstrip())#they have a \n so I removed it

def write_to_file(topic, case):
    with open("sent_log_topic.csv", 'a', encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([datetime.datetime.now(), topic, case])

for ele in cases:
    for i in range(100000):
        topic = rad.fuzz(ele.encode("UTF-8"))
        topic = topic.decode("UTF-8", "ignore")

        client.publish(topic, payload=message, qos=0, retain=False)
        write_to_file(topic, message)

print("Done")

client.loop_forever()