import matplotlib.pyplot as plt

departmentsa=["IT","finance","hr"]
salaries=[60000,70000,50000]


plt.bar(departmentsa,salaries,color=["blue","red","green"])
plt.title("salaries by department")
plt.xlabel("department")
plt.ylabel("avcerage salaries")

plt.show()

plt.barh(departmentsa,salaries,color="gold")
plt.title("salaries by department")
plt.xlabel("department")
plt.ylabel("avcerage salaries")
plt.show()