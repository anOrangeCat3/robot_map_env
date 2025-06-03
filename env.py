import numpy as np
from skimage import io
from typing import Tuple

from robot import Robot
from sensor import Lidar


class Env:
    '''
    环境类
    用于管理机器人和地图的交互

    包含：
    map: 地图文件
    robot: 机器人类
    
    '''

    def __init__(self,
                 map_path:str,
                 ) -> None:
        '''
        
        '''
        # self.map_dir = 'maps'
        # self.map_list = os.listdir(self.map_dir)
        # self.map_index = 0
        self.map_path = map_path
        self.global_map, self.robot_position = self.map_setup(self.map_path)
        self.map_size = self.global_map.shape

        self.robot = Robot(position=self.robot_position, 
                           lidar=Lidar())
        

    def map_setup(self, 
                  map_path:str
                  )->Tuple[np.ndarray, np.ndarray]:
        '''
        将地图二值化，并返回机器人初始位置(黄点中心)
        
        参数:
        map_path: 地图路径
        
        返回:
        global_map: 全局地图
        robot_position: 机器人位置
        '''
        # 第二个参数 1 表示以灰度模式读取图像
        # 图像数据通常加载为 0-1 的浮点数，所以这里乘以 255，将图像数据转换为 0-255 的整数范围
        # astype(int) 将图像矩阵的数据类型转换为整型
        global_map = (io.imread(map_path, 1) * 255).astype(int)

        # 地图中黄点位置 
        robot_location = np.nonzero(global_map == 208)

        robot_location = np.array([np.array(robot_location)[1, 127], 
                                   np.array(robot_location)[0, 127]])
        
        global_map = (global_map > 150)
        global_map = global_map * 254 + 1   
        
        return global_map, robot_location