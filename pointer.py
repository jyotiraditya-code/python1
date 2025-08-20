file = open("example.txt", "r")

print("Initial pointer position:", file.tell())  

content = file.read(10)  
print("Read content:", content)

print("Pointer position after reading 10 chars:", file.tell())  

file.seek(0) 

print("Pointer position after seek(0):", file.tell())

file.close()

