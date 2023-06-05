class task():
    def __init__(self, name,age):
        self.name= name 
        self.age= age

    def getName(self):
        print("Your name is: ",self.name)
    def getage(self):
        print("Your  age is:  ",self.age)



t= task("Ayaz",21)
t.getName()
t.getage()