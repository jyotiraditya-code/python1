import array
arr = array.array('i', [10, 20, 30, 40, 50])

print("Original array:", arr)
print("First element:", arr[0])
print("Last element:", arr[-1])


arr.append(60)
print("After append:", arr)

arr.insert(2, 25)
print("After insert at index 2:", arr)

arr.remove(30)
print("After removing 30:", arr)

popped = arr.pop(1)
print("Popped element:", popped)
print("After pop:", arr)

index = arr.index(40)
print("Index of 40:", index)


arr.reverse()
print("Reversed array:", arr)

count = arr.count(20)
print("Count of 20:", count)


