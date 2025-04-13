import matplotlib.pyplot as plt

# 定义三角形三个顶点坐标
x0, y0 = 0, 0
x1, y1 = 3, 0
x2, y2 = 3, 2

# 绘制三角形
plt.plot([x0, x1, x2, x0], [y0, y1, y2, y0], 'b')

# 标注点 P
plt.text(x0 - 0.2, y0 - 0.2, r'$P(x_0, f(x_0))$', fontsize=12)
# 标注点 Q
plt.text(x2 - 0.7, y2 + 0.1, r'$Q(x_0+\Delta x, f(x_0+\Delta x))$', fontsize=12)
# 标注 Δx
plt.text((x0 + x1) / 2, y0 - 0.2, r'$\Delta x$', fontsize=12, ha='center')
# 标注 Δf
plt.text(x2 + 0.2, (y0 + y2) / 2, r'$\Delta f$', fontsize=12, va='center')

# 标注割线
plt.text((x0 + x2 -1) / 2, (y0 + y2 +0.5) / 2, 'secant line', fontsize=12, color='b')

# 关闭坐标轴显示（可选，若不想显示坐标轴刻度等）
plt.axis('off')

# 显示图形
plt.show()