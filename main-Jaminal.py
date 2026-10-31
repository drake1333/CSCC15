class groupcommand:
    def __init__(self):
        self.symbol = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", 
          "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", 
          "2", "3", "4", "5", "6", "7", "8", "9","", " " ,"_"]    
        self.labelindicator = ""
        self.temporarylist = []
        self.counter = 0
        self.labeldictionary={}
        self.file = open("source.txt","r")
        
    def  groupmethod(self):
        for x, y in enumerate(self.file, start = 1 ):
            
            i = y.strip().split()
            if len(i) == 1:
                labelstring = str(i[0])
                if labelstring.endswith(":"):
                    self.labelindicator = labelstring
                    self.symbol.append(self.labelindicator.replace(":",""))
                    self.symbol.append(self.labelindicator)
                    self.counter =1
                    self.temporarylist.append(x)
                    
            if y.isspace() and self.counter ==1:
                self.temporarylist.append(x- 1)
                self.labeldictionary[self.labelindicator] = self.temporarylist.copy()
                self.temporarylist.clear()
                self.counter = 0
                
        if self.counter == 1:
                self.temporarylist.append(x)
                self.labeldictionary[self.labelindicator] = self.temporarylist.copy()
           
class firstsyntaxchecker:
        def __init__(self):
             self.file =  open("source.txt","r")
        def firstcheck(self):
                temporarylist = []
                for  x ,y in enumerate(self.file, start =1) :
                        i = y.strip().split()
                        if len(i) == 1:
                                labelstring = str(i[0])
                                if labelstring.endswith(":"):
                                        temporarylist.append(labelstring)
                                        if temporarylist.count(labelstring) >= 2:
                                                print(f"the label {labelstring} is duplicate label in the line {x}")   
                                                exit()   
                                                
class secondsyntaxchecker:
    def __init__(self,labeldictionary,symbollist):
        self.command = ["GOTO","IF GOTO", "WRITE","LEFT","RIGHT","HALT", "Goto", "If goto", "Write", "Left", "right" ,"halt", "START","Start","IF", "If"]
        self.gotolist = []
        self.labeldictionary = labeldictionary
        self.file = open("source.txt","r")
        self.symbol = symbollist
        self.firstlist = ["halt", "left", "right"] 
        self.secondlist = [ "goto" ,"write"]
        
    def secondcheck(self):
        for  x ,y in enumerate(self.file, start =1) :
                i = y.strip().split()
                
              
                if y.isspace():
                        continue
        
                elif  str(i[0]).lower() in self.firstlist : 
                          continue
                        
                elif   str(i[0]).lower() in self.secondlist: 
                        if i[1]  not in  self.symbol:
                                print(f" the symbol {i[1]} is  invalid in the line {x}")
                                exit()
                                
                elif   str(i[0]).lower() == "if": 
                        if  str(i[2]).lower() == "goto":
                                if i[1]  not in  self.symbol :
                                        print(f" the symbol {i[1]} is invalid in the line {x}")
                                        exit()
                                elif i[3]  not in  self.symbol:
                                        print(f" the label {i[3]} is invalid in the line {x}")
                                        exit()       
                        else:
                                print(f"the command {i[2]} is  invalid in the line {x}")
                                
                elif str(i[0]).endswith(":"):
                                continue        
                
                elif i[0] is not self.command:           
                     print(f"the command {str(i[0])} is invalid in the line {x} ") 
                     exit()
                     
        
class turingmachine:
    def __init__(self, inputlist,labeldictionary,symbol):
        self.symbol = symbol
        self.labeldictionary = labeldictionary
        self.pointer = 0
        self.counter = 0
        self.file = open("source.txt","r")
        self.inputlist = inputlist
        self.dictionary = {}
        self.counter1= 0
        self.i = 1
        self.list = []
        self.arrow = "↓"
    def filereading(self):
            
        for  itemIter in self.file:  
                self.counter +=1
                self.dictionary[self.counter] = itemIter.strip().split()
                
        self.finitestatecontrol()
        
    def finitestatecontrol(self):  
        self.list = [" "] * len(self.inputlist)
        self.list[self.pointer] = self.arrow    
        print("program starting")
        print(self.list)
        print(self.inputlist)      
                      
        while self.i < len(self.dictionary):
                
            y = self.dictionary[self.i]
            
            input("press enter to proceed: ")
            
            if len(y) <= 0:
                self.i +=1  
                self.list = [" "] * len(self.inputlist)
                self.list[self.pointer] = self.arrow
                print(self.list)
                print(self.inputlist)     
                  
            elif  str(y[0]).endswith(":"):
                    self.i +=1  
                    self.list = [" "] * len(self.inputlist)
                    self.list[self.pointer] = self.arrow
                    print(self.list)
                    print(self.inputlist)  
                    
            elif   str(y[0]).lower()== "left":
                    self.pointer -=1  
                    if  self.pointer < 0:
                            self.pointer = 0       
                    self.i +=1
                    self.list = [" "] * len(self.inputlist)
                    self.list[self.pointer] = self.arrow
                    print(self.list)
                    print(self.inputlist)      
                    
            elif str(y[0]).lower() == "right" :
                    self.pointer +=1
                    if self.pointer >= len(self.inputlist):
                            self.inputlist.append(" ")
                    self.i +=1
                    self.list = [" "] * len(self.inputlist)
                    self.list[self.pointer] = self.arrow
                    print(self.list)
                    print(self.inputlist)        
                    
            elif  str(y[0]).lower()== "halt" :
                    print("program ending")
                    exit()                  
                            
            elif str(y[0]).lower() == "write"   and y[1] in self.symbol:
                    self.inputlist[self.pointer] = y[1]
                    self.i +=1
                    self.list = [" "] * len(self.inputlist)
                    self.list[self.pointer] = self.arrow
                    print(self.list)
                    print(self.inputlist)       
                    
            elif   str(y[0]).lower() == "goto" and y[1] in self.symbol:
                    o = str(y[1])
                    p = o + ":"
                    l = self.labeldictionary[p]
                    self.i = l[0] 
                    self.list = [" "] * len(self.inputlist)
                    self.list[self.pointer] = self.arrow
                    print(self.list)
                    print(self.inputlist)               
                    
            elif str(y[0]).lower() == "if"  and y[1] in self.symbol and str(y[2]).lower() == "goto" and  y[3] in self.symbol:
                    if  y[1]  == self.inputlist[self.pointer]:
                            if y[3] in self.symbol:
                                    o = str(y[3])
                                    p = o + ":"
                                    l = self.labeldictionary[p]
                                    self.i = l[0] 
                                    self.list = [" "] * len(self.inputlist)
                                    self.list[self.pointer] = self.arrow
                                    print(self.list)
                                    print(self.inputlist)       
                    else:
                        self.i +=1
                        self.list = [" "] * len(self.inputlist)
                        self.list[self.pointer] = self.arrow
                        print(self.list)
                        print(self.inputlist)       
       
if __name__ == "__main__":
        firstcheck = firstsyntaxchecker()
        firstcheck.firstcheck()
       
        groupobject = groupcommand()
        groupobject.groupmethod()
      
        checker = secondsyntaxchecker(groupobject.labeldictionary,groupobject.symbol)
        checker.secondcheck()
        
        white = ""
        userinput = str(input('what the initial tape:'))
        newinput = userinput.split()
        inputlist = []  
        for l in newinput:
                if  l.isspace() :
                        continue 
                inputlist.extend(l)
                
        turingmachineobject = turingmachine(inputlist,groupobject.labeldictionary,groupobject.symbol)
        turingmachineobject.filereading()
        