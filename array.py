import array
numbers = array.array('i', [10, 20, 30, 40, 50])
print("Original array:")
for num in numbers:
    print(num)


numbers.append(60)
print("\nAfter appending 60:")
print(numbers)

numbers.insert(2, 25)
print("\nAfter inserting 25 at index 2:")
print(numbers)


numbers.remove(40)
print("\nAfter removing 40:")
print(numbers)


numbers.reverse()
print("\nAfter reversing:")
print(numbers)


