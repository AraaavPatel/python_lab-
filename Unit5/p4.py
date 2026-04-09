import matplotlib.pyplot as plt

# Sample data
data = [
    [10, 20, 30, 40, 50],
    [15, 25, 35, 45, 55],
    [5, 15, 25, 35, 45]
]

plt.figure(figsize=(8,5))

plt.boxplot(data,
            patch_artist=True,
            labels=['Set1', 'Set2', 'Set3'],
            showmeans=True)

plt.title("Box Plot Example")
plt.xlabel("Data Sets")
plt.ylabel("Values")

plt.grid(True)

plt.show()