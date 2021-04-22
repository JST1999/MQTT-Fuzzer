import paho.mqtt.client as mqtt
import time
import csv
import datetime
import pyradamsa

rad = pyradamsa.Radamsa()
topic = "dev/test"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    
client = mqtt.Client()
client.username_pw_set(username="username",password="password")
client.on_connect = on_connect
client.connect("192.168.0.16", 1883, 60)

cases = []
with open("messages-to-mutate.txt") as f:
    lines = f.readlines()
    for ele in lines:
        cases.append(ele.rstrip())#they have a \n so I removed it

def write_to_file(topic, case):
    with open("sent_log.csv", 'a', encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([datetime.datetime.now(), topic, case])

for ele in cases:
    for i in range(100000):
        case = rad.fuzz(ele.encode("UTF-8"))
        decodedCase = case.decode("UTF-8", "ignore")

        client.publish(topic, payload=case, qos=0, retain=False)
        write_to_file(topic, case)

        client.publish(topic, payload=decodedCase, qos=0, retain=False)
        write_to_file(topic, decodedCase)

print("Done")

client.loop_forever()