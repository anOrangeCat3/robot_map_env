import numpy as np
from skimage import io
from typing import Tuple

from robot import Robot
from map import Map

class Env:
    '''
    环境类
    用于管理机器人和地图的交互

    包含：
    map: 地图类
    robot: 机器人类
    
    '''

    def __init__(self,
                 robot:Robot,
                 map:Map,
                 ) -> None:
        '''
        初始化环境

        属性：
        robot: Robot
            机器人
        map: Map
            地图
        '''
        self.robot = robot
        self.map = map

    def reset(self,)->np.ndarray:
        '''
        重置环境

        返回：
        obs: np.ndarray
            机器人自己的地图
        '''
        # 更新机器人自己的地图
        obs = self.robot.reset(self.map.robot_start_position, self.map.global_map)
        
        return obs

