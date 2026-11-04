file = open("test.txt","r")   

for x, y in enumerate(file,start=1):
    a = y.strip().split()
    print(a)
        