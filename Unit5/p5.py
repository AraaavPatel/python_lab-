import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6]
y = [10, 20, 25, 30, 40, 50]

plt.figure(figsize=(8,5))

plt.scatter(x, y,
            color='red',
            marker='o',
            s=100,        # size
            alpha=0.7,
            label='Data Points')

plt.title("Scatter Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.grid(True)
plt.legend()

plt.show()