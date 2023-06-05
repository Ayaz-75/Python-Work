
class Test1:

    def __init__(self, first, last, add):
        self.first = first
        self.last = last
        self.add = add
        self.mail = first + "." + last +"@company.com"


test1 = Test1('ayaz', 'lakho', 75)
print(test1.mail)
