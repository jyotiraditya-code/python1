class emp:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class fun(emp):
    def __init__(self,id,name,email):
        super().__init__(id,name)
        self.email = email

ob = fun(62,"Vishwajeet","gavalivishwajeet@gmail.com")
print(ob.id, ob.name, ob.email)