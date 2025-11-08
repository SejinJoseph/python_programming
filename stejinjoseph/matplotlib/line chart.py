import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
visits = [250, 270, 300, 280, 350, 400, 420]

plt.plot(days, visits)
plt.title("Website Traffic Over a Week")
plt.xlabel("Days of the Week")
plt.ylabel("Number of Visitors")
plt.show()

plt.plot(days, visits, color = "blue", linestyle="--", linewidth=2)
plt.title("Website Traffic Over a Week")
plt.xlabel("Days of the Week")
plt.ylabel("Number of Visitors")
plc.show()
