from sys import stdin
from collections import deque

input = stdin.readline

T = int(input().strip())
arr = []
for _ in range(T):
    arr.append(list(map(int, input().strip())))
# 회전하기 전 극이 다르면 반대방향으로 회전

# 톱니 돌리는 함수
def rotate(num, dir):
    cur = arr[num-1]
    # 시계방향
    if dir == 1:
        temp = cur.pop()
        cur.insert(0, temp)
    # 반시계방향
    else:
        temp = cur.pop(0)
        cur.append(temp)

# 돌아가기 전 좌우에 있는 톱니 체크 (좌:6, 우:2)
def left(num):
    if num > 1 and arr[num-2][2] != arr[num-1][6]:
        return True
    return False

def right(num):
    if num < T and arr[num-1][2] != arr[num][6]:
        return True
    return False   

K = int(input().strip())
lq = deque()
rq = deque()
for _ in range(K):
    num, dir = map(int, input().split())
    if left(num):
        lq.append((num-1, dir*-1))
    if right(num):
        rq.append((num+1, dir*-1))
    rotate(num, dir)
    while lq or rq:
        if lq:
            cnum, cdir = lq.popleft()
            if left(cnum):
                lq.append((cnum-1, cdir*-1))
            rotate(cnum,cdir)
        if rq:
            cnum, cdir = rq.popleft()
            if right(cnum):
                rq.append((cnum+1, cdir*-1))
            rotate(cnum,cdir)
answer = 0
for a in arr:
    if a[0] == 1:
        answer += 1
print(answer)