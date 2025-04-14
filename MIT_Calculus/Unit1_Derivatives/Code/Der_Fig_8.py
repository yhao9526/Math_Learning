import numpy as np
import matplotlib.pyplot as plt

# 定义指数函数
def exponential_function(x, a):
    return a ** x

# 定义指数函数的导数（这里以a = 2为例说明求导，a为其他值时求导公式为a^x * ln(a) ）
def derivative(x):
    return 2 ** x * np.log(2)

# 生成x值
x = np.linspace(-2, 2, 100)
a = 2
y = exponential_function(x, a)

# 选择一个点求切线，这里选x = 0
x0 = 0
y0 = exponential_function(x0, a)
m = derivative(x0)  # 切线斜率
# 切线方程 y - y0 = m(x - x0)，变形为 y = m(x - x0) + y0
tangent_y = m * (x - x0) + y0

# 绘制指数函数曲线，修改label
plt.plot(x, y, label=f'$y = a^x$')
# 绘制切线，修改label
plt.plot(x, tangent_y, label=f'slop = M(a)')
plt.scatter(x0, y0, color='red', label='Tangent point')

# 隐藏坐标轴刻度

plt.yticks([])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Function and Its Tangent')
plt.grid(True)
plt.legend()
plt.show()