import matplotlib.pyplot as plt
import numpy as np

# 创建图形和坐标轴
fig, ax = plt.subplots()

# 绘制直角三角形的三条边
# 假设直角边长度为1和x（这里先简单假设x = 2，可根据实际调整）
x = 2
ax.plot([0, x], [0, 0], 'k')  # 底边
ax.plot([0, 0], [0, 1], 'k')  # 左边直角边
ax.plot([0, x], [1, 0], 'k')  # 斜边

# 标注直角边和斜边
ax.text(x / 2, -0.1, '$x$', ha='center', va='top', fontsize=12)
ax.text(-0.1, 1 / 2, '1', ha='right', va='center', fontsize=12)
hypotenuse_length = np.sqrt(1 + x ** 2)
ax.text(1.03, 0.6, f'$\sqrt{{1 + x^{2}}}$', ha='center', va='center', fontsize=12)

# 设置坐标轴比例相等，以保证图形显示为直角三角形
# ax.set_aspect('equal')

# 隐藏坐标轴刻度
ax.set_xticks([])
ax.set_yticks([])

# 隐藏坐标轴边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# 显示图形
plt.show()