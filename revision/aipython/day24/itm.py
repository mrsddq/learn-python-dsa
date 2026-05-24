import matplotlib.pyplot as plt

hours=[2,4,6,8,10]
math_marks=[21,38,64,85,98]
sci_marks=[10,15,19,25,35]

print(plt.scatter(hours,math_marks, label="math"))
print(plt.scatter(hours,sci_marks, label="sci"))
plt.xlabel("Hours Spent")
plt.ylabel("Marks Scored")
plt.title("Student data of hours spent vs marks scored")
plt.legend()
plt.show()