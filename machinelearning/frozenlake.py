import gym
from gym.envs.registration import register

# 새로운 환경을 커스텀 설정으로 등록
register(
    id="FrozenLake-v3",  # 환경의 고유 ID
    entry_point="gym.envs.toy_text:FrozenLakeEnv",  # 환경 클래스의 경로
    kwargs={"map_name": "4x4", "is_slippery": False}  # 커스텀 설정: 4x4 맵과 미끄럽지 않게 설정
)

# 환경 생성
env = gym.make("FrozenLake-v3")
state = env.reset()  # 초기 상태로 환경 재설정
if isinstance(state, tuple):
    state = state[0]  # 상태가 튜플로 반환될 경우 상태만 추출

# 키보드 입력에 대한 행동 매핑 정의
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

arrow_keys = {
    'w': UP,     # 위로 이동
    's': DOWN,   # 아래로 이동
    'd': RIGHT,  # 오른쪽으로 이동
    'a': LEFT    # 왼쪽으로 이동
}

# 환경의 현재 상태를 출력하는 함수
def print_state(state):
    state_desc = env.unwrapped.desc.tolist()  # 환경 설명 가져오기
    state_desc = [[c.decode('utf-8') for c in line] for line in state_desc]  # 바이트를 문자열로 디코딩
    row, col = state // 4, state % 4  # 상태 인덱스에서 행과 열 계산
    state_desc[row][col] = 'P'  # 에이전트의 위치를 'P'로 표시
    for line in state_desc:
        print("".join(line))  # 환경 출력
    print()

# 메인 게임 루프 설명
print("Use 'w', 'a', 's', 'd' keys to move the agent")  # 이동을 위한 키 설명
print("Press 'q' to quit the game")  # 게임 종료를 위한 키 설명
print("Initial state:")  # 초기 상태 출력
print_state(state)  # 초기 상태 출력

while True:
    key = input("Enter action: ").strip().lower()  # 사용자 입력 받기
    if key == 'q':
        print("Game aborted!")
        break  # 'q' 입력 시 루프 종료

    if key not in arrow_keys:
        print("Invalid key! Use 'w', 'a', 's', 'd' to move.")
        continue  # 잘못된 키 입력 시 루프 계속

    action = arrow_keys[key]  # 키에 해당하는 행동 가져오기
    state, reward, done, truncated, info = env.step(action)  # 환경에서 한 단계 진행
    if isinstance(state, tuple):
        state = state[0]  # 상태가 튜플로 반환될 경우 상태만 추출

    action_name = {UP: 'UP', DOWN: 'DOWN', LEFT: 'LEFT', RIGHT: 'RIGHT'}[action]
    print(f"Action: {action_name}, State: {state}, Reward: {reward}, Info: {info}")  # 행동 세부 정보 출력

    print("Current state:")
    print_state(state)  # 현재 상태 출력

    if done or truncated:
        if reward == 1.0:
            print("Congratulations! You reached the goal!")  # 목표 지점에 도달한 경우
        else:
            print("Game over. You fell into a hole.")  # 구멍에 빠진 경우
        break  # 게임 종료 시 루프 종료

print("Game ended.")  # 게임 종료 메시지 출력