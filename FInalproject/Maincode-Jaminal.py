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
firstletter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", 
          "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
steplimit = 1

class groupcommand:
    def __init__(self):
        self.labelindicator = ""
        self.temporarylist = []
        self.counter = 0
        self.textfile = open("source.txt","r")
        self.textfile1 = open("source.txt","r")
        
    def  groupmethod(self):
        current_label = None
        last_nonblank_line = None

        for x, y in enumerate(self.textfile, start=1):
            i = y.strip().split()

            # Ignore blank lines. They are not part of a label's instruction range.
            if not i:
                continue

            labelstring = i[0]

            # A label must have an instruction on the same line.
            if len(i) >= 2 and labelstring.endswith(":"):
                # Finish the previous label at the last nonblank source line.
                if current_label is not None:
                    labeldictionary[current_label][1] = last_nonblank_line

                # Remove only the final colon from the label name.
                labelname = labelstring[:-1]
                current_label = labelstring

                labelnocolon.append(labelname)
                labelwithcolon.append(labelstring)

                # Store [start line, end line]. The end is filled in when
                # the next label is found, or after the file has been read.
                labeldictionary[current_label] = [x, None]

            # Keep track of the last nonblank source line in the current section.
            last_nonblank_line = x

        # Finish the final label at the last nonblank line in the file.
        if current_label is not None:
            labeldictionary[current_label][1] = last_nonblank_line


            
            
        for x, y in enumerate(self.textfile, start = 1 ):
            i = y.strip().split()
            
            labelstring = str(i[0])
            if len(i) >=2 and  labelstring.endswith(":") :
                        self.counter = 1
                        self.labelindicator = labelstring
                        labelnocolon.append(self.labelindicator.replace(":",""))
                        labelwithcolon.append(self.labelindicator)
                        self.temporarylist.append(x)
                        
            if len(i) >=2 and  labelstring.endswith(":")  and  self.counter == 1:              
                        self.temporarylist.append(x+1)
                        labeldictionary[self.labelindicator] = self.temporarylist.copy()
                        self.temporarylist.clear()
                        self.counter = 2
                        
                        self.labelindicator = labelstring
                        labelnocolon.append(self.labelindicator.replace(":",""))
                        labelwithcolon.append(self.labelindicator)
                        self.temporarylist.append(x)
                        
           
                        
            print(labeldictionary)
            print(self.temporarylist)
                        
                        
        self.temporarylist.append(x)
        labeldictionary[self.labelindicator] = self.temporarylist.copy()
        print(labeldictionary)
        
            
    def filereading(self):
        for x, y in enumerate(self.textfile1, start = 1 ):
                q = y.strip().split()
                if len(q) == 0:
                        continue
                
                instructiondictionary[x] = q
                a =  instructiondictionary [x]
                
                if len(a) >=2:
                        if str(a[0]).endswith(":"):
                                a.pop(0)
                                
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
                        exit()
                        
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
                m = x[:1]    
                if m not in firstletter:
                        p = x + ":"
                        l = labeldictionary[p]
                        a = l[0]        
                        print(f"The label {x} is an invalid label in the line {a}")
                        exit()
                        
                n = x[1:]
                for y in n:
                        if y not in symbol:
                                p = x + ":"
                                l = labeldictionary[p]
                                a = l[0]        
                                print(f"The label {x} is an invalid label in the line {a}")
                                exit()    
                        
                                                 
        def syntaxchecker(self):
            for x, y in instructiondictionary.items():
        
                
                    
                if y[0] in ["LEFT","RIGHT","HALT"]  and len(y) ==1:
                    continue
                
                elif y[0] not in ["LEFT","RIGHT","HALT"]  and len(y) ==1:           
                     print(f"the command {str(y[0])} is invalid in the line {x} ") 
                     exit()
                     
                elif len(y) >=6:
                        print (f"The Instruction {y} has 6 or more word on the line. which is invalid in turing machine in the line {x}")
                        exit()
                
                elif   str(y[0]) in ["GOTO"] and len(y) ==2:        
                        if y[1]  not in  labelnocolon:
                                print(f" the label {y[1]} is  invalid in the line {x}")
                                exit()
                   
                elif   str(y[0]) in ["WRITE"] and len(y) ==2:                      
                        if y[1]  not in  symbol:
                                print(f" the symbol {y[1]} is  invalid in the line {x}")
                                exit()
                                
                elif   str(y[0]) in ["IF"] and len(y)==4: 
                        if  str(y[2]) in  ["GOTO"]:
                                if y[1]  not in symbol :
                                        print(f" the symbol {y[1]} is invalid in the line {x}")
                                        exit()
                                
                                if y[3]  not in  labelnocolon:
                                        print(f" the label  {y[3]} is invalid in the line {x}")
                                        exit()
                                        
                        else:
                                print(f"the command {y[2]} is  invalid in the line {x}")
                                exit()
                                
                else:
                    print(f"the instruction {str(y)} is invalid in line {x} ")
                    exit()
                    
