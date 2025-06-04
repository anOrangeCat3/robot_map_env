from env import Env

class TrainManager():
    def __init__(self,
                 env:Env,
                 episode_num:int,
                 ) -> None:
        '''
        初始化训练管理类

        属性：
        train_env: Env
            训练环境
            
        episode_num: int
            训练轮数
        '''
        self.train_env = env
        self.episode_num = episode_num

    def train(self,)->None:
        for _ in range(self.episode_num):
            # TODO: 每一轮训练，记录一个episode的总reward用于评估
            episode_reward = self.train_episode()
            pass
    
    def train_episode(self)->None:
        '''
        一轮游戏
        '''
        # 重置环境
        # TODO: 完成 Env.reset()
        obs,_ = self.train_env.reset()
        done = False

        while not done:
            # 根据当前状态选择动作
            # TODO: 完成 Agent.get_action()
            action = self.agent.get_action(obs)
            # 执行动作，获取下一个状态和奖励
            # TODO: 完成 Env.step()
            next_obs, reward, _ = self.train_env.step(action)
            # next_obs, reward, terminated, truncated, info = self.train_env.step(action)
            # 更新策略
            # TODO: 完成 Agent.train_policy()
            self.agent.train_policy(obs,action,reward,next_obs,done)
            obs = next_obs



