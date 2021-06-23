import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("received_log.csv")
# count = len(df.index)
# print(count)
df2 = pd.read_csv("sent_log.csv")
# count2 = len(df2.index)
# print(count2)

# print(df.iloc[1500000])
# print(df2.iloc[1500000])

# print(df)
# print(df2)

# for i in range(len(df.index)):
#     if df.iloc[i, 2] != df2.iloc[i, 2]:
#         print("Received log:")
#         print(df.iloc[i, 2])
#         print("Sent log:")
#         print(df2.iloc[i, 2])
#         print()

for i in range(40000, 40010):
    print(df.iloc[i])
    print(df2.iloc[i])
    print()