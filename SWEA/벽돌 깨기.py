from collections import deque
from copy import deepcopy

def shoot(x):
    ret = 0
    for y in range(H):
        if MAP[y][x]:
            ret = breaking(y, x)
            update()
            break
    return ret

def breaking(y, x):
    global MAP
    dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    q.append((y, x, MAP[y][x]))
    MAP[y][x] = 0
    ret = 1  # 부순 벽돌의 개수
    while q:
        y, x, d = q.popleft()
        for i in range(1, d):
            for k in range(4):
                ny, nx = y+i*dys[k], x+i*dxs[k]
                if ny < 0 or ny >= H or nx < 0 or nx >= W: continue
                if MAP[ny][nx]:
                    q.append((ny, nx, MAP[ny][nx]))
                    MAP[ny][nx] = 0
                    ret += 1
    return ret

def update():
    global MAP
    for x in range(W):
        cnt = 0
        for y in range(H-1, -1, -1):
            if MAP[y][x]:
                MAP[H-1-cnt][x], MAP[y][x] = MAP[y][x], MAP[H-1-cnt][x]
                cnt += 1

def simulation(level):
    global answer, MAP
    if level == N:
        ret = 0
        for i in selected:
            ret += shoot(i)
        answer = max(answer, ret)
        MAP = deepcopy(copied_MAP) # 다시 원래 상태로 백업해줘야 함!
        return
    for i in range(W):
        selected.append(i)
        simulation(level+1)
        selected.pop()


T = int(input())
for t in range(1, T+1):
    N, W, H = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(H)]
    copied_MAP = deepcopy(MAP)
    remain = 0 # 초기 벽돌의 개수
    for y in range(H):
        for x in range(W):
            if MAP[y][x]:
                remain += 1
    answer = 0
    selected = []
    simulation(0)
    print(f"#{t} {remain-answer}")
