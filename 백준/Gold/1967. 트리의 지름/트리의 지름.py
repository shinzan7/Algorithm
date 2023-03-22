from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**9)
# https://www.acmicpc.net/problem/1967

N = int(input().strip())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

distance = [-1] * (N+1)
distance[1] = 0
# x로부터 모든 노드의 거리 구하기
def dfs(x, weight):
    for n,w in graph[x]:
        if distance[n] == -1:
            distance[n] = w + weight
            dfs(n, w + weight)

# 루트 1으로부터 가장 먼 노드 edge 구하기
dfs(1,0)
edge = distance.index(max(distance))

# edge로 부터 가장 먼 노드와의 거리 구하기
distance = [-1] * (N+1)
distance[edge] = 0
dfs(edge,0)
print(max(distance))