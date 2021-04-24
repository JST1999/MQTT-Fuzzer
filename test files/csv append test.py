import csv

string = "Hello world"

for i in range(10000000):
    with open("test.csv", 'a', encoding="utf-8", newline="") as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the fields
        csvwriter.writerow([string])#use array elements to seperate by column