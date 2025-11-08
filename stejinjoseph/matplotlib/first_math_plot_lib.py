import matplotlib.pyplot as plt

x_value=[1,2,3,4,5]
y_value=[2,4,6,8,10]

plt.plot(x_value,y_value,'ro')
plt.xlabel("x_axis_value")
plt.ylabel("y_axis_value")
plt.title("my first matplotlib plot")
plt.plot(x_value,y_value,color='red',marker='o')
plt.grid()
plt.show()