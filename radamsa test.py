import pyradamsa

rad = pyradamsa.Radamsa()

cases = []
with open("messages-to-mutate.txt") as f:
    lines = f.readlines()
    for ele in lines:
        cases.append(ele.rstrip())#they have a \n so I removed it

print(cases)
for ele in cases:
    for i in range(2):
        case = rad.fuzz(ele.encode("UTF-8"), seed=117)
        print(case.decode("UTF-8"))