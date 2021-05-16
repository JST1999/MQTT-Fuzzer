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
client.connect("192.168.0.16", 1883, 60)

for i in range(1):
    client.publish(topic, payload=i, qos=0, retain=False)
    print(f"sent {i} to {topic}")

    # with open("sent_log.csv", 'a', encoding="utf-8", newline="") as csvfile:
    #     csvwriter = csv.writer(csvfile)
    #     csvwriter.writerow([datetime.datetime.now(), topic, str(i)])
    
    time.sleep(1)

client.loop_forever()
#C:\Users\Jason\AppData\Local\Programs\Python\Python36-32\python.exe C:\Users\Jason\Documents\MQTT-Fuzzer\netcat.py -t 127.0.0.1 -p 7000 -l