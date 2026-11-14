command = ["GOTO","IF GOTO", "WRITE","LEFT","RIGHT","HALT"] 
symbol = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", 
          "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", 
          "2", "3", "4", "5", "6", "7", "8", "9","_"]    
labeldictionary={}
labelwithcolon = []
labelnocolon = []
dictionary = {}

class groupcommand:
    def __init__(self):
        self.labelindicator = ""
        self.temporarylist = []
        self.counter = 0
        self.textfile = open("source.txt","r")
        self.textfile1 = open("source.txt","r")
        
    def  groupmethod(self):
        for x, y in enumerate(self.textfile, start = 1 ):
            i = y.strip().split()
            
            if len(i) >=2:
                labelstring = str(i[0])
                if labelstring.endswith(":") :
                        self.labelindicator = labelstring
                        labelnocolon.append(self.labelindicator.replace(":",""))
                        labelwithcolon.append(self.labelindicator)
                        self.counter =1
                        self.temporarylist.append(x)
                
            if y.isspace() and self.counter ==1:
                self.temporarylist.append(x- 1)
                labeldictionary[self.labelindicator] = self.temporarylist.copy()
                self.temporarylist.clear()
                self.counter = 0
                
        if self.counter == 1:
                self.temporarylist.append(x)
                labeldictionary[self.labelindicator] = self.temporarylist.copy()
                
        print(labeldictionary)        
        print(labelwithcolon)
        print(labelnocolon)
        
        self.filereading()
    def filereading(self):
        for x, y in enumerate(self.textfile1, start = 1 ):
                
                
                dictionary[x] = y.strip().split()
                a =  dictionary [x]
                if len(a) >=2:
                        if str(a[0]).endswith(":"):
                                a.pop(0)
                        
                
        print(dictionary)
        

 #duplicate label checker
 # reject empty program
 #comment are rejected
class firstsyntaxchecker:
        def __init__(self):
             self.file =  open("source.txt","r")
             self.file1 =  open("source.txt","r") 
             self.counterforempty = 0
             
        def rejectemptyprogramchecker(self):
                for x in self.file:
                        if x.isspace():
                                continue
                        else:
                                self.counterforempty +=1; 
                                      
                if self.counterforempty ==0:
                        print("the program is empty")
                        exit()
                
                self.duplicatelabelchecker()
                   
        def duplicatelabelchecker(self):
                temporarylist = []
                for  x ,y in enumerate(self.file1, start =1) :
                        i = y.strip().split() 
                        if len(i) >= 2:
                                labelstring = str(i[0])
                                if labelstring.endswith(":"):
                                        temporarylist.append(labelstring)
                                        if temporarylist.count(labelstring) >= 2:
                                                print(f"the label {labelstring} is duplicate label in the line {x}")   
                                                exit()   
# unknown commands
# wrong symbol
# undefined jump target
class secondsyntaxchecker:
    def __init__(self):
        self.file = open("source.txt","r")

    def secondcheck(self):
        for  x ,y in enumerate(self.file, start =1) :
                i = y.strip().split()
           
                if len(i)==0:
                        continue
                
                elif len(i) >=5:
                        print (f"The Instruction {i} has 5 or more letter on the line. which is invalid in turing machine in the line {x}")
                        exit()
                        
                elif  str(i[0])  in ["HALT", "LEFT","RIGHT"] : 
                          continue
                  
                elif   str(i[0]) in ["GOTO"]:        
                        if i[1]  not in  labelnocolon:
                                print(f" the label {i[1]} is  invalid in the line {x}")
                                exit()
                   
                elif   str(i[0]) in ["WRITE"]:                      
                        if i[1]  not in  symbol:
                                print(f" the symbol {i[1]} is  invalid in the line {x}")
                                exit()        
                                
                elif   str(i[0]) in ["IF"]: 
                        if  str(i[2]) in  ["GOTO"]:
                                if i[1]  not in symbol :
                                        print(f" the symbol {i[1]} is invalid in the line {x}")
                                        exit()
                                
                                if i[3]  not in  labelnocolon:
                                        print(f" the label  {i[3]} is invalid in the line {x}")
                                        exit()       
                        else:
                                print(f"the command {i[2]} is  invalid in the line {x}")
                                
                elif str(i[0]).endswith(":"):
                                continue        
                
                elif i[0] is not command:           
                     print(f"the command {str(i[0])} is invalid in the line {x} ") 
                     exit()
                     
