import paho.mqtt.client as mqtt
import time
import csv
import datetime

topic = "dev/test"
m = "testing from the tester"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    
client = mqtt.Client()
client.username_pw_set(username="username",password="password")
client.on_connect = on_connect
client.connect("192.168.0.30", 9997, 60)#127.0.0.1 9998 for the proxy setup i think

for i in range(1):
    client.publish(topic, payload=m, qos=0, retain=False)
    print(f"sent {m} to {topic}")

    # with open("sent_log.csv", 'a', encoding="utf-8", newline="") as csvfile:
    #     csvwriter = csv.writer(csvfile)
    #     csvwriter.writerow([datetime.datetime.now(), topic, str(i)])
    
    # client.disconnect()
    # time.sleep(1)
    # client.reconnect()

#client.loop_forever()
#C:\Users\Jason\AppData\Local\Programs\Python\Python36-32\python.exe C:\Users\Jason\Documents\MQTT-Fuzzer\netcat.py -t 127.0.0.1 -p 7000 -l