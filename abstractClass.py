from abc import ABC, abstractmethod
class animal(ABC):
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        print("dog barks")

d = dog()
d.sound()