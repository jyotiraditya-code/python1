class Access_Modifier:
    
    def __init__(self):
     self.public_Var = "This is public variable"
     self._protected_Var = "This is protected variable"
     self.__private_Var = "This is private variable"

    def public_method(self):
        print("This is public method")
        
    def _protected_mrthod(self):
        print("This is protected method")
        
    def __private_method(self):
        return "This is private method"

        
    def access_private_method(self):
        return self.__private_method()
    
s = Access_Modifier()
print(s.public_Var)
print(s._Access_Modifier__private_Var)
print(s._protected_Var)

s.public_method()
s._protected_mrthod()
print(s.access_private_method())