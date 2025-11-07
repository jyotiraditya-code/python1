class student1:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print("the first name is ",self.fname)
        print("the last name is ",self.lname)

class student2(student1):
    def __init__(self,fname,lname):
         super().__init__(fname, lname)

    def display(self):
        print("the first name is ",self.fname)
        print("the last name is ",self.lname) 

obj1 = student1("Vishwajeet","zambre") 
obj1.display()
obj2 = student2("Vivek","zambre") 
obj2.display()



        
