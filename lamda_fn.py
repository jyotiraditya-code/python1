add = lambda a, b: a + b

print(add(5, 3))  

nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)

nums = [10, 15, 20, 25, 30]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
