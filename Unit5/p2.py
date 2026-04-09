import matplotlib.pyplot as plt

# Sample data
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]
colors = ['gold', 'lightblue', 'lightgreen', 'pink']
explode = (0.1, 0, 0, 0)  # highlight first slice

plt.figure(figsize=(6,6))

plt.pie(sizes,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        explode=explode,
        shadow=True)

plt.title("Programming Language Usage")

plt.axis('equal')  # perfect circle

plt.show()