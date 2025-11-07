import numpy as np # type: ignore
arr = np.array([1, 2, 3])
print(arr)

zeros_array = np.zeros((2, 3))
print(zeros_array)

ones_array = np.ones((3, 2))
print(ones_array)

range_array = np.arange(0, 10, 2) 
print(range_array)

linear_array = np.linspace(0, 1, 5)  
print(linear_array)

random_array = np.random.rand(2, 3) 
print(random_array)

reshaped = np.reshape(np.arange(6), (2, 3))
print(reshaped)

a = np.array([1, 2])
b = np.array([3, 4])
concatenated = np.concatenate((a, b))
print(concatenated)

array = np.array([1, 2, 3])
total = np.sum(array) 
print(total)

mean_value = np.mean(array)  
print(mean_value)

sorted_array = np.sort(np.array([3, 1, 2]))
print(sorted_array)