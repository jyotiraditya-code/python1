class grandfather:
    def __init__(self,name):
        self.name = name

    def display(self):
        print("The name of the grandfather is: ",self.name)

class father(grandfather):
    def __init__(self,name):
        self.name = name

    def display(self):
        print("The name of the father is: ",self.name)

class son(father):
    def __init__(self,name):
        self.name = name

    def display(self):
        print("The name of the son is: ",self.name)


obj1 = grandfather("Bhimrao")
obj1.display()
obj2 = father("Amar")
obj2.display()
obj3 = son("Vishwajeet")
obj3.display()