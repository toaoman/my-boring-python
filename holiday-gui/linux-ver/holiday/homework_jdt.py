bfb_raw = open("/home/redapple/.holiday/homework_bfb.txt", "r").read()
bfb = int(bfb_raw)
b = int((bfb)/2)
a = int(50-b)
c = ("["+"="*b+" "*a+"]"+str(bfb)+"%")
print(c)
