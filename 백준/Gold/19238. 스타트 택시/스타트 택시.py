from sys import stdin
from collections import deque

input = stdin.readline

def minus_one(x):
    return int(x)-1

# https://www.acmicpc.net/problem/19238
N,M,FUEL = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(N)]
SR,SC = map(minus_one, input().split())
customer = [list(map(minus_one, input().split())) for _ in range(M)]
# 같은 거리의 손님일때 작은 행,열을 기준으로 하기 위해 정렬
customer = sorted(customer, key = lambda x : (x[0], x[1]))

dr = [1,-1,0,0]
dc = [0,0,1,-1]
# 두 지점 사이의 거리 찾는 함수
def calculate_dist(tr,tc):
    q = deque()
    visit = [[-1 for _ in range(N)] for _ in range(N)]
    q.append((tr,tc,0))
    visit[tr][tc] = 0

    while q:
        cr, cc, cnt = q.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == -1 and mapp[nr][nc] == 0:
                q.append((nr, nc, cnt+1))
                visit[nr][nc] = cnt+1

    return visit

def work():
    global N,M,FUEL,SR,SC,customer
    # 택시 위치
    tr, tc = SR,SC
    fuel = FUEL

    while customer:
        idx, min_cost = -1, 500001
        distance = calculate_dist(tr, tc)
        for i in range(len(customer)):
            # 최단거리 손님 태우기
            cr, cc = customer[i][0], customer[i][1]
            customer_cost = distance[cr][cc]
            # 벽이 막혀있는 경우
            if customer_cost == -1:
                return -1
            if min_cost > customer_cost:
                idx = i
                min_cost = customer_cost

        # 손님태우러 가기
        if fuel >= min_cost:
            fuel -= min_cost
            tr,tc = customer[idx][0], customer[idx][1]
        else:
            return -1

        distance = calculate_dist(tr, tc)
        # 목적지까지 가고 연료채우기
        destination_cost = distance[customer[idx][2]][customer[idx][3]]
        if fuel >= destination_cost:
            fuel += destination_cost
            tr,tc = customer[idx][2], customer[idx][3]
        else:
            return -1

        # 승객 목적지 도착하면 목록에서 지우기
        customer.pop(idx)

    return fuel

# 남은 연료 출력
print(work())