class turingmachine:
    def __init__(self):
        self.pointer = 0
        self.counter = 0
        self.file = open("source.txt","r")
        self.i = 1
        self.list = []
        self.arrow = "↓"
        self.programcounter = 0
        
    
    def finitestatecontrol(self):  
        self.list = [" "] * len(inputlist)
        self.list[self.pointer] = self.arrow    
        print("program starting")
        print(self.list)
        print(inputlist)      
                      
        while self.i <= len(dictionary):
                
            y = dictionary[self.i]
            
            input("press enter to proceed: ")
            print(dictionary[self.i])
           
            if self.programcounter == 10000:
                if y[0] in ["HALT"]:
                        print("HALT")    
                else:    
                        print("Limit Reach for 10,000 step ")
                        exit()
                        
            if len(y) == 0:
                    continue
            
            if len(y) <= 0:
                self.i +=1  
                self.statusfortape()        
                
                  
            if   str(y[0])  in ["LEFT"] :
                    self.programcounter +=1
                    self.pointer -=1  
                    
                    if  self.pointer < 0:
                            self.pointer = 0    
                               
                    self.i +=1
                    self.statusfortape()        

            elif    str(y[0])  in ["RIGHT"] :
                    self.programcounter +=1
                    self.pointer +=1
                    
                    if self.pointer >= len(inputlist):
                            inputlist.append("_")
                            
                    self.i +=1
                    self.statusfortape()        
    
                    
            elif  str(y[0])  in ["HALT"] :
                    self.programcounter +=1
                    self.statusfortape()        
                    print("Program Halting")
                    exit()                  
                            
            elif str(y[0])  in ["WRITE"]   and y[1] in symbol:
                    self.programcounter +=1
                    inputlist[self.pointer] = y[1]
                    self.i +=1
                    self.statusfortape()        
      
                    
            elif   str(y[0])  in ["GOTO"]  and y[1] in labelnocolon:
                    self.programcounter +=1
                    o = str(y[1])
                    p = o + ":"
                    l = labeldictionary[p]
                    self.i = l[0] 
                    self.statusfortape()                      
                    
            elif  str(y[0])  in ["IF"]   and y[1] in symbol and  str(y[2])  in ["GOTO"]  and  y[3] in labelnocolon:
                    self.programcounter +=1
                    if  y[1]  == inputlist[self.pointer]:
                            if y[3] in labelnocolon:
                                    o = str(y[3])
                                    p = o + ":"
                                    l = labeldictionary[p]
                                    self.i = l[0] 
                                    self.statusfortape()        
                            
                    else:
                        self.i +=1
                        self.statusfortape()        
            

    def statusfortape(self):
        print(f"program counter: {self.programcounter}")
        self.list = [" "] * len(inputlist)
        self.list[self.pointer] = self.arrow
        print(self.list)
        print(inputlist) 

class test:
        def __init__(self):
               pass
       
        def press(self):
               print(inputlist)        
                
if __name__ == "__main__":
      
        #firstcheck = firstsyntaxchecker()
        #firstcheck.rejectemptyprogramchecker()
        
        groupobject = groupcommand()
        groupobject.groupmethod()
        groupobject.filereading()
        
        #secondchecker = secondsyntaxchecker()
        #secondchecker.secondcheck()
        
        userinput = str(input('what the initial tape:'))
        newinput = userinput.split()
        inputlist = []  
        
        for l in newinput:
                if  l.isspace() :
                        continue 
                inputlist.extend(l)
        print(inputlist)       
         

        turingmachineobject = turingmachine()
        turingmachineobject.finitestatecontrol()
        
