import pyradamsa

rad = pyradamsa.Radamsa()

mydata = b"Hello World"

for i in range(10):
    print(rad.fuzz(mydata))