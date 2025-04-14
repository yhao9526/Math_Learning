import numpy as np
import matplotlib.pyplot as plt


# 定义示例函数 y = f(x) ，这里以 y = x**2 为例（x>=0）
def f(x):
    return  x ** 2


# 定义其反函数 y = f^{-1}(x) ，这里为 y = sqrt(x)
def f_inverse(x):
    return np.sqrt(x)


x = np.linspace(0, 4, 100)
y_f = f(x)
y_f_inverse = f_inverse(x)
y_x = x

# 创建图形和坐标轴对象
fig, ax = plt.subplots()

# 绘制 y = f(x)
ax.plot(x, y_f, label=r'$y = f(x)$', color='blue')
# 绘制 y = f^{-1}(x)
ax.plot(x, y_f_inverse, label=r'$y = f^{-1}(x)$', color='blue')
# 绘制 y = x
ax.plot(x, y_x, label=r'$y = x$', linestyle='--', color='gray')

# 设置坐标轴标签
ax.set_xlabel('x')
ax.set_ylabel('y')

# 添加图例
ax.legend()

# 设置坐标轴范围
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

# 显示网格
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# 显示图形
plt.show()