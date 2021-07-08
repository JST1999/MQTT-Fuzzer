import paho.mqtt.client as mqtt
import time
import csv
import datetime
import pyradamsa

rad = pyradamsa.Radamsa()

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    
client = mqtt.Client()
client.username_pw_set(username="username",password="password")
client.on_connect = on_connect
client.connect("192.168.0.25", 1883, 60)

cases = []
with open("topics-to-mutate.txt") as f:
    lines = f.readlines()
    for ele in lines:
        cases.append(ele.rstrip())#they have a \n so I removed it

def write_to_file(topic, mutatedTopic):
    with open("sent_log.csv", 'a', encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([datetime.datetime.now(), topic, mutatedTopic])

for ele in cases:
    client.subscribe(ele)
    for i in range(1):
        case = rad.fuzz(ele.encode("UTF-8"))
        decodedCase = case.decode("UTF-8", "ignore")

        write_to_file(ele, decodedCase)

        client.unsubscribe(decodedCase)

        client.unsubscribe(case)

print("Done")