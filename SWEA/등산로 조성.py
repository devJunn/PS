dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]
def dfs(y, x, flag, cnt):
    global MAP, check, answer
    answer = max(answer, cnt)
    for direction in range(4):
        ny, nx = y+dys[direction], x+dxs[direction]
        if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
        if check[ny][nx]: continue
        if flag:
            for k in range(1, K+1):
                flag = False
                MAP[ny][nx] -= k
                if MAP[ny][nx] < MAP[y][x]:
                    check[ny][nx] = True
                    dfs(ny, nx, flag, cnt+1)
                    check[ny][nx] = False
                MAP[ny][nx] += k
                flag = True
        if MAP[ny][nx] < MAP[y][x]:
            check[ny][nx] = True
            dfs(ny, nx, flag, cnt+1)
            check[ny][nx] = False


def solution():
    max_height = max([max(row) for row in MAP])
    starts = []
    for y in range(N):
        for x in range(N):
            if MAP[y][x] == max_height:
                starts.append((y, x))
    for y, x in starts:
        check[y][x] = True
        dfs(y, x, True, 1)
        check[y][x] = False


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    check = [[False] * N for _ in range(N)]
    answer = 1
    solution()
    print(f"#{t} {answer}")
