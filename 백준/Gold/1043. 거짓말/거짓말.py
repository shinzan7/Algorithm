from sys import stdin

input = stdin.readline

# https://www.acmicpc.net/problem/1043
N,M = map(int, input().split())
truth = list(map(int, input().split()))
if truth:
    truth.pop(0)

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
parties = []

for _ in range(M):
    party = list(map(int, input().split()))
    party.pop(0)
    parties.append(party)
    # 파티 참석자들끼리 연결하기
    for i in range(len(party)):
        for j in range(i+1, len(party)):
            graph[party[i]][party[j]] = 1
            graph[party[j]][party[i]] = 1

know_truth = [False] * (N+1)
# 파티참석자들에게 진실 퍼트리기
def dfs(num):
    for i in range(1, N+1):
        if graph[num][i] == 1 and not know_truth[i]:
            know_truth[i] = True
            dfs(i)

for t in truth:
    know_truth[t] = True
    dfs(t)

answer = M
# 1명이라도 진실을 아는 파티에서는 answer에서 -1 해준다
for party in parties:
    for p in party:
        if know_truth[p]:
            answer -= 1
            break
print(answer)