class turingmachine:
    def __init__(self):
        self.pointer = 0
        self.i = 1
        self.list = []
        self.arrow = "↓"
        self.programcounter = 0
        
    def finitestatecontrol(self):  
        global status
        self.list = [" "] * len(inputlist)
        self.list[self.pointer] = self.arrow   
        
        print(self.list)
        print(inputlist)      
        print(f"status: {status}") 
        print(f"Instructions: { instructiondictionary[self.i ]}")
                    
        while self.i <= len(instructiondictionary):
                
            y = instructiondictionary[self.i]
            
        
            if operation  == "1":
                input("press enter to proceed: ")
            
            if self.programcounter >= steplimit:
                if y[0] in ["HALT"]:
                        print("HALT")    
                else:   
                        status = "Limit Reach"
                        print(f"Status: {status}") 
                        print("Limit Reach for 10,000 step ")
                        self.resetvalues()
                        
            
                
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
                    status = "Halted"
                    print(f"Status: {status}") 
                    print(f"Total Steps: {self.programcounter}")
                    
                    self.list = [" "] * len(inputlist)
                    self.list[self.pointer] = self.arrow
        
                    print(f"Head Index: {self.pointer}")
                    
                    print(self.list)
                    print(inputlist) 
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
                          
        status = "ERROR"
        print(f"Status: {status}") 
        self.resetvalues()
        
    def statusfortape(self):
        print(f"Total steps: {self.programcounter}")
        self.list = [" "] * len(inputlist)
        self.list[self.pointer] = self.arrow
        
        print(f"Head Index: {self.pointer}")
        print(self.list)
        print(inputlist) 
        print(f"Next Instructions: { instructiondictionary[self.i ]}")
        
    def resetvalues(self):
        global inputlist    
        global operation
        global status
        print("Choose the two operation: \n 1.Step \n 2.Run \n 3.Reset")
        
        choice = str(input("Type the number here of your chosen operation: "))
        
        if choice =="1":
                print("Reject: Reset Required")
                self.resetvalues()
        elif choice == "2": 
                print("Reject: Reset Required")
                self.resetvalues() 
        elif choice == "3":              
                operation = "2"
                status = "Running"
                inputlist = copiedinput.copy()
                self.pointer = 0
                self.i = 1
                self.programcounter = 0
                self.chosenoperation()
        else:
              self.resetvalues()
    
    def chosenoperation(self):  
        global operation
        global status
        
        print("Choose the two operation: \n 1.Step \n 2.Run")
        
        choice = input("Type the number here of your chosen operation: ")
        print("Status: Ready")
  
        if choice =="1":
                operation = "1"
                status = "Running"
                self.finitestatecontrol()
        elif choice == "2": 
                operation = "2"
                status = "Running"
                self.finitestatecontrol()
        else:
                self.chosenoperation()
              
class inputs:
   def __init__(self):
        pass

   def userinput1(self):
        global copiedinput
        global steplimit
        
        
        steplimit = int(input("Give positive steplimit number:"))
        
        if steplimit <= 0:
                print(f"The number given is not a positive steplimit number ")
                exit()
        
        userinput= str(input('What the initial tape:'))
        newinput = userinput.strip()
        copiedinput = inputlist.copy()
        
        if len(newinput) == 0:
             inputlist.extend("_")
             copiedinput = inputlist.copy()
             print(inputlist)
             return
    
        for l in newinput:
                if  l.isspace() :
                        print(f"There whitespace on the input {userinput1}") 
                        exit()
                        
                inputlist.extend(l)  
                copiedinput = inputlist.copy()
                       
if __name__ == "__main__":
        #Class
        errorcheckers= errorchecker()
        userinputs = inputs()
        groupobject = groupcommand()
        turingmachineobject = turingmachine()
        
        # Method
        errorcheckers.rejectemptyprogramchecker()
        errorcheckers.duplicatelabel_invalidformat()
    
        groupobject.groupmethod()

        errorcheckers.validlabel()

        groupobject.filereading()
        errorcheckers.syntaxchecker()
 
        
        print(instructiondictionary)
        userinputs.userinput1()
        
        turingmachineobject.chosenoperation()
        
        turingmachineobject.finitestatecontrol()

        