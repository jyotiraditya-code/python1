class student:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

        
    def output(self):
        print("The name is ",self.name)
        print("The age is: ",self.age)
        
s1 = student("Vishwajeet",19)
s1.output()