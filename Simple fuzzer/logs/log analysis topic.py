import pandas as pd
import csv
#import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("received_log_topic.csv")
# count = len(df.index)
# print(count)
df2 = pd.read_csv("sent_log_topic.csv")
# count2 = len(df2.index)
# print(count2)

# for i in range(34, 40):
#     print(df2.iloc[i, 1])
#     print()

#below might not be right   try \xc281
#caseNorm = "dev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdevó ·test"
#caseNorm = caseNorm.encode("UTF-8")
#print(caseNorm)
#caseNorm = caseNorm.decode("UTF-8", "ignore")
#print(caseNorm)

#og in theory, could be wrong, hopefully right that this is the og one
caseOG = b'dev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev\xc3\xb3\xc2\xa0\xc2\x81\xc2\xb7test'
#print(caseOG.decode("UTF-8", "ignore"))
#print(caseOG.decode("UTF-8", "ignore"))
caseOG = caseOG.decode("UTF-8", "ignore")

for i in range(2):
    with open("single case test.csv", 'a', encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([caseOG])