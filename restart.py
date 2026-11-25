first = 1
second = 2
third = 4
fourth = ["1","2","3"]
class one:
    def __init__(self):
        self.one = 1
        self.two= 2
        self.file = open("test.txt", "r")
        
    def first(self):
        self.one = 111
        self.two = 222 
        for x in self.file:
            print(x)
        print(self.one)
        print(self.two)
        #self.reset()
        restart()
        
    #def reset(self):
        #self.one=1
        # self.two = 2
        
def restart():

    global first
    global second
    global third

    first = 1111
    second = 211
    third = 3111
    fourth.clear()
    main()
    
def stop():
    print("w")
    return False
    
def stop1():   
    main()
    
def main():
   
    if stop() == False:
        main()
        return False
    print(("g"))
""""
    class1 = one()
    print(class1.one)
    print(class1.two)
    class1.first()
 """   


main()