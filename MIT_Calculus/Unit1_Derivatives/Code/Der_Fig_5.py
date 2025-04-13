import matplotlib.pyplot as plt
import numpy as np

# 创建一个图形和坐标轴对象
fig, ax = plt.subplots()

# 设置坐标轴范围
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)

# 绘制正方形的四条边
ax.plot([0, 3, 3, 0, 0], [0, 0, 3, 3, 0], 'b-')
ax.plot([0, 2, 2, 0, 0], [0, 0, 2, 2, 0], 'b-')
ax.plot([2, 3, 3, 2, 2], [2, 2, 3, 3, 2], 'b-')
ax.plot([0, 2, 2, 0, 0], [2, 2, 3, 3, 2], 'b-')



# 标注区域S
ax.text(1, 1, 'S', fontsize=15, ha='center', va='center')

# 标注字母和变化量
ax.text(-0.2, 1, r'v', ha='center', va='top')
ax.text(-0.2, 2.5, r'$\Delta$v', ha='center', va='top')
ax.text(1, -0.2, r'u', ha='center', va='top')
ax.text(2.5, -0.2, r'$\Delta$u', ha='center', va='top')

# 关闭坐标轴显示（可选，若不想显示坐标轴刻度等）
plt.axis('off')

# 显示图形
plt.show()