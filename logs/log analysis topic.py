import pandas as pd
import csv
import matplotlib.pyplot as plt
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
case = "dev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdev/testdevó ·test"
case = case.encode("UTF-8")
print(case)
case = case.decode("UTF-8", "ignore")
print(case)

for i in range(10):
    with open("single case test.csv", 'a', encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([case])