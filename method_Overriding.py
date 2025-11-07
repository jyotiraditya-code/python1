class parent:
    def mymethod(self):
        print("Call from parent")

class child(parent):
    def mymethod(self):
        print("Call from child")

c = child()
c.mymethod()