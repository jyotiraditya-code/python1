print("This is set: ")
fruits = {"apple","bananna","guava","mango"}
print(fruits)
days = set(["monday","tuesday","wednesday"])
print(days)

print("by using add method")
fruits.add("orange")
print(fruits)
print()

print("by using clear method")
fruits.clear()
print(fruits)
print()

print("by using difference method ")
x = {"apple", "banana", "mango"}
y = {"tcs", "infosys", "apple"}
z = x.difference(y)
print(z)
print()

fruits = {"apple","bananna","guava","mango"}
print("by using remove method ")
fruits.remove("bananna")
print(fruits)
print()

days = set(["monday","tuesday","wednesday"])
fruits = {"apple","bananna","guava","mango"}
print("by using union method")
concat = days.union(fruits)
print(concat)
print()

print("by using symmetric difference")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
print()

fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)