from sys import stdin

input = stdin.readline

# https://www.acmicpc.net/problem/2668
N = int(input().strip())
second = [0]
for _ in range(N):
    second.append(int(input().strip()))

# dfs로 자기자신까지 돌아오는지 탐색
def find(idx, num):
    if second[idx] == num:
        return True
    
    elif not visit[idx]:
        if second[idx] == idx:
            return False
        else:
            visit[idx] = True
            if find(second[idx], num):
                return True
    else:
        return False

answer = []
visit = []
for i in range(1,N+1):
    visit = [False] * (N+1)
    if find(i,i):
        answer.append(i)

print(len(answer))
for i in answer:
    print(i)