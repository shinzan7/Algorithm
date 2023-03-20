from sys import stdin
from collections import deque

input = stdin.readline
# https://www.acmicpc.net/problem/2252

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
cnt = [0 for _ in range(N+1)]

# a 뒤에 b 그래프로 입력
# b 에 들어오는 간선만큼 cnt 세기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    cnt[b] += 1

# 들어오는 간선이 없으면(앞에 서는 학생이 없다면)
# queue 에 추가
q = deque()
for i in range(1, N+1):
    if cnt[i] == 0:
        q.append(i)
        cnt[i] = -1

# answer 배열에 순서대로 저장
answer = []
while q:
    cur = q.popleft()
    answer.append(cur)

    for next in graph[cur]:
        cnt[next] -= 1
        if cnt[next] == 0:
            q.append(next)

print(*answer)