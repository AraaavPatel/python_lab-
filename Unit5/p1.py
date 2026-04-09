import matplotlib.pyplot as plt

# Sample data
subjects = ['Math', 'Science', 'English', 'History', 'Computer']
marks = [85, 90, 78, 88, 95]

plt.figure(figsize=(8,5))

plt.bar(subjects, marks,
        color='skyblue',
        edgecolor='black',
        linewidth=2)

plt.title("Student Marks Bar Chart", fontsize=14)
plt.xlabel("Subjects", fontsize=12)
plt.ylabel("Marks", fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()