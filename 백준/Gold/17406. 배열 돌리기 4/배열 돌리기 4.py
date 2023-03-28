from sys import stdin
from itertools import permutations

input = stdin.readline

# https://www.acmicpc.net/problem/17406

R, C, K = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(R)]
original = [m[:] for m in mapp]
order = [list(map(int, input().split())) for _ in range(K)]
permute = list(permutations(order, K))

# a,b 에서 x,y까지 한바퀴 돌리는 함수
def rotate(a,b,x,y):
    temp = mapp[a][b]
    # 상
    for r in range(a, x):
        mapp[r][b] = mapp[r+1][b]
    # 좌
    for c in range(b, y):
        mapp[x][c] = mapp[x][c+1]
    # 하
    for r in range(x, a, -1):
        mapp[r][y] = mapp[r-1][y]
    # 우
    for c in range(y, b, -1):
        mapp[a][c] = mapp[a][c-1]
    mapp[a][b+1] = temp

# r,c,s를 받아 정사각형들을 회전하는 함수
def do_order(mr,mc,ms):
    a = mr-ms
    b = mc-ms
    x = mr+ms
    y = mc+ms
    while a != mr:
        rotate(a,b,x,y)
        a += 1
        b += 1
        x -= 1
        y -= 1
# 최대 초기값 설정
MAX = 100 * C + 1
answer = MAX

# 배열 값 계산 함수
def calculate():
    result = sum(mapp[0])
    for i in range(1, R):
        result = min(result, sum(mapp[i]))
    return result

for p in permute:
    # 해당 순서대로 배열돌리기
    for rcs in p:
        r,c,s = rcs
        do_order(r-1,c-1,s)
    # 배열값 계산하여 answer 갱신
    answer = min(answer, calculate()) 

    # 회전한 배열 원래대로 돌리기
    mapp = [o[:] for o in original]

print(answer)