class father:
    fathername = ""

    def __init__(self,fathername):
        self.fathername = fathername

class mother:
    mothername = ""

    def __init__(self,mothername):
        self.mothername = mothername

class son(father,mother):


    def __init__(self,fathername,mothername):
        self.fathername = fathername
        self.mothername = mothername

    def details(self):
        print("The fathername is : ",self.fathername)
        print("The mothername is : ",self.mothername)

s1 = son("Amar","Sanjiwani")
s1.details()