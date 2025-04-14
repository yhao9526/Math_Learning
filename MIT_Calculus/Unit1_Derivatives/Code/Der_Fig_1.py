import matplotlib.pyplot as plt
import numpy as np

# 定义函数
def f(x):
    return x ** 2

# 生成x轴数据
x = np.linspace(0, 3, 100)
y = f(x)

# 固定点P的横坐标
xp = 1
yp = f(xp)

# 定义点Q的横坐标（靠近P点）
xq = 2
yq = f(xq)

# 计算切线斜率（利用导数，对于y = x^2，导数为y' = 2x ）
tangent_slope = 2 * xp
# 切线方程 y - yp = tangent_slope * (x - xp)
tangent_y = tangent_slope * (x - xp) + yp

# 割线方程 y - yp = ((yq - yp) / (xq - xp)) * (x - xp)
secant_slope = (yq - yp) / (xq - xp)
secant_y = secant_slope * (x - xp) + yp

# 绘制函数曲线
plt.plot(x, y, label='f(x)')
# 绘制切线
plt.plot(x, tangent_y, label='tangent_line')
# 绘制割线
plt.plot(x, secant_y, '--', label='secant_line')
# 标记点P和Q
plt.scatter(xp, yp, color='black', label='P')
plt.scatter(xq, yq, color='blue', label='Q')

# 添加坐标轴标签和标题
plt.xlabel('x')
plt.ylabel('y')
plt.title('The distance between points P and Q approaches 0 (point P is fixed)')
# 添加图例
plt.legend()
# 显示网格
plt.grid(True)
# 显示图形
plt.show()