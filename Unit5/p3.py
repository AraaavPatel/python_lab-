import matplotlib.pyplot as plt

# Sample data
days = [1, 2, 3, 4, 5]
temperature = [30, 32, 35, 33, 31]

plt.figure(figsize=(8,5))

plt.plot(days, temperature,
         color='blue',
         marker='o',
         linestyle='-',
         linewidth=2,
         markersize=8,
         label='Temperature')

plt.title("Temperature Over Days")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")

plt.grid(True)
plt.legend()

plt.show()