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

print(cases)
for ele in cases:
    for i in range(3):
        case = rad.fuzz(ele.encode("UTF-8"), seed=117)

        client.publish(topic, payload=case, qos=0, retain=False)

        with open("sent_log.csv", 'a', encoding="utf-8", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([datetime.datetime.now(), topic, case])

    # for i in range(2):
    #     case = rad.fuzz(ele.encode("UTF-8"), seed=117)
    #     print(case.decode("UTF-8"))

# case = b"asdfasdf"
# for i in range(3):
#     client.publish(topic, payload=case, qos=0, retain=False)
#     #print(f"sent {i} to {topic}")
#     print(f"sent {case} to {topic}")

#     with open("sent_log.csv", 'a', encoding="utf-8", newline="") as csvfile:
#         csvwriter = csv.writer(csvfile)
#         csvwriter.writerow([datetime.datetime.now(), topic, case])
    
#     #time.sleep(1)

client.loop_forever()