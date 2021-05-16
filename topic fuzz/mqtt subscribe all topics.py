import paho.mqtt.client as mqtt
import csv
import datetime

# The callback function of connection
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    

    
# The callback function for received message
def on_message(client, userdata, msg):
    # with open("received_log_topic.csv", 'a', encoding="utf-8", newline="") as csvfile:
    #     csvwriter = csv.writer(csvfile)
    #     csvwriter.writerow([datetime.datetime.now(), msg.topic, msg.payload.decode("utf-8", "ignore")])
    
    print(msg.topic+" "+msg.payload.decode("utf-8", "ignore"))

client = mqtt.Client()
client.username_pw_set(username="username",password="password")
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.0.16", 1883, 60)
client.subscribe("#")#subscribes to all topics
client.loop_forever()