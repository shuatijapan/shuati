import numpy as np
import matplotlib.pyplot as plt

# 时间参数
t1 = 30  # 0到-30米
t2 = 29  # -30到-50米
t3 = 4   # 海底停留
t4 = 50  # -50米上浮到海平面

# 生成时间数据
time_to_30m = np.linspace(0, t1, t1+1)
time_to_50m = np.linspace(t1, t1+t2, t2+1)
time_at_bottom = np.linspace(t1+t2, t1+t2+t3, t3+1)
time_to_surface = np.linspace(t1+t2+t3, t1+t2+t3+t4, t4+1)

# 生成深度数据
depth_to_30m = -time_to_30m  # 速率1m/s
depth_to_50m = -30 - 0.7 * (time_to_50m - t1)  # 速率0.7m/s
depth_at_bottom = np.full_like(time_at_bottom, -50)  # 海底停留

# 上升过程中深度的计算
# 使用二次函数模拟加速上升
a = (0 - (-50)) / t4**2  # 加速度
depth_to_surface = -50 + a * (time_to_surface - (t1+t2+t3))**2

# 确保深度不超过海平面
depth_to_surface = np.clip(depth_to_surface, None, 0)

# 合并数据
time = np.concatenate((time_to_30m, time_to_50m[1:], time_at_bottom[1:], time_to_surface))
depth = np.concatenate((depth_to_30m, depth_to_50m[1:], depth_at_bottom[1:], depth_to_surface))

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(time, depth, label='Depth over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Depth (meters)')
plt.title('Depth vs Time for a Free Diver with Accelerating Ascent')

# 添加速率标注
plt.text(15, -15, '1m/s', fontsize=12, color='blue', ha='center')
plt.text(45, -40, '0.7m/s', fontsize=12, color='blue', ha='center')

plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()
