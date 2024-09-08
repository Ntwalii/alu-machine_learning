#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(10, 8))
fig.suptitle("All in One")
gs = GridSpec(3, 2, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
y0 = np.arange(0, 11) ** 3
ax1.plot(y0, c='r')
ax1.set_xlim(0, 10)
ax1.set_title("Cubed Values", fontsize="x-small")
ax1.set_xlabel("X", fontsize="x-small")
ax1.set_ylabel("Y", fontsize="x-small")

ax2 = fig.add_subplot(gs[0, 1])
mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180
ax2.scatter(x1, y1, s=10, c="m")
ax2.set_title("Men's Height vs Weight", fontsize="x-small")
ax2.set_xlabel("Height (in)", fontsize="x-small")
ax2.set_ylabel("Weight (lbs)", fontsize="x-small")

ax3 = fig.add_subplot(gs[1, 0])
x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)
ax3.set_xlim(0, 28650)
ax3.set_yscale('log')
ax3.plot(x2, y2)
ax3.set_title("Exponential Decay of C-14", fontsize="x-small")
ax3.set_xlabel("Time (years)", fontsize="x-small")
ax3.set_ylabel("Fraction Remaining", fontsize="x-small")
ax4 = fig.add_subplot(gs[1, 1])
x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)
ax4.set_xlim(0, 20000)
ax4.set_ylim(0, 1)
ax4.plot(x3, y31, 'r--', label='C-14')
ax4.plot(x3, y32, 'g-', label='Ra-226')
ax4.set_title("Exponential Decay of Radioactive Elements", fontsize="x-small")
ax4.set_xlabel("Time (years)", fontsize="x-small")
ax4.set_ylabel("Fraction Remaining", fontsize="x-small")
ax4.legend(fontsize="x-small")

ax5 = fig.add_subplot(gs[2, :])
np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
ax5.hist(student_grades, bins=np.arange(0, 101, 10), edgecolor='black')
ax5.set_title("Project A", fontsize="x-small")
ax5.set_xlabel("Grades", fontsize="x-small")
ax5.set_ylabel("Number of Students", fontsize="x-small")
ax5.set_xlim(0, 100)
ax5.set_ylim(0, 30)
plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()