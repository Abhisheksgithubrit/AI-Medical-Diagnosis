import matplotlib.pyplot as plt

# Sample Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create a Plot
plt.plot(x, y, marker='o', linestyle='--', color='b', label="Data Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.legend()
plt.grid()

# Show the Plot
plt.show()
