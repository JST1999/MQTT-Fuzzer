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

def write_to_file(topic, case):
    with open("sent_log.csv", 'a', encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([datetime.datetime.now(), topic, case])

for i in range(10):
    case = "Sending message number " + str(i)

    client.publish(topic, payload=case, qos=0, retain=False)
    write_to_file(topic, case)

    #time.sleep(1)

print("Done")

#client.loop_forever()#not really needed