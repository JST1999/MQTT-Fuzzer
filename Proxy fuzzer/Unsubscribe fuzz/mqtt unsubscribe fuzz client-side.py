import paho.mqtt.client as mqtt
import time
import csv
import datetime

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    
client = mqtt.Client()
client.username_pw_set(username="username",password="password")
client.on_connect = on_connect
client.connect("192.168.0.30", 9998, 60)

cases = ["dev/test",
"#",
"house/+/light"]#,
#"\x104\x00\x04MQTT\x04\xc2\x00\xff\x00\x19alicedoesnotneedaclientid\x00\x05alice\x00\x06secret\x82\x19\xa5\xa6\x00\x15hello/topic/of/alice\x00"]

# cases = ["abcdefghi", "abcdefghij", "abcdefghijk", "abcdefghijkl", "abcdefghijklm", "abcdefghijklmn", "abcdefghijklmno", "abcdefghijklmnop", "abcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopqabcdefghijklmnopq"]

def write_to_file(topic):
    with open("sent_log2.csv", 'a', encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([datetime.datetime.now(), topic])

for ele in cases:
    # client.subscribe(ele)
    for i in range(100):
        write_to_file(ele)
        client.unsubscribe(ele)
        client.disconnect()
        time.sleep(0.1)#seperates each connection
        client.reconnect()

print("Done")