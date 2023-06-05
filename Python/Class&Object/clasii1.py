




class numbrs:
    def __init__(self,num1,num2,num3):
        self.num1=num1 
        self.num2=num2
        self.num3=num3

    def myname(self):
        print("No1 is: ",self.num1)
        print("No2 is: ",self.num2)
        print("No3 is: ",self.num3)

    def avg(self):
        
        avr=((self.num1+self.num2+self.num3)/3)
        print("Average is: ",avr)
        


  
n=numbrs(10,20,30)
n.myname()
n.avg()
