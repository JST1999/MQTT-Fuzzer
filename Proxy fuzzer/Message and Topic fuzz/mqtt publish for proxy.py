import paho.mqtt.client as mqtt
import time
import csv
import datetime

topic = "dev/test"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    
client = mqtt.Client()
client.username_pw_set(username="username",password="password")
client.on_connect = on_connect
client.connect("192.168.0.25", 9998, 60)

def write_to_file(topic, message):
    with open("sent_log.csv", 'a', encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([datetime.datetime.now(), topic, message])

cases = []
with open("messages-to-mutate.txt") as f:
    lines = f.readlines()
    for ele in lines:
        cases.append(ele.rstrip())#they have a \n so I removed it

for ele in cases:
    for connection in range(100):
        write_to_file(topic, ele)
        for i in range(14):
            message = ele# + str(i)

            client.publish(topic, payload=message, qos=0, retain=False)

            time.sleep(0.001)

        client.disconnect()
        time.sleep(0.1)#seperate out each 'block'
        client.reconnect()

print("Done")

#client.loop_forever()#not really needed