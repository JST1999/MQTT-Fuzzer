import paho.mqtt.client as mqtt
import time
import csv
import datetime
import pyradamsa

rad = pyradamsa.Radamsa()
topic = "dev/test"
m = "Sending message "

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    
client = mqtt.Client()

cases = []
with open("usernames-to-mutate.txt") as f:
    lines = f.readlines()
    for ele in lines:
        cases.append(ele.rstrip())#they have a \n so I removed it

def write_to_file(testCase, topic, message):
    with open("sent_log.csv", 'a', encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([datetime.datetime.now(), testCase, topic, message])

for ele in cases:
    for i in range(10000):
        case = rad.fuzz(ele.encode("UTF-8"))
        decodedCase = case.decode("UTF-8", "ignore")

        client.username_pw_set(username=decodedCase, password="password")#make sure allow anonymous is true and there is no linked password file
        client.on_connect = on_connect
        client.connect("192.168.0.25", 1883, 60)

        message = m + str(i) + " with original topic " + ele
        client.publish(topic, payload=message, qos=0, retain=False)
        write_to_file(decodedCase, topic, message)

        client.disconnect()

print("Done")