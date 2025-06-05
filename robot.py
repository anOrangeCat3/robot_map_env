import numpy as np
from typing import Tuple

from sensor import Lidar

UPDATE_FREQUENCY = 10
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
        self.odom = np.zeros((0,2))   

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
        
        self.position = robot_start_position  # 初始化机器人位置
        self.belief_map=np.ones_like(global_map) * 127  # 初始化机器人自己的地图
        self.odom = np.zeros((0,2))  # 初始化odom

        # 更新机器人自己的地图
        self.belief_map = self.update_belief_map(global_map)

        return self.belief_map
    
    def step_move(self,
             move_direction:str,
             global_map:np.ndarray
             )->np.ndarray:
        '''
        移动机器人, 仅移动一步

        参数:
        move_direction: str
            移动方向

        global_map: np.ndarray
            全局地图

        返回:
        belief_map: np.ndarray
            机器人自己认知的地图
        '''
        if move_direction == 'left':
            move_vector = np.array([-1,0])
            # self.position[0] -= 1    
        elif move_direction == 'right':
            move_vector = np.array([1,0])
            # self.position[0] += 1
        elif move_direction == 'down':
            move_vector = np.array([0,-1])
            # self.position[1] -= 1
        elif move_direction == 'up':
            move_vector = np.array([0,1])
            # self.position[1] += 1

        self.position += move_vector
        self.odom = np.vstack((self.odom,move_vector))

        return self.update_belief_map(global_map)
    
    def update_belief_map(self,
                         global_map:np.ndarray,
                         update_frequency:int=UPDATE_FREQUENCY
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
        if len(self.odom) % update_frequency == 0:
            self.belief_map=self.lidar.scan(self.position,self.belief_map,global_map)
        
        return self.belief_map
    
    
        
