import paho.mqtt.client as mqtt
import time
import csv
import datetime

topic = "dev/test"
m = "testing"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    
client = mqtt.Client()
# client.username_pw_set(username="username",password="password")
client.on_connect = on_connect
client.connect("192.168.0.30", 9997, 60)#127.0.0.1 9998 for the proxy setup i think
client.loop_start()#needed for quality of service 2

for i in range(100):
    client.publish(topic, payload=m, qos=2, retain=False)
    print(f"sent {m} to {topic}")

    with open("sent_log.csv", 'a', encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([datetime.datetime.now(), str(i)])

    time.sleep(3)#there probs is a better way