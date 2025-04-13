import matplotlib.pyplot as plt
import numpy as np

# 生成角度值（弧度制）
theta = np.linspace(0, np.pi, 100)

# 计算正弦值
sin_theta = np.sin(theta)

# 创建图形和坐标轴
fig, ax = plt.subplots()

# 绘制半圆
ax.plot(np.cos(theta), np.sin(theta), color='blue')

# 设定一个特定角度（这里以np.pi/4为例）
specific_theta = np.pi / 4
sin_specific_theta = np.sin(specific_theta)
cos_specific_theta = np.cos(specific_theta)

# 绘制角度线
ax.plot([0, cos_specific_theta], [0, sin_specific_theta], color='blue')

# 绘制表示sin(theta)的线段
ax.plot([cos_specific_theta, cos_specific_theta], [0, sin_specific_theta], color='blue')

# 绘制y = 0直线
ax.plot([-1.2, 1.2], [0, 0], color='blue') 

# 添加标注
ax.text(0.25, 0.4, r'1', ha='center', va='top')
ax.text(1, 0.4, r'$\theta$', ha='left', va='center')
ax.text( 0.15, 0.06, r'$\theta$', ha='left', va='center')
ax.text(0.3, -0.03, r'$\cos\theta$', ha='center', va='top')
ax.text(0.85, -0.03, r'$1-\cos\theta$', ha='center', va='top')

# 设置坐标轴范围和刻度
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-0.2, 1.2)
ax.set_aspect('equal')
ax.grid(True)

# 关闭坐标轴显示（可选，若不想显示坐标轴刻度等）
plt.axis('off')

# 显示图形
plt.show()