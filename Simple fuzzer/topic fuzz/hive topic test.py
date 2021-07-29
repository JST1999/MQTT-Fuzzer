import paho.mqtt.client as mqtt
import time
import csv
import datetime
import pyradamsa

rad = pyradamsa.Radamsa()
message = "hi"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    
client = mqtt.Client()
client.username_pw_set(username="username",password="password")
client.on_connect = on_connect
client.connect("192.168.0.30", 1883, 60)

# cases = [#'dev/ó ‡test',
# '"dev/te',
# 'st"',
# 'â€†dev/test',
# 'sÂ·t',
# 'dev/tesó €»t',
# #'â€¯ó žtó žtesesu',
# #'deó €¿dedáš€eddó Ÿâ¦áš€ó ªeó ¾ó €¾vtest',
# 'dev/ó €»test',
# 'eá…Ÿâ€­s',
# "normal/topic",
# "room/light",
# "oblivion/skyrim"
# ]

cases = ['dev/ó ‡test',
'â€¯ó žtó žtesesu',
'deó €¿dedáš€eddó Ÿâ¦áš€ó ªeó ¾ó €¾vtest',
"testing/chars",
"normal/topic",
"room/light",
"oblivion/skyrim"]

def write_to_file(topic, case):
    with open("sent_log_topic.csv", 'a', encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([datetime.datetime.now(), topic, case])

for ele in cases:
    time.sleep(0.1)
    print(ele)
    client.publish(ele, payload=message, qos=0, retain=False)
    # mess = b"\xc2\x81"    #in utf-8 it is like a ^ but smaller
    # mess2 = mess.decode("UTF-8", "ignore")
    # print(mess2)
    # client.publish(mess2, payload=message, qos=0, retain=False)

print("Done")