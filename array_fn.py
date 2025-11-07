import array

arr = array.array('i', [10, 20, 30, 40, 50])

arr.append(60)
arr.insert(2, 25)
arr.remove(40)
arr.pop(1)
arr.reverse()

print("Index of 30:", arr.index(30))
print("Modified:", arr)

import array

arr = array.array('i', [10, 20, 30, 40, 50])

print("Traverse:", [x for x in arr]) 

arr.insert(2, 25)
print("After Insertion:", arr)

arr.remove(40)
print("After Deletion:", arr)

index = arr.index(30)
print("Index of 30:", index)

arr[1] = 99
print("After Updating:", arr)
