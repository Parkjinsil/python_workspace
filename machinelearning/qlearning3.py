import gym
import numpy as np
import matplotlib.pyplot as plt
from gym.envs.registration import register
import random as pr

def rargmax(vector):
    """ 최대 보상(가장 큰 Q값)의 인덱스(행동 인덱스) 값을 리턴, 동일할 땐 랜덤하게 리턴 """
    m = np.amax(vector)
    indices = np.nonzero(vector == m)[0]
    return pr.choice(indices)


# 환경을 등록
register(
 id='FrozenLake-v3',
 entry_point='gym.envs.toy_text:FrozenLakeEnv',
 # 'FrozenLake'환경을 미끄럽지 않게 'is_slippery=False'로 등록
 kwargs={'map_name': '4x4', 'is_slippery': False}
)

# 환경을 생성합니다.
env = gym.make('FrozenLake-v3')

# 상태와 행동에 대한 Q테이블을 0으로 초기화
Q = np.zeros([env.observation_space.n, env.action_space.n])

# for 문의 반복 횟수 (episode의 수)를 지정합니다.
num_episodes = 2000

# 할인율(Discount factor) 설정하는 변수
# 할인율 : 미래 보상에 대한 현재 가치의 가중치 (0 ~ 1 사이 값)
# 할인율이 높을수록 미래 보상에 더 큰 가치 부여 -> 먼 미래의 보상도 중요하게 여김 (장기적인 전략 고려)
# 할인율이 낮을수록 가까운 미래의 보상에만 관심 가짐 -> 즉각적인 보상을 더 중요하게 여김 (단기적인 이득 최대화)
dis = .99

# 한번 반복할때마다 해당 episode의 총 보상을 기록합니다.
rList = []

for i in range(num_episodes):
    # 한번 시작할때마다 state를 초기화합니다.
    state_ = env.reset()
    state = state_[0]
    rAll = 0 # 현재 에피소드 동안 에이전트가 받은 총 보상 저장
    done = False

    # The Q-Table learning algorithm (Q 테이블 학습 알고리즘)
    while not done:

        '''
        탐사(Exploration)
        : 에이전트가 아직 충분히 알지 못하는 상태나 행동을 시도하는 과정
         -> 환경에 대한 더 많은 정보 수집, 더 나은 정책 학습 가능
         -> 장기적으로 보상을 극대화하는 데 중요
         
        탐험(Exploitation)
        : 에이전트가 현재까지 학습한 정책을 기반으로 가장 높은 보상을 예상하는 행동
         -> 단기적으로 보상을 극대화하는 데 중점
        '''

        # 탐사(Exploration)을 위해 해당 상태 벡터, 즉 예상 보상 값에 랜덤값을 더합니다.
        # Q[state, :]는 현재 상태에서 가능한 모든 행동에 대한 Q-값
        # np.random.randm(1, env.action_space.n) : 표준 정규 분포(평균 0,분산 1)를 따르는 랜덤한 값 생성 -> 이 값들이 노이즈 역할
        # /(i+1) : 에피소드가 진행될수록 'i'의 값이 커지므로, 노이즈의 크기는 점점 작아짐 
        # 즉 초기에는 큰 노이즈를 추가하여 탐사를 더 많이 하도록 하고, 시간이 지남에 따라 노이즈를 줄여 탐험을 더 많이 하도록 유도
        action = np.argmax(Q[state, :] + np.random.randn(1, env.action_space.n) / (i + 1))

        # 행동을 취하고 나면 해당 행동의 결과를 불러옵니다.
        # 행동의 결과는 새로운 상태, 보상, 종료 여부가 있습니다.( _ : 무시된 값(추가적인 정보 무시))
        new_state, reward, done, _, _ = env.step(action)

        # 행동을 취하기 전의 상태인 state와, 취한 행동인 action을 인덱스 삼아
        # 취한 행동의 결과로 인한 보상과 새로운 상태에서 가장 큰 값 (보상)에 discount factor를 곱한 값을 더합니다.
        Q[state, action] = reward + dis * np.max(Q[new_state, :])

        # 상태를 업데이트합니다.
        state = new_state

        # 해당 결과로 인해 얻은 보상을 합산합니다.
        rAll += reward

    # 해당 episode에서 얻은 누적 보상 값을 rList에 저장합니다.
    rList.append(rAll)

# 성공률을 계산합니다.
print("Success rate: " + str(sum(rList)/num_episodes))

# Q테이블의 최종값을 출력합니다.
print("Final Q-Table Values")
print("LEFT DOWN RIGHT UP")
print(Q)

# rList를 bar chart로 시각화합니다.
plt.bar(range(len(rList)), rList, color="blue")
plt.show()