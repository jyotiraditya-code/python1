import matplotlib.pyplot as plt

names = ['A', 'B', 'C']
marks = [80, 60, 90]

plt.bar(names, marks, color='skyblue')
plt.title("Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
