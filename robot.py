import numpy as np
from typing import Tuple

from sensor import Lidar


class Robot:
    '''
    Robot类
    主要用于和地图(environment)交互
    最好和agent分开, 方便训练
    即: agent负责决策(训练), robot负责和环境交互

    包含：
    position: 机器人自身位置
    belief_map: 机器人认知地图, 确认地图上的座标点是否已经探索过 
    lidar: 传感器, sensor类

    功能：(和地图交互)
    移动
    扫描
    更新自身认知地图
    '''
    def __init__(self,
                 ) -> None:
        '''
        初始化机器人

        属性：
        position: np.ndarray
            机器人位置
        lidar: Lidar
            传感器
        belief_map: np.ndarray
            机器人自己的地图
        '''
        self.position = None
        self.belief_map = None
        self.lidar = Lidar()        

    def reset(self,
              robot_start_position:np.ndarray,
              global_map:np.ndarray
              )->np.ndarray:
        '''
        每轮游戏开始前重置机器人

        参数:
        robot_start_position: np.ndarray
            机器人初始位置

        global_map: np.ndarray
            本次游戏全局地图

        返回：
        belief_map: np.ndarray
            机器人自己的地图
        '''
        # 初始化机器人位置和自己的地图
        self.position = robot_start_position
        self.belief_map=np.ones_like(global_map) * 127
        # self.local_map = np.zeros(global_map.shape)

        # 更新机器人自己的地图
        self.belief_map = self.update_belief_map(global_map)

        return self.belief_map
    
    def update_belief_map(self,
                         global_map:np.ndarray
                         )->np.ndarray:
        '''
        更新机器人自己的地图

        参数:
        global_map: np.ndarray
            全局地图

        返回：
        belief_map: np.ndarray
            机器人自己认知的地图
        '''
        self.belief_map=self.lidar.scan(self.position,self.belief_map,global_map)
        
        return self.belief_map
    
    
        
