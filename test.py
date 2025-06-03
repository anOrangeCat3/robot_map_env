import matplotlib.pyplot as plt
import numpy as np

import env

env = env.Env(map_path='maps/map1.png')

def visualize_map(env_map):
    """
    可视化环境地图
    
    参数:
    env_map: numpy.ndarray, 环境地图数组
    """
    # 创建图形
    plt.figure(figsize=(10, 10))
    
    # 使用imshow显示地图
    # cmap='binary' 使用黑白配色
    # origin='lower' 设置坐标原点在左下角
    plt.imshow(env_map, cmap='binary')
    
    # 添加颜色条
    plt.colorbar(label='Map Value')
    
    # 添加标题和轴标签
    plt.title('global map')
    plt.xlabel('X')
    plt.ylabel('Y')
    
    # 显示网格
    # plt.grid(True)
    
    # 显示图形
    plt.show()

def test1():
    # visualize_map(env.global_map)
    # print(env.global_map)
    # print(env.map_list)
    # print(env.env_map.shape)
    # print(env.env_map.shape)
    # print(env.robot_position)
    print(type(env.global_map))
    print(type(env.robot_position))

def test2():
    print(env.robot.position)
    print(type(env.robot.position))
    # print(env.robot.lidar.scan(env.robot.position))
    print(type(env.robot.lidar.scan(env.robot.position)))

# test1()
test2()