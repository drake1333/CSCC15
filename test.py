command = ["GOTO","IF GOTO", "WRITE","LEFT","RIGHT","HALT"] 
symbol = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", 
          "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", 
          "2", "3", "4", "5", "6", "7", "8", "9","_"]    

labeldictionary={}
labelwithcolon = []
labelnocolon = []
instructiondictionary = {}
inputlist = []
operation = ""
status = ""
copiedinput = []


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
            
    def filereading(self):
        for x, y in enumerate(self.textfile1, start = 1 ):
                instructiondictionary[x] = y.strip().split()
                a =  instructiondictionary [x]
                if len(a) >=2:
                        if str(a[0]).endswith(":"):
                                a.pop(0)
                                
                                
        # self.resetvalues()
        
    def resetvalues(self):
        self.temporarylist=[]
        self.counter = 0
        self.labelindicator=""

 #duplicate label checker
 # reject empty program
 #comment are rejected
class errorchecker:
        def __init__(self):
             self.file =  open("source.txt","r")
             self.file1 =  open("source.txt","r") 
             self.counterforempty = 0
             self.temporarylist = [] 
        def rejectemptyprogramchecker(self):
                for x in self.file:
                        if x.isspace():
                                continue
                        else:
                                self.counterforempty +=1; 
                                      
                if self.counterforempty ==0:
                        print("the program is empty")
                        #self.resetvalues()
                        
                   #duplicate label and the label have no command afterward
        def duplicatelabel_invalidformat(self):
               
                for  x ,y in enumerate(self.file1, start =1) :
                        i = y.strip().split() 
                       
                        if len(i) >= 2:
                                labelstring = str(i[0])
                                if labelstring.endswith(":"):
                                        self.temporarylist.append(labelstring)
                                        if self.temporarylist.count(labelstring) >= 2:
                                                print(f"the label {labelstring} is duplicate label in the line {x}")   
                                                exit()
                        if len(i) == 1:
                                labelstring2 = str(i[0])
                                if labelstring2.endswith(":"):
                                        print(f"The label {labelstring2} have no command afterward. which is an invalid format of label in the line {x} ")        
                                        exit()
                                        
        def validlabel(self):
                for x in labelnocolon:
                        for y in loop:
                                print("i")
                
                                                 
        def syntaxchecker(self):
            for x, y in instructiondictionary.items():
        
                if len(y)==0:
                        continue
                
                elif len(y) >=6:
                        print (f"The Instruction {y} has 6 or more word on the line. which is invalid in turing machine in the line {x}")
                        exit()
                        
                elif  str(y[0])  in ["HALT", "LEFT","RIGHT"] : 
                          continue
                  
                elif   str(y[0]) in ["GOTO"]:        
                        if y[1]  not in  labelnocolon:
                                print(f" the label {y[1]} is  invalid in the line {x}")
                                exit()
                   
                elif   str(y[0]) in ["WRITE"]:                      
                        if y[1]  not in  symbol:
                                print(f" the symbol {y[1]} is  invalid in the line {x}")
                                exit()
                                
                elif   str(y[0]) in ["IF"]: 
                        if  str(y[2]) in  ["GOTO"]:
                                if y[1]  not in symbol :
                                        print(f" the symbol {y[1]} is invalid in the line {x}")
                                        exit()
                                
                                if y[3]  not in  labelnocolon:
                                        print(f" the label  {y[3]} is invalid in the line {x}")
                                        exit()
                                        
                        else:
                                print(f"the command {y[2]} is  invalid in the line {x}")
                                
                elif y[0] is not command:           
                     print(f"the command {str(y[0])} is invalid in the line {x} ") 
                     exit()
            
        def resetvalues(self):
                self.counterforempty =0
                self.temporarylist =[]
                
                   
class turingmachine:
    def __init__(self):
        self.pointer = 0
        self.counter = 0
        self.i = 1
        self.list = []
        self.arrow = "↓"
        self.programcounter = 0
        
    
    def finitestatecontrol(self):  
        global status
        self.list = [" "] * len(inputlist)
        self.list[self.pointer] = self.arrow   
        
        print("program starting")
        print(self.list)
        print(inputlist)      
        print(f"status: {status}") 
                    
        while self.i <= len(instructiondictionary):
                
            y = instructiondictionary[self.i]
            
            if operation  == "1":
                input("press enter to proceed: ")
        
        
            print(instructiondictionary[self.i])
            
            if self.programcounter == 10000:
                if y[0] in ["HALT"]:
                        print("HALT")    
                else:   
                        status = "Limit Reach"
                        print(f"status: {status}") 
                        print("Limit Reach for 10,000 step ")
                        self.resetvalues()
            if len(y) <= 0:
                self.i +=1  
                self.statusfortape() 
                
                  
            elif   str(y[0])  in ["LEFT"] :
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
                    status = "Halted"
                    print(f"status: {status}") 
                    print("Program Halting")
                    self.resetvalues()
                            
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
                          
        status = "Not successful halting"
        print(f"status: {status}") 
        self.resetvalues()
        
    def statusfortape(self):
        print(f"program counter: {self.programcounter}")
        self.list = [" "] * len(inputlist)
        self.list[self.pointer] = self.arrow
        
        print(self.list)
        print(inputlist) 
        
    def resetvalues(self):
        global inputlist    
        global operation
        global status
        
        
        input("Require reset operation:")
        inputlist = copiedinput
        self.pointer = 0
        self.counter = 0
        self.i = 1
        self.list = []
        self.arrow = "↓"
        self.programcounter = 0 
        
                
        print("Choose the two operation: \n 1.Step \n 2.Run ")
        
        choice = str(input("Type the number here of your chosen operation: "))
        print("Ready")
  
        if choice =="1":
                operation = "1"
                status = "Running"
                self.finitestatecontrol()
        elif choice == "2": 
                operation = "2"
                status = "Running"
                self.finitestatecontrol()

        else:
                
              self.resetvalues()          

        
class inputs:
   def __init__(self):
        pass

   def userinput1(self):
        global copiedinput
        userinput = str(input('What the initial tape:'))
        newinput = userinput.split()
        
        for l in newinput:
                if  l.isspace() :
                        continue 
                inputlist.extend(l)
        print(inputlist)       
        copiedinput = inputlist.copy()
                
   def chosenoperation(self):
        global operation
        global status
        print("Choose the two operation: \n 1.Step \n 2.Run")
        
        choice = str(input("Type the number here of your chosen operation: "))
        print("Ready")
  
        if choice =="1":
                operation = "1"
                status = "Running"
        elif choice == "2": 
                operation = "2"
                status = "Running"
        else:
              self.chosenoperation()          

        
def main():
                #Class
        errorcheckers= errorchecker()
        userinputs = inputs()
        groupobject = groupcommand()
        turingmachineobject = turingmachine()
        
        # Method
        errorcheckers.rejectemptyprogramchecker()
        errorcheckers.duplicatelabel_invalidformat()
                   
        
        groupobject.groupmethod()
        groupobject.filereading()


        errorcheckers.syntaxchecker()
        
        userinputs.userinput1()
        userinputs.chosenoperation()
        
        turingmachineobject.finitestatecontrol()
        

if __name__ == "__main__":
        main()
        
        
        
""""                 
def reset():
            userinput = str (input("want to reset program? type y for yes and n for no:"))
            if userinput == "y":
                global labeldictionary
                global labelwithcolon
                global instructiondictionary
                global labelnocolon
                
                labeldictionary={}
                labelwithcolon = []
                labelnocolon = []
                instructiondictionary = {}
                
                main()
                
            elif userinput==   "n":      
                exit()
            
            else:
                reset()
"""