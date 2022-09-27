'''
SW Expert Academy
5658 [모의 SW 역량테스트] 보물상자 비밀번호
'''

def solution(N, K, arr):
    hex_table = {'0': 0, '1': 1, '2': 2, '3': 3,
                 '4': 4, '5': 5, '6': 6, '7': 7,
                 '8': 8, '9': 9, 'A': 10, 'B': 11,
                 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    l = N//4 # 한 변의 길이
    ret = set()
    for i in range(N):
        x = 0
        for j in range(l):
            x += hex_table[arr[(i+j)%N]]*(16**(l-j-1))
        ret.add(x)
    ret = list(ret)
    ret.sort(key=lambda x: -x)
    return ret[K-1]


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = input()
    answer = solution(N, K, arr)
    print(f"#{t} {answer}")
