import matplotlib.pyplot as plt

labels = ['Apple', 'Banana', 'Mango', 'Grapes']
sizes = [30, 25, 25, 20]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow = True)
plt.title("Pie Chart")
plt.show()
