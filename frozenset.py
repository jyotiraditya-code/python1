myFruits = ['apple', 'banana', 'cherry']
x = frozenset(myFruits)
print(myFruits)
animals = frozenset(["cat", "dog", "tiger"])
print("cat" in animals) 
print("elephant" in animals)

A =frozenset(1,2,3,4)
B =frozenset(3,4,5,6)
C =frozenset(5,6)

# isdisjoint() method
print(A.isdisjoint(C)) 

# issubset() method
print(C.issubset(B))  

# issuperset() method
print(B.issuperset(C))