import paho.mqtt.client as mqtt
import time
import csv
import datetime
from collections import Counter

message = "hi"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    
def write_to_file(topic, case):
    with open("sent_log_topic.csv", 'a', encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([datetime.datetime.now(), topic, case])


client = mqtt.Client()
client.username_pw_set(username="username",password="password")
client.on_connect = on_connect
client.connect("192.168.0.16", 1883, 60)

#cases = [b'hello/there', b'dev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev\xc3\xb3\xc2\xa0\xc2\x81\xc2\xb7test', b'clannad/nagisa']
cases = [b'hello/there', b'd/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d', b'clannad/nagisa']

for ele in cases:
    topic = ele.decode("UTF-8", "ignore")
    print(len(topic))
    c = Counter(topic)
    for letter in "/":
        print("%s : %d" % (letter, c[letter]))

    client.publish(topic, payload=message, qos=0, retain=False)
    write_to_file(topic, message)

print("Done")