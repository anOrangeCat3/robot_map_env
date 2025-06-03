import numpy as np

LIDAR_RANGE = 10
LIDAR_ANGLE_STEP = 0.5 / 180 * np.pi  # 0.5度的角度增量

class Lidar:
    '''
    Lidar类

    包含：
    激光雷达的扫描范围
    激光雷达的扫描角度增量(扫描步长)

    功能：
    扫描地图, 与地图交互
    '''
    def __init__(self,
                 )->None:
        self.lidar_range = LIDAR_RANGE
        self.angel_step = LIDAR_ANGLE_STEP

    def scan(self,
             robot_position:np.ndarray,):
        '''
        以机器人坐标为中心, 扫描一圈

        返回一个雷达扫描最外围坐标的集合
        '''
        x0 = robot_position[0]
        y0 = robot_position[1]

        angle = 0
        explored_region = set()
        while angle < 2 * np.pi:
            x1 = x0+np.cos(angle)*self.lidar_range
            y1 = y0+np.sin(angle)*self.lidar_range

            x1=x1.round()
            y1=y1.round()

            explored_region.add((x1,y1))

            angle += self.angel_step
        
        return explored_region


